# File-level metadata: path -> (summary, tags, languageNotes-or-None)
FILES = {
"src-tauri/src/agent_sessions/cli/agent_core_bridge.rs": (
 "Bridges CLI agent sessions to the embedded agent-core execution engine, running turns, snapshotting available tools, and relaying plan approval responses.",
 ["agent-core","bridge","cli","integration"], None),
"src-tauri/src/agent_sessions/cli/commands.rs": (
 "Defines the Tauri command surface for CLI-based agent sessions -- creating, running, messaging, approving, resuming, deleting, merging, and inspecting worktree state for CLI agent sessions.",
 ["tauri-command","api-handler","cli","session-management"], None),
"src-tauri/src/agent_sessions/cli/hook_approvals.rs": (
 "Tracks interactive permission-approval requests raised by CLI agent tool-call hooks, broadcasting them to the frontend and resolving user decisions.",
 ["approval","hooks","permissions","cli"], None),
"src-tauri/src/agent_sessions/cli/launch_profile_store.rs": (
 "Persists and resolves per-agent CLI launch profiles (permission mode, command/args/env overrides) to a JSON file on disk.",
 ["configuration","persistence","cli","launch-profile"], None),
"src-tauri/src/agent_sessions/cli/mod.rs": (
 "Module root for CLI agent session support: initializes/migrates the SQLite schema for CLI agent sessions and re-exports the agent_core_bridge, commands, hook_approvals, launch_profile_store, native_transcript, parsers, persistence, platform_adapters, session_runner, skill_sync, tui_bridge, and types submodules.",
 ["entry-point","module-root","database","migration"], None),
"src-tauri/src/agent_sessions/cli/native_transcript.rs": (
 "Resolves how a CLI agent session's transcript is sourced -- either from the app's own managed chunk store or from a natively-imported transcript file belonging to the underlying CLI tool.",
 ["transcript","native-transcript","cli"], None),
"src-tauri/src/agent_sessions/cli/parsers/acp_common.rs": (
 "Shared implementation of the Agent Client Protocol (ACP) JSON-RPC session loop and message normalization used by all ACP-based CLI agent adapters (Kiro, Copilot, OpenCode) -- handles approvals, tool-call/result normalization, diff synthesis, and the core run_acp_protocol event loop.",
 ["acp-protocol","json-rpc","parser","shared-library"], "Largest parser file in the batch; centralizes protocol logic shared across multiple thin per-agent adapters."),
"src-tauri/src/agent_sessions/cli/parsers/alias_map.rs": (
 "Minimal three-line module providing CLI agent identifier alias mappings, re-exported by the parsers module.",
 ["alias","cli-agent","utility"], None),
"src-tauri/src/agent_sessions/cli/parsers/antigravity.rs": (
 "Parses the Antigravity CLI agent's raw stdout stream into normalized transcript chunks.",
 ["parser","cli-agent","antigravity"], None),
"src-tauri/src/agent_sessions/cli/parsers/claude_code.rs": (
 "Parses Claude Code CLI's streaming JSON output into normalized transcript chunks, handling tool-call deltas, results, and token usage.",
 ["parser","cli-agent","claude-code"], None),
"src-tauri/src/agent_sessions/cli/parsers/codex.rs": (
 "Parses the legacy Codex CLI streaming JSON-lines output format into normalized transcript chunks.",
 ["parser","cli-agent","codex"], None),
"src-tauri/src/agent_sessions/cli/parsers/codex_app_server.rs": (
 "Implements the newer Codex 'app-server' JSON-RPC protocol: builds/sends turn requests, parses server notifications and thread/turn events, and manages graceful interruption of in-flight turns.",
 ["json-rpc","parser","cli-agent","codex"], "Second-largest parser file; models a full JSON-RPC client/event-parser pair rather than simple line parsing."),
"src-tauri/src/agent_sessions/cli/parsers/copilot.rs": (
 "Thin ACP adapter for the GitHub Copilot CLI agent that delegates the protocol loop to the shared acp_common implementation.",
 ["acp-protocol","adapter","copilot"], None),
"src-tauri/src/agent_sessions/cli/parsers/cursor.rs": (
 "Parses the Cursor CLI agent's streaming JSON-lines output into normalized transcript chunks.",
 ["parser","cli-agent","cursor"], None),
"src-tauri/src/agent_sessions/cli/parsers/kiro.rs": (
 "ACP adapter and session-management utilities for the Kiro CLI agent -- tool-kind mapping, stale session-lock cleanup, and listing of on-disk Kiro sessions.",
 ["acp-protocol","adapter","kiro"], None),
"src-tauri/src/agent_sessions/cli/parsers/mod.rs": (
 "Defines the CliAgentParser trait implemented by all CLI-agent-specific parsers and re-exports the parser submodules and a parser-factory used by the session runner.",
 ["trait","entry-point","module-root","parser"], None),
"src-tauri/src/agent_sessions/cli/parsers/normalizer.rs": (
 "Normalizes CLI-agent-specific tool names, commands, and file-path arguments into the app's canonical vocabulary, shared across all parser implementations.",
 ["normalization","parser","shared-library"], None),
"src-tauri/src/agent_sessions/cli/parsers/opencode.rs": (
 "ACP adapter and helper functions for the OpenCode CLI agent -- extracts subagent task prompts/results embedded in tool-call text and maps OpenCode-specific tool kinds.",
 ["acp-protocol","adapter","opencode"], None),
"src-tauri/src/agent_sessions/cli/parsers/types.rs": (
 "Defines shared CLI-agent-related types: the CliAgentType enum enumerating every supported CLI agent, and the TokenUsage struct for tracking token consumption.",
 ["type-definition","domain-model","cli-agent"], None),
"src-tauri/src/agent_sessions/cli/persistence/chunk_ops.rs": (
 "CRUD and side-effect operations for CLI agent session transcript chunks -- inserting, loading, truncating, and cascading persistence of subagent child sessions.",
 ["persistence","database","transcript"], None),
"src-tauri/src/agent_sessions/cli/persistence/mod.rs": (
 "Module root for CLI agent session persistence; re-exports chunk_ops, session_crud, types, and worktree_state submodules.",
 ["module-root","persistence","entry-point"], None),
"src-tauri/src/agent_sessions/cli/persistence/session_crud.rs": (
 "Core CRUD and state-transition operations for CLI agent sessions in SQLite -- creation, retrieval, listing, status/model/account updates, resume-state management, and deletion.",
 ["persistence","database","crud","session-management"], "Largest persistence file; centralizes nearly all session lifecycle writes."),
"src-tauri/src/agent_sessions/cli/persistence/types.rs": (
 "Defines the core CLI agent session data model -- the persisted CodeSession row, its history-mutation record, and the parameters accepted when creating a new session.",
 ["type-definition","domain-model","database"], None),
"src-tauri/src/agent_sessions/cli/persistence/worktree_state.rs": (
 "Persists a CLI agent session's git worktree path/branch and merge status.",
 ["persistence","git","worktree"], None),
"src-tauri/src/agent_sessions/cli/platform_adapters/claude_code/mod.rs": (
 "Module root for the Claude Code platform adapter; re-exports the oauth submodule.",
 ["module-root","claude-code","oauth"], None),
"src-tauri/src/agent_sessions/cli/platform_adapters/claude_code/oauth.rs": (
 "Implements the Claude Code OAuth (PKCE) login flow: launching a webview, exchanging the authorization code for tokens, and fetching account/organization profile metadata.",
 ["oauth","authentication","claude-code","webview"], None),
"src-tauri/src/agent_sessions/cli/platform_adapters/codex/mod.rs": (
 "Module root for the Codex platform adapter; re-exports the oauth submodule.",
 ["module-root","codex","oauth"], None),
"src-tauri/src/agent_sessions/cli/platform_adapters/codex/oauth.rs": (
 "Implements the Codex OAuth (PKCE) login flow: launching a webview, exchanging the authorization code for tokens, and detecting the popup-based sign-in redirect.",
 ["oauth","authentication","codex","webview"], None),
"src-tauri/src/agent_sessions/cli/platform_adapters/cursor/mod.rs": (
 "Module root for the Cursor platform adapter; re-exports the session_capture and usage submodules.",
 ["module-root","cursor"], None),
"src-tauri/src/agent_sessions/cli/platform_adapters/cursor/session_capture.rs": (
 "Captures a Cursor account session by driving a native OAuth login webview and polling for the resulting session token/cookie.",
 ["oauth","authentication","cursor","webview"], None),
"src-tauri/src/agent_sessions/cli/platform_adapters/cursor/usage/mod.rs": (
 "Module root for the Cursor usage-tracking adapter; re-exports the tracker submodule.",
 ["module-root","cursor","usage"], None),
"src-tauri/src/agent_sessions/cli/platform_adapters/cursor/usage/tracker.rs": (
 "Fetches and normalizes Cursor CLI usage/token statistics from Cursor's usage-events API, matching cross-source model names to the app's canonical model identifiers.",
 ["usage-tracking","cursor","http"], None),
"src-tauri/src/agent_sessions/cli/platform_adapters/kiro/kiro_auth.rs": (
 "Implements Kiro's AWS-identity-provider login flow (device/browser-based auth) via an embedded webview, including cancellation and token retrieval.",
 ["oauth","authentication","kiro","webview"], None),
"src-tauri/src/agent_sessions/cli/platform_adapters/kiro/mod.rs": (
 "Module root for the Kiro platform adapter; re-exports the kiro_auth and proxy_auth submodules.",
 ["module-root","kiro"], None),
"src-tauri/src/agent_sessions/cli/platform_adapters/kiro/proxy_auth.rs": (
 "Sets up a local SQLite-backed auth database and home directory so the Kiro CLI can authenticate through the app's managed proxy instead of its own login flow.",
 ["proxy","authentication","kiro","database"], None),
}

# FUNC[path][name] = (summary, tags)
FUNC = {}
FUNC["src-tauri/src/agent_sessions/cli/agent_core_bridge.rs"] = {
 "run": ("Runs an agent-core turn for a session using the given request parameters, driving execution through the embedded agent-core engine.", ["agent-core","execution","bridge"]),
 "tools_snapshot": ("Returns a snapshot of the tools currently registered/available to the agent-core engine for the given session.", ["agent-core","tools","introspection"]),
 "respond_plan_approval": ("Forwards a plan approval/rejection decision from the UI into the agent-core engine for the session.", ["agent-core","approval","plan"]),
 "cli_registered_tool_names": ("Lists tool names registered with the CLI agent bridge for exposure to the agent-core engine.", ["agent-core","tools","registry"]),
 "register": ("Registers the agent-core bridge's Tauri commands/handlers with the application.", ["agent-core","registration","setup"]),
}
FUNC["src-tauri/src/agent_sessions/cli/commands.rs"] = {
 "cli_launch_profile_get": ("Tauri command that retrieves the stored launch profile for a CLI agent by delegating to the launch profile store.", ["tauri-command","launch-profile"]),
 "cli_launch_profile_update": ("Tauri command that updates permission mode, command, args, or env overrides for a CLI agent's launch profile.", ["tauri-command","launch-profile","configuration"]),
 "cli_launch_profile_reset": ("Tauri command that resets a CLI agent's launch profile to defaults.", ["tauri-command","launch-profile"]),
 "inject_ide_context_into_prompt": ("Merges IDE context (open files, selections, etc.) into the user's prompt text before sending it to a CLI agent.", ["prompt","ide-context","utility"]),
 "cli_agent_create": ("Tauri command that creates a new CLI agent session, provisioning session state and persistence records.", ["tauri-command","session-management","entry-point"]),
 "cli_agent_tui_release": ("Tauri command that releases a TUI-bound CLI agent session so it can be reattached or torn down.", ["tauri-command","tui","session-management"]),
 "cli_agent_run": ("Tauri command that starts or resumes a CLI agent run for a session with the given prompt and options.", ["tauri-command","session-management","execution"]),
 "cli_agent_message": ("Tauri command that sends a follow-up message to a running or new CLI agent session.", ["tauri-command","session-management","messaging"]),
 "cli_agent_approval_response": ("Tauri command that submits the user's approve/deny decision for a pending CLI agent tool-call approval.", ["tauri-command","approval"]),
 "cli_agent_status": ("Tauri command that returns the current status of a CLI agent session.", ["tauri-command","session-management"]),
 "cli_agent_history_mutation": ("Tauri command that returns the current history-mutation epoch for a CLI agent session.", ["tauri-command","session-management"]),
 "cli_agent_cancel": ("Tauri command that cancels a running CLI agent session.", ["tauri-command","session-management"]),
 "cli_agent_list": ("Tauri command that lists all CLI agent sessions.", ["tauri-command","session-management"]),
 "load_native_transcript_chunks": ("Loads transcript chunks for a session from its native (imported) transcript source rather than the managed chunk store.", ["transcript","native-transcript"]),
 "cli_agent_transcript_path": ("Tauri command that resolves the on-disk transcript location (native or managed) for a CLI agent session.", ["tauri-command","transcript"]),
 "synthesized_user_message_chunk": ("Builds a synthesized user-message chunk representing the session's initial prompt for display.", ["transcript","chunk"]),
 "cli_agent_chunks": ("Tauri command that returns the transcript chunks for a CLI agent session, from native or managed storage.", ["tauri-command","transcript"]),
 "cli_agent_truncate_after_chunk": ("Tauri command that truncates a session's transcript after a given point, optionally reverting file changes.", ["tauri-command","transcript","mutation"]),
 "cli_agent_resume": ("Tauri command that resumes a previously paused/stopped CLI agent session.", ["tauri-command","session-management"]),
 "cli_agent_delete": ("Tauri command that deletes a CLI agent session and its associated state.", ["tauri-command","session-management"]),
 "cli_agent_merge": ("Tauri command that merges a CLI agent session's worktree changes back into the base branch using the given strategy.", ["tauri-command","worktree","git"]),
 "cli_agent_worktree_diff": ("Tauri command that returns the diff between a CLI agent session's worktree and its base branch.", ["tauri-command","worktree","git"]),
 "cli_agent_worktree_discard": ("Tauri command that discards uncommitted changes in a CLI agent session's worktree.", ["tauri-command","worktree","git"]),
}
FUNC["src-tauri/src/agent_sessions/cli/hook_approvals.rs"] = {
 "as_wire_str": ("Converts a HookApprovalDecision variant to its wire-protocol string representation.", ["approval","serialization"]),
 "register_session_permission_mode": ("Registers the active permission mode for a CLI agent session so hook approvals can be resolved automatically when appropriate.", ["approval","permissions"]),
 "unregister_session": ("Removes a session's registered permission mode and pending-approval state on session teardown.", ["approval","cleanup"]),
 "session_permission_mode": ("Looks up the currently registered permission mode for a session.", ["approval","permissions"]),
 "session_wants_interactive_approval": ("Determines whether a session's permission mode requires interactive user approval for tool calls.", ["approval","permissions"]),
 "broadcast_permission_request": ("Emits a permission-request event to the frontend for a pending tool-call approval.", ["approval","events"]),
 "park_hook_approval": ("Registers a pending hook approval and blocks/waits (with timeout) for the user's decision.", ["approval","concurrency"]),
 "resolve_hook_approval": ("Resolves a pending hook approval with the user's decision, unblocking the waiting hook.", ["approval","concurrency"]),
 "has_pending_hook_approval": ("Checks whether a specific hook approval request is still pending.", ["approval","query"]),
}
FUNC["src-tauri/src/agent_sessions/cli/launch_profile_store.rs"] = {
 "store_path": ("Resolves the filesystem path of the launch profile store JSON file.", ["persistence","filesystem"]),
 "read_store": ("Reads and deserializes the launch profile store from disk.", ["persistence","deserialization"]),
 "write_store": ("Serializes and writes the launch profile store back to disk.", ["persistence","serialization"]),
 "parse_cli_agent": ("Parses a CLI agent name string into its corresponding CliAgentType.", ["parsing","cli-agent"]),
 "normalize_optional_string": ("Normalizes an optional override string, treating blank values as unset.", ["utility","normalization"]),
 "normalize_optional_args": ("Normalizes an optional list of CLI argument overrides.", ["utility","normalization"]),
 "normalize_optional_env": ("Normalizes an optional map of environment variable overrides.", ["utility","normalization"]),
 "normalize_permission_mode": ("Validates and normalizes a requested permission mode against an agent's supported defaults.", ["utility","permissions"]),
 "resolve_cli_launch_profile": ("Resolves the effective launch profile (defaults merged with stored overrides) for a CLI agent type.", ["launch-profile","resolution"]),
 "cli_launch_profile_get": ("Retrieves the effective launch profile for a named CLI agent.", ["launch-profile","query"]),
 "cli_launch_profile_update": ("Applies an update to a CLI agent's launch profile overrides and persists the store.", ["launch-profile","mutation"]),
 "cli_launch_profile_reset": ("Clears a CLI agent's launch profile overrides, reverting it to defaults.", ["launch-profile","mutation"]),
}
FUNC["src-tauri/src/agent_sessions/cli/mod.rs"] = {
 "init_cli_agent_tables": ("Creates and migrates the SQLite tables/columns backing CLI agent sessions and their transcript chunks, applying incremental ALTER TABLE migrations.", ["database","migration","schema"]),
 "migrate_strip_ide_context": ("One-time data migration that strips embedded <ide_context> markup from stored user inputs and chunk results.", ["database","migration","data-cleanup"]),
}
FUNC["src-tauri/src/agent_sessions/cli/native_transcript.rs"] = {
 "imported_session_id": ("Derives the imported-transcript session identifier from a raw CLI session id using the binding's prefix convention.", ["transcript","identifier"]),
 "native_transcript_binding": ("Looks up the native-transcript binding configuration (source and id prefix) for a given CLI agent type.", ["transcript","configuration"]),
 "native_transcript_enabled": ("Reports whether native transcript import is enabled for the given CLI agent type.", ["transcript","feature-flag"]),
 "native_store_key_for_managed_session": ("Computes the native transcript store key that a managed session maps to, if any.", ["transcript","mapping"]),
 "imported_transcript_id_for_managed_session": ("Resolves the native transcript id associated with a managed CLI agent session.", ["transcript","mapping"]),
}
FUNC["src-tauri/src/agent_sessions/cli/parsers/acp_common.rs"] = {
 "resolve_approval": ("Resolves a pending ACP tool-call approval with the user's decision.", ["acp-protocol","approval"]),
 "register_acp_approval": ("Registers a channel to await an ACP approval decision for a session.", ["acp-protocol","approval","concurrency"]),
 "await_acp_approval": ("Blocks (with timeout) waiting for an ACP tool-call approval decision to arrive.", ["acp-protocol","approval","concurrency"]),
 "truncate_str_safe": ("Truncates a string to a maximum character count without splitting multi-byte UTF-8 sequences.", ["utility","string"]),
 "count_diff_lines": ("Counts the number of added/removed lines in a unified diff string.", ["diff","utility"]),
 "extract_edit_content": ("Extracts old/new file content fields from a raw ACP edit tool-call input payload.", ["acp-protocol","diff"]),
 "synthesize_diff": ("Synthesizes a unified diff string from old and new file content for display.", ["diff","utility"]),
 "normalize_tool_result": ("Normalizes a raw ACP tool-call result into the app's canonical tool-result chunk shape.", ["acp-protocol","normalization"]),
 "parse_markdown_todos": ("Parses a markdown checklist into structured todo items.", ["parsing","todos"]),
 "extract_tool_call_content": ("Extracts display content (title, args, diff) from an ACP tool-call update payload.", ["acp-protocol","parsing"]),
 "new_with_task": ("Constructs a new ACP notification parser bound to a specific adapter, session, and task.", ["acp-protocol","constructor"]),
 "parse_update": ("Dispatches an incoming ACP session update to the appropriate handler based on its type.", ["acp-protocol","dispatch"]),
 "flush_thought_buffer": ("Flushes any buffered agent 'thought' text as a thinking-delta chunk.", ["acp-protocol","streaming"]),
 "emit_thinking_delta": ("Emits a thinking/reasoning delta chunk to the transcript stream.", ["acp-protocol","streaming"]),
 "emit_todo_from_thought_json": ("Emits a todo-list update chunk parsed from buffered thought JSON.", ["acp-protocol","todos"]),
 "parse_thought_chunk": ("Parses an ACP 'thought' update into buffered reasoning text or structured todo output.", ["acp-protocol","parsing"]),
 "parse_message_chunk": ("Parses an ACP 'message' update into an assistant text delta chunk.", ["acp-protocol","parsing"]),
 "parse_tool_call_start": ("Parses an ACP tool-call-start update, mapping tool kind and initial arguments into a pending tool call.", ["acp-protocol","parsing","tool-call"]),
 "parse_tool_call_update": ("Parses an ACP tool-call-update (progress/completion) payload and merges it into the pending tool call state.", ["acp-protocol","parsing","tool-call"]),
 "extract_permission_request_info": ("Extracts tool name, description, and arguments from an ACP permission-request notification.", ["acp-protocol","approval","parsing"]),
 "select_acp_option_id": ("Selects the correct ACP permission option id to respond with based on the user's approve/deny/always-allow decision.", ["acp-protocol","approval"]),
 "broadcast_acp_permission_request": ("Broadcasts an ACP permission request event to the frontend for user approval.", ["acp-protocol","approval","events"]),
 "acp_send": ("Writes a JSON-RPC request to the ACP agent process's stdin.", ["acp-protocol","json-rpc","io"]),
 "acp_respond": ("Writes a JSON-RPC success response back to the ACP agent process.", ["acp-protocol","json-rpc","io"]),
 "acp_read": ("Reads and parses the next line-delimited JSON-RPC message from the ACP agent process's stdout.", ["acp-protocol","json-rpc","io"]),
 "run_acp_protocol": ("Drives the full ACP JSON-RPC session loop for a spawned CLI agent process -- sending the task, reading notifications, and streaming normalized chunks until completion.", ["acp-protocol","json-rpc","orchestration","entry-point"]),
 "process_notification": ("Routes an incoming ACP JSON-RPC notification to the appropriate handler (session update, permission request, or custom method).", ["acp-protocol","json-rpc","dispatch"]),
}
FUNC["src-tauri/src/agent_sessions/cli/parsers/antigravity.rs"] = {
 "new": ("Constructs a new AntigravityParser for the given session.", ["parser","constructor"]),
 "parse_line": ("Parses a single line of Antigravity CLI output into normalized chunk(s).", ["parser","streaming"]),
 "on_exit": ("Finalizes parser state when the Antigravity CLI process exits.", ["parser","lifecycle"]),
}
FUNC["src-tauri/src/agent_sessions/cli/parsers/claude_code.rs"] = {
 "new": ("Constructs a new ClaudeCodeParser for the given session.", ["parser","constructor"]),
 "normalize_args": ("Normalizes Claude Code tool-call arguments into the app's canonical argument shape.", ["parser","normalization"]),
 "tool_call_delta_chunk": ("Builds a streaming tool-call argument delta chunk from partial Claude Code tool-call JSON.", ["parser","streaming","tool-call"]),
 "count_lines": ("Counts the number of lines in a text block, used for diff/result summaries.", ["utility"]),
 "normalize_result": ("Normalizes a Claude Code tool-call result payload into the canonical result chunk shape.", ["parser","normalization"]),
 "parse_line": ("Parses a single line of Claude Code CLI JSON output, dispatching to the appropriate event handler and emitting normalized chunks.", ["parser","streaming","entry-point"]),
 "on_exit": ("Finalizes parser state and emits a completion chunk when the Claude Code CLI process exits.", ["parser","lifecycle"]),
}
FUNC["src-tauri/src/agent_sessions/cli/parsers/codex.rs"] = {
 "new": ("Constructs a new CodexParser for the given session.", ["parser","constructor"]),
 "item_call_id": ("Extracts the tool-call id from a raw Codex event item.", ["parser","tool-call"]),
 "stamp_tool_call_identity": ("Attaches a stable tool-call id to an emitted chunk for correlation with later results.", ["parser","tool-call"]),
 "extract_reasoning_text": ("Extracts reasoning/thinking text from a raw Codex event item.", ["parser","reasoning"]),
 "parse_new_format": ("Parses a Codex event in the newer JSON event schema, dispatching by top-level type into normalized chunks.", ["parser","streaming"]),
 "parse_line": ("Parses a single line of Codex CLI JSON output into normalized transcript chunks.", ["parser","streaming","entry-point"]),
 "on_exit": ("Finalizes parser state when the Codex CLI process exits.", ["parser","lifecycle"]),
}
FUNC["src-tauri/src/agent_sessions/cli/parsers/codex_app_server.rs"] = {
 "register": ("Registers an interrupt sender for an in-flight Codex app-server turn so it can be cancelled.", ["concurrency","cancellation"]),
 "interrupt_sender": ("Looks up the registered interrupt sender for a session's in-flight turn.", ["concurrency","cancellation"]),
 "interrupt_registered": ("Checks whether a session currently has a registered, interruptible turn.", ["concurrency","query"]),
 "interrupt_session_gracefully": ("Sends a graceful interrupt signal to a running Codex app-server turn.", ["concurrency","cancellation"]),
 "thread_permission_params": ("Maps the app's permission mode to Codex app-server thread permission parameters.", ["permissions","mapping"]),
 "approval_auto_accept": ("Determines whether a given permission mode should auto-accept tool-call approvals without prompting the user for the Codex app-server.", ["permissions","approval"]),
 "new": ("Constructs a new CodexAppServerEventParser for a session.", ["parser","constructor"]),
 "on_thread_response": ("Handles a thread-creation JSON-RPC response, capturing the new thread id.", ["json-rpc","parser"]),
 "emit_session_start": ("Emits a session-start chunk once the Codex app-server thread has been established.", ["parser","lifecycle"]),
 "handle_notification": ("Dispatches an incoming Codex app-server JSON-RPC notification by method name to the appropriate item/event parser.", ["json-rpc","dispatch"]),
 "exec_item_type": ("Maps a Codex app-server v2 item type string to the app's canonical execution item type.", ["mapping","normalization"]),
 "stamp_tool_call_identity": ("Attaches a stable tool-call id to an emitted chunk for later correlation.", ["parser","tool-call"]),
 "parse_item": ("Parses a Codex app-server 'item' payload (command, patch, message, reasoning) into normalized transcript chunks.", ["parser","streaming"]),
 "rpc_send": ("Writes a JSON-RPC request to the Codex app-server process's stdin.", ["json-rpc","io"]),
 "rpc_notify": ("Writes a JSON-RPC notification (no response expected) to the Codex app-server process.", ["json-rpc","io"]),
 "rpc_respond": ("Writes a JSON-RPC success response to a request from the Codex app-server process.", ["json-rpc","io"]),
 "rpc_respond_error": ("Writes a JSON-RPC error response to a request from the Codex app-server process.", ["json-rpc","io"]),
 "write_line": ("Writes a single JSON-RPC message as a newline-delimited line to the process stdin.", ["json-rpc","io"]),
 "read_message": ("Reads and parses the next line-delimited JSON-RPC message from the Codex app-server process's stdout.", ["json-rpc","io"]),
 "await_response": ("Reads server messages until the response matching a given request id arrives, dispatching other messages along the way.", ["json-rpc","concurrency"]),
 "dispatch_server_message": ("Routes a parsed Codex app-server JSON-RPC message to notification handling, approval requests, or response resolution.", ["json-rpc","dispatch"]),
 "emit_approval_chunk": ("Emits an approval-decision chunk and responds to the Codex app-server for an auto/interactive permission request.", ["json-rpc","approval"]),
 "run_app_server_turn": ("Drives a full Codex app-server turn -- sending the thread/turn request, streaming notifications, and returning the final turn result.", ["json-rpc","orchestration","entry-point"]),
}
FUNC["src-tauri/src/agent_sessions/cli/parsers/copilot.rs"] = {
 "run_acp_protocol": ("Runs the ACP session loop for the Copilot CLI agent by delegating to the shared acp_common::run_acp_protocol implementation.", ["acp-protocol","entry-point"]),
}
FUNC["src-tauri/src/agent_sessions/cli/parsers/cursor.rs"] = {
 "new": ("Constructs a new CursorParser for the given session.", ["parser","constructor"]),
 "flush_pending_text": ("Flushes any buffered assistant text as a text-delta chunk.", ["parser","streaming"]),
 "extract_tool": ("Extracts tool name and arguments from a raw Cursor CLI tool-call event.", ["parser","tool-call"]),
 "parse_line": ("Parses a single line of Cursor CLI JSON output into normalized transcript chunks.", ["parser","streaming","entry-point"]),
 "on_exit": ("Finalizes parser state when the Cursor CLI process exits.", ["parser","lifecycle"]),
}
FUNC["src-tauri/src/agent_sessions/cli/parsers/kiro.rs"] = {
 "map_tool_kind": ("Maps a raw Kiro ACP tool-call kind/name into the app's canonical tool kind (Edit, Read, Shell, Grep, etc.).", ["acp-protocol","mapping"]),
 "handle_custom_notification": ("Handles Kiro-specific custom ACP notification methods not covered by the standard protocol.", ["acp-protocol","notification"]),
 "run_acp_protocol": ("Runs the ACP session loop for the Kiro CLI agent by delegating to the shared acp_common::run_acp_protocol implementation.", ["acp-protocol","entry-point"]),
 "build_kiro_proxy_env": ("Builds the proxy-related environment variables needed to run the Kiro CLI through a corporate/organization proxy.", ["proxy","environment"]),
 "kiro_sessions_dir": ("Resolves the directory where Kiro CLI stores its local session files.", ["filesystem","kiro"]),
 "clean_stale_lock": ("Detects and removes a stale Kiro session lock file left behind by a dead process.", ["filesystem","concurrency","cleanup"]),
 "list_kiro_sessions": ("Lists Kiro CLI sessions discovered on disk, including cwd, last-modified time, and lock status.", ["filesystem","kiro","query"]),
 "list_kiro_sessions_cmd": ("Tauri command wrapper that lists discovered Kiro CLI sessions.", ["tauri-command","kiro"]),
}
FUNC["src-tauri/src/agent_sessions/cli/parsers/normalizer.rs"] = {
 "normalize_tool_name": ("Maps a raw, agent-specific tool name to the app's canonical tool name.", ["normalization","tool-call"]),
 "unwrap_codex_command": ("Unwraps a Codex shell-command argument (e.g. a bash -lc wrapper) to the underlying command string.", ["normalization","codex"]),
 "extract_file_path": ("Extracts a file path from a tool call's raw argument payload.", ["normalization","file-path"]),
 "extract_command": ("Extracts a shell command string from a tool call's raw argument payload.", ["normalization","command"]),
}
FUNC["src-tauri/src/agent_sessions/cli/parsers/opencode.rs"] = {
 "extract_task_result": ("Extracts the <task_result> payload embedded in an OpenCode subagent tool-call's text content.", ["acp-protocol","parsing"]),
 "quoted_attr": ("Extracts a quoted attribute value (e.g. prompt=\"...\") from an XML-like tag header string.", ["parsing","utility"]),
 "is_generic_task_label": ("Checks whether a string is a generic, non-informative task label to be filtered from display.", ["heuristic","filtering"]),
 "is_paste_placeholder": ("Checks whether a string is a paste/attachment placeholder rather than real content.", ["heuristic","filtering"]),
 "is_result_like_report": ("Checks whether a string looks like a completion report rather than a task prompt.", ["heuristic","filtering"]),
 "strip_known_prompt_prelude": ("Strips known boilerplate prelude text from a subagent task prompt string.", ["heuristic","normalization"]),
 "non_generic_string": ("Returns the value only if it passes all the generic/placeholder/report filters, otherwise None.", ["heuristic","filtering"]),
 "first_raw_input_string": ("Returns the first non-generic string value found among a set of candidate keys in a raw tool-call input payload.", ["parsing","utility"]),
 "extract_task_prompt": ("Extracts the best-guess subagent task prompt from multiple candidate sources in an OpenCode tool call.", ["acp-protocol","parsing"]),
 "opencode_app_session_id": ("Validates and extracts an OpenCode application session id from a raw string.", ["parsing","session"]),
 "extract_task_session_id": ("Extracts the OpenCode subagent session id embedded in a task-result payload.", ["acp-protocol","parsing"]),
 "is_completed_task_result": ("Checks whether tool-call content represents a completed subagent task result.", ["heuristic","filtering"]),
 "map_tool_kind": ("Maps a raw OpenCode ACP tool-call kind/name into the app's canonical tool kind.", ["acp-protocol","mapping"]),
 "map_tool_result_chunk": ("Builds a normalized tool-result chunk for OpenCode tool calls, special-casing subagent task delegation results.", ["acp-protocol","normalization"]),
 "should_emit_tool_start": ("Decides whether a tool-start event should be emitted for a given OpenCode tool name.", ["acp-protocol","filtering"]),
 "should_emit_tool_result": ("Decides whether a tool-result event should be emitted for a given OpenCode tool call outcome.", ["acp-protocol","filtering"]),
 "run_acp_protocol": ("Runs the ACP session loop for the OpenCode CLI agent by delegating to the shared acp_common::run_acp_protocol implementation.", ["acp-protocol","entry-point"]),
}
FUNC["src-tauri/src/agent_sessions/cli/parsers/types.rs"] = {
 "as_str": ("Converts a CliAgentType variant to its canonical string identifier.", ["serialization","enum"]),
 "parse": ("Parses a string into a CliAgentType variant.", ["parsing","enum"]),
}
FUNC["src-tauri/src/agent_sessions/cli/persistence/chunk_ops.rs"] = {
 "max_chunk_sequence": ("Returns the highest chunk sequence number currently stored for a session.", ["persistence","query"]),
 "insert_chunk": ("Inserts a new transcript chunk row for a session at the given sequence number.", ["persistence","mutation"]),
 "run_chunk_side_effects": ("Runs any side effects triggered by a newly inserted chunk (e.g. persisting subagent child sessions).", ["persistence","side-effects"]),
 "run_chunk_side_effects_with_args": ("Runs chunk side effects using a pre-serialized arguments string, avoiding redundant serialization.", ["persistence","side-effects"]),
 "is_subagent_chunk": ("Checks whether a chunk represents a subagent task-delegation tool call.", ["persistence","subagent"]),
 "subagent_session_id": ("Extracts the subagent session id from a subagent-delegation chunk, if present.", ["persistence","subagent"]),
 "persist_subagent_child_session": ("Creates/links a persisted child session record for a subagent task spawned from a chunk.", ["persistence","subagent","mutation"]),
 "truncate_label": ("Truncates a label string to a display-safe length.", ["utility","string"]),
 "load_chunks": ("Loads all transcript chunks for a session in sequence order.", ["persistence","query"]),
 "truncate_chunks_after": ("Deletes transcript chunks created after a given timestamp for a session.", ["persistence","mutation"]),
 "truncate_chunks_after_with_reason": ("Deletes transcript chunks after a given timestamp and records a history-mutation reason.", ["persistence","mutation","audit"]),
}
FUNC["src-tauri/src/agent_sessions/cli/persistence/session_crud.rs"] = {
 "now_iso": ("Returns the current UTC timestamp formatted as an RFC 3339 string.", ["utility","time"]),
 "sync_orgtrack_mirror": ("Synchronizes a session's state to the org-tracking mirror table/service.", ["persistence","org-sync"]),
 "create_session": ("Inserts a new CLI agent session row with the given creation parameters.", ["persistence","mutation","entry-point"]),
 "get_session": ("Fetches a single CLI agent session by id.", ["persistence","query"]),
 "list_sessions": ("Lists all CLI agent sessions.", ["persistence","query"]),
 "list_sessions_page": ("Lists CLI agent sessions with pagination.", ["persistence","query","pagination"]),
 "update_status": ("Updates a session's status.", ["persistence","mutation"]),
 "update_status_with_error": ("Updates a session's status and records an associated error message.", ["persistence","mutation"]),
 "update_pid": ("Records the OS process id of a session's running CLI agent.", ["persistence","mutation"]),
 "clear_pid": ("Clears the recorded process id for a session once it has exited.", ["persistence","mutation"]),
 "resume_profile_key": ("Computes the profile key used to look up per-account CLI resume state.", ["persistence","resume"]),
 "update_cli_session_id": ("Records the underlying CLI tool's own session id for resume purposes.", ["persistence","resume","mutation"]),
 "update_cli_session_id_for_account": ("Records a per-account CLI resume session id, supporting multi-account resume.", ["persistence","resume","mutation"]),
 "session_persists_chunks": ("Determines whether a session persists its transcript via managed chunks (vs. a native transcript source).", ["persistence","transcript"]),
 "latest_native_transcript_id": ("Fetches the most recently bound native transcript id for a session and source.", ["persistence","transcript"]),
 "get_cli_session_id_for_account": ("Fetches the CLI resume session id recorded for a specific account.", ["persistence","resume","query"]),
 "bump_history_mutation_with_tx": ("Increments a session's history-mutation epoch within an existing transaction.", ["persistence","audit"]),
 "clear_cli_resume_state_with_tx": ("Clears a session's CLI resume state within an existing transaction, recording the mutation reason.", ["persistence","resume","mutation"]),
 "clear_cli_resume_state": ("Clears a session's CLI resume state (used when truncating history invalidates resumability).", ["persistence","resume","mutation"]),
 "get_history_mutation": ("Fetches a session's current history-mutation record.", ["persistence","audit","query"]),
 "mapped_cli_session_id_for_account_with_conn": ("Resolves the CLI resume session id mapped for an account using an explicit connection.", ["persistence","resume","query"]),
 "update_name": ("Renames a session.", ["persistence","mutation"]),
 "update_model_and_account": ("Updates the model and account associated with a session.", ["persistence","mutation"]),
 "update_agent_exec_mode": ("Updates a session's agent execution mode (e.g. interactive vs. autonomous).", ["persistence","mutation"]),
 "update_draft_text": ("Persists an in-progress draft message for a session.", ["persistence","mutation"]),
 "update_reply_target_event_id": ("Sets the event id a session's next reply should be threaded under.", ["persistence","mutation"]),
 "update_pinned": ("Toggles whether a session is pinned.", ["persistence","mutation"]),
 "update_proxy_credentials": ("Updates a session's proxy authentication credentials.", ["persistence","mutation","proxy"]),
 "delete_session": ("Deletes a session and its associated persisted state.", ["persistence","mutation"]),
 "sweep_stale_sessions": ("Sweeps and cleans up sessions left in a stale/running state from a previous app run.", ["persistence","cleanup"]),
 "row_to_session": ("Maps a SQLite row into a CodeSession domain struct.", ["persistence","mapping"]),
}
FUNC["src-tauri/src/agent_sessions/cli/persistence/worktree_state.rs"] = {
 "update_worktree_info": ("Records the git worktree path and branch information for a session.", ["persistence","git","mutation"]),
 "update_merge_status": ("Updates the recorded merge status of a session's worktree.", ["persistence","git","mutation"]),
}
FUNC["src-tauri/src/agent_sessions/cli/platform_adapters/claude_code/oauth.rs"] = {
 "start_claude_code_oauth_login": ("Begins a Claude Code OAuth login by generating PKCE parameters and the authorization URL.", ["oauth","authentication"]),
 "exchange_claude_code_oauth_code": ("Exchanges a Claude Code OAuth authorization code for access/refresh tokens after validating the state parameter.", ["oauth","authentication"]),
 "create_claude_code_oauth_webview": ("Creates an embedded webview to drive the Claude Code OAuth login (including Google SSO popup handling) and detect the callback URL.", ["oauth","webview"]),
 "close_claude_code_oauth_webview": ("Closes the Claude Code OAuth login webview.", ["oauth","webview"]),
 "clear_claude_code_oauth_browser_session": ("Clears the Claude Code OAuth webview's browser session/cookies to force a fresh login.", ["oauth","webview","cleanup"]),
 "is_google_accounts_url": ("Checks whether a URL belongs to Google's account/SSO domains.", ["oauth","url-matching"]),
 "is_claude_code_callback_url": ("Checks whether a URL is the Claude Code OAuth callback URL.", ["oauth","url-matching"]),
 "is_google_gsi_transform_url": ("Checks whether a URL is Google's GSI (Sign-In) transform/redirect URL.", ["oauth","url-matching"]),
 "random_base64url": ("Generates a random base64url-encoded string of the given byte length, used for PKCE verifiers/state.", ["oauth","crypto"]),
 "pkce_challenge": ("Derives a PKCE code challenge (S256) from a code verifier.", ["oauth","crypto"]),
 "build_authorize_url": ("Builds the Claude Code OAuth authorization URL with the given state and PKCE challenge.", ["oauth","url-building"]),
 "clean_authorization_code": ("Strips extraneous characters/whitespace from a raw authorization code.", ["oauth","normalization"]),
 "exchange_code_for_tokens": ("Sends the token-exchange HTTP request to Claude Code's OAuth token endpoint.", ["oauth","http"]),
 "fetch_claude_code_oauth_profile": ("Fetches the authenticated user's Claude Code account/organization profile.", ["oauth","http"]),
 "parse_claude_code_oauth_profile_response": ("Parses the Claude Code profile endpoint's JSON response body.", ["oauth","parsing"]),
 "normalize_metadata_field": ("Normalizes an optional account-metadata string field, treating blanks as unset.", ["oauth","normalization"]),
}
FUNC["src-tauri/src/agent_sessions/cli/platform_adapters/codex/oauth.rs"] = {
 "start_codex_oauth_login": ("Begins a Codex OAuth login by generating PKCE parameters and the authorization URL.", ["oauth","authentication"]),
 "exchange_codex_oauth_code": ("Exchanges a Codex OAuth authorization code for access/refresh tokens after validating state.", ["oauth","authentication"]),
 "create_codex_oauth_webview": ("Creates an embedded webview to drive the Codex OAuth login, including popup-window handling for the sign-in flow.", ["oauth","webview"]),
 "close_codex_oauth_webview": ("Closes the Codex OAuth login webview.", ["oauth","webview"]),
 "clear_codex_oauth_browser_session": ("Clears the Codex OAuth webview's browser session/cookies to force a fresh login.", ["oauth","webview","cleanup"]),
 "should_open_oauth_popup": ("Determines whether a navigated URL should trigger opening a separate OAuth sign-in popup window.", ["oauth","url-matching"]),
 "is_codex_callback_url": ("Checks whether a URL is the Codex OAuth callback URL.", ["oauth","url-matching"]),
 "random_base64url": ("Generates a random base64url-encoded string, used for PKCE verifiers/state.", ["oauth","crypto"]),
 "pkce_challenge": ("Derives a PKCE code challenge (S256) from a code verifier.", ["oauth","crypto"]),
 "build_authorize_url": ("Builds the Codex OAuth authorization URL with redirect URI, state, and PKCE challenge.", ["oauth","url-building"]),
 "clean_authorization_code": ("Strips extraneous characters/whitespace from a raw authorization code.", ["oauth","normalization"]),
 "exchange_code_for_tokens": ("Sends the token-exchange HTTP request to Codex's OAuth token endpoint.", ["oauth","http"]),
}
FUNC["src-tauri/src/agent_sessions/cli/platform_adapters/cursor/session_capture.rs"] = {
 "start_cursor_native_oauth_login": ("Begins a Cursor native OAuth login by generating a login UUID/verifier and building the login URL.", ["oauth","authentication"]),
 "poll_cursor_native_oauth_token": ("Polls Cursor's OAuth endpoint for the access token corresponding to a pending native login.", ["oauth","polling"]),
 "create_cursor_session_webview": ("Creates a hidden webview used to capture a Cursor session cookie via the account sign-in flow.", ["oauth","webview"]),
 "poll_cursor_session": ("Polls the hidden Cursor session webview for the session cookie once available.", ["oauth","polling"]),
 "close_cursor_session_webview": ("Closes the hidden Cursor session-capture webview.", ["oauth","webview","cleanup"]),
 "stop_cursor_session_polling": ("Stops an in-progress poller for a Cursor session-capture webview.", ["oauth","polling","cleanup"]),
 "clear_cursor_session": ("Clears and closes a Cursor session-capture webview and its poller.", ["oauth","webview","cleanup"]),
 "clear_cursor_oauth_browser_session": ("Clears the Cursor OAuth webview's browser session/cookies to force a fresh login.", ["oauth","webview","cleanup"]),
 "random_base64url": ("Generates a random base64url-encoded string used for PKCE/login verifiers.", ["oauth","crypto"]),
 "pkce_challenge": ("Derives a PKCE code challenge from a login verifier.", ["oauth","crypto"]),
 "start_token_poller": ("Starts a background task that repeatedly polls a Cursor session-capture webview until a session cookie is found or it times out.", ["oauth","polling","concurrency"]),
 "stop_poller": ("Signals a running Cursor session-token poller to stop.", ["oauth","polling","concurrency"]),
 "get_cursor_session_token": ("Retrieves the captured Cursor session token/cookie once polling completes.", ["oauth","query"]),
}
FUNC["src-tauri/src/agent_sessions/cli/platform_adapters/cursor/usage/tracker.rs"] = {
 "fetch_cursor_usage": ("Fetches Cursor CLI usage events for a session token and time range, aggregating token counts by model.", ["usage-tracking","http"]),
 "make_request": ("Sends an authenticated HTTP request to Cursor's usage-events endpoint.", ["usage-tracking","http"]),
 "is_auth_failure": ("Checks whether an HTTP status code indicates an authentication failure requiring re-login.", ["usage-tracking","http"]),
 "build_alt_token": ("Builds an alternate authorization token format to retry against Cursor's API.", ["usage-tracking","authentication"]),
 "extract_user_id_from_jwt": ("Extracts the user id claim from a Cursor session JWT without verifying its signature.", ["usage-tracking","jwt"]),
 "normalize_model": ("Normalizes a raw Cursor usage-event model name into the app's canonical model identifier.", ["usage-tracking","normalization"]),
 "models_match": ("Determines whether a CLI-reported model name and an API-reported model name refer to the same model.", ["usage-tracking","matching"]),
 "get_local_cursor_session_token": ("Reads the Cursor session token from the local Cursor CLI/IDE state on disk.", ["usage-tracking","filesystem"]),
 "get_cursor_state_db_path": ("Resolves the filesystem path of Cursor's local state database.", ["usage-tracking","filesystem"]),
}
FUNC["src-tauri/src/agent_sessions/cli/platform_adapters/kiro/kiro_auth.rs"] = {
 "start_kiro_login": ("Drives the full Kiro AWS identity-provider login flow -- launching the auth webview, waiting for completion, and reading resulting tokens.", ["oauth","authentication","entry-point"]),
 "cancel_kiro_login": ("Cancels an in-progress Kiro login attempt.", ["oauth","cancellation"]),
 "create_kiro_auth_webview": ("Creates the embedded webview used to drive Kiro's identity-provider sign-in page.", ["oauth","webview"]),
 "close_kiro_auth_webview": ("Closes the Kiro auth webview.", ["oauth","webview"]),
 "read_kiro_tokens": ("Reads the Kiro CLI's persisted auth tokens from disk after a successful login.", ["oauth","filesystem"]),
 "cancel_existing_login": ("Signals any existing in-progress Kiro login to stop before starting a new one.", ["oauth","cancellation"]),
}
FUNC["src-tauri/src/agent_sessions/cli/platform_adapters/kiro/proxy_auth.rs"] = {
 "kiro_sqlite_relative_path": ("Resolves the relative path of Kiro's local SQLite auth database within its home directory.", ["filesystem","kiro"]),
 "create_kiro_auth_schema": ("Creates the SQLite schema Kiro's CLI expects for its local auth database.", ["database","schema"]),
 "write_kiro_auth_records": ("Writes proxy-issued token and device-registration records into Kiro's local auth database.", ["database","mutation"]),
 "prepare_kiro_home": ("Prepares a Kiro CLI home directory (config/state layout) for proxied or own-key operation.", ["filesystem","setup"]),
 "setup_proxy_auth_db": ("Provisions a fresh Kiro home directory and auth database configured to use the app's managed proxy credentials.", ["proxy","database","setup"]),
 "setup_own_key_home": ("Prepares a Kiro CLI home directory configured to use the user's own AWS/Kiro credentials rather than the proxy.", ["authentication","setup"]),
}

# CLASS[path][name] = (summary, tags)
CLASS = {}
CLASS["src-tauri/src/agent_sessions/cli/hook_approvals.rs"] = {
 "HookApprovalDecision": ("Enum representing the outcome of a hook permission decision: Allow, Deny, or Passthrough.", ["approval","enum","domain-model"]),
}
CLASS["src-tauri/src/agent_sessions/cli/parsers/acp_common.rs"] = {
 "AcpAgentAdapter": ("Trait describing agent-specific ACP hooks -- mapping tool kinds, handling custom notifications, and controlling which tool events get emitted.", ["acp-protocol","trait","adapter"]),
}
CLASS["src-tauri/src/agent_sessions/cli/parsers/antigravity.rs"] = {
 "AntigravityParser": ("Streaming parser state for the Antigravity CLI agent, implementing the CliAgentParser trait to convert raw output into transcript chunks.", ["parser","cli-agent","state"]),
}
CLASS["src-tauri/src/agent_sessions/cli/parsers/claude_code.rs"] = {
 "ClaudeCodeParser": ("Streaming parser state for the Claude Code CLI agent -- tracks thread id, token usage, and in-flight tool-call blocks while converting raw JSON events into transcript chunks.", ["parser","cli-agent","state"]),
}
CLASS["src-tauri/src/agent_sessions/cli/parsers/codex.rs"] = {
 "CodexParser": ("Streaming parser state for the legacy Codex CLI output format, tracking thread id, usage, and turn-completion status.", ["parser","cli-agent","state"]),
}
CLASS["src-tauri/src/agent_sessions/cli/parsers/codex_app_server.rs"] = {
 "InterruptRegistration": ("Tracks the interrupt sender registered for an in-flight Codex app-server session, enabling graceful cancellation.", ["concurrency","state"]),
 "CodexAppServerEventParser": ("Streaming parser/state machine for the Codex app-server protocol, tracking thread/turn ids, usage, and turn status while converting notifications into transcript chunks.", ["parser","state","json-rpc"]),
 "CodexAppServerTurn": ("Request parameters for a single Codex app-server turn -- task prompt, working directory, resume thread id, model, permission mode, and image attachments.", ["json-rpc","domain-model"]),
 "CodexAppServerResult": ("Result of a completed Codex app-server turn -- resulting thread id, turn status, and token usage.", ["json-rpc","domain-model"]),
}
CLASS["src-tauri/src/agent_sessions/cli/parsers/cursor.rs"] = {
 "CursorParser": ("Streaming parser state for the Cursor CLI agent, buffering pending text and tracking token usage while converting raw output into transcript chunks.", ["parser","cli-agent","state"]),
}
CLASS["src-tauri/src/agent_sessions/cli/parsers/kiro.rs"] = {
 "KiroAcpAdapter": ("ACP adapter implementing Kiro-specific tool-kind mapping and custom notification handling.", ["acp-protocol","adapter"]),
}
CLASS["src-tauri/src/agent_sessions/cli/parsers/mod.rs"] = {
 "CliAgentParser": ("Trait implemented by every CLI-agent-specific parser, defining the common interface (parse_line, on_exit, token_usage, cli_session_id) used to convert raw CLI output into transcript chunks.", ["trait","parser","interface"]),
}
CLASS["src-tauri/src/agent_sessions/cli/parsers/opencode.rs"] = {
 "OpenCodeAdapter": ("ACP adapter implementing OpenCode-specific tool-kind mapping and subagent task-result normalization.", ["acp-protocol","adapter"]),
}
CLASS["src-tauri/src/agent_sessions/cli/parsers/types.rs"] = {
 "CliAgentType": ("Enum of every CLI agent integration supported by the app (Claude Code, Codex, Cursor, Kiro, Copilot, OpenCode, and many more), used throughout parsing, launch profiles, and persistence.", ["enum","domain-model","cli-agent"]),
 "TokenUsage": ("Struct tracking input/output/cache token counts and model name for a CLI agent turn, used across all parser implementations.", ["domain-model","token-usage"]),
}
CLASS["src-tauri/src/agent_sessions/cli/persistence/types.rs"] = {
 "CodeSession": ("Row type representing a persisted CLI agent session -- includes identity, status, runner/model/account, git worktree state, proxy credentials, org/project linkage, and timestamps.", ["domain-model","database"]),
 "CreateCodeSessionParams": ("Parameters accepted when creating a new CLI agent session, covering agent selection, git repo/branch, isolation, and org/project context.", ["domain-model","database"]),
}

# Extra-include: (path, name) pairs for functions below the 10-line threshold that are
# still meaningful (exported Tauri commands / thin delegating wrappers surfaced by
# cross-file call-graph evidence), excluding pure trait-getter accessors.
EXTRA_FUNCS = {
 ("src-tauri/src/agent_sessions/cli/commands.rs", "cli_agent_history_mutation"),
 ("src-tauri/src/agent_sessions/cli/commands.rs", "cli_agent_status"),
 ("src-tauri/src/agent_sessions/cli/commands.rs", "cli_launch_profile_reset"),
 ("src-tauri/src/agent_sessions/cli/commands.rs", "cli_agent_cancel"),
 ("src-tauri/src/agent_sessions/cli/commands.rs", "cli_launch_profile_get"),
 ("src-tauri/src/agent_sessions/cli/commands.rs", "cli_agent_list"),
 ("src-tauri/src/agent_sessions/cli/commands.rs", "cli_agent_tui_release"),
 ("src-tauri/src/agent_sessions/cli/hook_approvals.rs", "unregister_session"),
 ("src-tauri/src/agent_sessions/cli/hook_approvals.rs", "as_wire_str"),
 ("src-tauri/src/agent_sessions/cli/hook_approvals.rs", "has_pending_hook_approval"),
 ("src-tauri/src/agent_sessions/cli/hook_approvals.rs", "register_session_permission_mode"),
 ("src-tauri/src/agent_sessions/cli/launch_profile_store.rs", "cli_launch_profile_reset"),
 ("src-tauri/src/agent_sessions/cli/native_transcript.rs", "native_transcript_enabled"),
 ("src-tauri/src/agent_sessions/cli/native_transcript.rs", "imported_session_id"),
 ("src-tauri/src/agent_sessions/cli/native_transcript.rs", "imported_transcript_id_for_managed_session"),
 ("src-tauri/src/agent_sessions/cli/parsers/acp_common.rs", "flush_thought_buffer"),
 ("src-tauri/src/agent_sessions/cli/parsers/antigravity.rs", "new"),
 ("src-tauri/src/agent_sessions/cli/parsers/claude_code.rs", "new"),
 ("src-tauri/src/agent_sessions/cli/parsers/codex.rs", "new"),
 ("src-tauri/src/agent_sessions/cli/parsers/codex_app_server.rs", "approval_auto_accept"),
 ("src-tauri/src/agent_sessions/cli/parsers/codex_app_server.rs", "thread_permission_params"),
 ("src-tauri/src/agent_sessions/cli/parsers/cursor.rs", "new"),
 ("src-tauri/src/agent_sessions/cli/parsers/kiro.rs", "list_kiro_sessions_cmd"),
 ("src-tauri/src/agent_sessions/cli/parsers/normalizer.rs", "extract_file_path"),
 ("src-tauri/src/agent_sessions/cli/parsers/normalizer.rs", "unwrap_codex_command"),
 ("src-tauri/src/agent_sessions/cli/persistence/chunk_ops.rs", "truncate_chunks_after"),
 ("src-tauri/src/agent_sessions/cli/persistence/chunk_ops.rs", "run_chunk_side_effects"),
 ("src-tauri/src/agent_sessions/cli/persistence/chunk_ops.rs", "max_chunk_sequence"),
 ("src-tauri/src/agent_sessions/cli/persistence/session_crud.rs", "clear_pid"),
 ("src-tauri/src/agent_sessions/cli/persistence/session_crud.rs", "update_pid"),
 ("src-tauri/src/agent_sessions/cli/persistence/session_crud.rs", "update_pinned"),
 ("src-tauri/src/agent_sessions/cli/persistence/session_crud.rs", "clear_cli_resume_state"),
 ("src-tauri/src/agent_sessions/cli/persistence/session_crud.rs", "now_iso"),
 ("src-tauri/src/agent_sessions/cli/persistence/worktree_state.rs", "update_merge_status"),
 ("src-tauri/src/agent_sessions/cli/platform_adapters/claude_code/oauth.rs", "close_claude_code_oauth_webview"),
 ("src-tauri/src/agent_sessions/cli/platform_adapters/codex/oauth.rs", "close_codex_oauth_webview"),
 ("src-tauri/src/agent_sessions/cli/platform_adapters/cursor/session_capture.rs", "stop_cursor_session_polling"),
 ("src-tauri/src/agent_sessions/cli/platform_adapters/kiro/kiro_auth.rs", "cancel_kiro_login"),
 ("src-tauri/src/agent_sessions/cli/platform_adapters/kiro/kiro_auth.rs", "close_kiro_auth_webview"),
}

EXTRA_CLASSES = {
 ("src-tauri/src/agent_sessions/cli/hook_approvals.rs", "HookApprovalDecision"),
 ("src-tauri/src/agent_sessions/cli/parsers/types.rs", "TokenUsage"),
 ("src-tauri/src/agent_sessions/cli/parsers/codex_app_server.rs", "CodexAppServerTurn"),
 ("src-tauri/src/agent_sessions/cli/parsers/codex_app_server.rs", "CodexAppServerResult"),
}

# High-confidence cross-file "calls" edges discovered via callGraph module-qualified
# callee names (mod::function) matched against sibling files in this same batch.
CROSS_CALLS = [
 ("src-tauri/src/agent_sessions/cli/commands.rs", "cli_launch_profile_get",
  "src-tauri/src/agent_sessions/cli/launch_profile_store.rs", "cli_launch_profile_get"),
 ("src-tauri/src/agent_sessions/cli/commands.rs", "cli_launch_profile_update",
  "src-tauri/src/agent_sessions/cli/launch_profile_store.rs", "cli_launch_profile_update"),
 ("src-tauri/src/agent_sessions/cli/commands.rs", "cli_launch_profile_reset",
  "src-tauri/src/agent_sessions/cli/launch_profile_store.rs", "cli_launch_profile_reset"),
 ("src-tauri/src/agent_sessions/cli/commands.rs", "load_native_transcript_chunks",
  "src-tauri/src/agent_sessions/cli/native_transcript.rs", "native_transcript_binding"),
 ("src-tauri/src/agent_sessions/cli/commands.rs", "cli_agent_transcript_path",
  "src-tauri/src/agent_sessions/cli/native_transcript.rs", "native_store_key_for_managed_session"),
 ("src-tauri/src/agent_sessions/cli/parsers/copilot.rs", "run_acp_protocol",
  "src-tauri/src/agent_sessions/cli/parsers/acp_common.rs", "run_acp_protocol"),
 ("src-tauri/src/agent_sessions/cli/parsers/kiro.rs", "run_acp_protocol",
  "src-tauri/src/agent_sessions/cli/parsers/acp_common.rs", "run_acp_protocol"),
 ("src-tauri/src/agent_sessions/cli/parsers/opencode.rs", "run_acp_protocol",
  "src-tauri/src/agent_sessions/cli/parsers/acp_common.rs", "run_acp_protocol"),
 ("src-tauri/src/agent_sessions/cli/parsers/claude_code.rs", "parse_line",
  "src-tauri/src/agent_sessions/cli/parsers/normalizer.rs", "normalize_tool_name"),
 ("src-tauri/src/agent_sessions/cli/parsers/codex.rs", "parse_new_format",
  "src-tauri/src/agent_sessions/cli/parsers/normalizer.rs", "normalize_tool_name"),
]

# Cross-batch "calls" edges to neighborMap symbols (webview_session.rs, batch 13),
# discovered via direct callee references in the callGraph.
NEIGHBOR_CALLS = [
 ("src-tauri/src/agent_sessions/cli/platform_adapters/claude_code/oauth.rs", "clear_claude_code_oauth_browser_session",
  "src-tauri/src/agent_sessions/cli/platform_adapters/webview_session.rs", "clear_oauth_browser_session_native"),
 ("src-tauri/src/agent_sessions/cli/platform_adapters/codex/oauth.rs", "clear_codex_oauth_browser_session",
  "src-tauri/src/agent_sessions/cli/platform_adapters/webview_session.rs", "clear_oauth_browser_session_native"),
 ("src-tauri/src/agent_sessions/cli/platform_adapters/cursor/session_capture.rs", "clear_cursor_oauth_browser_session",
  "src-tauri/src/agent_sessions/cli/platform_adapters/webview_session.rs", "clear_oauth_browser_session_native"),
]
