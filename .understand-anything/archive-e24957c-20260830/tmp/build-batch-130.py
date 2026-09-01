import json

with open('/home/misael/pj/gui-repos/ORG2/.understand-anything/tmp/ua-file-extract-results-130.json') as f:
    extract = json.load(f)

results_by_path = {r['path']: r for r in extract['results']}

PREFIX = 'src-tauri/crates/session-persistence/src/'

# ---- Per-file metadata (summary, tags, complexity, languageNotes) ----
FILES = {
    'agent_core_bridge.rs': dict(
        summary="Wire-side adapter that registers this crate's SQLite-backed implementations into agent_core's IoC slots (db_bridge, session_bridge) so agent_core's memory, consolidation, reflection, and turn-processor code can persist token usage and turn-intent state without a dependency back on session_persistence.",
        tags=["adapter", "bridge", "dependency-injection", "persistence"],
        complexity="moderate",
        languageNotes="Uses a one-shot register() call to install trait-object implementations into agent_core's foundation slots, keeping the dependency edge one-directional.",
    ),
    'commands.rs': dict(
        summary="Tauri-command layer exposing ~23 async wrappers around the blocking SQLite CRUD, editing, and telemetry operations of this crate, each offloading work via spawn_blocking so the Tauri main thread is never blocked.",
        tags=["api-handler", "tauri-command", "async", "persistence"],
        complexity="complex",
        languageNotes="Commands are re-registered from app::commands::handler_list.inc under the bare session_persistence::* path rather than being invoked directly from this file.",
    ),
    'connection.rs': dict(
        summary="Thin re-export shim exposing database::db connection helpers (get_connection, begin_immediate, with_sessions_writer) under the session_persistence namespace for legacy in-crate callers.",
        tags=["barrel", "re-export", "database"],
        complexity="simple",
    ),
    'crud.rs': dict(
        summary="Synchronous rusqlite CRUD operations for session and event persistence -- save/load/search/delete sessions and events -- intended to be called from a blocking thread via spawn_blocking.",
        tags=["data-access", "persistence", "database", "crud"],
        complexity="complex",
    ),
    'editing.rs': dict(
        summary="Session event log editing operations -- truncate-after-event, delete, and update -- backing the edit-and-resend chat flow used by useEditUserMessage.",
        tags=["editing", "persistence", "database"],
        complexity="moderate",
    ),
    'lib.rs': dict(
        summary="Crate root for session_persistence: wires up SQLite-backed session/event/token-usage persistence on top of the shared database::db connection, re-exports the crud/editing/turn_index/turn_window public surface, and exposes ~23 Tauri commands re-registered by app::commands::handler_list.",
        tags=["entry-point", "barrel", "crate-root"],
        complexity="simple",
        languageNotes="Pure host adapter with no back-edges into the app crate; provider-neutral provenance projection lives in orgtrack_core and is only materialized here into ORG2's local session cache.",
    ),
    'schema.rs': dict(
        summary="Owns DDL for session-domain SQLite tables (events, sessions, turn intents, token/tool usage) and legacy FTS5 index teardown, registered with the database crate's schema dispatcher at app startup.",
        tags=["database", "schema", "migration"],
        complexity="complex",
    ),
    'sequence.rs': dict(
        summary="In-memory, mutex-guarded per-session sequence counter cache that keeps event ordering deterministic across concurrent async writers, capped at 500 entries to bound growth in long-running processes.",
        tags=["concurrency", "cache", "sequence"],
        complexity="simple",
    ),
    'token_usage.rs': dict(
        summary="Persists per-chat-round token usage records to session_token_usage, shared by code sessions and OS Agent sessions.",
        tags=["persistence", "token-usage", "database"],
        complexity="moderate",
    ),
    'tool_usage.rs': dict(
        summary="Persists per-LLM-call usage spans and per-tool-call usage attribution records used to break down token/byte cost by tool invocation.",
        tags=["persistence", "telemetry", "database"],
        complexity="complex",
    ),
    'turn_index.rs': dict(
        summary="Builds and maintains a materialized 'turn' index derived from the normalized session event log, grouping raw events into user-facing conversational turns with summaries, status, and backfilled synthetic user events.",
        tags=["indexing", "persistence", "database"],
        complexity="complex",
    ),
    'turn_index_debounce.rs': dict(
        summary="Coalescing debouncer that batches rapid-fire rebuild_turn_index calls (from the streaming agent + subagents pipeline) into a single deferred rebuild per session, avoiding redundant writer-lock contention.",
        tags=["concurrency", "debounce", "performance"],
        complexity="moderate",
        languageNotes="Uses a global HashMap<session_id, ScheduledEntry> guarded by a Mutex plus a generation counter to coalesce reschedules without spawning duplicate workers.",
    ),
    'turn_intents.rs': dict(
        summary="Canonical user-intent lifecycle store: persists and transitions session_turn_intents rows that give one identity to a user submission across optimistic UI, wire layer, scheduler, and the persisted event/turn-index.",
        tags=["state-machine", "persistence", "database"],
        complexity="complex",
    ),
    'turn_window.rs': dict(
        summary="Turn-window queries over the normalized session event cache, returning CachedEvent rows for specific turn ranges or the initial window shown when a session is opened.",
        tags=["query", "persistence", "database"],
        complexity="moderate",
    ),
    'types.rs': dict(
        summary="Shared persistence-layer data types for the session cache: CachedEvent (mirrors the frontend SessionEvent shape), session metadata, search results, and cache stats.",
        tags=["data-model", "type-definition", "persistence"],
        complexity="simple",
    ),
}

FUNC_META = {
    'agent_core_bridge.rs': {
        'record_token_usage_adapter': ("Adapter that maps agent_core's TokenUsageRow into a token_usage::insert_token_usage_record call, returning the new row id.", ["adapter", "token-usage"]),
        'map_attribution_method': ("Maps a wire-format attribution method string to the local AttributionMethod enum.", ["mapping", "utility"]),
        'record_usage_telemetry_batch_adapter': ("Adapter that converts a batch of agent_core LLM usage spans and tool attributions into local record types and persists them via tool_usage::insert_usage_telemetry_batch.", ["adapter", "telemetry", "batch"]),
        'map_bridge_status': ("Maps a wire-format turn-intent status string to the local TurnIntentStatus enum.", ["mapping", "turn-intent"]),
        'map_bridge_source': ("Maps a wire-format turn-intent source string to the local TurnIntentSource enum.", ["mapping", "turn-intent"]),
        'upsert_turn_intent_adapter': ("Adapter that inserts or updates a turn intent record via turn_intents::upsert_initial using mapped source and status enums.", ["adapter", "turn-intent"]),
        'update_turn_intent_status_adapter': ("Adapter that transitions a turn intent's status via turn_intents::update_status.", ["adapter", "turn-intent"]),
        'register': ("Installs this crate's concrete db_bridge and session_bridge implementations into agent_core's IoC container at startup.", ["entry-point", "dependency-injection", "registration"]),
    },
    'commands.rs': {
        'cache_save_session': ("Tauri command wrapper that persists a full CachedSession via crud::save_session on a blocking thread.", ["tauri-command", "api-handler", "persistence"]),
        'cache_load_session': ("Tauri command wrapper that loads a cached session by id via crud::load_session.", ["tauri-command", "api-handler", "persistence"]),
        'cache_update_session_specs': ("Tauri command wrapper that updates a session's specs JSON via crud::update_session_specs.", ["tauri-command", "api-handler"]),
        'cache_save_events': ("Tauri command wrapper that persists a batch of session events via crud::save_events.", ["tauri-command", "api-handler", "persistence"]),
        'cache_load_events': ("Tauri command wrapper that loads all cached events for a session via crud::load_events.", ["tauri-command", "api-handler"]),
        'cache_load_turn_index': ("Tauri command wrapper that loads the materialized turn index for a session via turn_index::load_turn_index.", ["tauri-command", "api-handler"]),
        'cache_search_events': ("Tauri command wrapper that performs a text search over a session's events via crud::search_events.", ["tauri-command", "api-handler", "search"]),
        'cache_search_all_sessions': ("Tauri command wrapper that searches events across all cached sessions via crud::search_all_sessions.", ["tauri-command", "api-handler", "search"]),
        'cache_get_session_metadata': ("Tauri command wrapper that fetches session metadata via crud::get_session_metadata.", ["tauri-command", "api-handler"]),
        'cache_delete_session': ("Tauri command wrapper that deletes a cached session via crud::delete_session.", ["tauri-command", "api-handler"]),
        'cache_clear_old_sessions': ("Tauri command wrapper that purges sessions older than a max age via crud::clear_old_sessions.", ["tauri-command", "api-handler", "maintenance"]),
        'cache_get_all_sessions': ("Tauri command wrapper that lists all cached session ids.", ["tauri-command", "api-handler"]),
        'cache_get_stats': ("Tauri command wrapper that returns aggregate cache stats (session/event counts, db size).", ["tauri-command", "api-handler", "monitoring"]),
        'cache_truncate_after_event': ("Tauri command wrapper that truncates a session's event log after a given event via editing::truncate_after_event, backing the edit-and-resend flow.", ["tauri-command", "api-handler", "editing"]),
        'cache_delete_event': ("Tauri command wrapper that deletes a single cached event via editing::delete_event.", ["tauri-command", "api-handler", "editing"]),
        'cache_update_event': ("Tauri command wrapper that updates a cached event's content via editing::update_event.", ["tauri-command", "api-handler", "editing"]),
        'cache_clear_session_history': ("Tauri command wrapper that clears a session's entire event history via editing::clear_session_history.", ["tauri-command", "api-handler", "editing"]),
        'cache_get_event': ("Tauri command wrapper that fetches a single cached event by id via crud::get_event.", ["tauri-command", "api-handler"]),
        'cache_get_session_diff': ("Tauri command wrapper that computes a session diff summary (event count / metadata) for a session id.", ["tauri-command", "api-handler"]),
        'get_session_token_usage_records': ("Tauri command wrapper that returns per-round token usage records for a session via token_usage::get_token_usage_records.", ["tauri-command", "api-handler", "token-usage"]),
        'get_session_llm_usage_spans': ("Tauri command wrapper that returns per-LLM-call usage spans for a session/turn via tool_usage::get_llm_usage_spans.", ["tauri-command", "api-handler", "telemetry"]),
        'get_session_tool_usage_attributions': ("Tauri command wrapper that returns tool-call usage attribution records for a session/turn via tool_usage::get_tool_usage_attributions.", ["tauri-command", "api-handler", "telemetry"]),
        'get_session_tool_usage_attributions_for_call': ("Tauri command wrapper that returns the usage attribution record for one specific tool call via tool_usage::get_tool_usage_attributions_for_call.", ["tauri-command", "api-handler", "telemetry"]),
    },
    'crud.rs': {
        'existing_event_sequence': ("Looks up the stored sequence number for an existing event row, if any.", ["query", "sequence"]),
        'normalize_session_sequences': ("Re-numbers a session's event sequence values to be contiguous, used after truncation or reordering.", ["data-integrity", "sequence"]),
        'save_events': ("Persists a batch of session events, assigning sequence numbers, upserting rows, and scheduling a debounced turn-index rebuild.", ["persistence", "batch", "write"]),
        'load_events': ("Loads all cached events for a session ordered by sequence.", ["query", "persistence"]),
        'escape_like_pattern': ("Escapes SQL LIKE wildcard characters in a user search query.", ["utility", "sql", "search"]),
        'build_excerpt': ("Builds a highlighted text excerpt around the first match of a search query within event content.", ["search", "text-processing"]),
        'search_events': ("Performs a LIKE-based full text search over a session's events, returning ranked results with excerpts.", ["search", "query"]),
        'search_all_sessions': ("Performs a LIKE-based search across all cached sessions' events.", ["search", "query"]),
        'get_session_metadata': ("Fetches aggregate metadata (event count, time range) for a session.", ["query", "metadata"]),
        'delete_session': ("Deletes a session and all its associated events from the cache.", ["delete", "persistence"]),
        'clear_old_sessions': ("Deletes cached sessions older than a given age threshold.", ["maintenance", "delete"]),
        'get_all_sessions': ("Lists all session ids present in the cache.", ["query"]),
        'get_cache_stats': ("Computes aggregate cache statistics: total sessions, events, and database size.", ["monitoring", "stats"]),
        'update_session_metadata': ("Recomputes and persists a session's cached metadata after event mutations.", ["metadata", "write"]),
        'save_session': ("Persists a full session (events + specs) atomically, resetting sequence counters and rebuilding the turn index.", ["persistence", "write", "transaction"]),
        'load_session': ("Loads a full cached session including its events and specs.", ["query", "persistence"]),
        'update_session_specs': ("Updates the stored specs JSON blob for a session.", ["write", "metadata"]),
        'find_awaiting_user_events_by_function': ("Finds events awaiting a user response for a given tool/function name, used to resume pending interactions.", ["query", "workflow"]),
        'get_event': ("Fetches a single cached event by session and event id.", ["query"]),
    },
    'editing.rs': {
        'truncate_after_event': ("Public entry point that truncates a session's event log after the given event, delegating to truncate_after_event_inner.", ["editing", "entry-point"]),
        'truncate_after_event_inner': ("Removes the target event and every later event in a session's linear history, then rebuilds the turn index.", ["editing", "delete", "transaction"]),
        'select_ids_by_seq': ("Selects event ids in a session with sequence number greater than a given value.", ["query", "helper"]),
        'select_ids_by_ts': ("Selects event ids in a session with timestamp greater than a given value.", ["query", "helper"]),
        'delete_event': ("Deletes a single event from a session's history and renormalizes metadata.", ["delete", "editing"]),
        'update_event': ("Updates the content of an existing cached event.", ["write", "editing"]),
        'clear_session_history': ("Deletes all events for a session while preserving the session record itself.", ["delete", "maintenance"]),
    },
    'schema.rs': {
        'init_session_tables': ("Creates all session-domain SQLite tables and indexes if they don't already exist, called once at app startup.", ["database", "migration", "schema"]),
        'drop_events_fts': ("Drops the legacy FTS5 virtual table and triggers for the events table, now superseded by LIKE-based search.", ["database", "migration", "cleanup"]),
    },
    'sequence.rs': {
        'get_next_sequence': ("Returns the next sequence number for a session, initializing the counter from the database if not already cached.", ["sequence", "cache"]),
        'increment_sequence': ("Atomically increments and returns the in-memory sequence counter for a session.", ["sequence", "concurrency"]),
        'reset_sequence': ("Resets a session's in-memory sequence counter to a specific value, used after truncation or save.", ["sequence", "reset"]),
    },
    'token_usage.rs': {
        'insert_token_usage_record': ("Inserts a new token usage row for a chat round and triggers projection recomputation.", ["write", "token-usage"]),
        'recompute_usage_projection': ("Recomputes derived token-usage projections for a session after a new usage record is inserted.", ["aggregation", "token-usage"]),
        'get_token_usage_records': ("Loads all token usage records for a session.", ["query", "token-usage"]),
        'delete_token_usage_records': ("Deletes all token usage records for a session.", ["delete", "token-usage"]),
    },
    'tool_usage.rs': {
        'insert_usage_telemetry_batch': ("Opens a connection and persists a batch of LLM usage spans and tool attributions in one transaction, delegating to insert_usage_telemetry_batch_with_conn.", ["write", "batch", "telemetry"]),
        'insert_usage_telemetry_batch_with_conn': ("Inserts a batch of LLM usage spans and tool attributions using a caller-supplied connection, then triggers projection recomputation.", ["write", "batch", "telemetry"]),
        'get_llm_usage_spans': ("Loads LLM usage spans for a session, optionally filtered by turn.", ["query", "telemetry"]),
        'get_tool_usage_attributions': ("Loads tool usage attribution records for a session, optionally filtered by turn.", ["query", "telemetry"]),
        'get_tool_usage_attributions_for_call': ("Loads the usage attribution record for one specific tool call.", ["query", "telemetry"]),
        'delete_usage_telemetry': ("Deletes all LLM usage spans and tool attributions for a session.", ["delete", "telemetry"]),
    },
    'turn_index.rs': {
        'load_index_rows': ("Loads the raw event rows needed to rebuild the turn index for a session.", ["query", "indexing"]),
        'is_synthetic_user_input': ("Determines whether an event row represents a synthetic (non-user-authored) input.", ["classification", "helper"]),
        'turn_intent_id_for_row': ("Resolves the turn-intent id associated with a given event row, if any.", ["helper", "turn-intent"]),
        'load_stale_intent_ids': ("Loads the set of turn-intent ids marked stale for a session, via turn_intents::list_for_session.", ["query", "turn-intent"]),
        'load_intent_status_overlay': ("Loads a session's turn-intent statuses to overlay onto derived turn summaries.", ["query", "turn-intent"]),
        'load_user_messages': ("Loads raw user message rows for a session used to backfill missing user events.", ["query", "backfill"]),
        'load_existing_user_event_keys': ("Loads dedup keys for user events already materialized in the index, to avoid duplicate backfill.", ["query", "dedup"]),
        'backfill_missing_user_events': ("Inserts synthetic user event rows for user messages not yet represented in the event log.", ["backfill", "write"]),
        'max_timestamp': ("Returns the later of two optional timestamp strings.", ["utility", "comparison"]),
        'build_turn_drafts': ("Groups ordered event rows into draft turn boundaries with start/end sequence and preview metadata.", ["indexing", "grouping"]),
        'materialized_turn_drafts': ("Converts turn drafts into finalized, insertable turn index rows.", ["indexing", "transform"]),
        'turn_summary_from_row': ("Deserializes a stored turn index row into a CachedTurnSummary.", ["deserialization", "indexing"]),
        'rebuild_turn_index': ("Public entry point that rebuilds the materialized turn index for a session, delegating to rebuild_turn_index_inner.", ["indexing", "entry-point"]),
        'rebuild_turn_index_inner': ("Recomputes turn boundaries from the raw event log, backfills missing user events, and rewrites the turn index table.", ["indexing", "write", "transaction"]),
        'ensure_turn_index_fresh': ("Rebuilds the turn index only if it is missing or stale relative to the event log.", ["indexing", "cache-invalidation"]),
        'load_turn_index': ("Loads the full materialized turn index for a session, rebuilding first if stale.", ["query", "indexing"]),
        'load_turn_summaries': ("Loads specific turn summaries by id for a session.", ["query", "indexing"]),
        'get_turn_summary': ("Loads a single turn summary by session and turn id.", ["query", "indexing"]),
    },
    'turn_index_debounce.rs': {
        'schedule': ("Schedules a debounced turn-index rebuild for a session, coalescing with any already-pending rebuild.", ["debounce", "scheduling"]),
        'debounce_worker': ("Background worker loop that waits out the debounce window and then triggers turn_index::rebuild_turn_index.", ["worker", "async", "debounce"]),
    },
    'turn_intents.rs': {
        'transition_allowed': ("Validates whether a transition between two turn-intent statuses is legal per the state machine.", ["state-machine", "validation"]),
        'row_from_sql': ("Deserializes a SQL row into a TurnIntentRow.", ["deserialization"]),
        'upsert_initial': ("Inserts a new turn intent row in its initial status, or is a no-op if one already exists for the id.", ["write", "state-machine"]),
        'update_status': ("Transitions a turn intent to a new status, enforcing the legal-transition state machine.", ["write", "state-machine"]),
        'mark_pending_stale': ("Marks all non-terminal turn intents for a session as stale, used on session reload or restart.", ["write", "state-machine"]),
        'reconcile_in_flight_after_restart': ("Reconciles turn intents left in a non-terminal state after an unclean process restart.", ["recovery", "state-machine"]),
        'get_intent': ("Fetches a single turn intent by session and turn-intent id.", ["query"]),
        'list_for_session': ("Lists all turn intents recorded for a session.", ["query"]),
    },
    'turn_window.rs': {
        'cached_event_from_row': ("Deserializes a SQL row into a CachedEvent.", ["deserialization", "helper"]),
        'load_events_for_turn_ranges': ("Loads all cached events falling within a set of turn sequence ranges.", ["query"]),
        'load_events_by_ids': ("Loads cached events by explicit event id list.", ["query"]),
        'mark_turn_preview': ("Marks and trims an event as the preview representative for its turn.", ["helper", "transform"]),
        'load_final_assistant_event_for_range': ("Loads the last assistant event within a sequence range, used to find a turn's final response.", ["query"]),
        'load_turn_body_window': ("Loads the full event body for one turn, ensuring the turn index is fresh first.", ["query", "indexing"]),
        'load_initial_turn_window': ("Loads the most recent N turns and their events for initial session display, ensuring the turn index is fresh first.", ["query", "indexing"]),
    },
}

CLASS_META = {
    'token_usage.rs': {
        'TokenUsageRecord': ("Row struct mirroring a persisted per-round token usage record (input/output/cache/context token counts, model, account).", ["data-model", "token-usage"]),
    },
    'tool_usage.rs': {
        'AttributionMethod': ("Enum of methods used to attribute token/byte cost to a tool call (provider-exact, split-evenly, estimated-tokenizer, etc.), with as_str/from_str conversions.", ["data-model", "enum", "telemetry"]),
        'LlmUsageSpanRecord': ("Row struct for a persisted per-LLM-call usage span (prompt/completion/cache token counts, related tool calls).", ["data-model", "telemetry"]),
        'NewLlmUsageSpan': ("Input struct for inserting a new LLM usage span record.", ["data-model", "telemetry"]),
        'ToolUsageAttributionRecord': ("Row struct for a persisted per-tool-call usage attribution (decision/result/followup token and byte costs).", ["data-model", "telemetry"]),
        'NewToolUsageAttribution': ("Input struct for inserting a new tool usage attribution record.", ["data-model", "telemetry"]),
    },
    'turn_index.rs': {
        'CachedTurnSummary': ("Materialized summary of one conversational turn: sequence range, timing, user preview, status, and associated modified files/resource interactions.", ["data-model", "indexing"]),
    },
    'turn_intents.rs': {
        'TurnIntentSource': ("Enum of origins that can mint a turn intent (user submit, queue, force-send, resume, agent-org, wingman, mobile-remote), with as_str/parse conversions.", ["data-model", "enum", "state-machine"]),
        'TurnIntentStatus': ("Enum of a turn intent's lifecycle states (optimistic, queued, running, completed, failed, cancelled, stale, coalesced, rejected) with terminal-state checks and as_str/parse conversions.", ["data-model", "enum", "state-machine"]),
        'TurnIntentRow': ("Row struct for a persisted turn intent record.", ["data-model"]),
        'IntentError': ("Error type for turn intent operations covering SQLite errors, illegal transitions, not-found, and invalid stored status.", ["error-handling", "data-model"]),
    },
    'turn_window.rs': {
        'CachedTurnBodyWindow': ("Bundle of a turn id and its body events, returned by load_turn_body_window.", ["data-model"]),
        'CachedInitialTurnWindow': ("Bundle of recent turn summaries plus their events, returned by load_initial_turn_window for session open.", ["data-model"]),
    },
    'types.rs': {
        'CachedEvent': ("Cached representation of one session event, structurally matching the frontend SessionEvent JSON shape for lossless round-tripping.", ["data-model"]),
        'SessionMetadata': ("Aggregate metadata for a cached session: event count, cache timestamp, time range.", ["data-model"]),
        'CachedSession': ("Full cached session bundle: events, specs JSON, and time range.", ["data-model"]),
        'SearchResult': ("One ranked search hit within a session's events, with a highlighted snippet.", ["data-model", "search"]),
        'CrossSessionSearchHit': ("One ranked search hit spanning all cached sessions.", ["data-model", "search"]),
        'CacheStats': ("Aggregate cache statistics: total sessions, total events, database size in bytes.", ["data-model", "monitoring"]),
        'TruncateResult': ("Result of a truncate-after-event operation: counts and ids of deleted events/sequences.", ["data-model"]),
    },
}

CALLS = [
    ('agent_core_bridge.rs', 'record_token_usage_adapter', 'token_usage.rs', 'insert_token_usage_record'),
    ('agent_core_bridge.rs', 'record_usage_telemetry_batch_adapter', 'tool_usage.rs', 'insert_usage_telemetry_batch'),
    ('agent_core_bridge.rs', 'upsert_turn_intent_adapter', 'turn_intents.rs', 'upsert_initial'),
    ('agent_core_bridge.rs', 'update_turn_intent_status_adapter', 'turn_intents.rs', 'update_status'),
    ('commands.rs', 'cache_save_session', 'crud.rs', 'save_session'),
    ('commands.rs', 'cache_load_session', 'crud.rs', 'load_session'),
    ('commands.rs', 'cache_update_session_specs', 'crud.rs', 'update_session_specs'),
    ('commands.rs', 'cache_save_events', 'crud.rs', 'save_events'),
    ('commands.rs', 'cache_load_events', 'crud.rs', 'load_events'),
    ('commands.rs', 'cache_load_turn_index', 'turn_index.rs', 'load_turn_index'),
    ('commands.rs', 'cache_search_events', 'crud.rs', 'search_events'),
    ('commands.rs', 'cache_search_all_sessions', 'crud.rs', 'search_all_sessions'),
    ('commands.rs', 'cache_get_session_metadata', 'crud.rs', 'get_session_metadata'),
    ('commands.rs', 'cache_delete_session', 'crud.rs', 'delete_session'),
    ('commands.rs', 'cache_clear_old_sessions', 'crud.rs', 'clear_old_sessions'),
    ('commands.rs', 'cache_truncate_after_event', 'editing.rs', 'truncate_after_event'),
    ('commands.rs', 'cache_delete_event', 'editing.rs', 'delete_event'),
    ('commands.rs', 'cache_update_event', 'editing.rs', 'update_event'),
    ('commands.rs', 'cache_clear_session_history', 'editing.rs', 'clear_session_history'),
    ('commands.rs', 'cache_get_event', 'crud.rs', 'get_event'),
    ('commands.rs', 'get_session_token_usage_records', 'token_usage.rs', 'get_token_usage_records'),
    ('commands.rs', 'get_session_llm_usage_spans', 'tool_usage.rs', 'get_llm_usage_spans'),
    ('commands.rs', 'get_session_tool_usage_attributions', 'tool_usage.rs', 'get_tool_usage_attributions'),
    ('commands.rs', 'get_session_tool_usage_attributions_for_call', 'tool_usage.rs', 'get_tool_usage_attributions_for_call'),
    ('crud.rs', 'save_events', 'turn_index_debounce.rs', 'schedule'),
    ('crud.rs', 'save_session', 'sequence.rs', 'reset_sequence'),
    ('crud.rs', 'save_session', 'turn_index.rs', 'rebuild_turn_index'),
    ('editing.rs', 'truncate_after_event_inner', 'turn_index.rs', 'rebuild_turn_index'),
    ('tool_usage.rs', 'insert_usage_telemetry_batch', 'token_usage.rs', 'recompute_usage_projection'),
    ('turn_index.rs', 'load_stale_intent_ids', 'turn_intents.rs', 'list_for_session'),
    ('turn_index.rs', 'load_intent_status_overlay', 'turn_intents.rs', 'list_for_session'),
    ('turn_index_debounce.rs', 'debounce_worker', 'turn_index.rs', 'rebuild_turn_index'),
    ('turn_window.rs', 'load_turn_body_window', 'turn_index.rs', 'ensure_turn_index_fresh'),
    ('turn_window.rs', 'load_turn_body_window', 'turn_index.rs', 'get_turn_summary'),
    ('turn_window.rs', 'load_initial_turn_window', 'turn_index.rs', 'load_turn_index'),
]

IMPORTS = [
    ('lib.rs', f) for f in [
        'agent_core_bridge.rs', 'commands.rs', 'connection.rs', 'crud.rs', 'editing.rs',
        'schema.rs', 'sequence.rs', 'token_usage.rs', 'tool_usage.rs',
        'turn_index_debounce.rs', 'turn_index.rs', 'turn_intents.rs', 'turn_window.rs', 'types.rs',
    ]
]

FILE_ORDER = [
    'agent_core_bridge.rs', 'commands.rs', 'connection.rs', 'crud.rs', 'editing.rs',
    'lib.rs', 'schema.rs', 'sequence.rs', 'token_usage.rs', 'tool_usage.rs',
    'turn_index.rs', 'turn_index_debounce.rs', 'turn_intents.rs', 'turn_window.rs', 'types.rs',
]

PARTS = [
    FILE_ORDER[0:5],
    FILE_ORDER[5:10],
    FILE_ORDER[10:15],
]


def full_path(fname):
    return PREFIX + fname


def included_subnodes(fname):
    r = results_by_path[full_path(fname)]
    functions = r.get('functions', [])
    classes = r.get('classes', [])
    exports = r.get('exports', [])
    exported_names = set(e['name'] for e in exports)
    method_names = set()
    for c in classes:
        for m in c.get('methods', []):
            method_names.add(m)
    included_funcs = []
    for fn in functions:
        if fn['name'] in method_names:
            continue
        lines = fn['endLine'] - fn['startLine'] + 1
        if lines >= 10 or fn['name'] in exported_names:
            included_funcs.append(fn)
    included_classes = []
    for c in classes:
        lines = c['endLine'] - c['startLine'] + 1
        nmethods = len(c.get('methods', []))
        if nmethods >= 2 or lines >= 20 or c['name'] in exported_names:
            included_classes.append(c)
    return included_funcs, included_classes, exported_names


# Build all nodes/edges keyed by owning file (for partitioning)
nodes_by_file = {f: [] for f in FILE_ORDER}
edges_by_source_file = {f: [] for f in FILE_ORDER}

for fname in FILE_ORDER:
    path = full_path(fname)
    r = results_by_path[path]
    meta = FILES[fname]
    file_id = f'file:{path}'
    node = {
        'id': file_id,
        'type': 'file',
        'name': fname,
        'filePath': path,
        'summary': meta['summary'],
        'tags': meta['tags'],
        'complexity': meta['complexity'],
    }
    if 'languageNotes' in meta:
        node['languageNotes'] = meta['languageNotes']
    nodes_by_file[fname].append(node)

    included_funcs, included_classes, exported_names = included_subnodes(fname)

    for fn in included_funcs:
        name = fn['name']
        fmeta = FUNC_META.get(fname, {}).get(name)
        if fmeta is None:
            summary = f"Helper function `{name}` in {fname}."
            tags = ["helper"]
        else:
            summary, tags = fmeta
        fn_id = f'function:{path}:{name}'
        lines = fn['endLine'] - fn['startLine'] + 1
        complexity = 'simple' if lines < 20 else ('moderate' if lines < 60 else 'complex')
        fnode = {
            'id': fn_id,
            'type': 'function',
            'name': name,
            'filePath': path,
            'lineRange': [fn['startLine'], fn['endLine']],
            'summary': summary,
            'tags': tags,
            'complexity': complexity,
        }
        nodes_by_file[fname].append(fnode)
        edges_by_source_file[fname].append({
            'source': file_id, 'target': fn_id, 'type': 'contains', 'direction': 'forward', 'weight': 1.0,
        })
        if name in exported_names:
            edges_by_source_file[fname].append({
                'source': file_id, 'target': fn_id, 'type': 'exports', 'direction': 'forward', 'weight': 0.8,
            })

    for c in included_classes:
        name = c['name']
        cmeta = CLASS_META.get(fname, {}).get(name)
        if cmeta is None:
            summary = f"Type `{name}` defined in {fname}."
            tags = ["data-model"]
        else:
            summary, tags = cmeta
        c_id = f'class:{path}:{name}'
        lines = c['endLine'] - c['startLine'] + 1
        complexity = 'simple' if lines < 20 else ('moderate' if lines < 60 else 'complex')
        cnode = {
            'id': c_id,
            'type': 'class',
            'name': name,
            'filePath': path,
            'lineRange': [c['startLine'], c['endLine']],
            'summary': summary,
            'tags': tags,
            'complexity': complexity,
        }
        nodes_by_file[fname].append(cnode)
        edges_by_source_file[fname].append({
            'source': file_id, 'target': c_id, 'type': 'contains', 'direction': 'forward', 'weight': 1.0,
        })
        if name in exported_names:
            edges_by_source_file[fname].append({
                'source': file_id, 'target': c_id, 'type': 'exports', 'direction': 'forward', 'weight': 0.8,
            })

# imports edges (source = lib.rs)
for src_fname, tgt_fname in IMPORTS:
    src_path = full_path(src_fname)
    tgt_path = full_path(tgt_fname)
    edges_by_source_file[src_fname].append({
        'source': f'file:{src_path}', 'target': f'file:{tgt_path}', 'type': 'imports', 'direction': 'forward', 'weight': 0.7,
    })

# calls edges
for src_fname, src_func, tgt_fname, tgt_func in CALLS:
    src_path = full_path(src_fname)
    tgt_path = full_path(tgt_fname)
    edges_by_source_file[src_fname].append({
        'source': f'function:{src_path}:{src_func}',
        'target': f'function:{tgt_path}:{tgt_func}',
        'type': 'calls', 'direction': 'forward', 'weight': 0.8,
    })

# Validate no duplicate node ids, and self-check counts
all_node_ids = []
for f in FILE_ORDER:
    for n in nodes_by_file[f]:
        all_node_ids.append(n['id'])
assert len(all_node_ids) == len(set(all_node_ids)), 'duplicate node ids!'

import_count_expected = len(IMPORTS)
import_count_actual = sum(1 for f in FILE_ORDER for e in edges_by_source_file[f] if e['type'] == 'imports')
assert import_count_expected == import_count_actual, (import_count_expected, import_count_actual)

# Write parts
out_dir = '/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate'
total_nodes = 0
total_edges = 0
for i, part_files in enumerate(PARTS, start=1):
    part_nodes = []
    part_edges = []
    for f in part_files:
        part_nodes.extend(nodes_by_file[f])
        part_edges.extend(edges_by_source_file[f])
    total_nodes += len(part_nodes)
    total_edges += len(part_edges)
    out_path = f'{out_dir}/batch-130-part-{i}.json'
    with open(out_path, 'w') as fo:
        json.dump({'nodes': part_nodes, 'edges': part_edges}, fo, indent=2)
    print(f'part {i}: files={part_files} nodes={len(part_nodes)} edges={len(part_edges)} -> {out_path}')

print('TOTAL nodes:', total_nodes, 'TOTAL edges:', total_edges)
