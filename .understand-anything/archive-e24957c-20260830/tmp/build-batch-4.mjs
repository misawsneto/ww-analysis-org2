import fs from 'node:fs';

const inputPath = '/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate/batch-inputs/batch-4.input.json';
const sigPath = '/home/misael/pj/gui-repos/ORG2/.understand-anything/tmp/ua-sig-4.json';
const outDir = '/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate';

const input = JSON.parse(fs.readFileSync(inputPath, 'utf8'));
const sig = JSON.parse(fs.readFileSync(sigPath, 'utf8'));
const batchImportData = input.batchImportData;

const P = 'src-tauri/crates/agent-core/src/core/session/';

// ---- META: hand-authored summaries, matched positionally to sigF/sigC order ----
const META = {
[`${P}recovery.rs`]: {
  summary: "Detects and repairs conversation histories left in an inconsistent state after an interrupted agent turn, pairing orphaned tool_use blocks with synthetic results before the session resumes.",
  tags: ["recovery","session-management","validation","message-history"],
  complexity: "complex",
  funcs: [
    { summary: "Scans a message history to detect an interrupted turn, distinguishing dangling tool_use blocks from an unterminated assistant message.", tags: ["validation","state-detection"], complexity: "moderate" },
    { summary: "Repairs a message history after a detected interruption by closing out dangling tool calls or trimming an unterminated assistant turn.", tags: ["recovery","message-history"], complexity: "moderate" },
    { summary: "Filters out tool_use entries that never received a matching tool_result, preventing malformed histories from being replayed.", tags: ["validation","filtering"], complexity: "moderate" },
    { summary: "Ensures every tool_use block in the message history has a corresponding tool_result, synthesizing placeholder results for any that are missing.", tags: ["validation","message-history"], complexity: "complex" },
  ],
  classes: [],
},
[`${P}scheduler.rs`]: {
  summary: "Implements DialogScheduler, a per-session message queue and worker task that serializes turn execution, tracks processing/idle state, and broadcasts queue status to the UI.",
  tags: ["scheduling","session-management","concurrency","orchestration"],
  complexity: "complex",
  funcs: [
    { summary: "Constructs a new DialogScheduler for a session with a bounded message channel of the given capacity.", tags: ["factory","scheduling"], complexity: "simple" },
    { summary: "Lazily spawns the scheduler's background worker task the first time messages are enqueued for a session.", tags: ["initialization","concurrency"], complexity: "moderate" },
    { summary: "Enqueues a scheduled message onto the session's channel, deduplicating by client_message_id and returning queue position.", tags: ["scheduling","deduplication"], complexity: "complex" },
    { summary: "Bumps the scheduler generation counter to invalidate any messages still pending in the queue.", tags: ["state-management","invalidation"], complexity: "moderate" },
    { summary: "Worker loop that drains the message channel, executes each scheduled turn or maintenance job, and updates processing state, catching panics along the way.", tags: ["orchestration","concurrency","event-loop"], complexity: "complex" },
    { summary: "Emits a queue-status event to the frontend once the worker becomes idle.", tags: ["event-handler","ui-integration"], complexity: "simple" },
  ],
  classes: [
    { summary: "Represents a single user message queued for turn execution, tagged with generation and dedup identifiers.", tags: ["data-model"], complexity: "simple" },
    { summary: "Per-session scheduler handle exposing enqueue/status operations backed by an mpsc channel to the worker task.", tags: ["data-model","scheduling"], complexity: "moderate" },
    { summary: "Background worker state that owns the receiving end of the message channel and tracks in-flight processing/generation counters.", tags: ["data-model","concurrency"], complexity: "simple" },
  ],
},
[`${P}session_id.rs`]: {
  summary: "Utility functions for constructing and versioning OS-level session identifiers from channel/chat metadata, including slug sanitization and next-version resolution.",
  tags: ["utility","identifier-generation","session-management"],
  complexity: "moderate",
  funcs: [
    { summary: "Sanitizes a raw string segment into a filesystem/ID-safe slug, falling back to a default when the result would be empty.", tags: ["utility","sanitization"], complexity: "simple" },
    { summary: "Determines the next available version suffix for a session ID base by scanning existing session IDs for conflicts.", tags: ["utility","versioning"], complexity: "moderate" },
  ],
  classes: [],
},
[`${P}title.rs`]: {
  summary: "Generates a short human-readable session title from the first user message via a side LLM query, with normalization, truncation, and fallback handling, then persists it to session state.",
  tags: ["utility","llm-integration","session-management","text-processing"],
  complexity: "moderate",
  funcs: [
    { summary: "Cleans up a raw LLM-generated title by stripping quotes/markdown and collapsing whitespace.", tags: ["text-processing","normalization"], complexity: "simple" },
    { summary: "Truncates an overly long title to a maximum length, breaking on a word boundary where possible.", tags: ["text-processing","utility"], complexity: "simple" },
    { summary: "Issues a side LLM query against the session's first message to produce a concise session title, falling back to a heuristic title on failure.", tags: ["llm-integration","generation"], complexity: "moderate" },
    { summary: "Generates a session title and writes it back into persisted session state.", tags: ["llm-integration","persistence"], complexity: "moderate" },
  ],
  classes: [],
},
[`${P}turn/background_reminder.rs`]: {
  summary: "Builds a system-message reminder that surfaces completed background job results (with inlined handles and formatted ages) to nudge the agent to review them.",
  tags: ["prompt-building","background-jobs","utility"],
  complexity: "moderate",
  funcs: [
    { summary: "Formats a list of completed background jobs into a system reminder message, including result previews and elapsed time.", tags: ["prompt-building","formatting"], complexity: "complex" },
    { summary: "Formats a millisecond duration into a human-readable age string (e.g. '2m ago').", tags: ["utility","formatting"], complexity: "simple" },
  ],
  classes: [],
},
[`${P}turn/entry.rs`]: {
  summary: "Turn-processing entry point: extracts LSP/screenshot resources from the app handle, expands skill slash-commands in the user's message, and hands the input off to the message processor.",
  tags: ["entry-point","turn-processing","message-handling"],
  complexity: "moderate",
  funcs: [
    { summary: "Pulls the ScreenshotStore out of the Tauri app handle's managed state.", tags: ["utility","tauri-state"], complexity: "simple" },
    { summary: "Expands a leading `/skill` slash-command in the user's message content into its full skill-invocation form, resolved against the workspace.", tags: ["command-parsing","utility"], complexity: "moderate" },
    { summary: "Top-level handler that prepares turn input (resources, slash-command expansion) and dispatches the message into the session's turn processor.", tags: ["entry-point","event-handler"], complexity: "complex" },
  ],
  classes: [],
},
[`${P}turn/event_handler/event_factory.rs`]: {
  summary: "Factory functions that construct UnifiedEvent payloads for assistant messages, tool calls, and tool results to be pushed onto the session event stream.",
  tags: ["factory","event-handler","serialization"],
  complexity: "moderate",
  funcs: [
    { summary: "Builds a UnifiedEvent representing a completed assistant message for a session.", tags: ["factory","event-handler"], complexity: "moderate" },
    { summary: "Builds a UnifiedEvent describing a tool invocation, deriving a display name and affected file path from the tool arguments.", tags: ["factory","event-handler"], complexity: "moderate" },
    { summary: "Builds a UnifiedEvent carrying a tool's result payload and UI metadata for display.", tags: ["factory","event-handler"], complexity: "moderate" },
  ],
  classes: [],
},
[`${P}turn/event_handler/helpers.rs`]: {
  summary: "Streaming-parse helpers that extract partial/complete string fields from incrementally-built JSON tool arguments and parse hook executor stdout into a structured HookDecision.",
  tags: ["parsing","streaming","utility","hooks"],
  complexity: "moderate",
  funcs: [
    { summary: "Derives a short human-readable status preview string from a tool's name and (possibly partial) arguments for live UI display.", tags: ["utility","ui-integration"], complexity: "moderate" },
    { summary: "Decodes a partially-streamed JSON string value's escape sequences into displayable text.", tags: ["parsing","streaming"], complexity: "moderate" },
    { summary: "Parses a hook executor's stdout into a structured HookDecision, handling both JSON and legacy plain-text formats.", tags: ["parsing","hooks"], complexity: "moderate" },
  ],
  classes: [],
},
[`${P}turn/event_handler/mod.rs`]: {
  summary: "Defines UnifiedEventHandler, the central callback implementation that turns raw LLM stream events (message/thinking deltas, tool calls, retries, cancellation) into UnifiedEvents pushed to the session store and broadcast to the frontend.",
  tags: ["event-handler","streaming","state-management","orchestration"],
  complexity: "complex",
  languageNotes: "Implements a large trait-like callback surface (on_* methods) that centralizes turn-execution side effects, decoupling the LLM streaming client from session state.",
  funcs: [
    { summary: "Determines whether a tool result payload represents an error outcome.", tags: ["validation","utility"], complexity: "simple" },
    { summary: "Decides whether a synthetic assistant-message event needs to be pushed given tool calls and streaming state.", tags: ["state-management","utility"], complexity: "simple" },
    { summary: "Checks whether a session is still on the turn generation this handler was created for, guarding against stale callbacks after cancellation.", tags: ["concurrency","validation"], complexity: "simple" },
    { summary: "Constructs a UnifiedEventHandler from an EventHandlerConfig, initializing streaming buffers and call counters.", tags: ["factory","initialization"], complexity: "simple" },
    { summary: "Flushes any buffered streaming message/thinking content for a session into a finalized event and the session store.", tags: ["streaming","event-handler"], complexity: "moderate" },
    { summary: "Pushes a UnifiedEvent into the session's event store.", tags: ["event-handler","persistence"], complexity: "simple" },
    { summary: "Broadcasts an incremental tool-call argument delta event to the frontend.", tags: ["event-handler","streaming"], complexity: "moderate" },
    { summary: "Finalizes any active streaming buffer content into the session store before a turn transitions.", tags: ["streaming","persistence"], complexity: "simple" },
    { summary: "Streaming callback invoked on each assistant message text delta; appends to the buffer and rebroadcasts.", tags: ["event-handler","streaming"], complexity: "moderate" },
    { summary: "Streaming callback invoked on each reasoning/thinking delta; appends to the buffer and rebroadcasts.", tags: ["event-handler","streaming"], complexity: "moderate" },
    { summary: "Streaming callback invoked on incremental tool-call argument fragments; buffers partial JSON and updates the live status preview.", tags: ["event-handler","streaming"], complexity: "complex" },
    { summary: "Streaming callback that records the latest context-window usage snapshot for the turn.", tags: ["telemetry","event-handler"], complexity: "simple" },
    { summary: "Callback fired when a tool call is fully resolved; emits the tool-call event, snapshots relevant state, and tees to wingman.", tags: ["event-handler","orchestration"], complexity: "complex" },
    { summary: "Callback fired when a tool modifies files on disk; emits a file-change event for the affected paths.", tags: ["event-handler","file-system"], complexity: "moderate" },
    { summary: "Callback fired when a tool call completes; forwards to on_tool_result_with_metadata with empty UI metadata.", tags: ["event-handler"], complexity: "simple" },
    { summary: "Callback fired when a tool call completes with UI metadata; emits the tool-result event and tees it to wingman.", tags: ["event-handler","ui-integration"], complexity: "complex" },
    { summary: "Callback fired at the end of an LLM iteration; flushes streaming content and pushes a finalized assistant-message event when needed.", tags: ["event-handler","streaming"], complexity: "complex" },
    { summary: "Callback fired just before a tool begins executing, used for UI status updates.", tags: ["event-handler"], complexity: "moderate" },
    { summary: "Pre-execution hook invoked before a tool runs, allowing dispatch of pre-tool hook checks.", tags: ["hooks","event-handler"], complexity: "moderate" },
    { summary: "Callback that checks whether the turn should stop early (cancellation, hook-driven stop) between tool executions.", tags: ["hooks","concurrency"], complexity: "complex" },
    { summary: "Callback fired when a user steering/injection message is consumed mid-turn, emitting the corresponding event.", tags: ["event-handler","orchestration"], complexity: "complex" },
    { summary: "Post-execution hook invoked after a tool finishes, used to dispatch post-tool hooks and diagnostics.", tags: ["hooks","event-handler"], complexity: "moderate" },
    { summary: "Runs the post-tool hook dispatch for a completed tool call.", tags: ["hooks"], complexity: "simple" },
    { summary: "Callback fired when the LLM stream connection is retried after an error, broadcasting a retry-status event.", tags: ["event-handler","resilience"], complexity: "complex" },
    { summary: "Callback fired when stream retries are exhausted, broadcasting a terminal error event to the frontend.", tags: ["event-handler","error-handling"], complexity: "moderate" },
  ],
  classes: [
    { summary: "Configuration bundle for constructing a UnifiedEventHandler, carrying workspace path, LSP manager, app handle, hook executor, and cancellation flag.", tags: ["data-model","configuration"], complexity: "moderate" },
    { summary: "Central streaming-event handler struct implementing all on_* callbacks for a turn, tracking tool-call counts and buffered stream state.", tags: ["event-handler","state-management"], complexity: "complex" },
  ],
},
[`${P}turn/event_handler/snapshots.rs`]: {
  summary: "Captures a pre-tool-call snapshot of the workspace state for a given tool invocation, used later to compute diffs shown in the UI.",
  tags: ["snapshotting","utility","file-system"],
  complexity: "simple",
  funcs: [
    { summary: "Takes a snapshot of the affected file(s) in the workspace before a mutating tool call executes, keyed by session and tool_call_id.", tags: ["snapshotting","file-system"], complexity: "moderate" },
  ],
  classes: [],
},
[`${P}turn/event_handler/wingman_tee.rs`]: {
  summary: "Tees tool-call and tool-result events into the Wingman floating status bar, keeping its live activity indicator in sync with the running turn.",
  tags: ["event-handler","ui-integration","wingman"],
  complexity: "simple",
  funcs: [
    { summary: "Forwards a tool-call event's status preview to the Wingman bar's tool indicator.", tags: ["event-handler","ui-integration"], complexity: "moderate" },
    { summary: "Forwards a tool-result outcome to the Wingman bar, updating its status text.", tags: ["event-handler","ui-integration"], complexity: "moderate" },
  ],
  classes: [],
},
[`${P}turn/mod.rs`]: {
  summary: "Turn module root that re-exports the turn subsystem (entry, event handling, processing, streaming) and provides debug helpers for probing prefetch timing and benchmarking the prompt cache.",
  tags: ["barrel","module-root","debugging"],
  complexity: "moderate",
  funcs: [
    { summary: "Debug-only probe that measures prefetch task latency under a configurable artificial delay.", tags: ["debugging","diagnostics"], complexity: "moderate" },
    { summary: "Debug-only benchmark that repeatedly rebuilds the system prompt for a session to measure prompt-cache hit/miss performance.", tags: ["debugging","benchmarking"], complexity: "complex" },
  ],
  classes: [],
},
[`${P}turn/post_turn.rs`]: {
  summary: "Spawns post-turn background tasks — session memory extraction, structured memory extraction, and auto-dream — on a forked LLM provider derived from the turn's model/account configuration.",
  tags: ["orchestration","background-jobs","memory","llm-integration"],
  complexity: "complex",
  funcs: [
    { summary: "Builds a fresh forked provider spec (model, account, reliability, harness type, workspace) for spawning side-query tasks off the main turn.", tags: ["factory","llm-integration"], complexity: "simple" },
    { summary: "Spawns a background task that extracts session memories from the turn's messages using a forked provider, guarded by state/config checks.", tags: ["background-jobs","memory"], complexity: "complex" },
    { summary: "Spawns a background task that runs structured memory extraction over the turn's final messages.", tags: ["background-jobs","memory"], complexity: "complex" },
    { summary: "Executes the structured memory-extraction task body: runs the extraction, applies results, and updates extraction state.", tags: ["background-jobs","memory"], complexity: "complex" },
    { summary: "Spawns a background 'auto-dream' task that reflects on the turn's transcript using a forked provider.", tags: ["background-jobs","memory"], complexity: "complex" },
  ],
  classes: [],
},
[`${P}turn/processor/compaction.rs`]: {
  summary: "Implements reactive (post-error) and pre-turn context compaction: summarizing/truncating message history via an LLM when it exceeds the token budget, while preserving leading runtime-system messages and handling rescue/fork redirects.",
  tags: ["context-management","compaction","llm-integration","state-management"],
  complexity: "complex",
  funcs: [
    { summary: "Adjusts session-memory compaction state to account for a prefix of runtime-system messages excluded from the compactable tail.", tags: ["state-management","context-management"], complexity: "simple" },
    { summary: "Runs LLM-based compaction on the tail of a message history with a rescue fallback if the primary compaction attempt fails.", tags: ["compaction","resilience"], complexity: "complex" },
    { summary: "Reactively compacts a session's message history after a provider context-overflow error, retrying the failed turn with the compacted history.", tags: ["compaction","error-handling"], complexity: "complex" },
    { summary: "Proactively compacts a session's message history before a turn begins if projected token usage exceeds the configured budget, potentially triggering a provider/model fork redirect.", tags: ["compaction","orchestration"], complexity: "complex" },
  ],
  classes: [],
},
[`${P}turn/processor/execute.rs`]: {
  summary: "Executes a turn against the LLM provider with reactive retry: on a context-overflow error it triggers reactive compaction and re-attempts the call with the reduced history.",
  tags: ["orchestration","resilience","llm-integration"],
  complexity: "complex",
  funcs: [
    { summary: "Executes a turn's LLM call, catching context-overflow provider errors and retrying once against a reactively-compacted message history.", tags: ["resilience","orchestration"], complexity: "complex" },
    { summary: "Helper that performs the reactive-compaction retry path: compacts the history, rebuilds the request, and re-invokes the LLM call.", tags: ["compaction","resilience"], complexity: "complex" },
  ],
  classes: [],
},
[`${P}turn/processor/inbox_drain/drain.rs`]: {
  summary: "Drains queued inbox messages addressed to a member agent, renders them into the session transcript, and applies their side effects (routing, shutdown signaling) before or during a turn.",
  tags: ["multi-agent","orchestration","message-handling","inbox"],
  complexity: "complex",
  funcs: [
    { summary: "Drains a member's inbox and renders the messages as a deferred attachment to be injected later in the turn.", tags: ["multi-agent","inbox"], complexity: "complex" },
    { summary: "Drains a member's inbox and immediately renders the pending messages into transcript form.", tags: ["multi-agent","inbox"], complexity: "simple" },
    { summary: "Applies the side effects encoded in drained inbox message payloads — recipient routing, session updates, and member-shutdown signaling.", tags: ["multi-agent","orchestration"], complexity: "complex" },
  ],
  classes: [],
},
[`${P}turn/processor/inbox_drain/guard.rs`]: {
  summary: "DrainGuard tracks which inbox messages were pulled out of a member's queue for a drain operation and commits (or discards) that batch once processing completes.",
  tags: ["multi-agent","inbox","state-management"],
  complexity: "simple",
  funcs: [
    { summary: "Constructs a DrainGuard populated with the pending message ids and rendered transcript for a completed drain.", tags: ["factory","multi-agent"], complexity: "simple" },
    { summary: "Commits the drained message batch, removing the drained ids from the member's inbox store.", tags: ["persistence","multi-agent"], complexity: "moderate" },
  ],
  classes: [
    { summary: "RAII-style guard holding the set of drained inbox message ids and rendered transcript for a single drain operation.", tags: ["data-model","multi-agent"], complexity: "simple" },
  ],
},
[`${P}turn/processor/inbox_drain/hooks.rs`]: {
  summary: "Defines the MemberShutdownHook trait and a thread-local installable guard used to cancel a member's session and wake the coordinator when a multi-agent member is shut down mid-drain.",
  tags: ["multi-agent","hooks","concurrency"],
  complexity: "simple",
  funcs: [],
  classes: [
    { summary: "Trait for hooking into member-session cancellation and coordinator wake-up during inbox draining.", tags: ["hooks","trait"], complexity: "simple" },
    { summary: "Scope guard that installs a MemberShutdownHook implementation for the duration it is held and clears it on drop.", tags: ["hooks"], complexity: "simple" },
  ],
},
[`${P}turn/processor/inbox_drain/mod.rs`]: {
  summary: "Barrel module for the inbox-drain subsystem, re-exporting the shutdown hook trait, DrainGuard, and drain_and_render_deferred from its submodules, plus an extensive unit test suite (29 tests) covering drain and side-effect behavior.",
  tags: ["barrel","multi-agent","test","inbox"],
  complexity: "complex",
  funcs: [],
  classes: [],
},
[`${P}turn/processor/inbox_drain/render.rs`]: {
  summary: "Renders drained inbox rows into transcript and attachment payloads (with type-specific formatting and XML escaping) that get injected into the LLM conversation.",
  tags: ["rendering","multi-agent","serialization","inbox"],
  complexity: "complex",
  funcs: [
    { summary: "Renders a set of drained inbox rows as an XML-tagged attachment block for inclusion in the prompt.", tags: ["rendering","serialization"], complexity: "moderate" },
    { summary: "Renders drained inbox rows into a flat transcript string joined for display.", tags: ["rendering"], complexity: "simple" },
    { summary: "Renders a single inbox row into its transcript representation based on message kind.", tags: ["rendering"], complexity: "moderate" },
    { summary: "Renders an inbox message payload into transcript-formatted text, branching on payload type (task update, mode change, etc.).", tags: ["rendering","serialization"], complexity: "complex" },
    { summary: "Renders an inbox message payload into its full XML representation for attachment injection, branching on payload type.", tags: ["rendering","serialization"], complexity: "complex" },
    { summary: "Escapes XML special characters in a string for safe embedding in rendered attachment/transcript output.", tags: ["utility","serialization"], complexity: "simple" },
  ],
  classes: [],
},
[`${P}turn/processor/inbox_drain/routing.rs`]: {
  summary: "Resolves inbox message routing: maps a recipient agent id to its runtime member id and identifies the sending member for an inbox row, using the multi-agent org context.",
  tags: ["multi-agent","routing","utility"],
  complexity: "simple",
  funcs: [
    { summary: "Resolves the runtime member id that should receive an inbox message given a recipient agent id and the org context.", tags: ["multi-agent","routing"], complexity: "moderate" },
    { summary: "Resolves the sending member for a drained inbox row, looking it up in the org context.", tags: ["multi-agent","routing"], complexity: "moderate" },
  ],
  classes: [],
},
[`${P}turn/processor/member_idle.rs`]: {
  summary: "Defines the MemberIdleHook mechanism and helpers that detect when a multi-agent org member has gone idle, computing unfinished task feedback and emitting the idle signal to the coordinator.",
  tags: ["multi-agent","hooks","orchestration","event-handler"],
  complexity: "complex",
  funcs: [
    { summary: "Default hook method invoked when a member becomes idle, carrying reason/mode/summary/unfinished-task context.", tags: ["hooks","multi-agent"], complexity: "moderate" },
    { summary: "Determines which coordinator/target should receive the idle notification for a given member.", tags: ["multi-agent","routing"], complexity: "moderate" },
    { summary: "Looks up the set of build/task ids still unfinished for a member within an org run.", tags: ["multi-agent","task-tracking"], complexity: "moderate" },
    { summary: "Builds feedback text describing unfinished task lifecycle state to include in an idle/stop signal.", tags: ["multi-agent","task-tracking"], complexity: "moderate" },
    { summary: "Conditionally emits a member-idle event if the member is eligible, delegating to the detailed emission path.", tags: ["event-handler","multi-agent"], complexity: "moderate" },
    { summary: "Emits a member-idle event with full detail (reason, mode, summary, failure reason, unfinished tasks) via the installed idle hook.", tags: ["event-handler","multi-agent"], complexity: "complex" },
  ],
  classes: [
    { summary: "Trait for reacting to a multi-agent member going idle, receiving run/member/mode/summary/unfinished-task context.", tags: ["hooks","trait"], complexity: "moderate" },
    { summary: "Scope guard that installs a MemberIdleHook implementation and clears it on drop.", tags: ["hooks"], complexity: "simple" },
  ],
},
[`${P}turn/processor/mod.rs`]: {
  summary: "Defines UnifiedMessageProcessor, the top-level orchestrator for a single turn: builds the system prompt, runs the LLM tool-use loop, records token/usage telemetry, and coordinates compaction and post-turn dispatch.",
  tags: ["orchestration","turn-processing","state-management","entry-point"],
  complexity: "complex",
  funcs: [
    { summary: "Wraps text in a scoped system-message envelope tagged with a scope identifier for later targeted removal.", tags: ["utility","prompt-building"], complexity: "simple" },
    { summary: "Constructs a UnifiedMessageProcessor from ProcessorParams, wiring up compaction/session-memory state and the event handler config.", tags: ["factory","initialization"], complexity: "complex" },
    { summary: "Computes the effective maximum tool-loop iteration count for the turn based on session/model policy.", tags: ["configuration","policy"], complexity: "moderate" },
    { summary: "Captures a snapshot of session state immediately before processing a new message, used for later diffing/telemetry.", tags: ["snapshotting","telemetry"], complexity: "moderate" },
    { summary: "Records prompt/completion/context token usage from a turn result into session usage tracking.", tags: ["telemetry"], complexity: "complex" },
    { summary: "Emits structured usage telemetry (tokens, tool calls, duration) for a completed turn.", tags: ["telemetry"], complexity: "complex" },
    { summary: "Builds a forked LLM provider suitable for issuing side-queries (e.g. title generation) during turn processing.", tags: ["llm-integration","factory"], complexity: "moderate" },
    { summary: "Main turn-processing loop: builds the prompt, drives the LLM tool-use iterations, handles compaction/interruption, and dispatches post-turn work.", tags: ["orchestration","turn-processing"], complexity: "complex" },
    { summary: "Injects a nudge message reminding a sub-agent to check its inbox if it appears idle mid-turn.", tags: ["multi-agent","prompt-building"], complexity: "moderate" },
  ],
  classes: [
    { summary: "Input payload for a single turn: user content, images, IDE context, agent mode, and resume/turn identifiers.", tags: ["data-model"], complexity: "moderate" },
    { summary: "Top-level per-session turn orchestrator holding runtime, policy, compaction/session-memory state, and the event-handler configuration.", tags: ["orchestration","state-management"], complexity: "complex" },
  ],
},
[`${P}turn/processor/post_turn_dispatch.rs`]: {
  summary: "Dispatches the set of post-turn background jobs (session-memory extraction, title generation, auto-dream) for a completed turn based on its inputs and final state.",
  tags: ["orchestration","background-jobs","post-turn"],
  complexity: "moderate",
  funcs: [
    { summary: "Dispatches all applicable post-turn background jobs for a completed turn, gating each on feature flags and final turn state.", tags: ["orchestration","background-jobs"], complexity: "complex" },
  ],
  classes: [],
},
[`${P}turn/processor/prefetch.rs`]: {
  summary: "Implements TurnPrefetchHook, which speculatively starts skill and memory-recall lookups concurrently with early turn processing, then collects and injects their results into the system/user prompt before the LLM call blocks on them.",
  tags: ["performance","prefetching","concurrency","prompt-building"],
  complexity: "complex",
  funcs: [
    { summary: "Constructs a TurnPrefetchHook from optional pre-started skill/memory prefetch tasks.", tags: ["factory"], complexity: "moderate" },
    { summary: "Test-only constructor that builds a TurnPrefetchHook with artificially delayed skill/memory outputs for timing tests.", tags: ["test","factory"], complexity: "moderate" },
    { summary: "Aborts any still-running skill/memory prefetch tasks, e.g. when the turn is cancelled.", tags: ["concurrency","cleanup"], complexity: "moderate" },
    { summary: "Awaits (with a bounded wait) and collects the skill-prefetch task's output, marking it as injected.", tags: ["prefetching","concurrency"], complexity: "complex" },
    { summary: "Awaits and collects the memory-prefetch task's output section and surfaced paths.", tags: ["prefetching","concurrency"], complexity: "complex" },
    { summary: "Hook invoked before each LLM iteration to opportunistically collect and inject any ready prefetch results.", tags: ["prefetching","prompt-building"], complexity: "moderate" },
    { summary: "Kicks off both the skill and memory prefetch tasks concurrently at the start of a turn.", tags: ["prefetching","concurrency"], complexity: "moderate" },
    { summary: "Spawns the background task that performs skill-catalog prefetching for the turn's content.", tags: ["prefetching","background-jobs"], complexity: "complex" },
    { summary: "Spawns the background task that performs memory-recall prefetching based on the turn's content and history.", tags: ["prefetching","background-jobs"], complexity: "complex" },
    { summary: "Prepends prefetched content (e.g. memory section) to the last user message in the conversation.", tags: ["prompt-building","utility"], complexity: "moderate" },
    { summary: "Inserts a new system message immediately after the last existing system message in the conversation.", tags: ["prompt-building","utility"], complexity: "moderate" },
  ],
  classes: [
    { summary: "Hook struct holding the in-flight/collected skill and memory prefetch task state for a turn.", tags: ["data-model","prefetching"], complexity: "simple" },
  ],
},
[`${P}turn/processor/prompt.rs`]: {
  summary: "Builds the turn's system prompt and assembles its dynamic sections — linked work-item context, memory-prefetch content, tool summaries — tracking how many rounds have passed since each tool was last used.",
  tags: ["prompt-building","llm-integration","orchestration"],
  complexity: "complex",
  funcs: [
    { summary: "Renders context about a linked work item (from the project tracker) for inclusion in the dynamic prompt sections.", tags: ["prompt-building","integration"], complexity: "moderate" },
    { summary: "Assembles the full system prompt for a session from its SystemPromptConfig and current dynamic state.", tags: ["prompt-building"], complexity: "complex" },
    { summary: "Builds the set of dynamic prompt sections (memory prefetch, linked work items, tool round reminders, etc.) appended to the system prompt for the current turn.", tags: ["prompt-building","orchestration"], complexity: "complex" },
    { summary: "Tracks and returns how many tool-use rounds have elapsed since a named tool was last invoked in the session.", tags: ["state-management","utility"], complexity: "moderate" },
  ],
  classes: [],
},
[`${P}turn/streaming.rs`]: {
  summary: "Defines structured StreamingError/StreamingErrorCode types for classifying provider stream failures, and broadcast helpers that emit agent-complete, agent-error, and agent-warning events to the frontend.",
  tags: ["error-handling","event-handler","streaming","data-model"],
  complexity: "complex",
  funcs: [
    { summary: "Maps a StreamingErrorCode variant to its wire-protocol string value sent to the frontend.", tags: ["serialization"], complexity: "moderate" },
    { summary: "Classifies a raw provider error message string into a StreamingErrorCode by pattern matching known failure signatures.", tags: ["error-handling","classification"], complexity: "moderate" },
    { summary: "Converts a provider error into a structured StreamingError, inferring its error code and retryability.", tags: ["error-handling","conversion"], complexity: "complex" },
    { summary: "Broadcasts an agent-complete event carrying token usage and final content to the frontend.", tags: ["event-handler","telemetry"], complexity: "moderate" },
    { summary: "Broadcasts a structured agent-error event derived from a StreamingError to the frontend.", tags: ["event-handler","error-handling"], complexity: "moderate" },
    { summary: "Broadcasts a non-fatal agent-warning event with a source label to the frontend.", tags: ["event-handler"], complexity: "simple" },
  ],
  classes: [
    { summary: "Structured representation of a stream failure, carrying the error code, retryability, and optional details.", tags: ["data-model","error-handling"], complexity: "simple" },
    { summary: "Enumerates the classes of streaming failure (auth, rate-limit, overload, context-overflow, cancelled, etc.) with retryability and wire-value mapping.", tags: ["data-model","error-handling"], complexity: "moderate" },
  ],
},
[`${P}types/context.rs`]: {
  summary: "Defines the core data types passed through turn processing: ProcessingContext/ProcessingResult for a turn's input/output, IdeContext and UserPresence/UserProfile capturing editor and user state, and SystemPromptConfig used to render the system prompt.",
  tags: ["type-definition","data-model"],
  complexity: "complex",
  funcs: [],
  classes: [
    { summary: "Per-message processing context carrying attached images, resume flag, display text, and turn/intent identifiers.", tags: ["data-model"], complexity: "moderate" },
    { summary: "Represents the user's current presence/availability state (interactive, defer-and-batch, autonomous) along with auto-resolve/approve timing knobs.", tags: ["data-model"], complexity: "moderate" },
    { summary: "Snapshot of the connected IDE's state — open files, selection, git status, terminal context, linter errors — passed into the system prompt.", tags: ["data-model","ide-integration"], complexity: "complex" },
    { summary: "Output of turn processing: final content, token counts, truncation flag, turn summary, and optional fork-redirect signal.", tags: ["data-model"], complexity: "moderate" },
    { summary: "Configuration bundle used to render a session's system prompt, combining model, agent identity/skills, workspace, and IDE/user-presence context.", tags: ["data-model","configuration"], complexity: "complex" },
  ],
},
[`${P}types/enums.rs`]: {
  summary: "Defines the SessionStatus lifecycle enum (pending through archived) and AgentExecMode (Build/Ask/Plan/Debug/Review/Wingman), each with string parsing and serialization helpers.",
  tags: ["type-definition","data-model","enum"],
  complexity: "moderate",
  funcs: [
    { summary: "Serializes a SessionStatus variant to its canonical string representation.", tags: ["serialization"], complexity: "simple", nameOverride: "SessionStatus::as_str" },
    { summary: "Parses a SessionStatus from its string representation, returning an error variant for unrecognized input.", tags: ["parsing"], complexity: "simple", nameOverride: "SessionStatus::parse" },
    { summary: "Reports whether a SessionStatus represents a terminal (non-continuable) state.", tags: ["utility"], complexity: "simple" },
    { summary: "Converts a raw status source type into a SessionStatus.", tags: ["conversion"], complexity: "simple" },
    { summary: "Serializes an AgentExecMode variant to its canonical string representation.", tags: ["serialization"], complexity: "simple", nameOverride: "AgentExecMode::as_str" },
    { summary: "Parses an AgentExecMode from its string representation.", tags: ["parsing"], complexity: "simple", nameOverride: "AgentExecMode::parse" },
  ],
  classes: [
    { summary: "Enum of a session's lifecycle states (Pending, Idle, Running, WaitingForUser, ..., Archived) with parsing/serialization and terminal/active checks.", tags: ["data-model","enum"], complexity: "moderate" },
    { summary: "Enum of agent execution modes (Build, Ask, Plan, Debug, Review, Wingman) with parsing/serialization.", tags: ["data-model","enum"], complexity: "simple" },
  ],
},
[`${P}types/filter.rs`]: {
  summary: "Tiny module stub (a type alias or narrow re-export) related to session type filtering; contains no substantial logic.",
  tags: ["type-definition","stub"],
  complexity: "simple",
  funcs: [], classes: [],
},
[`${P}types/mod.rs`]: {
  summary: "Barrel module re-exporting the session types submodules (context, enums, filter, turn) as a single `types` namespace.",
  tags: ["barrel","type-definition","module-root"],
  complexity: "simple",
  funcs: [], classes: [],
},
[`${P}types/turn.rs`]: {
  summary: "Defines DialogTurn and its lifecycle state/stats types, tracking a single turn's running/completed/cancelled/failed state, token/tool-call counters, and elapsed duration.",
  tags: ["type-definition","data-model","turn-processing"],
  complexity: "moderate",
  funcs: [
    { summary: "Constructs a new DialogTurn in the Running state from the user input and a cancellation flag.", tags: ["factory"], complexity: "simple" },
  ],
  classes: [
    { summary: "Represents a single in-flight or completed turn: its id, state, user input, stats, start time, and cancellation flag.", tags: ["data-model","turn-processing"], complexity: "moderate" },
  ],
},
[`${P}wingman/bar.rs`]: {
  summary: "Tauri window-management commands to open, close, and query the visibility of the Wingman floating status bar for a session, positioning it on a chosen monitor.",
  tags: ["ui-integration","tauri-command","wingman"],
  complexity: "simple",
  funcs: [
    { summary: "Opens (or creates) the Wingman floating bar window for a session on the given monitor and mission label.", tags: ["ui-integration","window-management"], complexity: "moderate" },
    { summary: "Closes the Wingman floating bar window if it is open.", tags: ["ui-integration","window-management"], complexity: "moderate" },
    { summary: "Reports whether the Wingman floating bar window is currently visible.", tags: ["ui-integration","window-management"], complexity: "moderate" },
  ],
  classes: [],
},
[`${P}wingman/bar_native.rs`]: {
  summary: "Native implementation of the Wingman bar's control surface: tracks last status and session list entries, and exposes init/show/hide/set_status/set_elapsed operations backed by platform-native UI callbacks rather than a Tauri webview window.",
  tags: ["ui-integration","wingman","state-management","native"],
  complexity: "complex",
  funcs: [
    { summary: "Returns the callback invoked when the user triggers the Wingman bar's stop control.", tags: ["ui-integration","callback"], complexity: "moderate" },
    { summary: "Dispatches a closure onto the main UI thread, used to safely mutate native bar state from callbacks.", tags: ["concurrency","ui-integration"], complexity: "moderate" },
    { summary: "Initializes the native Wingman bar with the given app handle, wiring up its callbacks.", tags: ["initialization","ui-integration"], complexity: "moderate" },
    { summary: "Shows the native Wingman bar for a session on the given screen.", tags: ["ui-integration"], complexity: "moderate" },
    { summary: "Re-asserts the Wingman bar's visibility and position, correcting for any drift after screen/monitor changes.", tags: ["ui-integration"], complexity: "moderate" },
    { summary: "Sets the Wingman bar's status text.", tags: ["ui-integration","state-management"], complexity: "simple" },
    { summary: "Inserts or updates a session entry (title, status, phase, elapsed) in the native Wingman bar's session list.", tags: ["ui-integration","state-management"], complexity: "moderate" },
  ],
  classes: [],
},
[`${P}wingman/handle.rs`]: {
  summary: "Defines WingmanHandle, tracking a running Wingman mission's cancellation flag and background task join handle, and WingmanSessionState which wraps an optional handle for the current session.",
  tags: ["state-management","concurrency","wingman","data-model"],
  complexity: "simple",
  funcs: [],
  classes: [
    { summary: "Handle to a running Wingman mission, exposing stop() to cancel it and is_running() to check its status.", tags: ["data-model","concurrency"], complexity: "simple" },
    { summary: "Wrapper holding the optional WingmanHandle for a session's currently active (or absent) Wingman mission.", tags: ["data-model","state-management"], complexity: "simple" },
  ],
},
};

// ---- Build nodes/edges ----
const nodes = [];
const edges = [];
const filePaths = Object.keys(sig).sort();

for (const path of filePaths) {
  const m = META[path];
  if (!m) throw new Error('Missing META for ' + path);
  const s = sig[path];
  if (m.funcs.length !== s.sigF.length) throw new Error(`func count mismatch ${path}: meta=${m.funcs.length} sig=${s.sigF.length}`);
  if (m.classes.length !== s.sigC.length) throw new Error(`class count mismatch ${path}: meta=${m.classes.length} sig=${s.sigC.length}`);

  const fileNode = {
    id: `file:${path}`,
    type: 'file',
    name: path.split('/').pop(),
    filePath: path,
    summary: m.summary,
    tags: m.tags,
    complexity: m.complexity,
  };
  if (m.languageNotes) fileNode.languageNotes = m.languageNotes;
  nodes.push(fileNode);

  s.sigF.forEach((f, i) => {
    const meta = m.funcs[i];
    const nodeName = meta.nameOverride || f.name;
    const id = `function:${path}:${nodeName}`;
    nodes.push({
      id, type: 'function', name: nodeName, filePath: path,
      lineRange: [f.s, f.e],
      summary: meta.summary, tags: meta.tags, complexity: meta.complexity,
    });
    edges.push({ source: `file:${path}`, target: id, type: 'contains', direction: 'forward', weight: 1.0 });
    if (s.exportsNames.includes(`${f.name}@${f.s}`)) {
      edges.push({ source: `file:${path}`, target: id, type: 'exports', direction: 'forward', weight: 0.8 });
    }
  });

  s.sigC.forEach((c, i) => {
    const meta = m.classes[i];
    const nodeName = meta.nameOverride || c.name;
    const id = `class:${path}:${nodeName}`;
    nodes.push({
      id, type: 'class', name: nodeName, filePath: path,
      lineRange: [c.s, c.e],
      summary: meta.summary, tags: meta.tags, complexity: meta.complexity,
    });
    edges.push({ source: `file:${path}`, target: id, type: 'contains', direction: 'forward', weight: 1.0 });
    if (s.exportsNames.includes(`${c.name}@${c.s}`)) {
      edges.push({ source: `file:${path}`, target: id, type: 'exports', direction: 'forward', weight: 0.8 });
    }
  });
}

// ---- imports edges: 1:1 from batchImportData ----
let importEdgeCount = 0;
for (const path of filePaths) {
  const targets = batchImportData[path] || [];
  for (const t of targets) {
    edges.push({ source: `file:${path}`, target: `file:${t}`, type: 'imports', direction: 'forward', weight: 0.7 });
    importEdgeCount++;
  }
}

// ---- high-confidence calls edges (grounded in neighborMap symbols + clear naming match) ----
const callsEdges = [
  // title.rs::generate_session_title -> side_query.rs::side_query
  { source: 'function:src-tauri/crates/agent-core/src/core/session/title.rs:generate_session_title',
    target: 'function:src-tauri/crates/agent-core/src/core/side_query.rs:side_query',
    type: 'calls', direction: 'forward', weight: 0.7 },
  // event_handler/mod.rs hook dispatch delegation
  { source: 'function:src-tauri/crates/agent-core/src/core/session/turn/event_handler/mod.rs:before_tool_execute',
    target: 'function:src-tauri/crates/agent-core/src/core/session/turn/event_handler/hooks_dispatch.rs:dispatch_pre_tool',
    type: 'calls', direction: 'forward', weight: 0.8 },
  { source: 'function:src-tauri/crates/agent-core/src/core/session/turn/event_handler/mod.rs:on_turn_stop_check',
    target: 'function:src-tauri/crates/agent-core/src/core/session/turn/event_handler/hooks_dispatch.rs:dispatch_stop_check',
    type: 'calls', direction: 'forward', weight: 0.8 },
  { source: 'function:src-tauri/crates/agent-core/src/core/session/turn/event_handler/mod.rs:post_tool_hook',
    target: 'function:src-tauri/crates/agent-core/src/core/session/turn/event_handler/hooks_dispatch.rs:dispatch_post_tool',
    type: 'calls', direction: 'forward', weight: 0.8 },
  // event_handler/mod.rs streaming buffer delegation (foundation/streaming.rs)
  { source: 'function:src-tauri/crates/agent-core/src/core/session/turn/event_handler/mod.rs:on_message_delta',
    target: 'function:src-tauri/crates/agent-core/src/foundation/streaming.rs:append_message_delta',
    type: 'calls', direction: 'forward', weight: 0.7 },
  { source: 'function:src-tauri/crates/agent-core/src/core/session/turn/event_handler/mod.rs:on_thinking_delta',
    target: 'function:src-tauri/crates/agent-core/src/foundation/streaming.rs:append_thinking_delta',
    type: 'calls', direction: 'forward', weight: 0.7 },
];
for (const e of callsEdges) edges.push(e);

console.log('TOTAL NODES', nodes.length);
console.log('TOTAL EDGES', edges.length);
console.log('  contains:', edges.filter(e=>e.type==='contains').length);
console.log('  exports:', edges.filter(e=>e.type==='exports').length);
console.log('  imports:', edges.filter(e=>e.type==='imports').length, '(expected', importEdgeCount, ')');
console.log('  calls:', edges.filter(e=>e.type==='calls').length);

// sanity: unique node ids
const idSet = new Set();
for (const n of nodes) {
  if (idSet.has(n.id)) throw new Error('Duplicate node id: ' + n.id);
  idSet.add(n.id);
}
console.log('unique node ids OK:', idSet.size);

// sanity: self-referencing edges
for (const e of edges) {
  if (e.source === e.target) throw new Error('Self-edge: ' + e.source);
}
console.log('no self-edges OK');

// ---- split into parts (parts = ceil(max(nodes/60, edges/120))) ----
const parts = Math.max(1, Math.ceil(Math.max(nodes.length/60, edges.length/120)));
console.log('PARTS:', parts);
const chunkSize = Math.ceil(filePaths.length / parts);

const partFilesArr = [];
for (let p = 0; p < parts; p++) {
  partFilesArr.push(filePaths.slice(p*chunkSize, (p+1)*chunkSize));
}

for (let p = 0; p < parts; p++) {
  const group = new Set(partFilesArr[p]);
  const partNodes = nodes.filter(n => group.has(n.filePath));
  const partNodeIds = new Set(partNodes.map(n => n.id));
  const partEdges = edges.filter(e => partNodeIds.has(e.source));
  const fragment = { nodes: partNodes, edges: partEdges };
  const fname = parts === 1 ? `batch-4.json` : `batch-4-part-${p+1}.json`;
  fs.writeFileSync(`${outDir}/${fname}`, JSON.stringify(fragment, null, 1));
  console.log(`wrote ${fname}: nodes=${partNodes.length} edges=${partEdges.length} files=${group.size}`);
}
