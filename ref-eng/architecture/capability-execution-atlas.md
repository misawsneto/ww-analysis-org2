---
type: implementation-reference
name: org2-capability-execution-atlas
description: Cross-cutting map from selected ORG2 capabilities to execution, state, persistence, interfaces, and evidence.
tags: [org2, architecture, capabilities, execution, atlas]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: source-observed
---

# ORG2 capability and execution atlas

## Purpose and evidence

This atlas connects four ORG2 capabilities that the accepted UA domain graph selected and the prior corpus did not explain in enough depth. UA supplied semantic domains and source candidates. Graphify supplied structural boundary paths. Direct source at revision `b315ba4f82fb1fe294496793d7322095e7efe262` proves the behavioral claims.

The [graph coverage matrix](ref-eng/evidence/G-ORG2-REF-002-graph-coverage.md#graph-guided-coverage-for-the-org2-capability-atlas) records why these journeys were selected and why existing session-runtime subjects were not repeated.

## Capability map

| Capability | User entry | Frontend/native boundary | Rust owners | Main domain values | State and persistence | External or tool boundary | Focused record |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Coordinate an Agent Org | Agent Org launch, run controls, tasks, intervention, plan approval | Session and org-task Tauri commands plus run-change events | Org launch, run store, inbox, finality, member sessions | Agent Org, Run, member session, task, inbox message, completion intent, plan approval | Run and coordination rows plus normal session persistence | Each member enters the native agent/provider/tool kernel | [Agent Org coordination](ref-eng/runtime/agent-org-coordination.md#agent-org-coordination) |
| Route an external channel conversation | Enable channel, send chat message, issue slash command, reset session | Integration configuration and gateway dispatch commands/events | Gateway service, binding store, channel handler, channel manager | Channel config, conversation key, binding, Agent Session, pending reset notice | In-memory and durable binding plus normal session history | Telegram, Discord, Feishu, WeCom, Weixin and event bus delivery | [Channel gateway routing](ref-eng/runtime/channel-gateway-routing.md#channel-gateway-routing) |
| Import external agent artifacts | Inline import tables for agents, rules, skills, and MCP | Typed external-import API and two Tauri commands | Source detectors, apply router, definition/policy/skill/MCP stores | Detected Item, Import Selection, Fidelity Warning, Import Report | No generic import store; each selected item enters its native owner | Cursor, Claude Code, Codex, Copilot, Kiro, filesystem, MCP config | [External artifact import seams](ref-eng/interfaces/external-artifact-import-seams.md#external-artifact-import-seams) |
| Review session activity | Chat timeline, session replay, search, statistics, and analytics | SessionCore typed RPC and event-store notifications | Ingestion, EventStore, cache bridge, search, pagination, analytics | Raw Activity Chunk, Session Event, Extracted Data, replay bookmark, search result | Live per-session store, SQLite event cache, turn index, shell replay artifact | Provider and tool callbacks, imported histories, frontend review views | [Session event pipeline](ref-eng/data-and-storage/session-event-pipeline.md#session-event-pipeline) |

## Shared execution relationships

```text
External artifact import
  -> changes native definitions, policies, skills, or MCP configuration
  -> runtime assembly consumes those native values later

Channel Gateway
  -> adapts an external conversation into AgentSession input
  -> native-agent execution emits SessionEvents

Agent Org Coordination
  -> creates root and member AgentSessions
  -> each member uses native-agent execution
  -> coordination adds tasks, inbox, approvals, and finality

AgentSession execution
  -> emits canonical SessionEvents
  -> event pipeline supports live UI, persistence, search, replay, and analytics
```

These relations do not merge ownership. Import has no authority over a later run. Channel bindings do not own session history. Agent Org finality does not replace member turn settlement. Event analytics does not determine task or run completion.

## Boundary matrix

| Boundary | Contract | State owner on each side | Failure containment |
| --- | --- | --- | --- |
| Agent Org definition to run | Freeze effective organization and coordinator context | Definition store -> run store | Invalid identity or workspace stops run creation. |
| Org coordinator to members | Typed tasks, inbox messages, approvals, and child sessions | Run coordination -> member session | Unread or failed side effects block finality. |
| Channel provider to gateway | Normalize provider event and retain conversation identity | Provider adapter -> gateway service | Adapter or access failure does not create a valid route. |
| Gateway to agent runtime | Reinjected message with original channel metadata and bound session | Binding store -> AgentSession | Dispatch errors return through the outbound route; reset uses conservative checks. |
| Foreign artifact to ORG2 | Detect, preview fidelity, then apply an explicit selection | Filesystem source -> native target store | Per-item reports isolate partial failures; overwrite is opt-in. |
| Runtime activity to event model | Consolidate, normalize, merge, and extract | Provider/tool callback -> EventStore | Invalid or orphan chunks remain filtered or independently visible. |
| Live events to durable cache | Typed `SessionEvent`/`CachedEvent` conversion | EventStore -> session persistence | A failed best-effort save does not erase the live result. |
| Cached events to review | Bounded query, turn windows, search, replay, and derived analytics | Session persistence -> frontend projection | Queries return errors or bounded results; derived values do not mutate runtime truth. |

## Domain and data ownership

| Concern | Authoritative current state | Historical or derived state |
| --- | --- | --- |
| Agent Org composition | Agent Org definition store | Run snapshot preserves launch-time composition. |
| Agent Org execution | Run, task, inbox, approval, and session stores | Run view derives bounded current operations; source inbox rows remain immutable. |
| Channel routing | Binding store and channel configuration | Session events preserve conversation activity, not binding authority. |
| Imported configuration | Policy, skill, MCP, or Agent Definition owner | Provenance comments and item reports describe the import operation. |
| Live session activity | Per-session EventStore and active AgentSession | SQLite event rows, turn index, and shell replay support reload and review. |
| Session analytics | None; analytics is derived | Recomputed from selected canonical events. |

## Architectural patterns

### Native-owner translation

The external importer translates foreign values into the existing ORG2 owner instead of introducing a parallel foreign-artifact runtime. This reduces downstream branching but requires explicit fidelity rules.

### Shared execution kernel with outer adapters

Channel and Agent Org flows converge on the normal `AgentSession` kernel. They add routing or coordination around it. They do not fork provider and tool execution.

### Durable control, derived navigation

Bindings, run facts, inbox rows, canonical events, and replay bookmarks persist. Run views, reverse relations, pagination pages, search hits, and analytics derive from those owners.

### One stored direction

The selected paths store routing and ownership once, then derive reverse navigation. Examples include session-to-root lineage, conversation-key-to-session binding, and event-to-session ownership.

### Bounded projections over large payloads

Run views omit large inbox bodies, event pagination filters before transport, session switching can load a turn window, and shell events keep a bounded preview while the replay artifact stores the full transcript.

### Explicit terminal gates

Agent Org completion depends on canonical blockers and a current completion intent. Session events can change display state, but an event status does not bypass run finality.

## Change-impact guide

| Planned change | Read first | Likely boundary tests |
| --- | --- | --- |
| Add an Agent Org coordination message | Agent Org coordination and core entities | Message serialization, sender/recipient routing, transcript-before-read, finality blockers. |
| Change run completion | Agent Org coordination and state lifecycles | Work revision, completion intent, transaction reload, terminal consistency, recovery. |
| Add a channel provider | Channel gateway routing and system topology | Codec, access policy, binding identity, reinjection metadata, delivery split/retry/media. |
| Change channel reset | Channel gateway routing | Active turn/child checks, conservative query failure, binding clear, lazy replacement notice. |
| Add an external artifact kind | External import seams and system topology | Detection bounds, preview/fidelity, target-name validation, native-store apply, partial report. |
| Add a provider event shape | Session event pipeline and native execution seams | Consolidation, normalization, extraction, tool-call pairing, runtime schema. |
| Change event persistence | Session event pipeline and state lifecycles | Live/durable conversion, provider-owned history, turn index, shell payload bounds, search. |

## Evidence paths

| Capability | Semantic guide | Structural guide | Direct source entry points |
| --- | --- | --- | --- |
| Agent Org coordination | UA Agent Org Coordination domain and flows | Graphify run-store, inbox, session, database, and frontend edges | [`src-tauri/crates/agent-core/src/core/coordination/agent_org_runs/`](src-tauri/crates/agent-core/src/core/coordination/agent_org_runs/), [`src-tauri/crates/agent-core/src/core/coordination/agent_inbox/`](src-tauri/crates/agent-core/src/core/coordination/agent_inbox/) |
| Channel Gateway | UA Channel Gateway domain and flows | Graphify gateway, bus, state, and frontend edges | [`src-tauri/crates/agent-core/src/integrations/gateway/`](src-tauri/crates/agent-core/src/integrations/gateway/), [`src-tauri/crates/agent-core/src/state/commands/channel_handler/`](src-tauri/crates/agent-core/src/state/commands/channel_handler/) |
| External Artifact Import | UA External Artifact Import domain and flows | Graphify importer, definition, policy, skill, and MCP edges | [`src-tauri/crates/agent-core/src/specialization/external_import/`](src-tauri/crates/agent-core/src/specialization/external_import/), [`src/scaffold/WizardSystem/shared/externalImport/`](src/scaffold/WizardSystem/shared/externalImport/) |
| Session Event Pipeline | UA Session Event Pipeline domain and flows | Graphify event type, persistence, transport, turn-index, and UI edges | [`src-tauri/src/agent_sessions/event_pipeline/`](src-tauri/src/agent_sessions/event_pipeline/), [`src-tauri/crates/types/src/session_event.rs`](src-tauri/crates/types/src/session_event.rs) |

## Known limits

The atlas covers the four gaps selected by the accepted matrix. It does not replace the [system topology](ref-eng/architecture/system-topology.md#org2-system-topology), [package dependencies](ref-eng/architecture/package-dependencies.md#org2-package-dependencies), [core entities](ref-eng/domain-models/core-entities.md#org2-core-entities), or [native-agent execution kernel](ref-eng/architecture/native-agent-execution-kernel.md#native-agent-execution-kernel). Project sync and existing native runtime flows remain outside this slice because the graph-guided scope review did not select them.
