#!/usr/bin/env python3
import json, math, os

RESULTS = "/home/misael/pj/gui-repos/ORG2/.understand-anything/tmp/ua-file-extract-results-14.json"
INPUT = "/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate/batch-inputs/batch-14.input.json"
OUTDIR = "/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate"

d = json.load(open(RESULTS))
inp = json.load(open(INPUT))
import_data = inp["batchImportData"]

results_by_path = {r["path"]: r for r in d["results"]}

def span(a, b):
    return b - a + 1

# ---------- File-level metadata ----------
FILES = {
"src-tauri/src/agent_sessions/event_pipeline/extractors/file_extractor.rs": dict(
    summary="File read, edit, apply_patch, and delete-file extractors that convert raw tool call args/results into structured ExtractedFileData for the rendering layer.",
    tags=["extraction", "file-operations", "diff-parsing", "rendering-data"],
    complexity="complex",
    base_tags=["extraction", "file-operations", "diff-parsing"],
),
"src-tauri/src/agent_sessions/event_pipeline/extractors/git_artifacts.rs": dict(
    summary="Thin re-export shim exposing the canonical `parse_git_artifacts` Git artifact parser from `orgtrack_core` to the live event pipeline, so live capture, imported history, and DB backfill cannot diverge.",
    tags=["re-export", "git-integration", "compatibility-shim", "extraction"],
    complexity="simple",
    languageNotes="Uses `pub use` re-export to keep a single canonical parser implementation shared across multiple ingestion paths.",
),
"src-tauri/src/agent_sessions/event_pipeline/extractors/helpers.rs": dict(
    summary="Collection of defensive helpers for extracting typed values (strings, numbers, bools, arrays) from serde_json Values/Maps and parsing diff-fence metadata, used across all rendering-data extractors.",
    tags=["utility", "json-parsing", "extraction", "helpers"],
    complexity="moderate",
    base_tags=["utility", "json-parsing", "extraction"],
),
"src-tauri/src/agent_sessions/event_pipeline/extractors/lang.rs": dict(
    summary="Programming-language detection from file extensions plus utilities for stripping editor-style line-number prefixes from pasted code/diff text.",
    tags=["language-detection", "text-processing", "utility", "extraction"],
    complexity="moderate",
    base_tags=["language-detection", "text-processing", "utility"],
),
"src-tauri/src/agent_sessions/event_pipeline/extractors/misc_extractor.rs": dict(
    summary="Extractors for thinking, message, todo, web_search, subagent, delete_file, and the org_task tool family, converting raw tool args/results into their respective ExtractedData variants.",
    tags=["extraction", "tool-parsing", "rendering-data", "task-management"],
    complexity="complex",
    base_tags=["extraction", "tool-parsing", "rendering-data"],
),
"src-tauri/src/agent_sessions/event_pipeline/extractors/mod.rs": dict(
    summary="Public entry point for the rendering-data extractors module; registers the dispatch hook mapping SessionEvent function names to their extractor so downstream code renders events with zero JSON parsing at display time.",
    tags=["entry-point", "extraction", "dispatch", "module-registration"],
    complexity="simple",
),
"src-tauri/src/agent_sessions/event_pipeline/extractors/search_extractor.rs": dict(
    summary="Extractors for search, glob, and list_dir tool calls, converting raw args/results into structured match/entry lists for display.",
    tags=["extraction", "search", "filesystem", "rendering-data"],
    complexity="complex",
    base_tags=["extraction", "search", "filesystem"],
),
"src-tauri/src/agent_sessions/event_pipeline/extractors/shell_extractor.rs": dict(
    summary="Extractors for shell command execution and its async await_output continuation, deriving command, output, exit status, and any git artifacts produced from tool payloads.",
    tags=["extraction", "shell", "git-integration", "rendering-data"],
    complexity="moderate",
    base_tags=["extraction", "shell", "rendering-data"],
),
"src-tauri/src/agent_sessions/event_pipeline/extractors/types.rs": dict(
    summary="Compatibility re-export shim exposing the canonical extracted-rendering-data types from `core_types::extracted` under the legacy `extractors::types` path.",
    tags=["re-export", "compatibility-shim", "type-definition", "extraction"],
    complexity="simple",
),
"src-tauri/src/agent_sessions/event_pipeline/history.rs": dict(
    summary="Rust-native session history querying: filtering, sorting, grouping, and pagination of session records, replacing a large TypeScript useSessionHistory hook implementation (~486 lines of filter/reduce/sort).",
    tags=["query-engine", "session-management", "data-model", "filtering"],
    complexity="complex",
    base_tags=["query-engine", "session-management", "filtering"],
),
"src-tauri/src/agent_sessions/event_pipeline/ingestion/consolidator.rs": dict(
    summary="Merges streaming thinking/message delta chunks into single consolidated events during ingestion; a Rust port of the TypeScript consolidateChunks logic using dual accumulators to handle interleaved thinking+message streams.",
    tags=["streaming", "chunk-merging", "ingestion", "data-transformation"],
    complexity="complex",
    base_tags=["streaming", "chunk-merging", "ingestion"],
),
"src-tauri/src/agent_sessions/event_pipeline/ingestion/function_map.rs": dict(
    summary="Normalizes raw tool/function names from CLI agent chunks into canonical storage names, delegating to the shared `cli_agents::alias_map` single source of truth for consistency with UI routing.",
    tags=["normalization", "aliasing", "ingestion", "canonicalization"],
    complexity="moderate",
    base_tags=["normalization", "aliasing", "ingestion"],
),
"src-tauri/src/agent_sessions/event_pipeline/ingestion/mod.rs": dict(
    summary="Entry point for the event ingestion pipeline; orchestrates consolidation, normalization, tool-call merging, and prompt backfill to turn raw activity chunks into SessionEvents.",
    tags=["entry-point", "pipeline", "ingestion", "orchestration"],
    complexity="moderate",
    base_tags=["pipeline", "ingestion", "orchestration"],
),
"src-tauri/src/agent_sessions/event_pipeline/ingestion/normalizer.rs": dict(
    summary="Converts raw RawActivityChunk records into normalized SessionEvent objects, inferring display variant/status/text and extracting structured metadata (file path, command, call id); a Rust port of the TypeScript normalizers.ts.",
    tags=["normalization", "ingestion", "data-transformation", "event-pipeline"],
    complexity="complex",
    base_tags=["normalization", "ingestion", "event-pipeline"],
),
"src-tauri/src/agent_sessions/event_pipeline/ingestion/prompt_backfill.rs": dict(
    summary="Heuristics for finding and backfilling a meaningful subagent delegation prompt when the original prompt was generic, redacted, or missing, enriching subagent-spawn events after ingestion.",
    tags=["heuristics", "prompt-resolution", "subagent", "ingestion"],
    complexity="moderate",
    base_tags=["heuristics", "prompt-resolution", "subagent"],
),
"src-tauri/src/agent_sessions/event_pipeline/ingestion/tool_call_merger.rs": dict(
    summary="Merges tool_call start (with args) and end (with result) chunk pairs sharing the same call_id into single unified events, for cases where historical/imported data splits a tool call across separate stream events.",
    tags=["merging", "tool-calls", "ingestion", "streaming"],
    complexity="moderate",
    base_tags=["merging", "tool-calls", "ingestion"],
),
"src-tauri/src/agent_sessions/event_pipeline/ingestion/types.rs": dict(
    summary="Defines the raw activity-chunk input type (mirroring the TypeScript ActivityChunk interface) and the IngestionResult summary type produced by the ingestion pipeline.",
    tags=["type-definition", "data-model", "ingestion"],
    complexity="simple",
),
"src-tauri/src/agent_sessions/event_pipeline/mod.rs": dict(
    summary="Root module for the agent-session event pipeline; wires together ingestion, storage, extractors, search, pagination, statistics, and streaming submodules for the full raw-chunk-to-UI event lifecycle.",
    tags=["entry-point", "module-root", "event-pipeline", "orchestration"],
    complexity="simple",
),
"src-tauri/src/agent_sessions/event_pipeline/pagination.rs": dict(
    summary="Cursor-based, filterable pagination over events stored in the EventStore, avoiding full-list transfer to the frontend; supports forward/backward cursors and combinable source/variant/text filters.",
    tags=["pagination", "query-engine", "event-pipeline", "filtering"],
    complexity="complex",
    base_tags=["pagination", "query-engine", "event-pipeline"],
),
"src-tauri/src/agent_sessions/event_pipeline/payload_compaction.rs": dict(
    summary="Compacts oversized event payload fields (message/tool bodies exceeding a size threshold) into a truncated preview plus a lazily-loadable body reference, keeping snapshot/IPC payloads small while preserving reload-on-demand access.",
    tags=["payload-compaction", "performance", "event-pipeline", "snapshotting"],
    complexity="complex",
    base_tags=["payload-compaction", "performance", "event-pipeline"],
),
"src-tauri/src/agent_sessions/event_pipeline/search.rs": dict(
    summary="In-memory full-text search across session chat events (plain, case-sensitive, regex, whole-word modes), replacing a TypeScript linear-scan search hook to avoid IPC-serializing the full event list.",
    tags=["search", "full-text-search", "event-pipeline", "performance"],
    complexity="complex",
    base_tags=["search", "full-text-search", "event-pipeline"],
),
"src-tauri/src/agent_sessions/event_pipeline/session_manager.rs": dict(
    summary="Pure policy layer tracking the active session, a pin set protecting long-running agent sessions from eviction, and an LRU order enforcing a max cached-session limit, decoupled from the per-session EventStore instances themselves.",
    tags=["session-management", "lru-cache", "state-management", "event-pipeline"],
    complexity="moderate",
    base_tags=["session-management", "lru-cache", "state-management"],
),
"src-tauri/src/agent_sessions/event_pipeline/session_providers.rs": dict(
    summary="Defines the SessionProvider trait and its Cursor-IDE and managed-CLI implementations, abstracting per-source differences in session-id matching, cache-save behavior, and history loading for imported/external sessions.",
    tags=["provider-pattern", "session-management", "abstraction", "external-integration"],
    complexity="moderate",
    base_tags=["provider-pattern", "session-management", "abstraction"],
),
"src-tauri/src/agent_sessions/event_pipeline/statistics.rs": dict(
    summary="Aggregates statistics across session records (counts by status/type, file-change totals, per-repo and per-model activity, daily activity buckets, most-impactful sessions) without loading full event data.",
    tags=["statistics", "aggregation", "analytics", "session-management"],
    complexity="complex",
    base_tags=["statistics", "aggregation", "analytics"],
),
"src-tauri/src/agent_sessions/event_pipeline/store/event_ops.rs": dict(
    summary="Single-event and batch mutation operations on EventStore: get/update/upsert, streaming finalization, transcript deduplication, stream-placeholder replacement, shell output/process stamping, and bulk removal/clear.",
    tags=["event-store", "crud", "mutation", "event-pipeline"],
    complexity="complex",
    base_tags=["event-store", "crud", "mutation"],
),
"src-tauri/src/agent_sessions/event_pipeline/store/helpers.rs": dict(
    summary="Pure, store-state-free helper functions for EventStore internals: synthetic/placeholder detection, transcript text/key extraction, and turn-id bookkeeping, kept separate for easy unit testing.",
    tags=["helpers", "event-store", "pure-functions", "testability"],
    complexity="moderate",
    base_tags=["helpers", "event-store", "pure-functions"],
),
"src-tauri/src/agent_sessions/event_pipeline/store/hydration.rs": dict(
    summary="Bulk event loading and merge operations for EventStore: full/round-window hydration, incremental appends, and the two-phase merge path used when paginating a round window of turns.",
    tags=["hydration", "event-store", "merging", "pagination"],
    complexity="complex",
    base_tags=["hydration", "event-store", "merging"],
),
"src-tauri/src/agent_sessions/event_pipeline/store/mod.rs": dict(
    summary="Defines EventStore, the high-performance per-session event storage backed by a Vec plus HashMap id/call-id indexes; declares the submodule split (helpers/hydration/event_ops/tool_ops/turn_ops/repair) implementing its full behavior.",
    tags=["event-store", "data-structure", "entry-point", "event-pipeline"],
    complexity="complex",
    base_tags=["event-store", "data-structure", "entry-point"],
),
"src-tauri/src/agent_sessions/event_pipeline/store/repair.rs": dict(
    summary="One-time post-load repair and cancellation operations run after events are loaded from SQLite, reconciling in-flight state (subagent links, orphaned interactive prompts) lost across a process restart.",
    tags=["repair", "event-store", "post-load", "recovery"],
    complexity="moderate",
    base_tags=["repair", "event-store", "recovery"],
),
"src-tauri/src/agent_sessions/event_pipeline/store/tool_ops.rs": dict(
    summary="Tool-call specific EventStore operations: locating the active spawning tool call and propagating argument/result updates to sibling events sharing the same call_id.",
    tags=["tool-calls", "event-store", "correlation", "event-pipeline"],
    complexity="moderate",
    base_tags=["tool-calls", "event-store", "correlation"],
),
"src-tauri/src/agent_sessions/event_pipeline/store/turn_ops.rs": dict(
    summary="Turn-window management for EventStore: unloading a turn's full event body into a lightweight preview placeholder, and turn-id queries used by round-window pagination.",
    tags=["turn-management", "pagination", "event-store", "memory-optimization"],
    complexity="moderate",
    base_tags=["turn-management", "pagination", "event-store"],
),
"src-tauri/src/agent_sessions/event_pipeline/streaming.rs": dict(
    summary="Compatibility re-export shim exposing the streaming delta-accumulation buffer implementation now owned by `agent_core::foundation::streaming`, keeping legacy `event_pipeline::streaming` import paths working.",
    tags=["re-export", "compatibility-shim", "streaming", "event-pipeline"],
    complexity="simple",
),
"src-tauri/src/agent_sessions/event_pipeline/types.rs": dict(
    summary="Compatibility re-export shim exposing the canonical SessionEvent and related event-store types from `core_types::session_event`, preserving legacy import paths while other crates depend on core_types directly.",
    tags=["re-export", "compatibility-shim", "type-definition", "event-pipeline"],
    complexity="simple",
),
"src-tauri/src/agent_sessions/external_cli_adapter/mod.rs": dict(
    summary="Defines the ExternalCliAdapter trait abstracting per-CLI-agent behavior (session-id namespacing, history loading, subagent prompt resolution) for imported/external CLI sessions such as OpenCode, plus the adapter registry lookup.",
    tags=["provider-pattern", "external-integration", "abstraction", "cli-agents"],
    complexity="simple",
    base_tags=["provider-pattern", "external-integration", "cli-agents"],
),
"src-tauri/src/agent_sessions/external_cli_adapter/opencode.rs": dict(
    summary="OpenCode CLI adapter implementation: maps OpenCode's native session ids to/from the app's imported-session namespace, loads OpenCode history from its SQLite connection, and converts OpenCode activity chunks into SessionEvents.",
    tags=["cli-agents", "external-integration", "opencode", "session-import"],
    complexity="complex",
    base_tags=["cli-agents", "external-integration", "opencode"],
),
}

# ---------- Function-level metadata: path -> {name: (summary, complexity, extra_tags)} ----------
FUNCS = {
"src-tauri/src/agent_sessions/event_pipeline/extractors/file_extractor.rs": {
    "extract_file": ("Extracts and normalizes file-read tool call args/results into ExtractedFileData for display, resolving the file path and content across multiple possible field names.", "complex", []),
    "read_line_metadata": ("Parses optional line-range metadata (start/end line numbers) from a read tool call's arguments.", "simple", []),
    "normalize_edit": ("Normalizes a raw file-edit payload into a canonical old/new text pair for diffing.", "moderate", []),
    "extract_edit": ("Extracts and normalizes file-edit tool call args/results, producing before/after content and diff metadata for the edit display.", "complex", []),
    "extract_apply_patch": ("Parses an apply_patch tool call's unified patch text into structured edit segments for rendering.", "moderate", []),
    "extract_real_apply_patch_result": ("Extracts the actual outcome of an apply_patch tool execution, distinguishing per-file success/failure segments from the raw result payload.", "complex", []),
    "segment_to_edit": ("Converts a single apply_patch result segment into an ExtractedEditData entry, attaching diff and language-detection metadata.", "complex", []),
},
"src-tauri/src/agent_sessions/event_pipeline/extractors/helpers.rs": {
    "safe_str": ("Recursively coerces a JSON value (string, nested object with content/text/message, or array) into a plain string.", "simple", []),
    "parse_diff_start_lines": ("Parses the starting line numbers of hunks out of a unified diff string for use in edit metadata.", "moderate", []),
    "obj_string_array": ("Reads a named field from a JSON object as an array of strings, tolerating scalar or missing values.", "simple", []),
    "parse_json_object_string": ("Attempts to parse a string field as an embedded JSON object, returning None on parse failure.", "simple", []),
    "normalized_result_object": ("Normalizes a tool result payload into a plain JSON object regardless of whether it is wrapped in a success/failure envelope.", "simple", []),
    "get_success_data": ("Extracts the 'success' branch of a tool result payload as a JSON object, handling multiple result envelope shapes.", "moderate", []),
    "get_failure_data": ("Extracts the 'failure'/error branch of a tool result payload as a JSON object, handling multiple result envelope shapes.", "moderate", []),
},
"src-tauri/src/agent_sessions/event_pipeline/extractors/lang.rs": {
    "strip_line_number_prefixes_with_start": ("Strips leading editor-style line-number prefixes from each line of text, validating that the numbering is sequential from a given start.", "moderate", []),
},
"src-tauri/src/agent_sessions/event_pipeline/extractors/misc_extractor.rs": {
    "extract_thinking": ("Extracts reasoning/thinking tool call content into ExtractedThinkingData.", "simple", []),
    "extract_todo": ("Parses a todo-list tool call's args/result into a structured list of todo items, handling multiple raw todo array encodings.", "complex", []),
    "parse_embedded_todo_array": ("Parses a todo array that has been embedded as a JSON string within a result field.", "simple", []),
    "extract_web_search": ("Extracts a web_search tool call's query and result entries into ExtractedWebSearchData.", "moderate", []),
    "extract_org_task_item": ("Extracts a single org_task list item's fields (id, title, status, etc.) from a raw JSON value.", "moderate", []),
    "extract_org_task_args_item": ("Extracts a single org_task item from the tool call's pre-execution `args` payload.", "moderate", []),
    "org_task_error_message": ("Derives a user-facing error message for a failed org_task operation from the raw failure payload.", "simple", []),
    "legacy_task_rejection_guidance": ("Builds guidance text explaining why a legacy-format task operation was rejected.", "simple", []),
    "org_task_operation_outcome": ("Determines the overall outcome (success/rejected/error) of an org_task operation and attaches relevant messaging.", "moderate", []),
    "extract_org_task": ("Extracts a full org_task tool call (args + result) into ExtractedOrgTaskData, combining item parsing and operation-outcome resolution.", "complex", []),
    "extract_subagent": ("Extracts a subagent-spawning tool call's args/result into ExtractedSubagentData, including the delegated task and outcome.", "moderate", ["subagent"]),
    "extract_delete_file": ("Extracts a delete_file tool call's args/result into ExtractedDeleteFileData.", "moderate", ["file-operations"]),
},
"src-tauri/src/agent_sessions/event_pipeline/extractors/search_extractor.rs": {
    "extract_search": ("Extracts a text-search tool call's query, path scope, and result matches into ExtractedSearchData.", "moderate", []),
    "extract_glob": ("Extracts a glob/file-pattern tool call's pattern and matched file list into structured data.", "complex", []),
    "parse_text_entries": ("Parses raw text-based search-result lines into structured entries (file, line number, snippet).", "moderate", []),
    "extract_list_dir": ("Extracts a directory-listing tool call's path and entries (files/dirs) into ExtractedListDirData.", "complex", []),
},
"src-tauri/src/agent_sessions/event_pipeline/extractors/shell_extractor.rs": {
    "extract_shell": ("Extracts a shell-command tool call's command, output, and exit status into ExtractedShellData, including any git artifacts produced.", "complex", []),
    "extract_await": ("Extracts an await_output tool call (polling a previously started shell command) into ExtractedShellData.", "moderate", []),
},
"src-tauri/src/agent_sessions/event_pipeline/history.rs": {
    "query_sessions": ("Filters, sorts, and paginates the full session record list according to a HistoryQuery, returning matched sessions with running/completed/failed counts.", "complex", []),
    "get_recent_sessions": ("Returns the most recently updated sessions, bounded by a count limit.", "simple", []),
    "group_sessions": ("Groups a list of sessions by a date bucket (today/yesterday/this week/etc.) for grouped history display.", "moderate", []),
    "format_group_label": ("Formats a date-group key into a human-readable label such as 'Today' or 'Last 7 Days'.", "simple", []),
},
"src-tauri/src/agent_sessions/event_pipeline/ingestion/consolidator.rs": {
    "consolidate_activity_chunks": ("Consolidates a raw stream of activity chunks into merged events, accumulating and flushing thinking/message deltas at boundaries.", "complex", []),
    "is_message_delta": ("Determines whether a chunk represents an incremental assistant-message delta.", "simple", []),
    "is_legacy_assistant_delta": ("Detects legacy-format assistant message delta chunks predating the current delta schema.", "simple", []),
    "is_thinking_end_marker": ("Detects a chunk that marks the end of a thinking/reasoning stream.", "simple", []),
    "is_complete_message": ("Determines whether a chunk represents a complete (non-delta) assistant message.", "simple", []),
    "is_empty_chunk": ("Determines whether a chunk carries no meaningful content and should be filtered out during consolidation.", "simple", []),
    "has_thinking_text": ("Checks whether an accumulated thinking buffer contains non-empty text.", "simple", []),
    "extract_thinking_content": ("Extracts the thinking/reasoning text content from a chunk.", "simple", []),
    "extract_message_content": ("Extracts the assistant-message text content from a chunk.", "simple", []),
    "dedup_assistant_messages": ("Removes duplicate consecutive assistant messages produced by overlapping stream chunks.", "moderate", []),
},
"src-tauri/src/agent_sessions/event_pipeline/ingestion/function_map.rs": {
    "resolve_function_name": ("Resolves a raw tool/function name (and optional CLI agent context) to its canonical database storage name via the shared alias map.", "moderate", []),
},
"src-tauri/src/agent_sessions/event_pipeline/ingestion/mod.rs": {
    "ingest_raw_chunks_with_prompt_resolver": ("Runs the full ingestion pipeline (consolidate, normalize, merge tool calls, backfill subagent prompts) using a caller-supplied prompt resolver.", "moderate", []),
},
"src-tauri/src/agent_sessions/event_pipeline/ingestion/normalizer.rs": {
    "normalize_chunk": ("Converts a single RawActivityChunk into a SessionEvent, resolving the canonical function name and computing display metadata.", "complex", []),
    "normalize_chunks": ("Normalizes a batch of RawActivityChunks into SessionEvents by mapping normalize_chunk over the collection.", "simple", []),
    "infer_display_variant": ("Infers which UI display variant (tool_call, message, thinking, etc.) a chunk should render as.", "moderate", []),
    "infer_display_status": ("Infers the display status (running/completed/failed/etc.) of a chunk from its action type and result.", "complex", []),
    "is_ask_question_action": ("Determines whether a chunk represents an interactive ask-question action requiring user input.", "moderate", []),
    "has_non_empty_result": ("Checks whether a chunk's result payload contains meaningful (non-empty) data.", "simple", []),
    "infer_activity_status": ("Maps a chunk's raw status/result into the canonical ActivityStatus enum.", "simple", []),
    "infer_display_text": ("Derives the human-readable display text/preview shown for an event from its chunk content and function type.", "complex", []),
    "raw_message_text": ("Extracts the raw, unprocessed message text from a chunk.", "simple", []),
    "extract_text_content": ("Extracts and concatenates text content blocks from a chunk's message/result payload.", "moderate", []),
    "strip_terminal_code_blocks": ("Strips wrapping markdown code-fence syntax from terminal/shell output text.", "simple", []),
    "extract_args": ("Extracts the raw args JSON value from a chunk, defaulting to an empty object.", "simple", []),
    "extract_file_path": ("Extracts a file path from a chunk's args across several possible field name variants.", "simple", []),
    "extract_call_id": ("Extracts the tool-call correlation id from a chunk's args or metadata.", "simple", []),
},
"src-tauri/src/agent_sessions/event_pipeline/ingestion/prompt_backfill.rs": {
    "strip_known_prompt_prelude": ("Strips known boilerplate prelude text from a subagent prompt before further analysis.", "simple", []),
    "prompt_from_history_chunks": ("Searches a session's prior history chunks for the earliest usable, non-generic subagent prompt.", "moderate", []),
    "backfill_subagent_prompts_with_resolver": ("Backfills generic/placeholder subagent prompts in a batch of session events with better prompts resolved via a caller-supplied history resolver.", "moderate", []),
},
"src-tauri/src/agent_sessions/event_pipeline/ingestion/tool_call_merger.rs": {
    "merge_tool_call_pairs": ("Scans a chunk list and merges matching tool_call start/end pairs by call_id into single combined events.", "complex", []),
    "is_tool_call_event": ("Determines whether a chunk represents any kind of tool_call event.", "simple", []),
    "is_tool_call_start": ("Determines whether a chunk is the 'start' half of a split tool_call pair.", "simple", []),
    "is_tool_call_end": ("Determines whether a chunk is the 'end' half of a split tool_call pair.", "simple", []),
    "merge_start_end": ("Combines a matched tool_call start and end chunk into a single merged event carrying both args and result.", "moderate", []),
},
"src-tauri/src/agent_sessions/event_pipeline/pagination.rs": {
    "paginate_events": ("Returns a cursor-paginated, filtered slice of events from the store along with next/prev cursors and the total match count.", "complex", []),
    "count_matching_events": ("Counts how many stored events match a given filter set without materializing them.", "simple", []),
    "get_distinct_functions": ("Computes the distinct set of function names present in the event store along with usage counts, for filter UI population.", "simple", []),
    "matches_filters": ("Evaluates whether a single event matches the combined set of active EventFilters (source, variant, function, path, text, time range).", "moderate", []),
},
"src-tauri/src/agent_sessions/event_pipeline/payload_compaction.rs": {
    "compact_event_for_snapshot": ("Compacts a single event's oversized payload fields for inclusion in a lightweight snapshot, replacing full bodies with size-bounded previews.", "moderate", []),
    "load_event_payload_body": ("Loads back the full-size body of a previously compacted payload field on demand.", "simple", []),
    "compact_display_text": ("Truncates an event's display text to the preview size threshold if it exceeds the compaction limit.", "simple", []),
    "compact_json_string_field": ("Compacts an embedded JSON-string field's value if it exceeds the size threshold, preserving JSON validity.", "simple", []),
    "compact_string_value": ("Truncates a raw string value to the preview byte budget, cutting on a valid character boundary.", "simple", []),
    "compact_extracted": ("Walks an ExtractedData variant's fields, compacting any oversized text/content fields in place for snapshot storage.", "complex", []),
    "compact_optional_string": ("Compacts an Option<String> field, replacing it with a preview if it exceeds the threshold.", "simple", []),
    "payload_string": ("Reads a payload's original field value as a string for size measurement and compaction.", "simple", []),
    "camel_to_snake": ("Converts a camelCase field-path segment to snake_case for payload field lookups.", "simple", []),
},
"src-tauri/src/agent_sessions/event_pipeline/search.rs": {
    "extract_strings_from_value": ("Recursively collects all string leaves from a JSON value into a flat searchable text buffer.", "moderate", []),
    "build_searchable_text": ("Builds the combined searchable text blob for a single event from its display text and extracted-data fields.", "simple", []),
    "floor_char": ("Rounds a byte offset down to the nearest valid UTF-8 character boundary.", "simple", []),
    "ceil_char": ("Rounds a byte offset up to the nearest valid UTF-8 character boundary.", "simple", []),
    "create_snippet": ("Builds a bounded-length text snippet around a match position, with ellipsis truncation at character boundaries.", "moderate", []),
    "find": ("Matches a Matcher::Plain or Matcher::Regex variant against a byte offset in the searchable text, returning the start/end/score of a match.", "moderate", []),
    "build_matcher": ("Constructs a Matcher (plain substring or compiled regex) from the search query and case/regex/whole-word options.", "moderate", []),
    "search_chat_events": ("Runs the configured search over a session's chat-visible events, returning ranked, snippeted results up to a max-results cap.", "moderate", []),
},
"src-tauri/src/agent_sessions/event_pipeline/session_manager.rs": {
    "set_active": ("Marks a session as the active target for commands that omit an explicit session id.", "simple", []),
    "register": ("Registers a newly-seen session with the manager, initializing its LRU/touch state.", "simple", []),
    "touch_lru": ("Moves a session to the most-recently-used end of the LRU order.", "simple", []),
    "enforce_limits": ("Evicts least-recently-used, unpinned sessions once the known-session count exceeds the configured cache limit.", "moderate", []),
},
"src-tauri/src/agent_sessions/event_pipeline/session_providers.rs": {
    "load_history_events": ("Loads prior history events for a session from whichever external CLI adapter matches its imported session id.", "simple", []),
    "subagent_prompt": ("Resolves a subagent's delegation prompt via the matching external CLI adapter.", "simple", []),
    "imported_parent_session_ids": ("Collects the set of imported parent session ids across all registered external CLI adapters.", "simple", []),
},
"src-tauri/src/agent_sessions/event_pipeline/statistics.rs": {
    "compute_session_statistics": ("Computes the full SessionStatistics aggregate (status/type breakdowns, per-repo/model activity, daily timeline, top impactful sessions) from a list of session records.", "complex", []),
    "empty_statistics": ("Returns a zeroed/empty SessionStatistics value for when there are no sessions to aggregate.", "simple", []),
},
"src-tauri/src/agent_sessions/event_pipeline/store/event_ops.rs": {
    "update_by_id": ("Updates an event in place by id, refreshing store indexes.", "simple", []),
    "upsert": ("Inserts a new event or updates an existing one by id, maintaining id/call-id indexes and streaming/version bookkeeping.", "moderate", []),
    "complete_last_running": ("Marks the most recent running tool/task event as completed.", "simple", []),
    "finalize_streaming_events": ("Finalizes any events still marked as streaming when a session's live stream ends, converting them to their terminal display state.", "moderate", []),
    "patch_by_ids": ("Applies a set of field patches to multiple events identified by id.", "simple", []),
    "truncate_before_id": ("Removes all events preceding a given event id, used to trim history before a resumption point.", "simple", []),
    "remove_by_id_prefix": ("Removes all events whose id starts with a given prefix.", "simple", []),
    "remove_by_ids": ("Removes a set of events identified by exact id.", "simple", []),
    "remove_synthetic_user_inputs": ("Removes synthetic/placeholder user-input events matching given criteria from the store.", "moderate", []),
    "replace_and_remove": ("Atomically replaces a set of events with new ones while removing others, reconciling indexes in a single pass.", "moderate", []),
    "update_last_shell_output": ("Appends incremental output to the most recent matching shell command event during live streaming.", "moderate", []),
    "update_last_shell_process": ("Updates process metadata (pid, status, exit code) on the most recent matching shell command event.", "complex", []),
    "update_last_matching_args": ("Updates the args payload of the most recent event matching given function-name criteria.", "moderate", []),
    "clear": ("Removes all events and resets store indexes.", "simple", []),
    "remove_matching_synthetic_transcript_placeholders": ("Removes synthetic stream-transcript placeholder events matching given predicate criteria.", "simple", []),
    "matching_synthetic_transcript_placeholder_ids": ("Collects the ids of synthetic stream-transcript placeholder events matching given criteria.", "simple", []),
    "remove_events_by_ids": ("Removes a batch of events identified by an explicit id list.", "simple", []),
    "replace_duplicate_stream_transcript_in_current_turn": ("Replaces a duplicate/superseded streaming transcript event within the current turn with its authoritative counterpart.", "moderate", []),
    "replace_matching_stream_placeholder": ("Replaces a matching streaming placeholder event with finalized content once the authoritative event arrives.", "complex", []),
    "would_downgrade_terminal_tool_call": ("Checks whether applying an incoming update would downgrade an already-terminal tool-call event's status.", "simple", []),
},
"src-tauri/src/agent_sessions/event_pipeline/store/helpers.rs": {
    "is_synthetic_transcript_placeholder": ("Determines whether an event is a synthetic (not-yet-authoritative) streaming transcript placeholder.", "simple", []),
    "transcript_text": ("Extracts the display transcript text used for deduplication/matching from a session event.", "moderate", []),
    "transcript_message_key": ("Builds a dedup key from a transcript message's source and text for matching duplicate events.", "simple", []),
    "normalized_event_text": ("Returns a whitespace-normalized version of an event's display text for comparison.", "simple", []),
    "is_completed_authoritative_stream_transcript": ("Determines whether an event is a completed, authoritative (non-placeholder) streaming transcript message.", "simple", []),
    "is_authoritative_transcript_message": ("Determines whether an event's source/variant marks it as an authoritative transcript message.", "simple", []),
    "reconcile_loaded_synthetic_transcript_placeholders": ("Reconciles freshly loaded events against previously known synthetic transcript placeholders, dropping stale placeholders superseded by authoritative content.", "moderate", []),
    "is_turn_placeholder": ("Determines whether an event is a turn-body placeholder used by round-window pagination.", "simple", []),
    "placeholder_turn_id": ("Extracts the turn id a placeholder event stands in for.", "simple", []),
    "placeholder_next_turn_id": ("Extracts the id of the turn following a placeholder, for ordering.", "simple", []),
    "loaded_turn_ids_from_events": ("Collects the set of turn ids that have full event bodies currently loaded.", "simple", []),
    "timeline_source_order": ("Returns a stable ordering key for an event's source, used to order concurrent timeline entries deterministically.", "simple", []),
    "stream_placeholder_prefix_for_authoritative": ("Derives the placeholder id prefix that should be reconciled once an authoritative streaming message with a given key arrives.", "simple", []),
},
"src-tauri/src/agent_sessions/event_pipeline/store/hydration.rs": {
    "set_round_window": ("Replaces the store's events with a round-window slice and marks the store as round-window hydrated.", "simple", []),
    "set_with_hydration": ("Replaces the store's events with a caller-specified hydration mode (full, round-window, or live-partial).", "simple", []),
    "append": ("Appends new events to the end of the store, updating indexes and version/change tracking.", "moderate", []),
    "merge_events": ("Merges a batch of events into the store using the default (non-round-window) merge path.", "simple", []),
    "merge_round_window_events": ("Merges a batch of events into the store using the round-window-aware merge path.", "simple", []),
    "merge_events_with_hydration": ("Merges a batch of newly-loaded events into the existing store contents according to the current hydration mode, reconciling placeholders and ordering.", "complex", []),
    "remove_turn_placeholders_for_turns": ("Removes turn-preview placeholder events for a given set of turn ids once their full bodies are loaded.", "moderate", []),
    "sort_round_window_events_by_timeline": ("Sorts a round-window's events into correct timeline order after a partial merge.", "simple", []),
},
"src-tauri/src/agent_sessions/event_pipeline/store/mod.rs": {
    "new": ("Constructs an empty EventStore with fresh indexes and default state.", "simple", []),
    "mark_full_snapshot_emitted": ("Records that a full snapshot has just been emitted, resetting delta tracking.", "simple", []),
    "take_delta_tracking": ("Drains and returns the set of changed/removed event ids accumulated since the last notification.", "simple", []),
    "set_streaming": ("Sets the store's live-streaming flag.", "simple", []),
    "mark_live_partial_if_windowed": ("Downgrades a round-window hydration mode to live-partial once live streaming begins.", "simple", []),
    "mark_removed": ("Records an event id as removed for the next delta notification.", "simple", []),
    "insert_index_entries": ("Inserts a single event's id and call-id into the store's lookup indexes.", "simple", []),
    "rebuild_indexes": ("Rebuilds the id and call-id lookup indexes from the current event list, e.g. after a bulk replace.", "simple", []),
    "cap_events": ("Trims the oldest events once the store exceeds a maximum retained-event cap.", "simple", []),
    "stamp_repo": ("Stamps the store's repo id/path onto an event that lacks one.", "simple", []),
},
"src-tauri/src/agent_sessions/event_pipeline/store/repair.rs": {
    "repair_subagent_links": ("Reconstructs parent/child subagent event links that were not fully persisted before an unexpected process restart.", "complex", []),
    "cancel_orphan_interactive_events": ("Cancels interactive ask-question/approval events left dangling (no response) after a restart.", "moderate", []),
},
"src-tauri/src/agent_sessions/event_pipeline/store/tool_ops.rs": {
    "find_last_spawning_tool": ("Finds the index of the most recent still-running tool_call event matching any of the given function names.", "moderate", []),
    "update_spawning_tool_args": ("Updates the arguments of the last active spawning tool-call event, e.g. as streamed args arrive incrementally.", "complex", []),
    "update_tool_args_by_call_id": ("Updates the arguments of all events sharing a given call_id, propagating updates to placeholder sibling events.", "complex", []),
    "complete_tool_call_by_call_id": ("Marks a tool call and its call_id siblings as completed with a final result.", "moderate", []),
},
"src-tauri/src/agent_sessions/event_pipeline/store/turn_ops.rs": {
    "is_final_reply_candidate": ("Determines whether an event is eligible to be the final-reply summary shown on a collapsed turn placeholder.", "simple", []),
    "mark_turn_preview": ("Marks a turn's placeholder event with preview metadata (summary, event count) before unloading its full body.", "simple", []),
    "unload_turn_body": ("Replaces a turn's full set of events with a single lightweight placeholder to reduce memory for turns outside the active pagination window.", "complex", []),
},
"src-tauri/src/agent_sessions/external_cli_adapter/opencode.rs": {
    "resolve_subagent_prompt_from_conn": ("Resolves a subagent's delegation prompt by querying OpenCode's SQLite connection for the parent task's original request.", "moderate", []),
    "imported_parent_session_id_from_conn": ("Looks up an OpenCode session's parent/spawning session id via a direct SQLite connection query.", "simple", []),
    "resolve_subagent_prompt": ("Opens an OpenCode SQLite connection and delegates to resolve_subagent_prompt_from_conn to resolve a subagent's prompt.", "simple", []),
    "imported_parent_session_id": ("Opens an OpenCode SQLite connection and delegates to imported_parent_session_id_from_conn to resolve a session's parent id.", "simple", []),
    "activity_chunk_to_session_event": ("Converts a raw OpenCode ActivityChunk into a normalized SessionEvent for import into the local event store.", "moderate", []),
},
}

# ---------- Class-level metadata ----------
CLASSES = {
"src-tauri/src/agent_sessions/event_pipeline/history.rs": {
    "SessionRecord": ("Serializable snapshot of a single agent session's metadata (status, repo, timestamps, model, event/file-change counts) used for history views.", "simple", []),
    "HistoryQuery": ("Query parameters (status/type/repo filters, search text, sort, pagination offset/limit) accepted by the session-history query function.", "simple", []),
},
"src-tauri/src/agent_sessions/event_pipeline/session_manager.rs": {
    "SessionStoreManager": ("Manages the set of known/pinned/active sessions and an LRU eviction order across per-session EventStore instances, enforcing a maximum cache size.", "moderate", []),
},
"src-tauri/src/agent_sessions/event_pipeline/session_providers.rs": {
    "SessionProvider": ("Trait describing source-specific behavior (session-id matching, cache-save skipping, history loading, subagent prompt resolution) implemented per session origin (native, Cursor IDE, external CLI).", "moderate", []),
    "CursorIdeProvider": ("Provider implementation matching Cursor-IDE-imported session ids and skipping event-cache persistence for them.", "simple", []),
    "ManagedCliProvider": ("Provider implementation for internally-managed CLI agent sessions (Claude Code, Codex, etc.), which participate in normal event-cache persistence.", "simple", []),
},
"src-tauri/src/agent_sessions/event_pipeline/statistics.rs": {
    "SessionStatistics": ("Aggregate statistics result: totals by status/type, file-change sums, per-repo and per-model activity breakdowns, daily activity timeline, and most-impactful sessions.", "simple", []),
},
"src-tauri/src/agent_sessions/event_pipeline/store/mod.rs": {
    "EventStore": ("Core per-session event storage: a Vec<SessionEvent> with O(1) id/call-id lookup indexes, streaming/hydration-mode state, and change/version tracking for delta notifications.", "complex", []),
},
"src-tauri/src/agent_sessions/external_cli_adapter/mod.rs": {
    "ExternalCliAdapter": ("Trait each external CLI agent integration (e.g. OpenCode) implements to plug into the agent_sessions import pipeline: session id mapping, history loading, and subagent prompt/parent resolution.", "moderate", []),
},
"src-tauri/src/agent_sessions/external_cli_adapter/opencode.rs": {
    "OpenCodeAdapter": ("Concrete ExternalCliAdapter implementation for OpenCode-imported sessions, handling id translation, history loading, and subagent prompt resolution against OpenCode's own SQLite database.", "moderate", []),
},
}

# ---------- Explicit high-confidence cross-file calls edges ----------
CALL_EDGES = [
    ("src-tauri/src/agent_sessions/event_pipeline/extractors/file_extractor.rs", "extract_apply_patch",
     "src-tauri/src/agent_sessions/event_pipeline/extractors/helpers.rs", "parse_diff_start_lines"),
    ("src-tauri/src/agent_sessions/event_pipeline/extractors/file_extractor.rs", "extract_edit",
     "src-tauri/src/agent_sessions/event_pipeline/extractors/helpers.rs", "get_success_data"),
    ("src-tauri/src/agent_sessions/event_pipeline/extractors/file_extractor.rs", "extract_edit",
     "src-tauri/src/agent_sessions/event_pipeline/extractors/helpers.rs", "parse_diff_start_lines"),
    ("src-tauri/src/agent_sessions/event_pipeline/extractors/file_extractor.rs", "extract_file",
     "src-tauri/src/agent_sessions/event_pipeline/extractors/helpers.rs", "get_success_data"),
    ("src-tauri/src/agent_sessions/event_pipeline/extractors/file_extractor.rs", "extract_file",
     "src-tauri/src/agent_sessions/event_pipeline/extractors/lang.rs", "strip_line_number_prefixes_with_start"),
    ("src-tauri/src/agent_sessions/event_pipeline/extractors/file_extractor.rs", "extract_real_apply_patch_result",
     "src-tauri/src/agent_sessions/event_pipeline/extractors/helpers.rs", "parse_diff_start_lines"),
    ("src-tauri/src/agent_sessions/event_pipeline/extractors/file_extractor.rs", "segment_to_edit",
     "src-tauri/src/agent_sessions/event_pipeline/extractors/helpers.rs", "parse_diff_start_lines"),
    ("src-tauri/src/agent_sessions/event_pipeline/extractors/misc_extractor.rs", "extract_org_task",
     "src-tauri/src/agent_sessions/event_pipeline/extractors/helpers.rs", "normalized_result_object"),
    ("src-tauri/src/agent_sessions/event_pipeline/extractors/misc_extractor.rs", "extract_org_task_args_item",
     "src-tauri/src/agent_sessions/event_pipeline/extractors/helpers.rs", "obj_string_array"),
    ("src-tauri/src/agent_sessions/event_pipeline/extractors/misc_extractor.rs", "extract_org_task_item",
     "src-tauri/src/agent_sessions/event_pipeline/extractors/helpers.rs", "obj_string_array"),
    ("src-tauri/src/agent_sessions/event_pipeline/extractors/shell_extractor.rs", "extract_shell",
     "src-tauri/src/agent_sessions/event_pipeline/extractors/helpers.rs", "get_failure_data"),
    ("src-tauri/src/agent_sessions/event_pipeline/extractors/shell_extractor.rs", "extract_shell",
     "src-tauri/src/agent_sessions/event_pipeline/extractors/helpers.rs", "get_success_data"),
    ("src-tauri/src/agent_sessions/event_pipeline/ingestion/normalizer.rs", "normalize_chunk",
     "src-tauri/src/agent_sessions/event_pipeline/ingestion/function_map.rs", "resolve_function_name"),
    ("src-tauri/src/agent_sessions/event_pipeline/store/event_ops.rs", "replace_duplicate_stream_transcript_in_current_turn",
     "src-tauri/src/agent_sessions/event_pipeline/store/helpers.rs", "is_completed_authoritative_stream_transcript"),
    ("src-tauri/src/agent_sessions/event_pipeline/store/hydration.rs", "set_with_hydration",
     "src-tauri/src/agent_sessions/event_pipeline/store/helpers.rs", "reconcile_loaded_synthetic_transcript_placeholders"),
    ("src-tauri/src/agent_sessions/event_pipeline/ingestion/mod.rs", "ingest_raw_chunks_with_prompt_resolver",
     "src-tauri/src/agent_sessions/event_pipeline/ingestion/consolidator.rs", "consolidate_activity_chunks"),
    ("src-tauri/src/agent_sessions/event_pipeline/ingestion/mod.rs", "ingest_raw_chunks_with_prompt_resolver",
     "src-tauri/src/agent_sessions/event_pipeline/ingestion/prompt_backfill.rs", "backfill_subagent_prompts_with_resolver"),
    ("src-tauri/src/agent_sessions/event_pipeline/ingestion/mod.rs", "ingest_raw_chunks_with_prompt_resolver",
     "src-tauri/src/agent_sessions/event_pipeline/ingestion/tool_call_merger.rs", "merge_tool_call_pairs"),
    ("src-tauri/src/agent_sessions/event_pipeline/store/hydration.rs", "merge_events_with_hydration",
     "src-tauri/src/agent_sessions/event_pipeline/store/event_ops.rs", "would_downgrade_terminal_tool_call"),
    ("src-tauri/src/agent_sessions/external_cli_adapter/opencode.rs", "resolve_subagent_prompt",
     "src-tauri/src/agent_sessions/event_pipeline/ingestion/prompt_backfill.rs", "prompt_from_history_chunks"),
]

# cross-batch call edge (verified via callGraph + neighborMap)
CROSS_BATCH_CALL_EDGES = [
    ("src-tauri/src/agent_sessions/event_pipeline/history.rs", "query_sessions",
     "src-tauri/src/agent_sessions/session_directory/status.rs", "is_active_status"),
]

def fn_id(path, name):
    return f"function:{path}:{name}"

def cls_id(path, name):
    return f"class:{path}:{name}"

def file_id(path):
    return f"file:{path}"

nodes = []
edges = []
seen_node_ids = set()

def add_node(n):
    assert n["id"] not in seen_node_ids, f"dup node {n['id']}"
    seen_node_ids.add(n["id"])
    nodes.append(n)

def add_edge(source, target, etype, weight):
    edges.append({"source": source, "target": target, "type": etype, "direction": "forward", "weight": weight})

order = [r["path"] for r in d["results"]]

for path in order:
    r = results_by_path[path]
    meta = FILES[path]
    fnode = {
        "id": file_id(path),
        "type": "file",
        "name": os.path.basename(path),
        "filePath": path,
        "summary": meta["summary"],
        "tags": meta["tags"],
        "complexity": meta["complexity"],
    }
    if "languageNotes" in meta:
        fnode["languageNotes"] = meta["languageNotes"]
    add_node(fnode)

    exports = set(e["name"] for e in r.get("exports", []))

    # functions
    fn_defs = {f["name"]: f for f in r.get("functions", [])}
    for name, (summary, complexity, extra_tags) in FUNCS.get(path, {}).items():
        f = fn_defs[name]
        base_tags = meta.get("base_tags", meta["tags"][:3])
        tags = list(dict.fromkeys(base_tags + extra_tags))[:5]
        if len(tags) < 3:
            tags = list(dict.fromkeys(tags + meta["tags"]))[:5]
        node = {
            "id": fn_id(path, name),
            "type": "function",
            "name": name,
            "filePath": path,
            "lineRange": [f["startLine"], f["endLine"]],
            "summary": summary,
            "tags": tags,
            "complexity": complexity,
        }
        add_node(node)
        add_edge(file_id(path), node["id"], "contains", 1.0)
        if name in exports:
            add_edge(file_id(path), node["id"], "exports", 0.8)

    # classes
    cls_defs = {c["name"]: c for c in r.get("classes", [])}
    for name, (summary, complexity, extra_tags) in CLASSES.get(path, {}).items():
        c = cls_defs[name]
        base_tags = meta.get("base_tags", meta["tags"][:3])
        tags = list(dict.fromkeys(base_tags + extra_tags))[:5]
        if len(tags) < 3:
            tags = list(dict.fromkeys(tags + meta["tags"]))[:5]
        node = {
            "id": cls_id(path, name),
            "type": "class",
            "name": name,
            "filePath": path,
            "lineRange": [c["startLine"], c["endLine"]],
            "summary": summary,
            "tags": tags,
            "complexity": complexity,
        }
        add_node(node)
        add_edge(file_id(path), node["id"], "contains", 1.0)
        if name in exports:
            add_edge(file_id(path), node["id"], "exports", 0.8)

    # imports (1:1 from batchImportData)
    for target in import_data.get(path, []):
        add_edge(file_id(path), file_id(target), "imports", 0.7)

# calls edges
for (sp, sn, tp, tn) in CALL_EDGES:
    add_edge(fn_id(sp, sn), fn_id(tp, tn), "calls", 0.8)

for (sp, sn, tp, tn) in CROSS_BATCH_CALL_EDGES:
    add_edge(fn_id(sp, sn), fn_id(tp, tn), "calls", 0.8)

print("TOTAL NODES", len(nodes))
print("TOTAL EDGES", len(edges))

# validate import edge count matches batchImportData sum for files in this batch
expected_imports = sum(len(v) for k, v in import_data.items() if k in order)
actual_imports = sum(1 for e in edges if e["type"] == "imports")
print("expected imports", expected_imports, "actual imports", actual_imports)
assert expected_imports == actual_imports

# ---------- Partition into parts ----------
NODE_LIMIT = 60
EDGE_LIMIT = 120
node_count = len(nodes)
edge_count = len(edges)
parts = max(1, math.ceil(max(node_count / NODE_LIMIT, edge_count / EDGE_LIMIT)))
print("parts:", parts)

if parts == 1:
    out = {"nodes": nodes, "edges": edges}
    outpath = os.path.join(OUTDIR, "batch-14.json")
    with open(outpath, "w") as fh:
        json.dump(out, fh, indent=2)
    print("WROTE", outpath, len(nodes), len(edges))
else:
    # partition files alphabetically into `parts` groups
    sorted_files = sorted(order)
    chunk_size = math.ceil(len(sorted_files) / parts)
    file_to_part = {}
    for i, p in enumerate(sorted_files):
        file_to_part[p] = i // chunk_size

    # node -> part (by filePath)
    node_part = {}
    for n in nodes:
        fp = n.get("filePath", n["id"].split(":", 2)[1] if n["id"].count(":") >= 2 else None)
        # for function/class nodes, filePath not required but we set it above for all
        fp = n.get("filePath")
        node_part[n["id"]] = file_to_part[fp]

    part_nodes = {i: [] for i in range(parts)}
    part_edges = {i: [] for i in range(parts)}
    for n in nodes:
        part_nodes[node_part[n["id"]]].append(n)
    for e in edges:
        # edge goes to source's part
        src_part = node_part.get(e["source"])
        if src_part is None:
            # source refers to a node outside batch (shouldn't happen here)
            src_part = 0
        part_edges[src_part].append(e)

    for i in range(parts):
        out = {"nodes": part_nodes[i], "edges": part_edges[i]}
        outpath = os.path.join(OUTDIR, f"batch-14-part-{i+1}.json")
        with open(outpath, "w") as fh:
            json.dump(out, fh, indent=2)
        print("WROTE", outpath, len(part_nodes[i]), len(part_edges[i]))

# sanity: every function/class in FUNCS/CLASSES exists in extraction results
for path, fmap in FUNCS.items():
    fn_names = set(f["name"] for f in results_by_path[path].get("functions", []))
    for name in fmap:
        assert name in fn_names, f"missing fn {name} in {path}"
for path, cmap in CLASSES.items():
    cls_names = set(c["name"] for c in results_by_path[path].get("classes", []))
    for name in cmap:
        assert name in cls_names, f"missing class {name} in {path}"

print("OK")
