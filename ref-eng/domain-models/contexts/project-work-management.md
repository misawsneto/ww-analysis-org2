---
type: domain-context
name: org2-project-work-management
description: Own durable project and work identities, work lifecycle, execution linkage, handoff, routines, review/proof-of-work, team inbox, and synchronization semantics.
tags: [org2, domain-model, bounded-context]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# Project & Work Management

## Purpose

Own durable project and work identities, work lifecycle, execution linkage, handoff, routines, review/proof-of-work, team inbox, and synchronization semantics.

**Classification:** Core

The boundary is Derived. The listed source paths and entity/lifecycle facts are source-observed or UA-observed where cited by the accepted reference corpus.

## Boundary

### Owns

- `ProjectOrg` and Project.
- Work Item aggregate and nested work lifecycle state.
- `WorkItemRun` execution attempt identity.
- Work Item execution locks and handoff.
- Routine and Routine Fire.
- Work-management Team Inbox.
- Project/work synchronization and lineage state where implemented in the project-management subsystem.

### Does not own

Git branches/worktrees are infrastructure used by work execution, not Work Management entities. `OrgTask` belongs to Agent Team Coordination.

## Invariants

- A Project Org is distinct from Agent Org and Cloud Org.
- Work Item identity persists independently of any Agent Session.
- Execution links and proof of work reference execution/provenance; they do not transfer work ownership.
- Run/handoff/lock state belongs to the work lifecycle.

## Consumes

- Repository/workspace references.
- Agent Execution for automated execution.
- Trajectory & Provenance for evidence/history references.
- Collaboration & Sharing for cloud org/project synchronization.

## Publishes

- Work execution request/binding to Agent Execution.
- Work/run status, metadata, and linkage to UI/collaboration.
- Proof-of-work references to provenance consumers.

## Representative implementation paths

- `src-tauri/crates/project-management/`

## Context relationship notes

See [Entity ownership](ref-eng/domain-models/entity-ownership.md) and [Context relationships](ref-eng/domain-models/context-relationships.md) for the canonical cross-context contracts.
