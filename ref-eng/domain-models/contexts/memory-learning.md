---
type: domain-context
name: org2-memory-learning
description: Preserve workspace-scoped memory and evolve structured learnings across executions through extraction, recall, reinforcement, consolidation, merge, deprecation, and reactivation.
tags: [org2, domain-model, bounded-context]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# Memory & Learning

## Purpose

Preserve workspace-scoped memory and evolve structured learnings across executions through extraction, recall, reinforcement, consolidation, merge, deprecation, and reactivation.

**Classification:** Core

The boundary is Derived. The listed source paths and entity/lifecycle facts are source-observed or UA-observed where cited by the accepted reference corpus.

## Boundary

### Owns

- Workspace memory entries/index/surface state.
- `Learning` records.
- Learning category, status, source, and evolution semantics.
- Consolidation triggers/runs and learning evolution state.

### Does not own

Trajectory & Provenance owns historical execution evidence. Memory & Learning owns durable knowledge selected/evolved from experience. They are not the same store or lifecycle.

## Invariants

- Memory has a lifecycle independent of session transcript retention.
- Surfacing tracks what has already been injected into a session to avoid uncontrolled repetition.
- Learning status distinguishes pending, active, merged, deprecated, and abandoned states.
- Consolidation/extraction produces durable knowledge rather than mutating live session identity.

## Consumes

- Execution experience/transcript signals.
- Workspace scope.
- Built-in or configured memory extractor/consolidator agents.

## Publishes

- Relevant recalled memory/learnings to Agent Execution.
- Memory status and management projections to UI.

## Representative implementation paths

- `src-tauri/crates/agent-core/src/specialization/memory/`
- `src-tauri/crates/agent-core/src/specialization/memory/learnings/types.rs`
- `src-tauri/crates/agent-core/src/specialization/memory/workspace_memory/`
- `src-tauri/crates/agent-core/src/core/definitions/builtin/memory_extractor.rs`
- `src-tauri/crates/agent-core/src/core/definitions/builtin/memory_consolidator.rs`

## Context relationship notes

See [Entity ownership](ref-eng/domain-models/entity-ownership.md) and [Context relationships](ref-eng/domain-models/context-relationships.md) for the canonical cross-context contracts.
