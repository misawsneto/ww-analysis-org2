---
type: dossier
subject: ORG2 (orgii) — architecture, data model, tracking, agent-awareness boundary
compiled: session working notes, verified against source unless flagged
---

# ORG2 Reference Dossier — 1

Everything below was verified against actual source (`src/`, `src-tauri/`) or actual copied databases in this repo, not inferred from the domain-graph alone. Where something is inference rather than confirmed fact, it's marked **(inferred)**. Where something was checked and found to contradict an earlier guess, the correction is kept, not silently smoothed over.

---

## 1. Data stores

Three SQLite databases exist under `.orgii/`, all copied into this folder for reference:

| File | Location here | Purpose |
|---|---|---|
| `sessions.db` | `ref-eng/sessions.db` | Native + ingested session/event data, agent orgs, work-item execution state |
| `projects.db` | `ref-eng/projects/projects.db` | Projects, work items, milestones, labels, routines, sync outbox |
| `<hash>.sqlite` | `ref-eng/code-map/code-map.sqlite` | Per-workspace static code index (files/nodes/edges/FTS) — unrelated bounded context, keyed by a hash of the workspace path |

Schema dumps: `sessions.schema.sql`, `projects/projects.schema.sql`, `code-map/code-map.schema.sql`.

`code-map.sqlite` was live (had `-shm`/`-wal` companion files) — copied all three and ran `PRAGMA wal_checkpoint(FULL)` before dumping, to avoid a torn read.

No other `.db`/`.sqlite*` files exist anywhere under `.orgii/` — confirmed by full-tree `find`.

---

## 2. `sessions.db` — table families are disjoint

Two independent, non-joining table families share the one file:

**Native** (ORG2 running its own agent): `sessions`, `events`, `session_turns`, `agent_sessions`, `code_sessions`
**Ingested** (orgtrack reading other tools' history): `orgtrack_core_sessions`, `orgtrack_core_activities`, `orgtrack_core_file_changes`, `orgtrack_core_edit_artifacts`, `orgtrack_core_diff_chunks`, `orgtrack_core_checkpoints`, `imported_history_*`

"Disjoint" = no shared rows or foreign keys between the two families — same DB file, two unrelated pipelines. Row counts on this machine at time of inspection: native `sessions`=2, `events`=2, `session_turns`=0; ingested `orgtrack_core_sessions`=119, `shell_replays`=163. Most real data volume was on the ingested side here.

### Event-oriented, consistently, not just in one table

- `events`: generic append-only log — `session_id, event_type, args_json, result_json, content, history_sequence`. No per-type schema, just a `TEXT` discriminator + JSON payload.
- `session_turns` stores no content — only `start_sequence`/`end_sequence` pointing into the `events` log, plus rollups (`event_count`, `modified_files_json`). A turn is a *view over a slice of the event sequence*.
- Nine further tables carry their own independent `sequence`/`seq` column: `agent_messages`, `code_session_chunks`, `orgtrack_core_edit_artifacts`, `orgtrack_core_diff_chunks`, `orgtrack_core_session_checkpoints`, `shell_replays`, `shell_replay_pages`, `session_turn_index_state`.
- `orgtrack_core_checkpoints` (keyed by `source`, holding `payload_json` + `parser_version`) is a snapshot/checkpoint pattern layered on the event log — the standard companion to event sourcing, so replay/ingest doesn't refold from zero every time.

**Conclusion, verified structurally, not just per the domain graph's business-rule claim:** event sourcing (read-side) is the load-bearing persistence pattern across the whole app, not a one-off replay detail.

---

## 3. Cross-tool ingestion — normalization pipeline (Orgtrack)

### The funnel

```
raw format (JSONL / SQLite / vendor-specific)
        │  tool-specific parser
        ▼
tool-specific "meta" struct        (e.g. ClaudeCodeHistoryMeta)
        │  per-tool mapping fn      (e.g. session_meta_to_cache_input)
        ▼
ImportedHistoryCacheInput          shared, tool-agnostic intermediate
        │  core_session_record_from_imported_input()
        ▼
SessionRecord (+ ActivityRecord, FileChangeRecord, ...)   ← canonical.rs, the true target type
```

Canonical types live in `src-tauri/crates/orgtrack-core/src/canonical.rs`. One trait, `SourceAdapter` (`sources/mod.rs`), one output bag, `SourceRecords`.

### Parser locations

| Tool | File | Mapping fn |
|---|---|---|
| Claude Code | `sources/claude_code/history.rs` | `session_meta_to_cache_input` |
| Cline | `sources/cline/history.rs` | `session_meta_to_cache_input` |
| Codex | `sources/codex/app.rs` | `session_meta_to_cache_input` |
| Cursor CLI | `sources/cursor_cli/history.rs` | `session_meta_to_cache_input` |
| Cursor IDE | `sources/cursor_ide/db.rs` + `summaries.rs` | `cache_input_from_raw` / `minimal_cache_input_from_index` |
| mimo_code | `sources/mimo_code/history.rs` | `meta_to_cache_input` |
| opencode | `sources/opencode/history.rs` | `session_meta_to_cache_input` |
| qoder | `sources/qoder/history.rs` | `session_meta_to_cache_input` |
| trae | `sources/trae/history.rs` | `session_meta_to_cache_input` |
| warp | `sources/warp/history.rs` | `conversation_to_cache_input` |
| windsurf | `sources/windsurf/history.rs` | `composer_meta_to_cache_input` |
| workbuddy | `sources/workbuddy.rs` (flat, no subdir) | `session_meta_to_cache_input` |
| zcode | `sources/zcode/history.rs` | `session_meta_to_cache_input` |
| **omp** | `sources/omp/history.rs` | *no own parser* — delegates to `anthropic_jsonl.rs` |
| **qoder_cli** | `sources/qoder_cli/history.rs` | *no own parser* — delegates to `anthropic_jsonl.rs` |
| — shared base | `sources/anthropic_jsonl.rs` | `meta_to_cache_input` — generic Anthropic-JSONL parser, parametrized by `omp`/`qoder_cli` config structs |

13 bespoke parsers + 1 shared parametrized parser reused by 2 tools. `omp`/`qoder_cli` aren't separate implementations, just `AnthropicJsonlSource{source, session_prefix, provider_slug, ...}` configs handed to one parser — don't write a bespoke parser when the wire format is already shared.

Activity-level normalization is a second, smaller funnel: `activity.rs`'s `activity_kind_from_event_type()` maps each tool's raw `event_type` string into a closed `ActivityKind` enum, defaulting unmatched types to `Heartbeat` (permissive fallback, not a hard failure).

**Architecturally: textbook Adapter pattern.** Lossy by design — `source_metadata_json` is the escape hatch where anything tool-specific that doesn't fit canonical shape goes; `SessionRecord` is a lossy projection, not a lossless union, of the source formats.

### What OMP actually is

Not something ORG2 is built on. A **peer external agent CLI**, touched at the same three points as every other supported tool:
1. Binary detection/launch (`cli_binary_resolver.rs`, config at `~/.oh-omp/agent/*.yml`)
2. Managed config injection — ORG2 can rewrite OMP's own `models.yml`/`config.yml` to route it through ORG2's model proxy (`managed_config/adapters.rs`)
3. History ingestion (read-only, `sources/omp/`)

---

## 4. Scheduling — who actually keeps ingestion fresh

**Correction applied during this session:** originally assumed a Rust-side cron/interval loop. Checked directly — no `tokio::spawn`/interval/sleep loop exists in `extraction_scheduler.rs` (that file is only a memory-pressure gate, `evaluate_memory_gate`) or in `importer.rs`.

**The actual scheduler is frontend TypeScript**, not backend: `src/store/session/useDataSourceAutoScan.ts`, mounted once in `AppBootstrap`.

- Self-rearming `setTimeout` loop, 30s base tick (`TICK_MS`)
- Forced full pass on app startup
- Per-source due-check against configurable cadence (`dataSourceConfigAtom` / `dataSourceGlobalFrequencyAtom`), gated by `lastScannedAt`
- Focus-adaptive: unfocused window stretches cadence to a 10-minute floor; regaining focus fires an immediate catch-up pass
- Cheap presence probe (30 min cadence) decoupled from the expensive full parse
- Dedup guard (`autoScanInFlight`) prevents overlapping passes
- Sources set to `"manual"` are never auto-scanned

Calls `externalHistoryRescanSources()` → Tauri command `external_history_rescan_sources` (`history_commands.rs`) → the `SourceAdapter::scan()` per tool.

---

## 5. Session Replay

Read-only projection, never re-executes the agent (verified structurally, not just asserted): `ReplaySession`/`ReplayTurn` are computed on demand from whichever event log backs a session (native `events` or ingested `orgtrack_core_*`).

Flow: `select_session → load_replay_events → reconstruct_diff_sections_per_turn → render_replay_in_code_panel → sync_browser_replay_tabs`. Backend assembly at `orgtrack-core/src/projectors/replay.rs`.

Simulator apps (Canvas, BackgroundTasks) use registry + matcher dispatch: `register_simulator_app_config → match_event_to_simulator_app → hydrate_full_event_history → render`. No central switch statement — new app types register independently.

---

## 6. Work items → agent execution — the prompt-only boundary

**Central finding of this session.** Traced `StartAgentButton` → `useWorkItemOrchestrator.ts` → `buildSdeTaskPrompt()` (`WorkItemDetail/promptBuilder.ts`) → `SessionService.create()`.

- `buildSdeTaskPrompt()` renders the work item (title, spec, todos, mode, review feedback) into **plain markdown text**, sent as the agent's initial user message.
- Separately, `workItemId: shortId` is passed as a structured field to `SessionService.create()` — but this goes into ORG2's own orchestrator/session bookkeeping (execution locks, collab-lock arbitration, status), **never into the agent's context**.
- Confirmed no `cliAgentType` is ever set in the work-item flow → `category = "rust_agent"` in `SessionService.create()` → work items always run through ORG2's own native agent runtime, never by shelling out to the actual `claude`/`codex`/`cursor` binaries.

**The agent has zero structural awareness of "work item" as a concept.** It sees rendered prose and a shortId string it's told to reference in commits — same as any prompt-engineering pattern, not a protocol field. The app's tracking of session↔work-item correlation is pure machinery on top, invisible to the model.

---

## 7. `agent-core` — internal layering (from its own `ARCHITECTURE.md`)

Strict, documented, enforced by code review — not inferred:

| Layer | Path | Role |
|---|---|---|
| 3 | `state/` | Tauri command handlers — the only TS-visible surface |
| 2b | `integrations/` | External I/O — chat gateways, automation triggers |
| 2a | `intelligence/` | Pluggable capabilities — memory, skills, MCP, hooks |
| 1 | `core/` | Domain — `AgentSession` (aggregate root), `turn_executor`, `tools` |
| 0 | `foundation/` | Infra — SQLite persistence, event bus, security/sandbox |

Rule: strict downward-only dependency (`foundation` imports nothing internal; everything may import it). One deliberate exception: `core ↔ intelligence` is bidirectional by design (`intelligence` is injected into the turn loop, not an outer wrapper) — narrowly scoped both directions.

Persistence: no migration framework — single source-of-truth file `session_snapshots::ensure_tables`, idempotent `ALTER TABLE` appends via `try_migrate`.

Cross-cutting: `foundation::bus` (`tokio::broadcast`) is the sanctioned UI/engine cross-talk mechanism — explicit anti-pattern warning against ad hoc `Mutex<Vec<Listener>>`.

### Bounded contexts = crates

Crate boundaries map ~1:1 onto the domain-graph's `domain:` nodes: `agent-core` (Chat + Orgs), `orgtrack-core` (Cross-Tool Tracking), `project-management` (Work Items — itself layered: `projects/` domain, `orchestrator/` application service, `sync/` anti-corruption to Linear/GitHub), `git`/`git-api`, `key-vault`, `lsp`/`terminal`/`browser`.

---

## 8. CLI hooks — what ORG2 installs into Claude Code / Codex / Cursor / etc.

Source: `src-tauri/crates/agent-cli/src/session_provenance.rs` (2865 lines), `src-tauri/src/orgtrack/session_provenance/{hook_capture,approval_gate}.rs`.

- ORG2 writes managed hook entries into each CLI tool's **own** hook config (e.g. `~/.claude/settings.json`), tagged with a marker (`--session-provenance-hook`) so only ORG2's own entries are ever touched on rewrite — user hooks preserved.
- Installed command is **ORG2's own binary**, re-invoked as a subprocess: `'/path/to/org2' --session-provenance-hook claude_code`.
- Hooked events (Claude Code): `PostToolUse` (file tools) + lifecycle (`UserPromptSubmit`, `Stop`, `StopFailure`, `PermissionRequest`, `PreToolUse`, `PostToolUseFailure`). 11 platforms supported total.
- `capture_hook_stdin()` reads the tool's own hook JSON off stdin, normalizes it, spools to the local DB (feeds `orgtrack_core_*`), optionally posts a live-status loopback ping to the desktop UI. **One-way telemetry — "provenance failures are diagnostic only and never block the provider tool."**

### The one exception: `PermissionRequest` actually gates execution

`approval_gate.rs` — long-polls the desktop app (`POST /hooks/agent-approval`, up to ~130s) while a human answers a permission card, then prints a decision to **stdout** in the CLI's own documented hook-decision format:
```json
{ "hookSpecificOutput": { "hookEventName": "PermissionRequest", "decision": { "behavior": "allow" } } }
```
Fail-open: silence (timeout, closed desktop, non-managed session) → no decision printed → CLI's normal permission flow applies. Can never wedge a run.

**Important distinction:** this speaks to the CLI *harness's* control flow, not to the LLM's context. The model is never told "ORG2 approved this" as text — same boundary as everywhere else in this system.

---

## 9. How much the agent is aware of ORG2's records/formats

**Effectively none**, and the mechanism is consistent everywhere checked:

| Layer | Agent-visible? |
|---|---|
| `events` table, `history_sequence` | No — it's the result of the agent acting, not an input |
| `SessionRecord`/canonical schema | No — Rust-only |
| `workItemId` correlation field | No — structured param to `SessionService.create`, never serialized into the prompt |
| Session/turn IDs | No — the agent doesn't reason about its own row identity |

**What the agent does see:** whatever is explicitly composed into a message string or a tool's JSON Schema. Two concrete mechanisms carry all format compliance:

1. **Tool JSON Schema — structural, provider-enforced.** E.g. `manage_todo`'s `parameters()`: `status` is a closed enum, `content` has `minLength: 1`, `blockedBy` is an array of non-negative ints. This is the load-bearing mechanism — the model is boxed into the shape by the tool-calling contract itself, the same way any function-calling API works. Not a "the agent learned the format" story; a structural constraint.
2. **Prose in tool `description()` + server-side validation as backstop + periodic `<system-reminder>` nudges** for anything schema can't express. Checked concretely: `manage_todo`'s "exactly ONE task in_progress at a time" rule is **not enforced anywhere in code** — pure prose, trusted, not guaranteed. This is a real, confirmed gap between structurally-guaranteed and merely-instructed, worth remembering if a todo list ever ends up with two `in_progress` rows.

The tool's `execute()` implementation is the seam absorbing translation from model-facing schema to DB row — same pattern as `ImportedHistoryCacheInput → SessionRecord` and the work-item prompt builder. The agent never sees the DB shape on the other side of that seam.

---

## 10. Open items / not yet verified

- Whether `claude_code/history.rs`'s `parse_claude_session_meta` is fully independent of `anthropic_jsonl.rs` or itself wraps it (naming suggests possible overlap — not confirmed either way).
- Whether any entry point *other than* the work-item orchestrator sets `cliAgentType` for a work-item-driven session (i.e., whether work items can ever be routed through an actual external CLI binary instead of the native `rust_agent`) — the type signature supports it, no call site found that uses it for work items specifically.
- Full enumeration of which other `core::tools` implementations (beyond `manage_todo`) rely on prose-only rules vs. schema/server-enforced ones — only `manage_todo` was inspected in depth.

---

## Appendix: unrelated tangent (different codebase)

A separate, unrelated project (`al-modules/al-5.1.5`, "Agent Loom") was briefly reviewed for its own architecture docs (`runtime-architecture-v2.md`, `data-layer-v1.md`) — a Gateway/Journal/Fact/Rule/View system with Postgres backing. Not part of ORG2. Relevant takeaway carried back into this dossier's framing: that system's explicit design principle — *"Internal names never reach the View. Implementation identifiers may exist in code and never appear in a Record, a View, or anything an Actor sees"* — is the same boundary ORG2 enforces in practice (Section 9 above), just stated as a formal contract there instead of an emergent pattern here.
