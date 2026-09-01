# ORG2 Agent Adapter Layer Verification

Date: 2026-07-05

Scope: verification of ORG2's API/CLI agent adapter layer by reading code only. No servers were run and no runtime behavior was exercised.

## Executive Verdict

ORG2 is best described as a session adapter and orchestration layer that supports both CLI-backed agents and native/API-backed Rust agents. "Proxy" is only partly accurate.

Observed facts:

- The frontend has a common `SessionAdapter` contract for different session categories. Its comments explicitly say each session type implements load-history, event normalization, setup, send prompt, and stop behavior (`src/engines/SessionCore/sync/types.ts:1-15`, `src/engines/SessionCore/sync/types.ts:170-208`).
- Frontend send-message dispatch is category-based: `SessionService.sendMessage` gets an adapter with `getAdapterForSession` and calls `adapter.sendMessage`, rather than directly branching in the service (`src/engines/SessionCore/services/SessionService.ts:279-330`).
- CLI agents are not native provider calls. They are OS subprocesses built by per-agent command constructors, spawned by `session_runner`, parsed line-by-line or over ACP JSON-RPC, persisted, and fanned out as normalized events (`src-tauri/src/agent_sessions/cli/session_runner/command.rs:26-46`, `src-tauri/src/agent_sessions/cli/session_runner/session.rs:888-1024`, `src-tauri/src/agent_sessions/cli/parsers/mod.rs:1-23`).
- Native/API agents use the Rust `agent-core` runtime and an `LLMProvider` trait. Anthropic native support is an implementation of that provider path, using the Anthropic Messages API (`src-tauri/crates/agent-core/src/core/providers/traits.rs:422-470`, `src-tauri/crates/agent-core/src/core/providers/anthropic_native/client.rs:1-13`, `src-tauri/crates/agent-core/src/core/providers/anthropic_native/streaming.rs:32-43`).
- There are real proxy pieces, but they are credential/network-adaptation mechanisms, not the whole architecture: hosted-key proxy token allocation on CLI create/message (`src-tauri/src/agent_sessions/cli/commands.rs:34-94`, `src-tauri/src/agent_sessions/cli/commands.rs:292-460`), per-agent proxy environment generation and MITM proxy startup for hosted keys (`src-tauri/src/agent_sessions/cli/session_runner/session.rs:461-539`), and event fanout from backend broadcast to Tauri IPC channels plus a WebSocket/debug tee (`src-tauri/src/api/websocket_handler.rs:1-20`, `src-tauri/src/api/websocket_handler.rs:280-297`).

Inference: the precise label is "adapter/orchestrator/process supervisor with provider adapters and selective proxy support." Calling it "a proxy layer" alone overstates the design.

## Claim Verification Table

| Prior claim | Status | Evidence | Correction |
| --- | --- | --- | --- |
| ORG2 abstracts both CLI and API/native agents behind common session concepts. | Verified | Frontend `SessionAdapter` contract and registry (`src/engines/SessionCore/sync/types.ts:170-208`, `src/engines/SessionCore/sync/adapters/index.ts:13-19`); Rust launch routing by session category (`src-tauri/crates/agent-core/src/state/commands/session/launch.rs:121-131`). | The common abstraction is strongest at session/UI orchestration, not a single backend execution interface for all agent types. |
| The frontend send path is adapter-dispatched. | Verified | `SessionService.sendMessage` gets adapter and calls `adapter.sendMessage` (`src/engines/SessionCore/services/SessionService.ts:279-330`). | None. |
| CLI agents are proxied requests. | Partially verified | CLI follow-up invokes `cli_agent_message` (`src/engines/SessionCore/sync/adapters/cliAdapter.ts:915-994`), which launches/kills/reruns subprocesses (`src-tauri/src/agent_sessions/cli/commands.rs:292-460`); command builders construct `claude`, `codex`, etc. commands (`src-tauri/src/agent_sessions/cli/session_runner/command.rs:101-157`). | CLI agents are better described as subprocess-supervised agents. Proxying exists for hosted credentials/network routing, not as the main execution model. |
| Native/API agents go through Rust `agent-core`. | Verified | Frontend Rust agent adapter invokes `agent_send_message` (`src/engines/SessionCore/sync/adapters/createRustAgentAdapter.ts:541-584`); command wrapper calls `send_message_impl` (`src-tauri/crates/agent-core/src/state/commands/session/mod.rs:164-220`); turn executor calls `provider.chat_streaming` (`src-tauri/crates/agent-core/src/core/turn_executor/mod.rs:221-244`). | None. |
| Claude Code CLI and Anthropic API share a common abstraction. | Partially verified | They share frontend session concepts and credential/model plumbing, but backend routes diverge: Claude Code is a CLI model type with no provider spec in `spec_for_model_type` (`src-tauri/crates/agent-core/src/core/providers/factory.rs:288-313`), while Anthropic API maps to `ANTHROPIC` provider and `AnthropicClient` (`src-tauri/crates/agent-core/src/core/providers/factory.rs:23-30`, `src-tauri/crates/agent-core/src/core/providers/factory.rs:343-453`). | They share session/UI abstractions, not a single execution adapter. Claude Code OAuth credentials can authenticate native Anthropic Messages API via credential detection (`src-tauri/crates/agent-core/src/core/providers/factory.rs:315-320`, `src-tauri/crates/agent-core/src/core/providers/factory.rs:651-661`). |
| Event streaming is normalized and persisted. | Verified | CLI `emit_chunk` persists chunks and broadcasts; streaming buffer flushes `agent:streaming_complete` (`src-tauri/src/agent_sessions/cli/session_runner/helpers.rs:42-55`, `src-tauri/src/agent_sessions/cli/session_runner/helpers.rs:95-174`). Frontend CLI adapter loads chunks and processes them through Rust ingestion (`src/engines/SessionCore/sync/adapters/cliAdapter.ts:324-338`, `src/engines/SessionCore/ingestion/rustBridge.ts:1-11`). | The backend broadcast function fans out to both WebSocket and Tauri IPC channels; Tauri IPC is documented as primary for in-app UI (`src-tauri/src/api/websocket_handler.rs:1-20`). |

## Layer Map With Evidence

### Frontend session abstraction and adapter registry

Observed: `SessionAdapter` is the core frontend abstraction. It defines `loadHistory`, `postLoad`, `createEventHandler`, `sendMessage`, and `stopSession` (`src/engines/SessionCore/sync/types.ts:170-208`). Session category selection is centralized in `getAdapterForSession`: agent sessions map to `"agent"`, CLI sessions to `"cli"`, Cursor IDE sessions to `"cursor_ide"`, and external histories to `"external_history"` (`src/engines/SessionCore/sync/types.ts:307-328`).

The registry is initialized in `src/engines/SessionCore/sync/adapters/index.ts`: it creates `agentAdapter = createRustAgentAdapter(AGENT_CONFIG)` and registers `agentAdapter`, `cliAdapter`, `cursorIdeAdapter`, and `externalHistoryAdapter` (`src/engines/SessionCore/sync/adapters/index.ts:13-19`). The sync index exports the registry and adapters, making that initialization reachable through the module import surface (`src/engines/SessionCore/sync/index.ts:14-17`).

### Frontend send-message dispatch

Observed: `SessionService.sendMessage` collects common inputs, resolves `sessionRepoPath`, calls `getAdapterForSession(session)`, and delegates to `adapter.sendMessage` (`src/engines/SessionCore/services/SessionService.ts:287-330`). The file comment says the old direct branching on `isAgentSession`/`isCliSession` was moved into adapter `sendMessage` methods (`src/engines/SessionCore/services/SessionService.ts:279-286`).

For CLI sessions, `cliAdapter.sendMessage` calls `cli_agent_message` with `sessionId`, content, model, account, mode, images, and IDE context (`src/engines/SessionCore/sync/adapters/cliAdapter.ts:915-994`). For Rust/native agent sessions, `createRustAgentAdapter.sendMessage` calls `agent_send_message` with the same session-level envelope plus native-agent fields such as `isResume`, `clientMessageId`, and `turnIntentId` (`src/engines/SessionCore/sync/adapters/createRustAgentAdapter.ts:541-584`).

### Event streaming/subscription and backend fanout

Observed: frontend session sync subscribes through Tauri IPC channels. `useSessionChannel` creates a `Channel<string>` and invokes `subscribe_session_events`; cleanup invokes `unsubscribe_session_events` (`src/engines/SessionCore/sync/useSessionChannel.ts:198-249`). Incoming raw strings are parsed and routed to the current adapter event handler (`src/engines/SessionCore/sync/sessionSyncChannel.ts:7-15`).

Backend fanout lives in `src-tauri/src/api/websocket_handler.rs`. Its module comment says in-app UI uses per-session Tauri IPC channels and WebSocket remains a debug/tee path (`src-tauri/src/api/websocket_handler.rs:1-20`). The broadcast path extracts a session id and dispatches to registered Tauri channels while also broadcasting to WebSocket clients (`src-tauri/src/api/websocket_handler.rs:108-134`, `src-tauri/src/api/websocket_handler.rs:280-297`). The Tauri commands are exposed in the handler list (`src-tauri/src/commands/handler_list.inc:488-489`).

### CLI adapter frontend side

Observed: `cliAdapter` loads persisted CLI chunks with `cli_agent_chunks`, then calls the Rust ingestion bridge `processChunksRust` (`src/engines/SessionCore/sync/adapters/cliAdapter.ts:324-338`). Its event handler recognizes finalized interactions, plan events, `code_session.activity`, streaming completion, status changes, token usage, and worktree events (`src/engines/SessionCore/sync/adapters/cliAdapter.ts:839-867`). Its send method invokes `cli_agent_message` and then waits for a run boundary and persisted user event (`src/engines/SessionCore/sync/adapters/cliAdapter.ts:915-994`).

### Rust CLI lifecycle command side

Observed: CLI Tauri commands are registered in `handler_list.inc` (`src-tauri/src/commands/handler_list.inc:491-499`). `cli_agent_create` creates the code session and allocates hosted proxy credentials when needed (`src-tauri/src/agent_sessions/cli/commands.rs:34-94`). `cli_agent_run` prevents duplicate runners, spawns a background `session_runner::run_session` task, and broadcasts running status (`src-tauri/src/agent_sessions/cli/commands.rs:194-287`). `cli_agent_message` is the follow-up path: it kills any existing runner, updates model/account overrides, resolves resume state, may reallocate hosted proxy credentials, and calls `cli_agent_run` (`src-tauri/src/agent_sessions/cli/commands.rs:292-460`).

Initial CLI creation can also come from `agent-core`'s unified `session_launch` path. `session_launch_impl` routes `SESSION_CATEGORY_CLI_AGENT` to `launch_cli_agent` (`src-tauri/crates/agent-core/src/state/commands/session/launch.rs:121-131`), builds `CliLaunchParams`, and calls the foundation bridge (`src-tauri/crates/agent-core/src/state/commands/session/launch.rs:293-356`). The app wires that bridge at startup (`src-tauri/src/lib.rs:176-179`), and the wire-side adapter calls `cli_agent_create` followed by `cli_agent_run` (`src-tauri/src/agent_sessions/cli/agent_core_bridge.rs:1-9`, `src-tauri/src/agent_sessions/cli/agent_core_bridge.rs:55-77`).

### CLI subprocess runner and per-agent command construction

Observed: CLI command construction is isolated in `session_runner/command.rs`, which maps the session's agent type to command-line invocations (`src-tauri/src/agent_sessions/cli/session_runner/command.rs:1-8`, `src-tauri/src/agent_sessions/cli/session_runner/command.rs:26-46`). Claude Code is invoked as `claude --output-format stream-json --verbose --dangerously-skip-permissions`, with optional resume, model, extra directories, and prompt (`src-tauri/src/agent_sessions/cli/session_runner/command.rs:101-127`). Codex is invoked as `codex exec --json --skip-git-repo-check --sandbox workspace-write`, with optional working directory, model, resume, extra directories, and task (`src-tauri/src/agent_sessions/cli/session_runner/command.rs:129-157`).

`run_session` loads session/account state, resolves model/account details, constructs the command, builds env vars, and spawns the child process (`src-tauri/src/agent_sessions/cli/session_runner/session.rs:198-260`, `src-tauri/src/agent_sessions/cli/session_runner/session.rs:380-418`, `src-tauri/src/agent_sessions/cli/session_runner/session.rs:888-1024`). For ACP agents, it runs bidirectional JSON-RPC over stdin/stdout; for standard agents, it reads stdout line-by-line and passes lines to the parser (`src-tauri/src/agent_sessions/cli/session_runner/session.rs:1046-1156`, `src-tauri/src/agent_sessions/cli/session_runner/session.rs:1199-1329`).

### CLI parser/chunk/event normalization

Observed: CLI parsers implement a common `CliAgentParser` trait with `parse_line`, `on_exit`, `token_usage`, and `cli_session_id` (`src-tauri/src/agent_sessions/cli/parsers/mod.rs:52-70`). Parser selection maps Cursor CLI, Claude Code, Codex, and Gemini CLI to parser implementations; Copilot/Kiro use ACP and API providers are explicitly not CLI agents in this factory (`src-tauri/src/agent_sessions/cli/session_runner/command.rs:235-250`).

Chunks are persisted and broadcast in `emit_chunk`. Deltas are accumulated by `CLI_STREAMING_BUFFER`; completion flushes a normalized `agent:streaming_complete` event (`src-tauri/src/agent_sessions/cli/session_runner/helpers.rs:42-55`, `src-tauri/src/agent_sessions/cli/session_runner/helpers.rs:95-174`). The frontend comment mirrors this split: deltas accumulate locally while Rust also accumulates and emits streaming completion; non-delta chunks are normalized via Rust (`src/engines/SessionCore/sync/adapters/cliAdapter.ts:1-13`).

### Rust/native API provider path

Observed: the Rust/native frontend adapter calls `agent_send_message` (`src/engines/SessionCore/sync/adapters/createRustAgentAdapter.ts:541-584`). The Tauri command wrapper is registered (`src-tauri/src/commands/handler_list.inc:1162-1165`) and calls `message::send_message_impl` (`src-tauri/crates/agent-core/src/state/commands/session/mod.rs:164-220`). `send_message_impl` resolves session identity, initializes or rehydrates session runtime, builds `TurnInput`, and calls the Rust session processing path (`src-tauri/crates/agent-core/src/state/commands/session/message.rs:88-157`, `src-tauri/crates/agent-core/src/state/commands/session/message.rs:307-345`).

Runtime construction creates a provider through `create_provider_with_native_harness_preflight` (`src-tauri/crates/agent-core/src/init/session_factory.rs:50-74`). The turn executor accepts `&dyn LLMProvider` and calls `provider.chat_streaming`, converting provider deltas into normalized handler calls for text, thinking, and tool-call deltas (`src-tauri/crates/agent-core/src/core/turn_executor/mod.rs:98-110`, `src-tauri/crates/agent-core/src/core/turn_executor/mod.rs:221-272`).

### Anthropic native provider path

Observed: `LLMProvider` is the API-provider abstraction (`src-tauri/crates/agent-core/src/core/providers/traits.rs:422-470`). The provider factory says Anthropic/Claude native Messages API uses `AnthropicClient` (`src-tauri/crates/agent-core/src/core/providers/factory.rs:23-30`). `spec_for_model_type` maps `AnthropicApi | AzureAnthropicApi` to `ANTHROPIC`, while CLI model types such as `ClaudeCode`, `CursorCli`, `Copilot`, and `Kiro` return `None` (`src-tauri/crates/agent-core/src/core/providers/factory.rs:288-313`).

`AnthropicClient` is an HTTP client for Anthropic Messages API `/v1/messages` (`src-tauri/crates/agent-core/src/core/providers/anthropic_native/client.rs:1-13`, `src-tauri/crates/agent-core/src/core/providers/anthropic_native/client.rs:200-226`). Request construction builds the Messages request body and applies API-key, Azure bearer, or Claude OAuth headers (`src-tauri/crates/agent-core/src/core/providers/anthropic_native/request.rs:29-103`, `src-tauri/crates/agent-core/src/core/providers/anthropic_native/request.rs:146-180`). Streaming sends the HTTP request, handles status and OAuth refresh cases, consumes SSE-style Anthropic events, and returns an `LLMResponse` (`src-tauri/crates/agent-core/src/core/providers/anthropic_native/streaming.rs:135-204`, `src-tauri/crates/agent-core/src/core/providers/anthropic_native/streaming.rs:245-308`, `src-tauri/crates/agent-core/src/core/providers/anthropic_native/streaming.rs:364-423`).

### Real proxy/hosted-key/MITM compatibility pieces

Observed: CLI hosted-key support allocates proxy credentials during create and follow-up message handling (`src-tauri/src/agent_sessions/cli/commands.rs:64-94`, `src-tauri/src/agent_sessions/cli/commands.rs:405-450`). The session runner derives provider-specific proxy environment variables from `KeyService::get_proxy_env_for_agent`; if the session uses a hosted key and the agent needs a MITM proxy, it starts a per-session MITM proxy and sets HTTP/HTTPS proxy and certificate environment variables (`src-tauri/src/agent_sessions/cli/session_runner/session.rs:461-539`).

Inference: these are compatibility layers for external CLIs and hosted credentials. They do not make the whole architecture a reverse proxy for all agent traffic.

## Verified Request Flows

### Flow 1: Claude Code CLI or generic CLI follow-up message

1. UI code calls `SessionService.sendMessage`, which resolves the active session adapter (`src/engines/SessionCore/services/SessionService.ts:287-330`).
2. For a CLI session, `cliAdapter.sendMessage` invokes Tauri command `cli_agent_message` with content, model/account overrides, mode, images, and IDE context (`src/engines/SessionCore/sync/adapters/cliAdapter.ts:915-994`).
3. `cli_agent_message` loads the persisted CLI session, persists overrides, kills an existing runner if present, resolves resume state, optionally reallocates proxy credentials, and calls `cli_agent_run` (`src-tauri/src/agent_sessions/cli/commands.rs:301-460`).
4. `cli_agent_run` ensures no duplicate runner, spawns `session_runner::run_session` in a background task, records the running handle, updates status, and broadcasts status (`src-tauri/src/agent_sessions/cli/commands.rs:223-287`).
5. `run_session` constructs the per-agent command. For Claude Code, this is the `claude` CLI with stream-json output and prompt/resume/model flags (`src-tauri/src/agent_sessions/cli/session_runner/command.rs:101-127`). It then spawns the child process and parses stdout (`src-tauri/src/agent_sessions/cli/session_runner/session.rs:888-1024`, `src-tauri/src/agent_sessions/cli/session_runner/session.rs:1199-1329`).
6. Parser output becomes `ActivityChunk`s; `emit_chunk` persists and broadcasts them, with streaming completion emitted through the streaming buffer (`src-tauri/src/agent_sessions/cli/session_runner/helpers.rs:42-174`).
7. Frontend subscription receives events through Tauri IPC channels and routes them to the CLI event handler (`src/engines/SessionCore/sync/useSessionChannel.ts:198-249`, `src/engines/SessionCore/sync/sessionSyncChannel.ts:7-15`, `src/engines/SessionCore/sync/adapters/cliAdapter.ts:839-867`).

### Flow 2: Anthropic native/API message

1. UI code calls `SessionService.sendMessage`, resolves the `"agent"` adapter, and delegates to `createRustAgentAdapter.sendMessage` (`src/engines/SessionCore/services/SessionService.ts:287-330`, `src/engines/SessionCore/sync/adapters/createRustAgentAdapter.ts:541-584`).
2. The adapter invokes Tauri command `agent_send_message` (`src/engines/SessionCore/sync/adapters/createRustAgentAdapter.ts:565`), which is registered in `handler_list.inc` (`src-tauri/src/commands/handler_list.inc:1162-1165`).
3. `agent_send_message` calls `send_message_impl` (`src-tauri/crates/agent-core/src/state/commands/session/mod.rs:164-220`). That function resolves session identity, initializes the runtime, builds `TurnInput`, and enters `crate::session::process_message` (`src-tauri/crates/agent-core/src/state/commands/session/message.rs:88-157`, `src-tauri/crates/agent-core/src/state/commands/session/message.rs:307-345`).
4. Runtime construction creates the provider with the native provider factory (`src-tauri/crates/agent-core/src/init/session_factory.rs:50-74`). If the model/account resolves to Anthropic, the factory selects `AnthropicClient` (`src-tauri/crates/agent-core/src/core/providers/factory.rs:23-30`, `src-tauri/crates/agent-core/src/core/providers/factory.rs:343-453`).
5. The turn executor calls `provider.chat_streaming`, not a CLI subprocess (`src-tauri/crates/agent-core/src/core/turn_executor/mod.rs:221-244`). For Anthropic, `AnthropicClient.chat_streaming` builds a `/v1/messages` request, applies headers, sends an HTTP request, consumes streaming events, and emits normalized deltas (`src-tauri/crates/agent-core/src/core/providers/anthropic_native/request.rs:29-180`, `src-tauri/crates/agent-core/src/core/providers/anthropic_native/streaming.rs:135-308`).

## Claude Code CLI vs Anthropic API

Claude Code CLI:

- Invoked as an external `claude` binary by the CLI session runner (`src-tauri/src/agent_sessions/cli/session_runner/command.rs:101-127`).
- Belongs to the CLI agent parser/runner path. `create_parser` maps `ClaudeCode` to `ClaudeCodeParser` (`src-tauri/src/agent_sessions/cli/session_runner/command.rs:235-250`).
- Uses process lifecycle controls: spawn, kill, resume id persistence, stdout parsing, hosted-key env/proxy setup, and persisted `ActivityChunk`s (`src-tauri/src/agent_sessions/cli/session_runner/session.rs:888-1024`, `src-tauri/src/agent_sessions/cli/session_runner/helpers.rs:42-174`).

Anthropic API/native:

- Invoked through Rust `agent-core` and `LLMProvider`, specifically `AnthropicClient` for Anthropic Messages API (`src-tauri/crates/agent-core/src/core/providers/traits.rs:422-470`, `src-tauri/crates/agent-core/src/core/providers/anthropic_native/client.rs:1-13`).
- Does not spawn `claude`; it sends HTTP requests to `/v1/messages` and streams provider events (`src-tauri/crates/agent-core/src/core/providers/anthropic_native/client.rs:200-226`, `src-tauri/crates/agent-core/src/core/providers/anthropic_native/streaming.rs:135-308`).
- It can use Claude OAuth credentials: `spec_for_credential` special-cases Claude OAuth credentials to `ANTHROPIC`, and `is_claude_oauth_key` documents that Claude Code OAuth can authenticate native Anthropic Messages API (`src-tauri/crates/agent-core/src/core/providers/factory.rs:315-320`, `src-tauri/crates/agent-core/src/core/providers/factory.rs:651-661`).

Shared abstraction:

- Shared at frontend session level, event streaming/subscription level, and some credential/model selection concepts.
- Not shared at execution level. Claude Code CLI uses subprocess/process supervision; Anthropic native uses provider HTTP streaming.

## Corrections and Uncertainty

Corrections from the initial broad report:

- "Proxy layer" is too broad. Verified code shows orchestration, subprocess supervision, provider adapters, event fanout, and selective proxy support.
- Initial CLI launch is not only `cli_agent_message`. New CLI sessions can be created through unified `session_launch`, which bridges to `cli_agent_create` plus `cli_agent_run`; follow-up prompts use `cli_agent_message`.
- Event transport should not be described as only WebSocket. Code comments identify Tauri IPC channels as primary for in-app session events and WebSocket as a debug/tee path, although `broadcast` still fans out to both.
- Claude Code CLI and Anthropic API are not the same backend adapter. They share UI/session abstractions and may share Claude OAuth credential material, but the execution paths diverge.

Uncertainty:

- This memo did not execute the app, so it verifies static call paths and registrations, not runtime ordering under every route.
- The report did not exhaustively inspect every frontend creator/control surface. The verified paths cover `SessionService.sendMessage`, unified `session_launch`, and registered Tauri commands; a future reader should inspect individual session creation UI flows if the question is about every entry point.
- The exact hosted-key/proxy semantics depend on `KeyService`, `integrations::proxy`, and MITM proxy modules, which were not deeply audited here. The existence and integration points are verified, not every network behavior.
- Graphify was used only for navigation. Code was treated as the source of truth.

## Verification Risks Checked

1. Risk: the adapter registry might exist but not be reachable. Re-check: `sync/index.ts` exports registry functions and adapters (`src/engines/SessionCore/sync/index.ts:14-17`), and `adapters/index.ts` performs registrations (`src/engines/SessionCore/sync/adapters/index.ts:13-19`). Wording kept to frontend module reachability, not runtime import proof for every bundle path.
2. Risk: Tauri commands might exist but not be exposed. Re-check: CLI commands and session-event subscription commands are listed in `handler_list.inc` (`src-tauri/src/commands/handler_list.inc:488-499`), and `agent_send_message`/`session_launch` are listed too (`src-tauri/src/commands/handler_list.inc:1162-1165`).
3. Risk: CLI request flow wording might collapse launch and follow-up paths. Re-check: follow-up uses `cli_agent_message` (`src/engines/SessionCore/sync/adapters/cliAdapter.ts:915-994`), while unified launch bridges `session_launch` to `cli_agent_create` + `cli_agent_run` (`src-tauri/crates/agent-core/src/state/commands/session/launch.rs:293-356`, `src-tauri/src/agent_sessions/cli/agent_core_bridge.rs:55-77`). Report now distinguishes them.
4. Risk: "event fanout" might imply only Tauri IPC or only WebSocket. Re-check: `websocket_handler.rs` documents Tauri IPC as primary and WebSocket as tee/debug, while `broadcast` fans out to both (`src-tauri/src/api/websocket_handler.rs:1-20`, `src-tauri/src/api/websocket_handler.rs:280-297`). Report uses both terms.
5. Risk: Anthropic native path might be incorrectly generalized to all Rust/native agents. Re-check: provider factory selects among Codex native, Anthropic, Gemini, OpenAI-compatible, and others (`src-tauri/crates/agent-core/src/core/providers/factory.rs:23-30`, `src-tauri/crates/agent-core/src/core/providers/factory.rs:343-453`). Report describes Anthropic as one provider path, not all native agents.
6. Risk: Claude Code OAuth might be confused with Claude Code CLI execution. Re-check: `ClaudeCode` model type returns no native provider spec, while Claude OAuth credentials can map to Anthropic native API (`src-tauri/crates/agent-core/src/core/providers/factory.rs:288-320`, `src-tauri/crates/agent-core/src/core/providers/factory.rs:651-661`). Report separates credential compatibility from execution path.
7. Risk: "proxy" might refer to different things. Re-check: evidence shows hosted proxy token allocation, proxy env vars, MITM proxy for selected CLI hosted-key flows, and event fanout, but no single universal request proxy for all agents (`src-tauri/src/agent_sessions/cli/commands.rs:64-94`, `src-tauri/src/agent_sessions/cli/session_runner/session.rs:461-539`, `src-tauri/src/api/websocket_handler.rs:1-20`). Report restricts proxy wording.

## Appendix: Key Files

- `src/engines/SessionCore/sync/types.ts`: frontend `SessionAdapter` contract, raw event shape, adapter registry, and category selection.
- `src/engines/SessionCore/sync/adapters/index.ts`: concrete frontend adapter registration.
- `src/engines/SessionCore/services/SessionService.ts`: frontend send-message dispatch into adapters.
- `src/engines/SessionCore/sync/adapters/cliAdapter.ts`: CLI history loading, event handling, and `cli_agent_message` send path.
- `src/engines/SessionCore/sync/adapters/createRustAgentAdapter.ts`: Rust/native agent adapter and `agent_send_message` send path.
- `src/engines/SessionCore/sync/useSessionChannel.ts` and `src/engines/SessionCore/sync/sessionSyncChannel.ts`: frontend event subscription and routing.
- `src-tauri/src/api/websocket_handler.rs`: backend fanout to Tauri IPC channels and WebSocket/debug clients.
- `src-tauri/src/commands/handler_list.inc`: exposed Tauri command list.
- `src-tauri/src/agent_sessions/cli/commands.rs`: CLI session lifecycle commands.
- `src-tauri/src/agent_sessions/cli/agent_core_bridge.rs`: bridge from `agent-core` unified session launch to CLI create/run.
- `src-tauri/src/agent_sessions/cli/session_runner/command.rs`: per-agent CLI command builders and parser selection.
- `src-tauri/src/agent_sessions/cli/session_runner/session.rs`: subprocess launch, env/proxy setup, stdout/ACP handling, status finalization.
- `src-tauri/src/agent_sessions/cli/session_runner/helpers.rs`: chunk persistence, broadcast, streaming completion.
- `src-tauri/src/agent_sessions/cli/parsers/mod.rs`: CLI parser trait and parser pipeline description.
- `src-tauri/crates/agent-core/src/state/commands/session/message.rs`: `agent_send_message` implementation path.
- `src-tauri/crates/agent-core/src/state/commands/session/launch.rs`: unified `session_launch` routing for Rust vs CLI sessions.
- `src-tauri/crates/agent-core/src/init/session_factory.rs`: native session runtime/provider construction.
- `src-tauri/crates/agent-core/src/core/turn_executor/mod.rs`: provider streaming call and normalized turn deltas.
- `src-tauri/crates/agent-core/src/core/providers/traits.rs`: `LLMProvider` abstraction.
- `src-tauri/crates/agent-core/src/core/providers/factory.rs`: provider selection, including Anthropic vs CLI model-type separation and Claude OAuth credential compatibility.
- `src-tauri/crates/agent-core/src/core/providers/anthropic_native/*`: Anthropic Messages API client, request building, headers, and streaming implementation.
