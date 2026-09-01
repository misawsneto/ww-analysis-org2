---
type: evidence-manifest
name: G-ORG2-REF-001-first-slice-sources
description: Source baseline for the first ORG2 native-agent execution slice.
tags: [org2, implementation-reference, evidence, native-agent]
---

# First-slice source baseline

**Goal:** G-ORG2-REF-001  
**Source revision:** `b315ba4f82fb1fe294496793d7322095e7efe262`  
**Status:** active investigation  
**Claim state:** Source-observed unless a row states otherwise

## Scope

This baseline identifies the current interactive native-agent launch path and the source owners that later architecture, interface, and runtime records must inspect. It does not claim runtime verification.

## Current launch trace

| Step | Current source evidence | Established fact |
| --- | --- | --- |
| Work-item option construction | `src/features/SessionCreator/variants/ChatPanel/workItemPickerModel.ts:61` and `:90` | The picker creates readable `contextText` and separate structured `workItemContext` fields. |
| Composer attachment | `src/features/SessionCreator/variants/ChatPanel/WorkItemAttachmentControl.tsx:210` | The UI inserts the readable text as a work-item pill and reports the primary structured context separately. |
| Model-facing input projection | `src/engines/SessionCore/hooks/session/useSessionCreator/useSessionLaunch/inputPreparation.ts:40` | Launch preparation keeps a display form for the UI and builds a separate agent form after context-pill expansion and projection. |
| Launch payload | `src/engines/SessionCore/hooks/session/useSessionCreator/useSessionLaunch/launchPayload.ts:210` | `buildSessionLaunchPayload()` places projected agent content and selected runtime fields into `SessionLaunchParams`. |
| Work-item metadata merge | `src/engines/SessionCore/hooks/session/useSessionCreator/useSessionLaunch/index.tsx:148` | `useSessionLaunch()` validates input, resolves keys and work-item context, then adds organization, project, work-item, role, and mode fields to the launch request. |
| Type-safe RPC seam | `src/api/tauri/agent/session.ts:520` and `src/api/tauri/rpc/procedures/agentSession.ts:169` | The frontend sends `SessionLaunchParams` through the `session_launch` RPC procedure and expects `SessionLaunchResult`. |
| Durable work-item dispatch | `src-tauri/crates/agent-core/src/state/commands/session/launch.rs:140` | A launch with `work_item_id` first creates and claims a durable manual Work Item Run, then routes by session category. |
| Native-agent launch | `src-tauri/crates/agent-core/src/state/commands/session/launch.rs:262` | The Rust path resolves target, workspace, organization context, work-item provenance, resources, mode, and initial content before `launch_rust_agent_run()`. |
| Unified message entry | `src-tauri/crates/agent-core/src/core/session/turn/entry.rs:115` | `process_message()` loads the session runtime, hooks, policy, context, skill and pill expansion, then calls `UnifiedMessageProcessor::process()`. |
| Linked work-item prompt | `src-tauri/crates/agent-core/src/core/session/turn/processor/prompt.rs:63` and `:273` | Project-mode sessions with a linked item receive dynamic system guidance that names the item and its work-management contract. |
| Agentic loop | `src-tauri/crates/agent-core/src/core/turn_executor/execute.rs:34` | `execute_turn()` orders input preparation, provider call and recovery, stream recovery, tool or non-tool handling, cancellation, and final result projection. |

## Corrected earlier findings

### Unused prompt builder

The earlier dossier describes `StartAgentButton → useWorkItemOrchestrator → buildSdeTaskPrompt() → SessionService.create()` as the work-item launch path.

Current source contains `buildSdeTaskPrompt()` at `src/modules/ProjectManager/WorkItems/components/WorkItemDetail/promptBuilder.ts:99`, but exact search of `src/` and `src-tauri/` finds no other source reference to `buildSdeTaskPrompt`, no `StartAgentButton`, and no `useWorkItemOrchestrator`. An older architecture-audit document still names `useWorkItemOrchestrator`, but it does not establish the current production path. The active interactive path runs through the Session Creator and `useSessionLaunch()`.

**Claim state:** Source-observed for the absent current references and present active path. Git history and runtime use at earlier revisions remain unverified.

### Work-item awareness is split, not absent

The earlier dossier states that the agent has no structural awareness of work items and that `workItemId` never enters agent context.

Current source contradicts the broad claim:

- The composer pill contributes work-item title, status, priority, description, labels, and todos to model-facing content.
- Structured launch metadata creates durable run and provenance state.
- Turn-time prompt construction renders a linked-work-item section and work-management CLI rules from persisted session fields.

The structured ID is not sent to the provider as an independent protocol field. Backend code uses it to construct runtime state and model-visible prompt text. This distinction must remain explicit in later records.

**Claim state:** Source-observed. Provider request capture or a controlled live session has not yet confirmed the exact final request bytes.

## Source-owner map

| Concern | Primary owners for the first slice |
| --- | --- |
| Session Creator and context attachment | `src/features/SessionCreator/variants/ChatPanel/`, `src/engines/SessionCore/hooks/session/useSessionCreator/useSessionLaunch/` |
| Frontend RPC contract | `src/api/tauri/agent/session.ts`, `src/api/tauri/rpc/procedures/agentSession.ts` |
| Launch validation and category routing | `src-tauri/crates/agent-core/src/state/commands/session/launch.rs` |
| Session construction and runtime ownership | `src-tauri/crates/agent-core/src/core/session/launch/`, `src-tauri/crates/agent-core/src/core/session/` |
| Prompt and context construction | `src-tauri/crates/agent-core/src/core/session/turn/entry.rs`, `src-tauri/crates/agent-core/src/core/session/turn/processor/prompt.rs` |
| Provider and tool loop | `src-tauri/crates/agent-core/src/core/turn_executor/`, `src-tauri/crates/agent-core/src/core/providers/`, `src-tauri/crates/agent-core/src/core/tools/` |
| Events and frontend projection | `src-tauri/crates/agent-core/src/core/session/turn/event_handler/`, `src-tauri/crates/agent-core/src/foundation/bus/`, `src/engines/SessionCore/` |
| Session persistence and recovery | `src-tauri/crates/agent-core/src/core/session/persistence/`, `src-tauri/crates/agent-core/src/foundation/persistence/session_snapshots.rs`, `src-tauri/crates/agent-core/src/core/session/recovery.rs` |

## Not yet established

- Exact final provider request bytes for a work-item launch.
- Which failure and cancellation branches publish which frontend events.
- The complete persistence commit order for user, assistant, tool, usage, work-item receipt, and session-state data.
- Which tool calls run in parallel and which policy or approval paths serialize them.
- The exact compaction triggers, retry budgets, and terminal settlement rules.
- Runtime parity among foreground native-agent, background native-agent, agent-organization, and external CLI categories.

These questions belong to later tasks. Do not fill them from generated summaries or adjacent implementations.
