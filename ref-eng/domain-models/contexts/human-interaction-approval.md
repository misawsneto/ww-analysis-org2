---
type: domain-context
name: org2-human-interaction-approval
description: Own explicit human/policy control obligations that gate or steer execution: permissions, questions, plan approvals, secret resolution, presence policy, and mode switches.
tags: [org2, domain-model, bounded-context]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# Human Interaction & Approval

## Purpose

Own explicit human/policy control obligations that gate or steer execution: permissions, questions, plan approvals, secret resolution, presence policy, and mode switches.

**Classification:** Supporting/control

The boundary is Derived. The listed source paths and entity/lifecycle facts are source-observed or UA-observed where cited by the accepted reference corpus.

## Boundary

### Owns

- Permission requests and persisted/session-scoped permission rules.
- Pending plan approvals and plan resolutions.
- Question requests/resolutions.
- Secret requests/capture lifecycle.
- Mode-switch requests/resolutions.
- Presence/auto-resolution policy for interaction obligations.

### Does not own

The action being controlled remains owned by Agent Execution or another requesting context. This context owns the obligation and resolution semantics.

## Invariants

- An execution request for control does not itself constitute approval.
- Durable pending approvals survive runtime restart where persistence exists.
- Policy may auto-resolve only according to explicit control rules.
- Secrets remain bounded control material rather than general session content.

## Consumes

- Control obligations emitted by Agent Execution.
- Workspace/policy scope.
- User or policy decisions.

## Publishes

- Approved/rejected/answered/cancelled control resolutions to Agent Execution.
- Pending-control projections to UI.

## Representative implementation paths

- `src-tauri/crates/agent-core/src/core/interaction/`
- `src-tauri/crates/agent-core/src/core/interaction/permission.rs`
- `src-tauri/crates/agent-core/src/core/interaction/plan_approval/`

## Context relationship notes

See [Entity ownership](ref-eng/domain-models/entity-ownership.md) and [Context relationships](ref-eng/domain-models/context-relationships.md) for the canonical cross-context contracts.
