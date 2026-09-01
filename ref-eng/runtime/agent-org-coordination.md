---
type: implementation-reference
name: org2-agent-org-coordination
description: Runtime, state, persistence, and finality model for coordinated Agent Org execution.
tags: [org2, runtime, agent-org, coordination, inbox]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: source-observed
---

# Agent Org coordination

## Scope and evidence

This record explains how ORG2 turns an `AgentOrg` definition into one durable coordinated run. It covers launch, member materialization, task and inbox routing, finality, recovery, and the frontend run view.

UA selected Agent Org Coordination as a semantic gap. Graphify then identified the launch, run store, inbox, session, database, and frontend boundaries. All behavioral claims are Source-observed at revision `b315ba4f82fb1fe294496793d7322095e7efe262`. The sequence and relation views are Derived from the cited source.

Read the [native-agent execution kernel](ref-eng/architecture/native-agent-execution-kernel.md#native-agent-execution-kernel) for one member's turn loop. This record starts one level above that kernel.

## Responsibility and boundary

Agent Org coordination owns the durable envelope around several agent sessions. It does not replace the session runtime. Each native member still executes through the normal `AgentSession` path.

```text
AgentOrg definition
  -> effective run snapshot
  -> AgentOrgRun and root coordinator session
  -> member session materialization
  -> tasks, inbox messages, and plan approvals
  -> ordinary native-agent turns
  -> finality assessment and terminal reconciliation
  -> bounded frontend run view
```

The root coordinator session remains the transcript source of truth. `AgentOrgRunRecord.root_session_id` supplies one durable anchor for the full run, even when a caller starts from a member session.

## User, harness, and agents

1. The user selects an Agent Org and launch context.
2. The harness resolves the org, validates the coordinator, applies member overrides, validates the workspace, and freezes the effective org snapshot.
3. The harness creates the run envelope and root coordinator session before it materializes workers.
4. Native members become child `UnifiedSessionRecord` values with `session_type=ORG_MEMBER`, the member ID, the root parent, and inherited project or Work Item context.
5. Agents coordinate through typed inbox messages, run-scoped tasks, interventions, and plan approvals.
6. Each member turn enters the shared native-agent execution kernel.
7. The harness evaluates canonical run facts before it publishes a terminal run state.
8. The frontend reads a bounded operational run view instead of the full inbox payload history.

CLI members and native Rust members share the organization snapshot but do not use the same session construction path. Native member materialization runs after the root launch and can fail independently.

## Core records and relations

| Record | Owner | Relation and purpose |
| --- | --- | --- |
| `AgentOrg` | Agent Org definition store | Composes reusable Agent Definitions and member overrides. |
| `AgentOrgRunRecord` | Agent Org run store | Freezes org identity, coordinator, root session, entry mode, optional work links, status, summary, error, and timestamps. |
| Root coordinator session | Session subsystem | Anchors the run transcript and coordinator identity. |
| Member session | Session subsystem | Links one run member to one child runtime session. |
| Org task | Run-scoped task store | Assigns coordinated work and contributes to finality. |
| Inbox row | Agent inbox store | Stores one typed message from a sender to a recipient, with optional run and request identity. |
| Inbox resolution row | Agent inbox store | Cancels or supersedes a source message without mutating that source row. |
| Completion intent | Run store | Records that the coordinator requested completion at a specific work revision. |
| Plan approval | Run-scoped approval store | Holds an agent plan until the required decision occurs. |

The system stores one authoritative direction for these relations. For example, a member session points to its parent/root lineage, and the run view derives the reverse roster view.

## Launch and materialization

`AgentRunTarget::AgentOrg` follows this order:

```text
load org
  -> validate coordinator and member identities
  -> apply launch overrides to an effective snapshot
  -> validate existing worktree and launch context
  -> create AgentOrgRun and root session
  -> return the root launch
  -> materialize members asynchronously
```

The ordering prevents org rows from appearing before workspace validation succeeds. It also lets the user enter the coordinator session without waiting for every worker runtime.

Member materialization flattens the org hierarchy, separates native and CLI members, and gives each native member its own effective runtime configuration. If native materialization fails, the run becomes failed and the launcher removes any partially created native sessions.

## Inbox delivery

`AgentMessage` is a closed message family. It includes plain messages, shutdown requests and responses, plan-approval requests and responses, and system notices such as member termination or idle state. A request ID correlates request-response exchanges.

The drain path applies these controls:

- It resolves the recipient from the persisted session member ID.
- It maps the root session to the coordinator member.
- It rejects an unknown non-roster member instead of inventing a route.
- It processes a bounded unread batch.
- It pauses delivery during user intervention.
- It materializes the transcript receipt before it marks the source row read.
- It leaves the source unread if a required side effect fails.

Large plan payloads can reach 256 KiB. The run view therefore exposes payload-free inbox previews. Full message payloads remain in the inbox store.

Source inbox rows are immutable. Cancellation and supersession append resolution rows, so operational queries can hide resolved work without rewriting historical input.

## Finality protocol

Run status supports `Running`, `Paused`, `Completed`, `Failed`, `Cancelled`, and `Abandoned`. `Paused` is nonterminal.

A completion request does not force `Completed`. It records completion intent only when the run is `Running` and no open task remains. The intent captures the current work revision.

Finality checks these blockers:

- missing root session;
- active member sessions;
- open or corrupt tasks;
- unread inbox messages;
- active user interventions;
- in-flight turn intents;
- pending plan approvals;
- missing or stale completion intent;
- coordinator progress that has not observed the latest work revision.

The store first assesses finality in a read transaction. Reconciliation then enters the shared session writer and an immediate transaction, reloads canonical facts under the lock, and chooses `Completed`, `Abandoned`, or `KeepRunning`. A terminal update and cancellation of pending plan approvals occur in that transaction before the frontend receives the change notification.

`Abandoned` is not a generic failure. It applies when unresolved tasks remain and the coordinator and all workers are permanently unavailable.

## Recovery and operational view

Startup recovery requeues abandoned member tasks, reconciles resolved runs, and changes still-running runs to paused. This prevents a process restart from presenting an old in-memory execution as active.

A bounded parent-session walk maps any member session to the root run anchor. The walk has cycle and depth controls. The run view combines finality, bounded task data, inbox previews, and pending approvals. It serves current operations and does not claim to be a complete message-history API.

## Seams and tradeoffs

| Choice | Benefit | Cost or limit |
| --- | --- | --- |
| Freeze the effective org snapshot | A run keeps the launch-time roster and overrides. | Later definition edits do not change the active run. |
| Use a root session as one anchor | Member-to-run resolution stays deterministic. | Every member lineage must preserve the parent relation. |
| Reuse native sessions for members | Provider, tool, policy, event, and cancellation behavior stay shared. | Org coordination must reconcile several independent session lifecycles. |
| Use typed inbox messages | Routing and side effects have explicit meaning. | Each new coordination protocol needs a new message variant and handler. |
| Append message resolutions | History remains immutable. | Readers must join or filter resolution state. |
| Gate terminal status on work revision | Late work cannot race a stale completion request. | Finality needs extra revision and coordinator-observation state. |
| Reload facts inside one writer transaction | The terminal decision uses current canonical state. | Finalization joins several stores and can wait for the shared writer. |

## Source map

| Concern | Current source |
| --- | --- |
| Run record and status | [`src-tauri/crates/agent-core/src/core/coordination/agent_org_runs/mod.rs`](src-tauri/crates/agent-core/src/core/coordination/agent_org_runs/mod.rs) |
| Run creation and persistence | [`src-tauri/crates/agent-core/src/core/coordination/agent_org_runs/helpers.rs`](src-tauri/crates/agent-core/src/core/coordination/agent_org_runs/helpers.rs), [`src-tauri/crates/agent-core/src/core/coordination/agent_org_runs/store.rs`](src-tauri/crates/agent-core/src/core/coordination/agent_org_runs/store.rs) |
| Finality rules | [`src-tauri/crates/agent-core/src/core/coordination/agent_org_runs/finality.rs`](src-tauri/crates/agent-core/src/core/coordination/agent_org_runs/finality.rs) |
| Org launch and member materialization | [`src-tauri/crates/agent-core/src/core/session/launch/mod.rs`](src-tauri/crates/agent-core/src/core/session/launch/mod.rs), [`src-tauri/crates/agent-core/src/core/session/launch/launch_org.rs`](src-tauri/crates/agent-core/src/core/session/launch/launch_org.rs) |
| Inbox model and storage | [`src-tauri/crates/agent-core/src/core/coordination/agent_inbox/message.rs`](src-tauri/crates/agent-core/src/core/coordination/agent_inbox/message.rs), [`src-tauri/crates/agent-core/src/core/coordination/agent_inbox/record.rs`](src-tauri/crates/agent-core/src/core/coordination/agent_inbox/record.rs) |
| Inbox routing and drain | [`src-tauri/crates/agent-core/src/core/session/turn/processor/inbox_drain/routing.rs`](src-tauri/crates/agent-core/src/core/session/turn/processor/inbox_drain/routing.rs), [`src-tauri/crates/agent-core/src/core/session/turn/processor/inbox_drain/drain.rs`](src-tauri/crates/agent-core/src/core/session/turn/processor/inbox_drain/drain.rs) |
| Run projection and controls | [`src-tauri/crates/agent-core/src/state/commands/session/org_tasks/run_view.rs`](src-tauri/crates/agent-core/src/state/commands/session/org_tasks/run_view.rs), [`src-tauri/crates/agent-core/src/state/commands/session/org_tasks/lifecycle.rs`](src-tauri/crates/agent-core/src/state/commands/session/org_tasks/lifecycle.rs) |
| Startup reconciliation | [`src-tauri/crates/agent-core/src/state/unified.rs`](src-tauri/crates/agent-core/src/state/unified.rs) |

## Known limits

This record does not prove multi-process coordination, network delivery between ORG2 instances, or parity between native and CLI members. It did not execute a live organization run. It describes the current local persistence and runtime contracts from source.

