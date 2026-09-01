---
type: implementation-reference
name: org2-interactive-native-agent-loop
description: Runtime trace for an interactive ORG2 native-agent launch and turn.
tags: [org2, runtime, native-agent, session, turn-loop]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: source-observed
---

# Interactive native-agent loop

## Scope and evidence

This record traces one interactive `rust_agent` launch from Session Creator input to frontend settlement. It includes the linked Work Item branch because that branch changes admission, prompt context, and durable completion.

All behavior is Source-observed at revision `b315ba4f82fb1fe294496793d7322095e7efe262`. Sequence views, state tables, and pseudocode are Derived from the cited source. No provider call or UI run occurred for this record.

Read the [execution-kernel architecture](ref-eng/architecture/native-agent-execution-kernel.md#native-agent-execution-kernel) for ownership and the [execution seams](ref-eng/interfaces/native-agent-execution-seams.md#native-agent-execution-seams) for caller-callee contracts.

## Nominal sequence

```mermaid
sequenceDiagram
    actor User
    participant UI as Session Creator
    participant RPC as session_launch RPC
    participant LC as Rust launch command
    participant WR as Work Run service
    participant Core as Core launch service
    participant Send as send_message_impl
    participant Q as DialogScheduler
    participant Proc as UnifiedMessageProcessor
    participant Loop as execute_turn
    participant LLM as LLMProvider
    participant Tools as ToolRegistry
    participant Events as UnifiedEventHandler
    participant View as SessionCore projection

    User->>UI: Submit composer content
    UI->>UI: Validate and build display/model projections
    UI->>RPC: SessionLaunchParams
    RPC->>LC: session_launch
    opt Linked Work Item
        LC->>WR: Enqueue and claim durable run
    end
    LC->>Core: AgentRunLaunchRequest
    Core->>Core: Resolve target, persist session, prepare workspace
    alt Durable launch
        Core->>Send: Await initial-turn submission
        Send->>Send: Resolve identity and initialize runtime
        Send->>Q: Enqueue ScheduledMessage
        Q-->>Send: Queue position or duplicate
        Send-->>Core: Scheduler accepted turn
        Core-->>LC: Launch accepted
        LC->>WR: Acknowledge dispatch started
    else Ordinary launch
        Core-->>Send: Spawn initial-turn submission
        Note over Core,Send: Core may return before queue acceptance
    end
    LC-->>UI: SessionLaunchResult
    opt Ordinary spawned submission
        Send->>Send: Resolve identity and initialize runtime
        Send->>Q: Enqueue ScheduledMessage
        Q-->>Send: Queue position or duplicate
    end
    Q->>Proc: Run one serialized turn closure
    Proc->>Proc: Persist input, load history, build prompt, compact
    Proc->>Loop: Messages, provider, tools, policy, handler
    loop Model/tool iterations
        Loop->>LLM: Streaming chat request
        LLM-->>Events: Deltas and usage
        alt Model requests tools
            Loop->>Tools: Policy, permission, and execute
            Tools-->>Events: Tool call and result
        else Model completes
            Loop-->>Proc: TurnResult
        end
    end
    Events-->>View: Live IPC and EventStore changes
    Proc-->>View: agent:complete
    Proc-->>Q: Processing result
    Q->>WR: Record durable terminal when applicable
    Q-->>View: agent:turn_completed and terminal status
```

The diagram shows semantic order, not thread ownership. The backend can emit live events before the launch request returns. An ordinary non-durable launch can spawn its initial submission. A durable Work Item launch awaits scheduler acceptance before it acknowledges dispatch delivery.

## Derived launch and turn pseudocode

```text
launch_from_creator(draft, selection):
    reject invalid configuration, declined short input, or detected secret
    display_input, agent_input = project_composer_input(draft)
    params = build_typed_launch_payload(agent_input, selection)
    merge structured Work Item context when selected
    result = session_launch(params)
    add result to frontend session state
    add the display-side optimistic user event when required
    mark the frontend turn as running
    return result

session_launch(params):
    validate workspace and worktree fields
    if params has Work Item and no durable run:
        run = enqueue durable Work Item Run
        lease = claim its dispatch
        params.durable_run_id = run.id
    result = launch the selected session category
    if a lease exists:
        acknowledge started on success
        record dispatch failure on error
    return result

launch_native_agent(request):
    resolve agent or Agent Org target
    persist session identity and launch context
    prepare local workspace or worktree
    if request has initial content and this durable intent is not already accepted:
        if request is durable:
            await submit_initial_turn(request)
        else:
            spawn submit_initial_turn(request)
    return launch result

submit_turn(input):
    resolve identity and lazily initialize SessionRuntime
    if input qualifies as mid-turn steering:
        add it to the active turn's steering queue and return
    persist session identity changes
    route Project work through its durable dispatcher when required
    write TurnIntent = queued
    enqueue one ScheduledMessage on the session scheduler
    return queue metadata

scheduler_worker(message):
    discard a stale generation
    write TurnIntent = running
    mark the session row running
    turn_id = begin_turn(message.content)
    result = process_message(turn_id, message)
    state = cancelled if cancel flag else completed if result ok else failed
    end_turn(state)
    record Work Item Run terminal when the intent owns one
    finalize session and emit authoritative terminal event
    write TurnIntent terminal state
```

The pseudocode omits optional Agent Org, background memory, title generation, Wingman, and coordinator branches. It preserves the ordering constraints that affect the interactive path.

## Runtime state transitions

### Turn intent

| From | To | Owner and trigger |
| --- | --- | --- |
| none or optimistic | queued | `send_message_impl` writes the durable intent before scheduler ownership. |
| queued | running | The session worker accepts the current generation and starts the closure. |
| queued | stale | Queue invalidation changes the generation before the worker starts the message. |
| queued | coalesced | The scheduler finds a duplicate client message ID and closes the new intent. |
| queued | rejected | The scheduler channel is full or closed. |
| running | completed | The execution closure returns success and no stronger terminal state exists. |
| running | failed | The closure or scheduler execution fails. |
| running | cancelled | The turn closure observes the cancel flag and writes cancellation before generic scheduler settlement. |

The bridge enum also contains `optimistic`. This trace does not claim that every interactive launch writes that state before `queued`.

### Active dialog turn

| State | Transition |
| --- | --- |
| idle | `begin_turn` creates a stable turn ID, sets the active generation, and stores the active turn. |
| running | Provider and tool iterations execute against the shared cancel flag. |
| completed, failed, or cancelled | `end_turn` finalizes statistics, clears the active turn, and clears its generation. |

### Durable Work Item Run

| Phase | Current action |
| --- | --- |
| Admission | The launch command creates a run, claims one dispatch lease, and places the run ID in launch parameters. |
| Delivery | Core launch awaits scheduler acceptance for durable content before the launch command acknowledges the dispatch. |
| Execution | The turn intent ID identifies the owned durable run for this turn. |
| Terminal | The closure records `Succeeded`, `Failed`, or `Cancelled` with token usage and error text before broader lifecycle fan-out. |

A Work Item Run owns one turn, not the whole Session. Later turns on the same Session must not settle the earlier run.

## Work Item context path

Work Item information crosses the runtime through separate channels:

1. The composer attachment contributes readable content to `agentInput`.
2. Structured launch fields carry organization, project, item, role, and product-mode identity.
3. The launch command creates and claims a durable Work Item Run for a new linked launch.
4. Session persistence retains the Work Item identity.
5. Prompt construction reads the current session row on each turn and injects linked-item guidance and the `org2-pm` brief.
6. Turn settlement records the durable run terminal and can create a fallback receipt after a completed non-stream-error turn.

The structured ID is not a provider-native field. Backend prompt construction turns current persisted work identity into model-visible text. This distinction corrects the stale claim recorded in the [source baseline](ref-eng/evidence/G-ORG2-REF-001-first-slice-sources.md#first-slice-source-baseline).

## Queue, steering, and ordering

- Each `AgentSession` owns one lazily started bounded `DialogScheduler` worker.
- The worker processes accepted jobs FIFO within the session. Different sessions execute independently.
- `Turn` jobs emit running and terminal signals. `Maintenance` jobs use the same serialization boundary without presenting a user turn.
- A client message ID coalesces duplicate queue submissions.
- A generation change invalidates pending work after Stop, rewind, or another boundary that discards queued intent.
- A plain-text user submit that arrives during a running turn can enter the steering queue. The agent loop drains it before a later model iteration.
- The steering path rechecks the active turn after enqueue to close the race where the turn ends during submission.

The queue returns acceptance metadata before execution finishes. Durable launch admission adds a stronger condition: it waits for queue acceptance before dispatch acknowledgement.

## Prompt and context assembly

The message processor performs these steps before the first provider call:

1. Restore session-memory state when enabled.
2. Take the configured pre-message snapshot.
3. Persist the user message, except an empty Resume input.
4. Load the durable LLM history and fail the turn if history load fails.
5. Start skill and memory prefetch without blocking the hot path.
6. Build the stable system prefix and volatile prompt body.
7. Repair cancelled, resumed, or interrupted history and restore tool-result pairing.
8. Drain durable Agent Org inbox input when the session belongs to a run.
9. Run pre-turn compaction and handle an optional compact-fork redirect.
10. Apply an optional provider-view MiniCPM overlay without changing canonical history.
11. Build dynamic sections, including linked Work Item guidance.
12. Attach volatile context at the tail and call the turn executor.

Stable prompt content stays before history for provider caching. Volatile content stays after history and is rebuilt each turn.

## Provider loop

`execute_turn` owns one ordered loop:

1. Prepare the iteration input and drain steering when present.
2. Filter tool definitions through the effective turn policy.
3. Call the selected `LLMProvider` with streaming callbacks and the shared cancel flag.
4. Record usage and apply provider or stream recovery.
5. Execute requested tools or accept non-tool completion.
6. Repeat until completion, cancellation, recovery exhaustion, or iteration limit.
7. Return one `TurnResult` to the message processor.

The provider is a session strategy created by the runtime factory. The loop does not branch on a concrete provider API.

## Tool and approval path

For each tool call, the executor follows this order:

1. Apply the pre-tool hook. A hook can block the call or replace its arguments.
2. Stop if cancellation is active.
3. Reject malformed streamed arguments before tool execution.
4. If policy returns `Ask`, call the session `PermissionProvider` and race the response against cancellation.
5. Run read-before-edit and freshness checks for file writes.
6. Call `ToolRegistry.execute_with_policy` with a typed `CallContext`.
7. Record file effects, truncate or preserve structured output as allowed, add the tool result to model history, persist its row, and emit live events.

An `Allow`, `Deny`, or `Ask` policy decision does not itself perform an effect. The registry and tool call remain behind the permission and cancellation checks. User denial becomes an error tool result that the model can observe.

## Cancellation

The frontend first marks local streaming stopped, then calls `agent_session_cancel` with a typed reason. `AgentAppState` resolves the live session and calls `AgentSession.cancel_active_turn`.

The reason controls boundary effects. A user-stop-like reason can:

- invalidate pending scheduler messages;
- clear queued steering;
- cancel background subagent workers;
- set the active turn's shared cancel flag;
- preserve a cancellation marker for the next history repair;
- clear pending plan approval.

The provider stream, permission wait, tool loop, processor, and event handler observe the same cancellation boundary. The event handler also checks the active turn generation before it writes a durable EventStore event. The frontend ignores later live stream deltas for a stopped turn.

## Retry and recovery

The runtime uses separate recovery mechanisms for separate failures:

| Failure | Current response |
| --- | --- |
| Provider or stream interruption | The turn executor applies its bounded retry budgets and emits retry status through the event handler. |
| Partial streamed response before retry | The event handler retracts uncommitted EventStore segments and clears its streaming buffer before regenerated output arrives. |
| `ContextTooLong` | The processor compacts the message list and retries the turn up to two times when compaction is enabled. |
| Previous user cancellation | The next turn consumes the durable cancel marker and removes unresolved tool uses without adding a synthetic interrupt prompt. |
| Resume after an interrupted tool exchange | The processor invalidates prompt cache and repairs orphan tool-use pairs before the next request. |
| Frontend event-dispatch error | The adapter logs the error; repeated non-terminal failures force a visible failed status, while a terminal-handler error still unlocks the input. |

Recovery that regenerates a response must remove only uncommitted stream segments. Completed earlier iterations remain authoritative.

## Compaction

Compaction has three distinct positions:

- Pre-turn compaction applies micro-compaction, aggregate budget checks, LLM context compaction, and an optional compact-fork redirect before dynamic context is built.
- The optional MiniCPM overlay changes only the provider request view after canonical compaction. It does not rewrite the transcript or automatic-compaction state.
- Reactive compaction runs only after `ContextTooLong` and retries at most twice.

The runtime rebuilds volatile context after pre-provider early returns and compaction. This prevents an empty wake or redirected fork from consuming a coordinator work revision that no provider observed.

## Persistence and event flow

The runtime uses both durable records and live projections:

| Data | Durable owner | Live projection |
| --- | --- | --- |
| Session identity and status | Session persistence and lifecycle service | Session list/status callbacks |
| User, assistant, and tool messages | Unified persistence plus per-session EventStore write-through | `es:changed` and agent events |
| Turn intent | `session_turn_intents` through the leaf-level session bridge | Queue and terminal status |
| Work Item Run | Project-management work-run service | Work-management views and lifecycle notifications |
| Thinking/message deltas | In-memory streaming buffer until flushed | `agent:thinking_delta`, `agent:message_delta`, and `agent:streaming_complete` |
| Tool file history | Per-tool-call snapshots | File-change and tool events |

Saving the user message and loading history are turn-critical: an error fails the turn. Some EventStore, tool-row, hook, diagnostic, and lifecycle notification failures log warnings so the provider result can still settle. The code does not claim one atomic transaction across all stores.

## Settlement and frontend projection

On a successful processor turn:

1. The handler flushes pending message and thinking segments.
2. The processor records usage.
3. Post-turn dispatch emits `agent:complete` before optional background work.
4. The execution closure calls `end_turn` with completed or cancelled state.
5. A durable Work Item Run receives its terminal result when present.
6. `finalize_session` persists session status and emits the terminal turn signal.
7. The scheduler updates turn-intent terminal state and emits queue status.

The frontend treats `agent:complete` as intermediate because it carries content and usage but not the authoritative intent settlement. `agent:turn_completed` supplies the final turn ID, turn-intent ID, and completed, failed, or cancelled status. Frontend event application runs through one promise chain so terminal state cannot overtake earlier events on the same channel.

When the processor fails before `agent:complete`, lifecycle finalization and the scheduler surface failure. The scheduler also converts a panicked execution closure into a structured error instead of terminating its worker silently.

## Runtime invariants

- One accepted interactive turn uses one session scheduler before it reaches the provider.
- Durable dispatch cannot report delivery before the scheduler accepts its turn.
- A turn ID and turn-intent ID have different roles and remain distinct through persistence and frontend settlement.
- The Work Item Run belongs to one durable turn, not to every future turn in the Session.
- Provider-visible tools equal ready tools allowed by the effective turn policy.
- A tool effect follows hook, cancellation, permission, and file-safety gates.
- A stopped or superseded turn cannot write later EventStore rows through the current-generation gate.
- Stable prompt content and volatile per-turn context stay in separate cache positions.
- `agent:complete` can present output, but only the terminal turn signal settles frontend finality.
- Retry can replace partial current-iteration output, but it does not retract committed earlier output.

## Failure boundaries

| Boundary | Stops launch or turn | Continues with warning or fallback |
| --- | --- | --- |
| Frontend validation, secret guard, or key resolution | Yes | No |
| Invalid workspace, category, target, or agent identity | Yes | No |
| Durable run enqueue, claim, or dispatch acknowledgement | Yes for linked launch | Dispatch failure is recorded before return |
| Session runtime creation or scheduler rejection | Yes | No |
| User-message save or history load | Yes | No |
| Optional prompt context or MiniCPM overlay | No | Omit, add bounded fallback, or warn |
| Provider recovery exhaustion | Yes | Terminal failure events remain |
| Tool denial or tool execution error | No by default | Error tool result returns to the model unless cancellation ends the batch |
| Tool-row or auxiliary EventStore write | Usually no | Warn; current code can continue |
| Final lifecycle notification | No after result exists | Warn and preserve the recorded result where possible |
| Repeated frontend projection failure | UI turn becomes visibly failed | Reload can reconcile from durable state |

## Known limits

- This record does not measure latency, retry duration, token cost, queue capacity under load, or provider parity.
- It does not prove database crash recovery or exactly-once behavior across process failure. It reports only the source's admission, idempotency, and terminal-write order.
- It does not fully trace Agent Org coordination, CLI agents, Wingman, mobile sends, imported history, plan-mode re-entry, or background job wakes.
- It does not prove that every optional hook, tool, provider, and frontend renderer works at the pinned revision.
- A controlled runtime trace is still required before any claim can move from Source-observed to Runtime-verified.

## Source map

| Concern | Current source |
| --- | --- |
| Composer input and launch | [`inputPreparation.ts`](src/engines/SessionCore/hooks/session/useSessionCreator/useSessionLaunch/inputPreparation.ts), [`launchPayload.ts`](src/engines/SessionCore/hooks/session/useSessionCreator/useSessionLaunch/launchPayload.ts), [`index.tsx`](src/engines/SessionCore/hooks/session/useSessionCreator/useSessionLaunch/index.tsx) |
| Typed launch RPC | [`session.ts`](src/api/tauri/agent/session.ts), [`agentSession.ts`](src/api/tauri/rpc/procedures/agentSession.ts) |
| Launch admission and durable dispatch | [`launch.rs`](src-tauri/crates/agent-core/src/state/commands/session/launch.rs), `session_launch_impl` |
| Core launch and initial-turn acceptance | [`launch/mod.rs`](src-tauri/crates/agent-core/src/core/session/launch/mod.rs), `launch_rust_agent_run`; [`launch_org.rs`](src-tauri/crates/agent-core/src/core/session/launch/launch_org.rs), `send_initial_turn` |
| Turn submission | [`send.rs`](src-tauri/crates/agent-core/src/state/commands/session/message/send.rs), `send_message_impl` |
| Queue and intent transitions | [`scheduler.rs`](src-tauri/crates/agent-core/src/core/session/scheduler.rs), [`session_bridge.rs`](src-tauri/crates/agent-core/src/foundation/session_bridge.rs) |
| Active turn and cancellation | [`session_runtime.rs`](src-tauri/crates/agent-core/src/state/session_runtime.rs), [`unified.rs`](src-tauri/crates/agent-core/src/state/unified.rs), [`session/mod.rs`](src-tauri/crates/agent-core/src/state/commands/session/mod.rs) |
| Prompt assembly and processor order | [`processor/mod.rs`](src-tauri/crates/agent-core/src/core/session/turn/processor/mod.rs), [`prompt.rs`](src-tauri/crates/agent-core/src/core/session/turn/processor/prompt.rs) |
| Provider loop and reactive compaction | [`execute.rs`](src-tauri/crates/agent-core/src/core/turn_executor/execute.rs), [`processor/execute.rs`](src-tauri/crates/agent-core/src/core/session/turn/processor/execute.rs) |
| Tool policy, permission, and effect | [`single.rs`](src-tauri/crates/agent-core/src/core/turn_executor/tool_execution/single.rs), [`permission.rs`](src-tauri/crates/agent-core/src/core/turn_executor/helpers/permission.rs), [`registry.rs`](src-tauri/crates/agent-core/src/core/tools/registry.rs) |
| Event persistence and streaming recovery | [`event_handler/mod.rs`](src-tauri/crates/agent-core/src/core/session/turn/event_handler/mod.rs), [`post_turn_dispatch.rs`](src-tauri/crates/agent-core/src/core/session/turn/processor/post_turn_dispatch.rs) |
| Session settlement | [`lifecycle.rs`](src-tauri/crates/agent-core/src/lifecycle.rs), `finalize_session` |
| Frontend projection | [`createRustAgentAdapter.ts`](src/engines/SessionCore/sync/adapters/createRustAgentAdapter.ts), [`eventHandlers/index.ts`](src/engines/SessionCore/sync/adapters/rustAgent/eventHandlers/index.ts), [`sessionHandlers.ts`](src/engines/SessionCore/sync/adapters/rustAgent/eventHandlers/sessionHandlers.ts) |

## Conformance note

This record provides the required sequence view, labeled pseudocode, state transitions, work-item, queue, provider, tool, approval, cancellation, retry, compaction, persistence, settlement, invariant, failure, limit, and source sections. It withholds runtime verification.
