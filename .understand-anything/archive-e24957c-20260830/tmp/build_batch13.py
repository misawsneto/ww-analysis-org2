import json

FILTERED = json.load(open('/home/misael/pj/gui-repos/ORG2/.understand-anything/tmp/ua-batch13-filtered.json'))
INPUT = json.load(open('/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate/batch-inputs/batch-13.input.json'))
BID = INPUT['batchImportData']

def fcx(n):
    return 'simple' if n < 50 else ('moderate' if n <= 200 else 'complex')

def icx(size):
    return 'simple' if size < 15 else ('moderate' if size <= 60 else 'complex')

FILE_META = {
"src-tauri/src/agent_sessions/cli/platform_adapters/mod.rs": (
  "Module root that declares and re-exports platform-specific CLI agent adapters (Claude Code, Codex, Cursor, Kiro) plus shared native webview OAuth session helpers.",
  ["barrel", "module-root", "platform-adapters", "cli-agent"]),
"src-tauri/src/agent_sessions/cli/platform_adapters/webview_session.rs": (
  "Provides native webview helpers to clear OAuth browser sessions and shared HTTP cookies scoped to specific domains during CLI agent account switching.",
  ["oauth", "webview", "session-management", "native-integration"]),
"src-tauri/src/agent_sessions/cli/session_runner/command.rs": (
  "Builds the executable command, arguments and environment needed to launch a CLI coding agent (Claude Code, Codex, Cursor, etc.), applying launch-profile overrides and model-specific mappings.",
  ["command-builder", "cli-agent", "launch-profile"]),
"src-tauri/src/agent_sessions/cli/session_runner/context_bridge.rs": (
  "Builds a condensed textual context bridge from a CLI session's prior chunks, used to prime resumed or handed-off agent sessions.",
  ["context-building", "cli-agent", "session"]),
"src-tauri/src/agent_sessions/cli/session_runner/cursor_usage.rs": (
  "Fetches Cursor CLI usage/quota data for a session by resolving the account's session token and calling the Cursor usage API.",
  ["cursor", "api-client", "usage-tracking"]),
"src-tauri/src/agent_sessions/cli/session_runner/helpers.rs": (
  "Shared helpers for streaming CLI agent output chunks: emitting to the frontend, persisting to the event store, tracking live status, file-edit snapshots, and attached images.",
  ["streaming", "event-pipeline", "cli-agent"]),
"src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs": (
  "Defines CLI agent launch-profile data models (permission modes, default args/env per mode, per-agent overrides) and helper accessors for resolving effective launch configuration.",
  ["data-model", "launch-profile", "configuration", "cli-agent"]),
"src-tauri/src/agent_sessions/cli/session_runner/lifecycle.rs": (
  "Manages CLI agent process lifecycle: signaling/terminating process trees, killing running agents, cancelling sessions, and cleaning up Cursor config directories.",
  ["process-management", "lifecycle", "cli-agent"]),
"src-tauri/src/agent_sessions/cli/session_runner/mod.rs": (
  "Module root that wires together the session_runner submodules (command building, context bridge, cursor usage, helpers, launch profiles, lifecycle, oauth setup, plan approval, proxy release, session execution, token sync).",
  ["barrel", "module-root", "orchestration", "cli-agent"]),
"src-tauri/src/agent_sessions/cli/session_runner/oauth_setup.rs": (
  "Detects CLI OAuth failures and API-overload errors in streamed output and drives retry logic, including refreshing OAuth credentials and writing CLI auth files.",
  ["oauth", "retry-logic", "cli-agent"]),
"src-tauri/src/agent_sessions/cli/session_runner/plan_approval.rs": (
  "Detects and registers 'plan' artifacts produced by CLI agents in Plan mode so they can be surfaced to the user for approval.",
  ["plan-mode", "approval-workflow", "cli-agent"]),
"src-tauri/src/agent_sessions/cli/session_runner/proxy_release.rs": (
  "Releases proxy API-key tokens that were checked out for a CLI session once the session finishes or is cancelled.",
  ["proxy", "token-management", "cleanup"]),
"src-tauri/src/agent_sessions/cli/session_runner/session.rs": (
  "Implements the core CLI agent session execution loop: spawns the CLI process, streams and parses its output, manages OAuth/model setup (including OpenCode/Zenmux profile setup), and persists resulting events.",
  ["cli-agent", "orchestration", "session-execution", "entry-point"]),
"src-tauri/src/agent_sessions/cli/session_runner/token_sync.rs": (
  "Synchronizes a freshly-launched Codex CLI OAuth access token back into the app's key vault so it stays available for API use.",
  ["oauth", "token-sync", "key-vault"]),
"src-tauri/src/agent_sessions/cli/skill_sync.rs": (
  "Syncs Orgii project skills and coding conventions into each CLI agent's expected rule/skill file locations (e.g. CLAUDE.md, .cursor/rules, AGENTS.md) within a workspace.",
  ["skills", "conventions", "cli-agent", "file-sync"]),
"src-tauri/src/agent_sessions/cli/tui_bridge.rs": (
  "Bridges native TUI (terminal UI) session state/status events into Orgii's session live-status tracking, translating TUI agent bindings into UI status updates.",
  ["tui", "status-bridge", "cli-agent"]),
"src-tauri/src/agent_sessions/cli/types.rs": (
  "Defines core CLI session enums SessionStatus (lifecycle state) and SessionRunner (execution transport), with parsing and display trait implementations.",
  ["data-model", "enum", "cli-agent", "type-definition"]),
"src-tauri/src/agent_sessions/event_pipeline/agent_core_bridge.rs": (
  "Adapter layer bridging the generic agent-core event push/notify/tool-call API onto Orgii's per-session event store, handling tool-call completion, streaming placeholders, plan-revision finalization, and stranded-event repair.",
  ["event-pipeline", "adapter", "agent-core"]),
"src-tauri/src/agent_sessions/event_pipeline/analytics.rs": (
  "Computes analytics (tool usage, file changes, conversation stats, token usage, timeline buckets, error rates) for a single session or aggregated across multiple sessions from their event streams.",
  ["analytics", "event-pipeline", "aggregation"]),
"src-tauri/src/agent_sessions/event_pipeline/commands/analytics.rs": (
  "Tauri command handlers exposing session analytics computation (single, cached, and multi-session) to the frontend.",
  ["tauri-command", "analytics", "api-handler"]),
"src-tauri/src/agent_sessions/event_pipeline/commands/batch_update.rs": (
  "Tauri command handlers for batch/targeted mutations of a session's event store: completing running tasks, patching/removing events by id, updating active-task args, and updating shell process state.",
  ["tauri-command", "event-mutation", "api-handler"]),
"src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs": (
  "Bridges the in-memory event store to the on-disk/SQLite event cache: loading/saving session events, full-text search, per-event payload loading, and full-session import/export.",
  ["tauri-command", "caching", "persistence"]),
"src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs": (
  "Converts between the persisted cached-event format and the in-memory SessionEvent model, including deduplication of tool calls, subagent-link backfilling, and compact-boundary event merging.",
  ["event-pipeline", "serialization", "deduplication"]),
"src-tauri/src/agent_sessions/event_pipeline/commands/extractors.rs": (
  "Tauri command handlers for extracting normalized per-event or windowed data payloads from a session's event store.",
  ["tauri-command", "extraction", "api-handler"]),
"src-tauri/src/agent_sessions/event_pipeline/commands/history.rs": (
  "Tauri command handlers for querying session history: filtering/searching sessions, grouping, computing statistics, and resolving parent/child session relationships.",
  ["tauri-command", "history", "session-management"]),
"src-tauri/src/agent_sessions/event_pipeline/commands/ingestion.rs": (
  "Tauri command handlers that ingest and normalize raw CLI output chunks into session events.",
  ["tauri-command", "ingestion", "api-handler"]),
"src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs": (
  "Central Tauri command module for the event-pipeline event store: manages EventStoreState, snapshot/notify scheduling, retrying persistence, runtime-artifact session records, and re-exports all sibling command submodules.",
  ["tauri-command", "event-store", "orchestration"]),
"src-tauri/src/agent_sessions/event_pipeline/commands/pagination.rs": (
  "Tauri command handlers for paginated and filtered access to a session's events, including distinct-function counts.",
  ["tauri-command", "pagination", "api-handler"]),
"src-tauri/src/agent_sessions/event_pipeline/commands/search.rs": (
  "Tauri command handler for full-text search over a session's chat events.",
  ["tauri-command", "search", "api-handler"]),
"src-tauri/src/agent_sessions/event_pipeline/commands/session_manager.rs": (
  "Tauri command handlers for switching, pinning/unpinning, evicting, and buffering events for sessions tracked by the event-store session manager.",
  ["tauri-command", "session-management", "api-handler"]),
"src-tauri/src/agent_sessions/event_pipeline/commands/snapshot.rs": (
  "Tauri command handlers for retrieving a session's current event-store snapshot, raw events, or a markdown export.",
  ["tauri-command", "snapshot", "api-handler"]),
"src-tauri/src/agent_sessions/event_pipeline/commands/store_commands.rs": (
  "Tauri command handlers for core mutating operations on a session's event store: set/append/upsert/update/merge/clear/truncate, plus repo-context configuration and streaming-state toggling.",
  ["tauri-command", "event-store", "api-handler"]),
"src-tauri/src/agent_sessions/event_pipeline/commands/turn_window.rs": (
  "Builds and loads paginated 'turn windows' (grouped user/assistant turns) for a session, including synthetic turn-header and placeholder events and lazy body loading.",
  ["tauri-command", "pagination", "turn-window"]),
"src-tauri/src/agent_sessions/event_pipeline/derived.rs": (
  "Computes derived, display-oriented state from a session's raw events: chat/simulator visibility filters, display status/variant mapping, canvas preview, and simulator preview indexes.",
  ["derived-state", "view-model", "event-pipeline"]),
"src-tauri/src/agent_sessions/event_pipeline/extractors/extractors.rs": (
  "Extracts normalized display data, including tool-call-specific args/result summaries, from raw session events in single and batch form for lightweight frontend consumption.",
  ["event-pipeline", "extraction"]),
}

FUNC_META = {
("src-tauri/src/agent_sessions/cli/platform_adapters/webview_session.rs", "clear_oauth_browser_session_native"): (
  "Clears the native OAuth webview's browsing session (cache/cookies) for the given domains, used when signing a CLI agent account out.", ["oauth", "webview", "cleanup"]),
("src-tauri/src/agent_sessions/cli/platform_adapters/webview_session.rs", "clear_shared_http_cookies"): (
  "Removes cookies from Tauri's shared HTTP cookie store that match any of the given owned domains, used to fully sign a CLI agent out.", ["oauth", "cookies", "cleanup"]),

("src-tauri/src/agent_sessions/cli/session_runner/command.rs", "build_command_with_launch_profile"): (
  "Assembles the full CLI invocation (binary, args, env vars) for a given agent/model/mode/repo combination, applying launch-profile overrides and model-specific mappings.", ["command-builder", "orchestration"]),
("src-tauri/src/agent_sessions/cli/session_runner/command.rs", "map_codex_model_variant"): (
  "Maps a requested Codex model identifier to its concrete Codex CLI model/config variant.", ["model-mapping"]),
("src-tauri/src/agent_sessions/cli/session_runner/command.rs", "claude_effort_token"): (
  "Extracts the reasoning-effort suffix token (e.g. high/medium/low) from a Claude model identifier.", ["model-mapping", "parsing"]),
("src-tauri/src/agent_sessions/cli/session_runner/command.rs", "map_claude_model_variant"): (
  "Maps a Claude model identifier to its concrete CLI model variant and effort settings.", ["model-mapping"]),
("src-tauri/src/agent_sessions/cli/session_runner/command.rs", "split_claude_effort"): (
  "Splits a Claude model string into its base model name and effort suffix.", ["parsing", "model-mapping"]),
("src-tauri/src/agent_sessions/cli/session_runner/command.rs", "create_parser"): (
  "Instantiates the appropriate CLI output parser for a given agent and session id.", ["factory", "parser"]),

("src-tauri/src/agent_sessions/cli/session_runner/context_bridge.rs", "chunk_text"): (
  "Extracts the plain text content from a session chunk.", ["parsing"]),
("src-tauri/src/agent_sessions/cli/session_runner/context_bridge.rs", "chunk_role"): (
  "Determines the conversational role (user/assistant/etc.) of a session chunk.", ["parsing"]),
("src-tauri/src/agent_sessions/cli/session_runner/context_bridge.rs", "build_context_bridge"): (
  "Builds a summarized text context bridge from a session's historical chunks for reuse in a new or resumed run.", ["context-building", "orchestration"]),

("src-tauri/src/agent_sessions/cli/session_runner/cursor_usage.rs", "fetch_cursor_usage_for_session"): (
  "Fetches and records Cursor CLI usage statistics for a running session using the resolved account token.", ["api-client", "usage"]),
("src-tauri/src/agent_sessions/cli/session_runner/cursor_usage.rs", "resolve_cursor_session_token"): (
  "Resolves the Cursor session token for a given account id, used to authenticate usage API calls.", ["auth", "token-resolution"]),

("src-tauri/src/agent_sessions/cli/session_runner/helpers.rs", "strip_ide_context"): (
  "Strips injected IDE-context wrapper markup from a raw CLI input string before persisting it.", ["parsing", "sanitization"]),
("src-tauri/src/agent_sessions/cli/session_runner/helpers.rs", "emit_chunk"): (
  "Core streaming entry point that emits a CLI output chunk to the frontend and persists it into the session's event store.", ["streaming", "event-emission"]),
("src-tauri/src/agent_sessions/cli/session_runner/helpers.rs", "broadcast_streaming_complete"): (
  "Broadcasts a streaming-complete event of a given stream type to the frontend for a session.", ["streaming", "event-emission"]),
("src-tauri/src/agent_sessions/cli/session_runner/helpers.rs", "persist_and_broadcast_streaming_complete"): (
  "Persists a completed streaming chunk to the event store and then broadcasts its completion.", ["streaming", "persistence"]),
("src-tauri/src/agent_sessions/cli/session_runner/helpers.rs", "persist_streaming_complete_chunk"): (
  "Persists a finalized streaming chunk (its completion event) into the session's event store.", ["persistence"]),
("src-tauri/src/agent_sessions/cli/session_runner/helpers.rs", "flush_and_broadcast"): (
  "Flushes any buffered streaming chunks for a session and broadcasts pending completion events.", ["streaming", "flush"]),
("src-tauri/src/agent_sessions/cli/session_runner/helpers.rs", "clear_live_status"): (
  "Clears the live status indicator for a running CLI session/agent pairing.", ["status", "cleanup"]),
("src-tauri/src/agent_sessions/cli/session_runner/helpers.rs", "snapshot_cli_file_edit"): (
  "Creates a file-edit snapshot (before/after) for a CLI-driven file edit chunk within a repo, used for diff/undo support.", ["snapshot", "file-edit"]),
("src-tauri/src/agent_sessions/cli/session_runner/helpers.rs", "persist_attached_images"): (
  "Persists images attached to a session's user turn to disk/storage.", ["persistence", "images"]),

("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "cli_binary_id_for_agent"): (
  "Returns the CLI binary identifier used to invoke the given agent type.", ["agent-mapping"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "defaults_for_agent"): (
  "Returns the built-in launch-profile defaults for a given agent type.", ["defaults"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "default_profile_for_mode"): (
  "Returns the default mode-specific profile settings for a given permission mode.", ["defaults"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "supports_permission_mode"): (
  "Checks whether a given agent's defaults support a specific permission mode.", ["permission-mode"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "supported_permission_modes"): (
  "Lists the permission modes supported by an agent's defaults.", ["permission-mode"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "default_permission_mode"): (
  "Determines the default permission mode for an agent's defaults.", ["permission-mode"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "mode_defaults_view"): (
  "Builds a read-only serializable view of the mode defaults (args/env) for display to the frontend.", ["view-model"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "default_args_for_mode"): (
  "Returns the default CLI arguments for a given permission mode.", ["defaults"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "default_env_for_mode"): (
  "Returns the default environment variables for a given permission mode.", ["defaults"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "static_env_to_map"): (
  "Converts a static list of key/value env pairs into a HashMap.", ["utility"]),

("src-tauri/src/agent_sessions/cli/session_runner/lifecycle.rs", "terminate_process_tree"): (
  "Terminates a process and its child process tree by pid, used to fully stop a spawned CLI agent.", ["process-management"]),
("src-tauri/src/agent_sessions/cli/session_runner/lifecycle.rs", "kill_running_agent"): (
  "Kills the currently running CLI agent process associated with a session.", ["process-management"]),
("src-tauri/src/agent_sessions/cli/session_runner/lifecycle.rs", "cancel_session"): (
  "Cancels an in-progress CLI session, terminating its process and recording the cancellation reason.", ["session-lifecycle"]),
("src-tauri/src/agent_sessions/cli/session_runner/lifecycle.rs", "cleanup_cursor_config_dir"): (
  "Removes the temporary Cursor CLI config directory created for a session.", ["cleanup"]),

("src-tauri/src/agent_sessions/cli/session_runner/oauth_setup.rs", "is_cli_oauth_failure_message"): (
  "Detects whether a message string indicates a CLI OAuth authentication failure.", ["oauth", "detection"]),
("src-tauri/src/agent_sessions/cli/session_runner/oauth_setup.rs", "chunk_error_message"): (
  "Extracts an error message string from a CLI output chunk, if present.", ["parsing"]),
("src-tauri/src/agent_sessions/cli/session_runner/oauth_setup.rs", "is_api_overloaded_message"): (
  "Detects whether a message indicates the upstream API is overloaded.", ["detection"]),
("src-tauri/src/agent_sessions/cli/session_runner/oauth_setup.rs", "is_retryable_overloaded_chunk"): (
  "Checks whether a CLI output chunk represents a retryable API-overloaded error.", ["retry-logic"]),
("src-tauri/src/agent_sessions/cli/session_runner/oauth_setup.rs", "is_cli_oauth_stderr_retry_candidate"): (
  "Determines whether a CLI process's stderr/exit-code combination is a candidate for an OAuth retry.", ["retry-logic"]),
("src-tauri/src/agent_sessions/cli/session_runner/oauth_setup.rs", "is_retryable_cli_oauth_failure_chunk"): (
  "Checks whether a chunk represents a retryable CLI OAuth failure for the given agent/key source.", ["retry-logic"]),
("src-tauri/src/agent_sessions/cli/session_runner/oauth_setup.rs", "is_cli_chunk_replay_unsafe"): (
  "Determines whether replaying a CLI chunk would be unsafe (e.g. contains side-effecting output).", ["safety-check"]),
("src-tauri/src/agent_sessions/cli/session_runner/oauth_setup.rs", "sanitize_cli_oauth_env_for_child"): (
  "Sanitizes OAuth-related environment variables before passing them to a spawned CLI child process.", ["sanitization", "security"]),
("src-tauri/src/agent_sessions/cli/session_runner/oauth_setup.rs", "write_codex_cli_auth_file"): (
  "Writes a Codex CLI auth file to disk for the given account so the CLI can authenticate.", ["oauth", "file-io"]),
("src-tauri/src/agent_sessions/cli/session_runner/oauth_setup.rs", "refresh_cli_oauth_for_retry"): (
  "Refreshes OAuth credentials for a CLI agent and updates environment variables before a retry attempt.", ["oauth", "retry-logic"]),

("src-tauri/src/agent_sessions/cli/session_runner/plan_approval.rs", "plan_candidate_path_from_chunk"): (
  "Extracts a candidate plan file path from a CLI output chunk relative to the working directory.", ["parsing"]),
("src-tauri/src/agent_sessions/cli/session_runner/plan_approval.rs", "is_successful_mode_tool"): (
  "Checks whether a chunk represents a successful tool call for a given tool name in the agent's mode.", ["detection"]),
("src-tauri/src/agent_sessions/cli/session_runner/plan_approval.rs", "plan_title_from_content"): (
  "Derives a short plan title from a plan's content text.", ["content-building"]),
("src-tauri/src/agent_sessions/cli/session_runner/plan_approval.rs", "looks_like_buildable_plan_body"): (
  "Heuristically checks whether a text block looks like a well-formed, approvable plan body.", ["heuristic"]),
("src-tauri/src/agent_sessions/cli/session_runner/plan_approval.rs", "create_plan_content_from_chunk"): (
  "Builds the plan content payload from a CLI output chunk.", ["content-building"]),
("src-tauri/src/agent_sessions/cli/session_runner/plan_approval.rs", "synthetic_cli_plan_path"): (
  "Generates a synthetic file path used to represent an ad-hoc plan not backed by a real file.", ["synthetic-artifact"]),
("src-tauri/src/agent_sessions/cli/session_runner/plan_approval.rs", "register_synthetic_cli_plan_approval"): (
  "Registers a synthetic plan-approval event for a plan that wasn't written to a real file.", ["approval-workflow"]),
("src-tauri/src/agent_sessions/cli/session_runner/plan_approval.rs", "plan_content_from_successful_write_chunk"): (
  "Extracts plan content from a chunk representing a successful plan-file write.", ["content-building"]),
("src-tauri/src/agent_sessions/cli/session_runner/plan_approval.rs", "register_cli_plan_approval"): (
  "Registers a plan-approval event for a session based on a detected plan file write.", ["approval-workflow"]),

("src-tauri/src/agent_sessions/cli/session_runner/proxy_release.rs", "release_proxy_token_for_session"): (
  "Releases the proxy token checked out for a session, returning it to the pool.", ["token-management"]),

("src-tauri/src/agent_sessions/cli/session_runner/session.rs", "cli_exec_mode_bridge"): (
  "Bridges a session's execution mode into the parameters expected by the CLI process spawner.", ["mode-mapping"]),
("src-tauri/src/agent_sessions/cli/session_runner/session.rs", "opencode_zenmux_config_payload"): (
  "Builds the Zenmux provider config payload injected into OpenCode's profile for a given model id.", ["opencode", "configuration"]),
("src-tauri/src/agent_sessions/cli/session_runner/session.rs", "setup_opencode_zenmux_profile"): (
  "Writes the OpenCode profile home directory with Zenmux auth and model config so the OpenCode CLI can run against the selected model/key.", ["opencode", "configuration", "file-io"]),
("src-tauri/src/agent_sessions/cli/session_runner/session.rs", "run_session"): (
  "Core orchestrator that spawns and runs a CLI coding agent for a session: builds the command, launches the process, streams stdout/stderr chunks through parsers, handles OAuth retries, plan approvals and cancellation, and persists resulting events.", ["orchestration", "entry-point", "cli-agent"]),
("src-tauri/src/agent_sessions/cli/session_runner/session.rs", "resolve_sde_skills"): (
  "Resolves the set of skills/dev-environment rules to inject for the session's agent and workspace.", ["skills"]),

("src-tauri/src/agent_sessions/cli/session_runner/token_sync.rs", "sync_codex_cli_auth_to_key_vault"): (
  "Reads the Codex CLI's on-disk auth file and syncs the launched access token into the key vault for the given account.", ["oauth", "key-vault"]),

("src-tauri/src/agent_sessions/cli/skill_sync.rs", "sync_skills_for_agent"): (
  "Writes the enabled project skills into the rule files expected by a given CLI agent within the workspace.", ["skill-sync"]),
("src-tauri/src/agent_sessions/cli/skill_sync.rs", "cleanup_synced_skill_files"): (
  "Deletes previously synced skill/rule files at the given paths.", ["cleanup"]),
("src-tauri/src/agent_sessions/cli/skill_sync.rs", "rule_targets_for_agent"): (
  "Determines which rule file paths a given CLI agent reads within a workspace.", ["agent-mapping"]),
("src-tauri/src/agent_sessions/cli/skill_sync.rs", "build_skills_prompt_injection"): (
  "Builds the prompt-injection text block listing enabled skills for a workspace.", ["content-building"]),
("src-tauri/src/agent_sessions/cli/skill_sync.rs", "build_skills_content"): (
  "Builds the full skills content/documentation to write into an agent's rule file.", ["content-building"]),
("src-tauri/src/agent_sessions/cli/skill_sync.rs", "write_rule_file"): (
  "Writes formatted rule content to a target file path.", ["file-io"]),
("src-tauri/src/agent_sessions/cli/skill_sync.rs", "sync_conventions_for_agent"): (
  "Writes the project's coding conventions into the convention files expected by a given CLI agent.", ["conventions", "file-sync"]),
("src-tauri/src/agent_sessions/cli/skill_sync.rs", "convention_targets_for_agent"): (
  "Determines which convention file paths a given CLI agent reads within a workspace.", ["agent-mapping"]),

("src-tauri/src/agent_sessions/cli/tui_bridge.rs", "status_for_state"): (
  "Maps a TUI application state into a display status string.", ["status-mapping"]),
("src-tauri/src/agent_sessions/cli/tui_bridge.rs", "native_id_for_binding"): (
  "Resolves the native process/session id bound to a TUI event for a given agent.", ["id-resolution"]),
("src-tauri/src/agent_sessions/cli/tui_bridge.rs", "on_live_status_event"): (
  "Handles an incoming live-status event from a TUI session and updates its tracked state.", ["event-handler"]),
("src-tauri/src/agent_sessions/cli/tui_bridge.rs", "apply_event"): (
  "Applies a TUI event to update Orgii's live status tracking for the corresponding session.", ["event-handler"]),
("src-tauri/src/agent_sessions/cli/tui_bridge.rs", "release_tui_session"): (
  "Releases/cleans up tracked state for a TUI session once it ends.", ["cleanup"]),

("src-tauri/src/agent_sessions/event_pipeline/agent_core_bridge.rs", "complete_tool_call_by_call_id_adapter"): (
  "Marks a tool call identified by call_id as complete/failed in the session's event store and updates its result.", ["tool-call", "event-mutation"]),
("src-tauri/src/agent_sessions/event_pipeline/agent_core_bridge.rs", "replace_streaming_event_adapter"): (
  "Replaces a streaming placeholder event with its finalized event content in the session's event store.", ["streaming", "event-mutation"]),
("src-tauri/src/agent_sessions/event_pipeline/agent_core_bridge.rs", "unpin_session_adapter"): (
  "Unpins a session in the event store so it becomes eligible for eviction.", ["session-management"]),
("src-tauri/src/agent_sessions/event_pipeline/agent_core_bridge.rs", "finalize_plan_revision_events_adapter"): (
  "Finalizes events tied to a plan revision, resolving the revision's outcome in the session's event store.", ["plan-mode", "event-mutation"]),
("src-tauri/src/agent_sessions/event_pipeline/agent_core_bridge.rs", "persist_events_async_adapter"): (
  "Asynchronously persists a batch of events for a session with retry, without blocking the caller.", ["persistence", "async"]),
("src-tauri/src/agent_sessions/event_pipeline/agent_core_bridge.rs", "persist_user_message_event_adapter"): (
  "Persists a user-authored message event (with optional images and turn intent) into the session's event store.", ["persistence", "event-creation"]),
("src-tauri/src/agent_sessions/event_pipeline/agent_core_bridge.rs", "repair_stranded_plan_events"): (
  "Repairs plan-mode events left in an inconsistent state (e.g. orphaned from a crashed session) across the event store.", ["repair", "data-integrity"]),
("src-tauri/src/agent_sessions/event_pipeline/agent_core_bridge.rs", "remove_events_by_ids_adapter"): (
  "Removes a set of events by id from a session's event store.", ["event-mutation"]),
("src-tauri/src/agent_sessions/event_pipeline/agent_core_bridge.rs", "register"): (
  "Registers this module's adapter functions as the concrete implementation used by the generic agent-core event pipeline.", ["registration", "wiring"]),

("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "compute_session_analytics"): (
  "Computes the full SessionAnalytics summary (tool usage, file changes, conversation stats, tokens, timeline, errors) for a single session's events.", ["analytics"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "compute_multi_session_analytics"): (
  "Aggregates SessionAnalytics across multiple sessions into a MultiSessionSummary.", ["analytics", "aggregation"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "empty_analytics"): (
  "Returns an empty/zeroed SessionAnalytics value for sessions with no events.", ["default-value"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "parse_iso_ms"): (
  "Parses an ISO-8601 timestamp string into milliseconds since epoch.", ["date-parsing"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "days_from_civil"): (
  "Converts a calendar year/month/day into a day count since epoch (civil calendar algorithm).", ["date-math"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "categorize_file_operation"): (
  "Categorizes a tool function name into a file-operation type (read/write/edit/etc.) for analytics grouping.", ["categorization"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "extract_token_info"): (
  "Extracts input/output token counts and model name from an event for token-usage analytics.", ["token-extraction"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "compute_timeline_buckets"): (
  "Buckets events into fixed time intervals to build a timeline chart of activity.", ["timeline", "aggregation"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "ms_to_iso"): (
  "Converts a millisecond epoch timestamp into an ISO-8601 string.", ["date-formatting"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "civil_from_days"): (
  "Converts a day count since epoch back into a calendar year/month/day (inverse of days_from_civil).", ["date-math"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/analytics.rs", "es_compute_analytics"): (
  "Tauri command that computes and returns SessionAnalytics for a session's currently loaded events.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/analytics.rs", "es_compute_cached_session_analytics"): (
  "Tauri command that computes SessionAnalytics from cached (persisted) events for a session.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/analytics.rs", "es_compute_multi_session_analytics"): (
  "Tauri command that computes aggregated analytics across a list of session ids.", ["tauri-command"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/batch_update.rs", "es_complete_last_running"): (
  "Tauri command that marks the last running task event in a session as complete.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/batch_update.rs", "es_patch_by_ids"): (
  "Tauri command that applies a JSON patch to a set of events identified by id.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/batch_update.rs", "es_remove_by_id_prefix"): (
  "Tauri command that removes events whose id starts with a given prefix.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/batch_update.rs", "es_remove_synthetic_user_inputs"): (
  "Tauri command that removes synthetic/placeholder user-input events from a session.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/batch_update.rs", "es_replace_and_remove"): (
  "Tauri command that replaces one event with a new event while removing another by id, in a single atomic update.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/batch_update.rs", "es_update_active_task_args"): (
  "Tauri command that merges additional arguments into the active (in-flight) tool-call event matching given function names.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/batch_update.rs", "es_update_last_shell_output"): (
  "Tauri command that appends streamed output to the most recent shell/process event.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/batch_update.rs", "es_update_last_shell_process"): (
  "Tauri command that updates the pid/status/exit-code/log-path of the most recent shell process event.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/batch_update.rs", "es_has_active_task"): (
  "Tauri command that checks whether a session currently has an active (in-flight) task matching given function names.", ["tauri-command"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs", "es_load_from_cache"): (
  "Tauri command that hydrates a session's in-memory event store from the persisted cache.", ["tauri-command", "hydration"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs", "es_save_to_cache"): (
  "Tauri command that persists a session's current in-memory events to the cache.", ["tauri-command", "persistence"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs", "cache_save_session_events"): (
  "Saves a session's events directly to the on-disk cache.", ["persistence"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs", "cache_load_session_events"): (
  "Loads a session's events directly from the on-disk cache.", ["persistence"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs", "cache_search_session_events"): (
  "Full-text searches a session's cached events for a query string.", ["search"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs", "cache_update_session_event"): (
  "Updates a single cached event record.", ["persistence"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs", "cache_get_session_event"): (
  "Retrieves a single cached event by id.", ["persistence"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs", "cache_load_event_payload"): (
  "Loads a specific field's payload for a cached event, used for lazy-loading large event bodies.", ["lazy-loading"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs", "cache_save_full_session"): (
  "Persists a full session payload (events, specs, time range) to the cache in one operation.", ["persistence"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs", "cache_load_full_session"): (
  "Loads a full session payload (events, specs, time range) from the cache in one operation.", ["persistence"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "merge_loser_into_winner"): (
  "Merges fields from a duplicate ('loser') event into the canonical ('winner') event when deduplicating.", ["deduplication"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "dedup_by_call_id"): (
  "Deduplicates events sharing the same tool-call id, merging duplicates into a single canonical event.", ["deduplication"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "is_stream_transcript_event"): (
  "Checks whether an event is part of a raw streaming transcript pair.", ["detection"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "dedup_stream_transcript_chunk_pairs"): (
  "Deduplicates matched streaming-transcript chunk pairs (start/end) into single events.", ["deduplication"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "read_tool_inputs_by_call_id"): (
  "Reads persisted tool-call input arguments indexed by call id for a session.", ["persistence", "lookup"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "merge_missing_args_from_tool_input"): (
  "Fills in missing tool-call arguments on an event from a previously recorded tool input.", ["data-repair"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "backfill_tool_inputs_from_messages"): (
  "Backfills missing tool-call input arguments by scanning a session's message history.", ["data-repair"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "backfill_subagent_links"): (
  "Backfills parent/child links between subagent session events based on heuristics over the event stream.", ["data-repair", "subagent"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "merge_compact_boundary_events"): (
  "Merges compact-boundary marker events (context-compaction points) into a session's event list.", ["compaction"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "read_compact_boundary_rows"): (
  "Reads raw compact-boundary rows from storage for a session.", ["persistence"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "compact_boundary_row_to_event"): (
  "Converts a raw compact-boundary storage row into a SessionEvent.", ["conversion"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "is_synthetic_turn_header_event"): (
  "Checks whether an event is a synthetic turn-header placeholder rather than real agent output.", ["detection"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "is_synthetic_persistence_artifact"): (
  "Checks whether an event is a synthetic artifact created only for persistence bookkeeping, not real content.", ["detection"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "normalize_event_record_value"): (
  "Normalizes a raw stored event JSON value into a consistent shape before conversion.", ["normalization"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "cached_event_to_session_event"): (
  "Converts a persisted CachedEvent row into the in-memory SessionEvent representation used by the frontend.", ["conversion"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "session_event_to_cached_event"): (
  "Converts an in-memory SessionEvent into the CachedEvent representation for persistence.", ["conversion"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "build_searchable_content"): (
  "Builds the flattened searchable text content for an event, used to populate full-text search indexes.", ["search-indexing"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/extractors.rs", "es_extract_event_data"): (
  "Tauri command that extracts normalized data for a single event by id.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/extractors.rs", "es_extract_all_event_data"): (
  "Tauri command that extracts normalized data for all of a session's events.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/extractors.rs", "es_extract_event_data_window"): (
  "Tauri command that extracts normalized data for a windowed page of a session's events.", ["tauri-command"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/history.rs", "es_query_session_history"): (
  "Tauri command that queries session history records with filter criteria.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/history.rs", "es_get_recent_sessions"): (
  "Tauri command that returns the most recent sessions up to a limit.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/history.rs", "es_group_sessions"): (
  "Tauri command that groups session history records by a given key.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/history.rs", "es_compute_session_statistics"): (
  "Tauri command that computes aggregate statistics over session history.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/history.rs", "clip_fields"): (
  "Clips a session record's status/timestamp fields for a lightweight summary view.", ["view-model"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/history.rs", "es_get_child_sessions"): (
  "Tauri command that returns child (subagent) sessions for a given parent session id.", ["tauri-command", "subagent"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/history.rs", "cli_child_session_records"): (
  "Resolves child-session records launched via CLI for a given parent session.", ["subagent", "cli-agent"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/history.rs", "imported_child_session_records"): (
  "Resolves child-session records that were imported (not CLI-launched) for a given parent session.", ["subagent", "import"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/history.rs", "es_get_parent_session"): (
  "Tauri command that resolves the parent session id for a given (subagent) session.", ["tauri-command", "subagent"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/history.rs", "debug_seed_child_session"): (
  "Debug-only command that seeds a synthetic child session record for testing parent/child relationships.", ["debug", "testing"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/ingestion.rs", "es_ingest_chunks"): (
  "Tauri command that ingests a batch of raw CLI chunks into a session's event store.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/ingestion.rs", "es_process_chunks"): (
  "Processes raw CLI chunks into normalized session events without persisting.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/ingestion.rs", "es_normalize_chunk"): (
  "Normalizes a single raw CLI chunk into a session event shape.", ["tauri-command"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "prepare_loaded_events"): (
  "Prepares freshly-loaded raw events for a session (backfilling subagent prompts, etc.) before they enter the store.", ["preprocessing"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "resolve_session_id"): (
  "Resolves an explicit or ambient session id to operate on.", ["id-resolution"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "with_store_mut"): (
  "Runs a closure with mutable access to a session's EventStore, creating it if needed.", ["state-management"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "schedule_notify"): (
  "Schedules a debounced frontend notification that a session's events changed.", ["notification", "debounce"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "emit_snapshot"): (
  "Builds and emits a full event-store snapshot (sorted/filtered/compacted) to the frontend for a session.", ["snapshot", "event-emission"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "pseudo_jitter_ms"): (
  "Computes a pseudo-random jitter delay in milliseconds used to stagger retry backoff.", ["retry-logic"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "save_events_retry"): (
  "Persists a batch of events with retry/backoff on failure.", ["persistence", "retry-logic"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "persist_events_with_retry"): (
  "Persists events for a session with retry, wrapping save_events_retry.", ["persistence", "retry-logic"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "persist_runtime_orgtrack_records_async"): (
  "Asynchronously persists runtime OrgTrack records derived from session events.", ["persistence", "async"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "persist_runtime_orgtrack_records"): (
  "Persists runtime OrgTrack records derived from session events.", ["persistence"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "runtime_artifact_session_record"): (
  "Builds the runtime-artifact session record used for OrgTrack reporting from a session id.", ["reporting"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "push_events_to_session"): (
  "Core entry point that appends new events to a session's store, updates indexes, schedules notification and persists them.", ["event-mutation", "orchestration"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "update_spawning_tool_args_with_persist"): (
  "Updates spawning tool-call arguments for matching function names and persists the change.", ["event-mutation", "persistence"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "update_tool_args_by_call_id_with_persist"): (
  "Updates a tool call's arguments by call id and persists the change.", ["event-mutation", "persistence"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/pagination.rs", "es_paginate_events"): (
  "Tauri command that returns a page of a session's in-memory events per a pagination request.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/pagination.rs", "es_paginate_cached_events"): (
  "Tauri command that returns a page of a session's cached (persisted) events.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/pagination.rs", "es_count_matching_events"): (
  "Tauri command that counts a session's events matching given filters.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/pagination.rs", "es_get_distinct_functions"): (
  "Tauri command that returns the distinct tool-call function names used in a session.", ["tauri-command"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/search.rs", "es_search_chat_events"): (
  "Tauri command that searches a session's chat events matching the given search options.", ["tauri-command", "search"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/session_manager.rs", "es_switch_session"): (
  "Tauri command that switches the active session in the event-store session manager.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/session_manager.rs", "es_pin_session"): (
  "Tauri command that pins a session to keep it resident in memory.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/session_manager.rs", "es_unpin_session"): (
  "Tauri command that unpins a previously pinned session.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/session_manager.rs", "es_evict_session"): (
  "Tauri command that evicts a session's in-memory event store.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/session_manager.rs", "es_buffer_events"): (
  "Tauri command that buffers incoming events for a session pending processing.", ["tauri-command"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/snapshot.rs", "es_get_snapshot"): (
  "Tauri command that returns the current event-store snapshot for a session.", ["tauri-command", "snapshot"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/snapshot.rs", "es_get_events"): (
  "Tauri command that returns the raw event list for a session.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/snapshot.rs", "es_export_markdown"): (
  "Tauri command that exports a session's events as a markdown transcript.", ["tauri-command", "export"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/store_commands.rs", "es_set_repo_context"): (
  "Tauri command that sets the repo id/path context for a session's event store.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/store_commands.rs", "es_set"): (
  "Tauri command that replaces a session's entire event list.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/store_commands.rs", "es_append"): (
  "Tauri command that appends new events to a session's store with merge/backfill handling.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/store_commands.rs", "es_upsert"): (
  "Tauri command that inserts or updates a single event in a session's store.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/store_commands.rs", "es_update_by_id"): (
  "Tauri command that applies a patch to a single event identified by id.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/store_commands.rs", "es_merge_tool_results"): (
  "Merges tool-call result events into their corresponding call events.", ["deduplication"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/store_commands.rs", "es_merge_events"): (
  "Tauri command that merges a batch of events into a session's store.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/store_commands.rs", "es_merge_round_window_events"): (
  "Tauri command that merges events within a bounded round/turn window into a session's store.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/store_commands.rs", "es_set_streaming"): (
  "Tauri command that toggles a session's streaming-in-progress flag.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/store_commands.rs", "es_clear"): (
  "Tauri command that clears all events from a session's store.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/store_commands.rs", "es_truncate_before_id"): (
  "Tauri command that truncates a session's events, discarding everything before a given event id.", ["tauri-command"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/turn_window.rs", "turn_has_user_header"): (
  "Checks whether a turn already has a synthetic user-header event present.", ["detection"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/turn_window.rs", "make_turn_user_header_event"): (
  "Builds a synthetic user-header event summarizing a turn's user message for display.", ["synthetic-event"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/turn_window.rs", "make_turn_placeholder_event"): (
  "Builds a placeholder event representing an unloaded turn's body, to be lazily hydrated.", ["synthetic-event", "lazy-loading"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/turn_window.rs", "cache_load_session_turn_body"): (
  "Loads the full body events for a single turn from the cache.", ["persistence", "lazy-loading"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/turn_window.rs", "load_initial_turn_window_events"): (
  "Loads the initial window of recent turns and their events for a session.", ["pagination"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/turn_window.rs", "cache_load_session_initial_turn_window"): (
  "Loads the initial turn window for a session directly from the cache.", ["persistence"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/turn_window.rs", "es_load_initial_turn_window"): (
  "Tauri command that returns the initial turn window (recent turns plus events) for a session.", ["tauri-command"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/turn_window.rs", "es_unload_turn_body"): (
  "Tauri command that unloads a turn's body events from memory to save space, leaving a placeholder.", ["tauri-command", "lazy-loading"]),

("src-tauri/src/agent_sessions/event_pipeline/derived.rs", "is_live_runtime_resource_event"): (
  "Checks whether an event represents a live runtime resource (e.g. a running shell process) requiring special handling.", ["detection"]),
("src-tauri/src/agent_sessions/event_pipeline/derived.rs", "is_visible_in_chat"): (
  "Determines whether an event should be visible in the main chat view.", ["visibility-filter"]),
("src-tauri/src/agent_sessions/event_pipeline/derived.rs", "is_visible_in_simulator_or_messages"): (
  "Determines whether an event should be visible in either the simulator view or the messages view.", ["visibility-filter"]),
("src-tauri/src/agent_sessions/event_pipeline/derived.rs", "display_variant_wire"): (
  "Maps an internal event display variant to its wire/serialized representation.", ["mapping"]),
("src-tauri/src/agent_sessions/event_pipeline/derived.rs", "latest_canvas_preview"): (
  "Finds the most recent canvas-preview-eligible event to show as a live preview.", ["preview"]),
("src-tauri/src/agent_sessions/event_pipeline/derived.rs", "build_simulator_preview_indexes"): (
  "Builds lookup indexes (by event id) used to render simulator previews efficiently.", ["indexing"]),
("src-tauri/src/agent_sessions/event_pipeline/derived.rs", "build_simulator_preview_indexes_from_iter"): (
  "Builds simulator preview indexes from an iterator of sorted simulator events, avoiding a full materialized copy.", ["indexing"]),
("src-tauri/src/agent_sessions/event_pipeline/derived.rs", "compute_derived"): (
  "Computes the full set of derived display state for a session's events at a given version.", ["derived-state"]),
("src-tauri/src/agent_sessions/event_pipeline/derived.rs", "has_thinking_content"): (
  "Checks whether a tool/model result contains visible 'thinking' content.", ["content-check"]),
("src-tauri/src/agent_sessions/event_pipeline/derived.rs", "has_visible_message_content"): (
  "Checks whether an event has visible message content to render.", ["content-check"]),
("src-tauri/src/agent_sessions/event_pipeline/derived.rs", "sort_if_unsorted"): (
  "Sorts a session's events by chat order only if they are not already sorted, avoiding unnecessary work.", ["sorting", "optimization"]),
("src-tauri/src/agent_sessions/event_pipeline/derived.rs", "sort_simulator_events"): (
  "Sorts events specifically for simulator-view chronological ordering.", ["sorting"]),

("src-tauri/src/agent_sessions/event_pipeline/extractors/extractors.rs", "extract_event_data"): (
  "Extracts normalized display data for a single event.", ["extraction"]),
("src-tauri/src/agent_sessions/event_pipeline/extractors/extractors.rs", "extract_tool_call_data"): (
  "Extracts and formats tool-call-specific display data (arguments and result) from an event.", ["extraction"]),
("src-tauri/src/agent_sessions/event_pipeline/extractors/extractors.rs", "extract_batch"): (
  "Extracts normalized display data for a batch of events.", ["extraction"]),
}

CLASS_META = {
("src-tauri/src/agent_sessions/cli/session_runner/command.rs", "CliCommandBuildRequest"): (
  "Request DTO carrying agent, model, task, resume, API key, endpoint, mode, repo path and additional directories needed to build a CLI launch command.", ["data-model", "dto"]),
("src-tauri/src/agent_sessions/cli/session_runner/command.rs", "ClaudeModelLaunchConfig"): (
  "Resolved Claude model launch configuration pairing a base model with its reasoning effort.", ["data-model"]),

("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "CliPermissionMode"): (
  "Enum of CLI agent permission modes: Plan, FullPermission, AutoEdit, Manual.", ["enum", "permission-mode"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "CliLaunchProfileDefaults"): (
  "Built-in default launch profile for an agent type, including command args and per-mode defaults.", ["data-model"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "CliLaunchProfileModeDefaults"): (
  "Default args/env for a specific permission mode within a launch profile.", ["data-model"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "CliLaunchProfileModeDefaultsView"): (
  "Serializable view of a mode's default args/env for the frontend.", ["view-model"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "CliLaunchProfileOverride"): (
  "User-configured overrides (permission mode, command, args, env, transport) for an agent's launch profile.", ["data-model", "configuration"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "CliLaunchProfileView"): (
  "Full frontend-facing view of an agent's launch profile, merging defaults and overrides into an effective command/args/env.", ["view-model"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "ResolvedCliLaunchProfile"): (
  "Fully resolved launch profile (permission mode, command, args, env, transport) ready to spawn a CLI process.", ["data-model"]),
("src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "CliLaunchProfileUpdate"): (
  "Update payload for modifying an agent's launch profile overrides.", ["data-model"]),

("src-tauri/src/agent_sessions/cli/types.rs", "SessionStatus"): (
  "Enum representing a CLI session's lifecycle status (Pending, Running, Idle, Completed, Failed, Cancelled) with helpers to check terminal/resumable state.", ["enum", "lifecycle", "state-machine"]),
("src-tauri/src/agent_sessions/cli/types.rs", "SessionRunner"): (
  "Enum representing which runtime executes a CLI session: Local process or Tui (terminal UI).", ["enum", "execution-transport"]),

("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "SessionAnalytics"): (
  "Top-level analytics summary for a session: event counts, duration, tool usage, file changes, conversation stats, token stats, timeline buckets and error stats.", ["data-model", "analytics"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "ToolUsageEntry"): (
  "Per-tool-function usage statistics: call/completion/failure counts, files touched, total duration.", ["data-model"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "FileChangeSummary"): (
  "Summary of file changes in a session: total files, breakdown by operation, and top-touched files.", ["data-model"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "FileOperationEntry"): (
  "Count and file list for a single file-operation category (e.g. reads, writes).", ["data-model"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "FileFrequencyEntry"): (
  "Touch count and operation list for a single file, used to rank most-active files.", ["data-model"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "ConversationStats"): (
  "Conversation-level stats: message counts, thinking-event count, character counts, average response time.", ["data-model"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "TokenStats"): (
  "Aggregated token usage: total input/output/total tokens broken down by model.", ["data-model"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "ModelTokenEntry"): (
  "Per-model token usage entry: input/output tokens and call count.", ["data-model"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "TimelineBucket"): (
  "A single time-bucketed activity slice: event/tool-call/message/error counts.", ["data-model"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "ErrorStats"): (
  "Aggregated error/failure statistics with a per-tool breakdown.", ["data-model"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "ToolErrorEntry"): (
  "Per-tool error and failure counts.", ["data-model"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "MultiSessionSummary"): (
  "Aggregated analytics summary across multiple sessions, including per-session entries.", ["data-model"]),
("src-tauri/src/agent_sessions/event_pipeline/analytics.rs", "SessionSummaryEntry"): (
  "Per-session summary entry within a multi-session analytics aggregation.", ["data-model"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs", "SessionEventSearchResult"): (
  "A single search-result hit: the matched event, its relevance rank, and a highlighted snippet.", ["data-model", "search"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs", "FullSessionPayload"): (
  "Full serialized session payload: id, events, specs JSON, and time range, used for full-session cache save/load.", ["data-model"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "CompactBoundaryRow"): (
  "Raw storage row representing a context-compaction boundary: id, content, timestamp and token counts before/after.", ["data-model"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/history.rs", "ChildSessionView"): (
  "Frontend view of a child (subagent) session: the underlying record plus derived terminal/ended-at state.", ["view-model", "subagent"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "EventStoreState"): (
  "Shared Tauri-managed state holding all active session EventStores, the session manager, and pending notification flags.", ["state-management", "tauri-state"]),

("src-tauri/src/agent_sessions/event_pipeline/commands/turn_window.rs", "SessionTurnBodyWindow"): (
  "A single turn's id paired with its (possibly lazily-loaded) body events.", ["data-model"]),
("src-tauri/src/agent_sessions/event_pipeline/commands/turn_window.rs", "SessionInitialTurnWindow"): (
  "The initial set of turns and events loaded for a session on open.", ["data-model"]),

("src-tauri/src/agent_sessions/event_pipeline/derived.rs", "SimulatorPreviewIndexes"): (
  "Precomputed lookup indexes (previews, timestamps, thread ids, function names, display status/variant) keyed by event id for fast simulator rendering.", ["data-model", "indexing"]),
}

nodes = []
edges = []
seen_ids = set()

def add_node(node):
    assert node['id'] not in seen_ids, f"DUPLICATE ID {node['id']}"
    seen_ids.add(node['id'])
    nodes.append(node)

for path, meta in FILTERED.items():
    fsum, ftags = FILE_META[path]
    file_id = f"file:{path}"
    add_node({
        "id": file_id,
        "type": "file",
        "name": path.split('/')[-1],
        "filePath": path,
        "summary": fsum,
        "tags": ftags,
        "complexity": fcx(meta['nonEmptyLines']),
    })

    for f in meta['functions']:
        key = (path, f['name'])
        if key not in FUNC_META:
            raise SystemExit(f"MISSING FUNC META: {key}")
        summary, tags = FUNC_META[key]
        fn_id = f"function:{path}:{f['name']}"
        add_node({
            "id": fn_id,
            "type": "function",
            "name": f['name'],
            "filePath": path,
            "lineRange": [f['startLine'], f['endLine']],
            "summary": summary,
            "tags": tags,
            "complexity": icx(f['size']),
        })
        edges.append({"source": file_id, "target": fn_id, "type": "contains", "direction": "forward", "weight": 1.0})
        if f['exported']:
            edges.append({"source": file_id, "target": fn_id, "type": "exports", "direction": "forward", "weight": 0.8})

    for c in meta['classes']:
        key = (path, c['name'])
        if key not in CLASS_META:
            raise SystemExit(f"MISSING CLASS META: {key}")
        summary, tags = CLASS_META[key]
        cl_id = f"class:{path}:{c['name']}"
        add_node({
            "id": cl_id,
            "type": "class",
            "name": c['name'],
            "filePath": path,
            "lineRange": [c['startLine'], c['endLine']],
            "summary": summary,
            "tags": tags,
            "complexity": icx(c['size']),
        })
        edges.append({"source": file_id, "target": cl_id, "type": "contains", "direction": "forward", "weight": 1.0})
        if c['exported']:
            edges.append({"source": file_id, "target": cl_id, "type": "exports", "direction": "forward", "weight": 0.8})

# imports edges: exactly 1:1 from batchImportData
import_edge_count = 0
for path, targets in BID.items():
    for t in targets:
        edges.append({"source": f"file:{path}", "target": f"file:{t}", "type": "imports", "direction": "forward", "weight": 0.7})
        import_edge_count += 1

expected_imports = sum(len(v) for v in BID.values())
assert import_edge_count == expected_imports, f"{import_edge_count} != {expected_imports}"

# curated high-confidence "calls" edges (within-batch, verified via callGraph + batchImportData)
CALLS_WITHIN = [
    ("src-tauri/src/agent_sessions/cli/session_runner/command.rs", "build_command_with_launch_profile",
     "src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "defaults_for_agent"),
    ("src-tauri/src/agent_sessions/cli/session_runner/command.rs", "build_command_with_launch_profile",
     "src-tauri/src/agent_sessions/cli/session_runner/launch_profiles.rs", "static_env_to_map"),
    ("src-tauri/src/agent_sessions/cli/session_runner/helpers.rs", "persist_and_broadcast_streaming_complete",
     "src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "save_events_retry"),
    ("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "emit_snapshot",
     "src-tauri/src/agent_sessions/event_pipeline/derived.rs", "build_simulator_preview_indexes"),
    ("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "emit_snapshot",
     "src-tauri/src/agent_sessions/event_pipeline/derived.rs", "compute_derived"),
    ("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "emit_snapshot",
     "src-tauri/src/agent_sessions/event_pipeline/derived.rs", "is_visible_in_chat"),
    ("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "emit_snapshot",
     "src-tauri/src/agent_sessions/event_pipeline/derived.rs", "latest_canvas_preview"),
    ("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "emit_snapshot",
     "src-tauri/src/agent_sessions/event_pipeline/derived.rs", "sort_if_unsorted"),
    ("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "emit_snapshot",
     "src-tauri/src/agent_sessions/event_pipeline/derived.rs", "sort_simulator_events"),
    ("src-tauri/src/agent_sessions/event_pipeline/commands/snapshot.rs", "es_get_snapshot",
     "src-tauri/src/agent_sessions/event_pipeline/derived.rs", "compute_derived"),
]

# cross-batch calls confirmed via neighborMap symbol lists (targets live in other batches, not created here)
CALLS_CROSS_BATCH = [
    ("src-tauri/src/agent_sessions/event_pipeline/commands/cache_bridge.rs", "cache_load_event_payload",
     "src-tauri/src/agent_sessions/event_pipeline/payload_compaction.rs", "load_event_payload_body"),
    ("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "cached_event_to_session_event",
     "src-tauri/src/agent_sessions/event_pipeline/ingestion/function_map.rs", "resolve_ui_canonical"),
    ("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "compact_boundary_row_to_event",
     "src-tauri/src/agent_sessions/event_pipeline/ingestion/function_map.rs", "resolve_ui_canonical"),
    ("src-tauri/src/agent_sessions/event_pipeline/commands/event_conversion.rs", "is_synthetic_persistence_artifact",
     "src-tauri/src/agent_sessions/event_pipeline/payload_compaction.rs", "is_compacted_event"),
    ("src-tauri/src/agent_sessions/event_pipeline/commands/mod.rs", "emit_snapshot",
     "src-tauri/src/agent_sessions/event_pipeline/payload_compaction.rs", "compact_event_for_snapshot"),
    ("src-tauri/src/agent_sessions/event_pipeline/commands/store_commands.rs", "es_append",
     "src-tauri/src/agent_sessions/event_pipeline/ingestion/function_map.rs", "resolve_ui_canonical"),
    ("src-tauri/src/agent_sessions/event_pipeline/commands/store_commands.rs", "es_upsert",
     "src-tauri/src/agent_sessions/event_pipeline/ingestion/function_map.rs", "resolve_ui_canonical"),
    ("src-tauri/src/agent_sessions/event_pipeline/derived.rs", "compute_derived",
     "src-tauri/src/agent_sessions/event_pipeline/payload_compaction.rs", "compact_event_for_snapshot"),
]

all_fn_ids = {n['id'] for n in nodes if n['type'] == 'function'}

for src_path, src_fn, tgt_path, tgt_fn in CALLS_WITHIN:
    src_id = f"function:{src_path}:{src_fn}"
    tgt_id = f"function:{tgt_path}:{tgt_fn}"
    assert src_id in all_fn_ids, src_id
    assert tgt_id in all_fn_ids, tgt_id
    edges.append({"source": src_id, "target": tgt_id, "type": "calls", "direction": "forward", "weight": 0.8})

for src_path, src_fn, tgt_path, tgt_fn in CALLS_CROSS_BATCH:
    src_id = f"function:{src_path}:{src_fn}"
    tgt_id = f"function:{tgt_path}:{tgt_fn}"
    assert src_id in all_fn_ids, src_id
    edges.append({"source": src_id, "target": tgt_id, "type": "calls", "direction": "forward", "weight": 0.8})

print("TOTAL NODES:", len(nodes))
print("TOTAL EDGES:", len(edges))

json.dump({"nodes": nodes, "edges": edges}, open('/home/misael/pj/gui-repos/ORG2/.understand-anything/tmp/ua-batch13-full.json', 'w'), indent=1)
