---
type: domain-context
name: org2-agent-execution
description: Execute one resolved native agent session, serialize its accepted inputs, run provider/tool iterations, preserve session continuity, and settle logical submissions.
tags: [org2, domain-model, bounded-context]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# Agent Execution

## Purpose

Execute one resolved native agent session, serialize its accepted inputs, run provider/tool iterations, preserve session continuity, and settle logical submissions.

**Classification:** Core

The boundary is Derived. The listed source paths and entity/lifecycle facts are source-observed or UA-observed where cited by the accepted reference corpus.

## Boundary

### Owns

- `AgentSession` live aggregate.
- `SessionRuntime` executable strategy bundle.
- `DialogTurn` active execution episode.
- `TurnIntent` durable logical submission identity.
- Session-scoped runtime tool registry and effective execution policy.

### Does not own

Editable `AgentDefinition` belongs to Agent Configuration. `WorkItem` and `WorkItemRun` belong to Work Management. Agent-org hierarchy/tasks belong to Agent Team Coordination. Durable observational history belongs to Trajectory & Provenance.

## Invariants

- Runtime assembly installs provider, registry, and policy before execution.
- Only one dialog turn is active in a session at a time.
- Compaction preserves active plan state and session continuity.
- `turn_intent_id` and `turn_id` remain distinct identities.

## Consumes

- Resolved agent configuration.
- Work/run bindings and execution requests.
- Agent-team member/run context.
- Human/policy control resolutions.
- Recalled memory and learnings.
- Execution infrastructure such as tools, Git, terminal, browser, search, and MCP connections.

## Publishes

- Execution activity and session metadata to Trajectory & Provenance.
- Experience/learning signals to Memory & Learning.
- Permission/question/plan/secret/mode obligations to Human Interaction & Approval.
- Execution status/outcome references to Work Management and Agent Team Coordination.

## Representative implementation paths

- `src-tauri/crates/agent-core/src/core/session/`
- `src-tauri/crates/agent-core/src/core/turn_executor/`
- `src-tauri/crates/agent-core/src/init/`
- `src-tauri/crates/agent-core/src/core/model_context/`

## Context relationship notes

See [Entity ownership](ref-eng/domain-models/entity-ownership.md) and [Context relationships](ref-eng/domain-models/context-relationships.md) for the canonical cross-context contracts.
