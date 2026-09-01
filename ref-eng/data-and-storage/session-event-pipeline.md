---
type: implementation-reference
name: org2-session-event-pipeline
description: Normalization, live storage, persistence, search, pagination, analytics, and review projections for session events.
tags: [org2, data, session-events, persistence, analytics]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: source-observed
---

# Session event pipeline

## Scope and evidence

This record explains how ORG2 turns raw runtime activity into canonical `SessionEvent` values and then supports live display, durable reload, browse, search, and analytics.

UA selected Session Event Pipeline as a missing journey. Graphify identified the canonical event types, persistence bridge, turn index, frontend RPC, replay, and extraction boundaries. All behavioral claims are Source-observed at revision `b315ba4f82fb1fe294496793d7322095e7efe262`.

This pipeline is separate from SQLite WAL. WAL protects database commits and reader/writer concurrency. Session events record application activity and can support review-facing projections.

## Pipeline shape

```text
provider, tool, or imported RawActivityChunk
  -> consolidate deltas and remove invalid duplicates
  -> normalize to canonical SessionEvent
  -> merge tool-call start and result by call_id
  -> backfill child-agent prompt context
  -> per-session in-memory EventStore
  -> frontend snapshots, deltas, browse, and live search
  -> SessionEvent/CachedEvent conversion
  -> SQLite session cache and turn index
  -> cached browse, cross-session search, replay, and analytics
```

The canonical type lives in the shared `types` crate. The event-pipeline module re-exports it for compatibility and registers extraction behavior at application startup.

## Ingestion

`ingest_raw_chunks` has three main stages:

1. Consolidation merges streaming thinking and message deltas, filters empty chunks, and removes duplicate assistant messages.
2. Normalization maps provider-specific action and function names into canonical event fields, display hints, metadata, and typed extracted data.
3. Tool-call merging joins start and result events that share `call_id`.

After these stages, prompt backfill can attach the known prompt for a child-agent event. `IngestionResult` reports raw, filtered, and processed counts beside the events.

Thinking and message consolidation use separate accumulators. This preserves interleaved provider streams such as thinking deltas mixed with assistant text. Each accumulator sorts by timestamp before it joins text.

Tool-call merge keeps the start event's timeline position and arguments, adds result fields from the end event, and prefers the final display status. A lone event or an event without a usable `call_id` remains visible.

## Canonical event and extracted data

`SessionEvent` contains identity, session, action and function names, arguments, result, time, source, display variant and status, optional file or command fields, call identity, metadata, extracted data, and shell replay state.

`ExtractedData` gives review features a typed view of file reads and edits, shell commands, search, TODOs, messages, directory and glob results, Git artifacts, web search, subagents, organization tasks, and file deletion. Rendering and analytics do not need to reinterpret every raw provider payload.

## Live EventStore

One `EventStore` owns one session's event vector and an ID-to-index map for constant-time lookup. The command layer keeps several stores by session ID and batches `es:changed` notifications to the frontend.

Live commands can set, append, upsert, patch, merge, buffer, snapshot, paginate, search, switch, pin, evict, and unload event bodies. This state serves the active UI. It is not the durable store by itself.

Shell events have an extra storage rule. When a durable shell replay exists, the event keeps replay metadata and a bounded terminal preview instead of a second full transcript. Terminal previews are limited to 32 KiB. A shell callback cannot move the visible replay watermark backward, and `Incomplete` wins over a later optimistic state.

## Durable cache bridge

The cache bridge converts between `SessionEvent` and `session_persistence::CachedEvent`. It can load a cached session into the in-memory store, save the current in-memory events, and load or save a full session payload.

A cache load does not overwrite a nonempty active store. Provider history can replace cached events for providers that own their history. The load path repairs derived links and cancels orphan interactive events before it exposes the result.

Imported events have a two-step publication path:

```text
cache_append_session_event_import
  -> save deferred event rows
  -> cache_finalize_session_event_import
  -> publish the completed imported session
```

The bridge can skip cache saves for session providers that own persistence elsewhere. `es_save_to_cache` treats auxiliary save failure as best effort and logs it, while direct cache commands return errors to the caller.

## Browse and search

Pagination applies filters in Rust before it returns a page. Filters include event source, display variant, function, file presence or prefix, text, and time bounds. Cursor-based forward and backward traversal avoids sending the entire event array to the frontend.

Live chat search reads one in-memory `EventStore`. Cached session search reads SQLite. Cross-session search supports the global session-search palette. These paths share canonical event identities but have different storage and freshness boundaries.

The frontend uses typed RPC procedures and runtime schemas for event arrays, partial patches, cache results, turn windows, and search hits. Session switching can load a bounded initial turn window and defer older turn bodies.

## Analytics and review projections

Per-session analytics run in Rust over live or cached canonical events. The output includes:

- tool call, completion, failure, duration, and file-impact counts;
- unique file and operation summaries;
- user, assistant, and thinking message counts;
- token totals and per-model totals;
- timeline buckets;
- error and failure summaries.

Multi-session analytics loads each selected cached session and then aggregates its events. Session statistics also group session metadata by status, type, repository, model, daily activity, and file impact.

The review model is a projection over canonical activity. It does not make analytics the source of truth for runtime state or work completion.

## State and consistency boundaries

| State | Owner | Consistency rule |
| --- | --- | --- |
| Raw activity chunks | Provider or adapter | Input can be partial, duplicated, or provider-specific. |
| Canonical event | Shared event type | Normalization gives display and extraction consumers one contract. |
| Live event sequence | Per-session `EventStore` | ID index and vector update together; frontend changes are batched. |
| Durable cached event | Session persistence | Conversion defines the disk boundary. |
| Turn index | Session persistence | Rebuilds a round-oriented projection from events and intents. |
| Shell transcript | Shell replay artifacts | Full output stays outside the event row; events carry bounded replay state. |
| Search result | Live store or SQLite query | Result freshness depends on the selected owner. |
| Analytics | Pure derived computation | It has no independent lifecycle or write authority. |

## Failure and recovery

| Failure | Response |
| --- | --- |
| Empty, malformed, or duplicate chunk | Consolidation filters or normalizes it without failing the full batch where possible. |
| Missing tool-call pair | The available event remains unmerged. |
| Cache load fails | The caller receives an error; active in-memory events are not replaced. |
| Provider history load fails | The bridge logs the failure and can retain prepared cached data. |
| Best-effort live-store save fails | The bridge logs the error and keeps the active runtime result. |
| Deferred import stops before finalize | The imported rows remain unpublished until finalization. |
| Shell replay durability fails | Replay state becomes `Incomplete`; later callbacks cannot restore an optimistic complete state. |
| Large shell output | The event keeps a bounded preview and the durable replay holds the full transcript. |

## Tradeoffs

| Choice | Benefit | Cost or limit |
| --- | --- | --- |
| Normalize provider activity once | Renderers, search, replay, and analytics share one event vocabulary. | The normalizer must evolve with new provider shapes. |
| Keep a live store and a durable cache | Active interaction stays fast and restart history remains available. | Conversion and reconciliation must prevent divergent views. |
| Merge streaming fragments | Review shows one coherent message or tool call. | The pipeline must preserve timeline identity and handle orphan fragments. |
| Compute filters and analytics in Rust | The frontend receives bounded typed results. | Cached analytics loads and converts the selected event sets. |
| Keep full shell replay outside events | Event rows and snapshots stay bounded. | Review needs a second artifact read for full terminal output. |
| Support mutable events | Streaming patches and retry remain practical. | Session events form an application journal, not strict event sourcing. |

## Source map

| Concern | Current source |
| --- | --- |
| Canonical event and extracted data | [`src-tauri/crates/types/src/session_event.rs`](src-tauri/crates/types/src/session_event.rs), [`src-tauri/crates/types/src/extracted.rs`](src-tauri/crates/types/src/extracted.rs) |
| Ingestion stages | [`src-tauri/src/agent_sessions/event_pipeline/ingestion/mod.rs`](src-tauri/src/agent_sessions/event_pipeline/ingestion/mod.rs), [`src-tauri/src/agent_sessions/event_pipeline/ingestion/consolidator.rs`](src-tauri/src/agent_sessions/event_pipeline/ingestion/consolidator.rs), [`src-tauri/src/agent_sessions/event_pipeline/ingestion/tool_call_merger.rs`](src-tauri/src/agent_sessions/event_pipeline/ingestion/tool_call_merger.rs) |
| Live store | [`src-tauri/src/agent_sessions/event_pipeline/store/mod.rs`](src-tauri/src/agent_sessions/event_pipeline/store/mod.rs), [`src-tauri/src/agent_sessions/event_pipeline/commands/`](src-tauri/src/agent_sessions/event_pipeline/commands/) |
| Cache bridge | [`src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs`](src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs), [`src-tauri/crates/session-persistence/src/`](src-tauri/crates/session-persistence/src/) |
| Pagination and search | [`src-tauri/src/agent_sessions/event_pipeline/pagination.rs`](src-tauri/src/agent_sessions/event_pipeline/pagination.rs), [`src-tauri/src/agent_sessions/event_pipeline/search.rs`](src-tauri/src/agent_sessions/event_pipeline/search.rs) |
| Analytics and statistics | [`src-tauri/src/agent_sessions/event_pipeline/analytics.rs`](src-tauri/src/agent_sessions/event_pipeline/analytics.rs), [`src-tauri/src/agent_sessions/event_pipeline/statistics.rs`](src-tauri/src/agent_sessions/event_pipeline/statistics.rs) |
| Typed frontend RPC | [`src/api/tauri/rpc/procedures/sessionCore.ts`](src/api/tauri/rpc/procedures/sessionCore.ts), [`src/api/tauri/rpc/schemas/sessionCore.ts`](src/api/tauri/rpc/schemas/sessionCore.ts) |
| Global session search | [`src/scaffold/GlobalSpotlight/palettes/AllSessionsSearchPalette/index.tsx`](src/scaffold/GlobalSpotlight/palettes/AllSessionsSearchPalette/index.tsx) |

## Known limits

This record does not benchmark large histories or prove that every provider action has a perfect canonical mapping. It did not execute a live session. The source supports the stated pipeline and failure contracts at the pinned revision.

