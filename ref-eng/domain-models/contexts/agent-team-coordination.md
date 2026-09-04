---
type: domain-context
name: org2-agent-team-coordination
description: Coordinate reusable agent teams and their runs: hierarchy, member identity, delegated tasks, inbox routing, completion intent, finality, and run reconciliation.
tags: [org2, domain-model, bounded-context]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# Agent Team Coordination

## Purpose

Coordinate reusable agent teams and their runs: hierarchy, member identity, delegated tasks, inbox routing, completion intent, finality, and run reconciliation.

**Classification:** Core

The boundary is Derived. The listed source paths and entity/lifecycle facts are source-observed or UA-observed where cited by the accepted reference corpus.

## Boundary

### Owns

- `AgentOrg` composition.
- `OrgMember` identity/hierarchy.
- `AgentOrgRunRecord` coordinated-run envelope.
- Run-scoped Org tasks.
- Agent-org inbox messages and resolutions.
- Completion intent and finality state.

### Does not own

An Org Task is not a durable project `WorkItem`. `AgentOrg` is not `ProjectOrg` or `CloudOrg`. Individual session execution remains owned by Agent Execution.

## Invariants

- Task routing is constrained by the organization hierarchy.
- Completion intent does not itself make a run terminal.
- Run finality is assessed against current blockers before terminal settlement.
- Member execution can use Agent Sessions without transferring coordination ownership.

## Consumes

- Agent definitions/resolved member configuration.
- Native Agent Execution for member sessions.
- Optional Work Item/run references.

## Publishes

- Member/run context and delegated input to Agent Execution.
- Run status/finality/progress to UI and work-link consumers.
- Coordination history to Trajectory & Provenance where recorded.

## Representative implementation paths

- `src-tauri/crates/agent-core/src/core/coordination/`
- `src-tauri/crates/agent-core/src/core/coordination/agent_org_runs/`
- `src-tauri/crates/agent-core/src/core/session/turn/processor/inbox_drain/routing.rs`

## Context relationship notes

See [Entity ownership](ref-eng/domain-models/entity-ownership.md) and [Context relationships](ref-eng/domain-models/context-relationships.md) for the canonical cross-context contracts.
