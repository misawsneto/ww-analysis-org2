---
type: domain-context
name: org2-trajectory-provenance
description: Own canonical historical and provenance semantics across native and external agent execution: sessions, activities, edits/diffs, file changes, checkpoints, usage, replay/search/analytics, and observational projections.
tags: [org2, domain-model, bounded-context]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# Trajectory & Provenance

## Purpose

Own canonical historical and provenance semantics across native and external agent execution: sessions, activities, edits/diffs, file changes, checkpoints, usage, replay/search/analytics, and observational projections.

**Classification:** Core

The boundary is Derived. The listed source paths and entity/lifecycle facts are source-observed or UA-observed where cited by the accepted reference corpus.

## Boundary

### Owns

- Canonical `SessionRecord` and related activity/provenance records.
- File change, edit artifact, diff, checkpoint, and usage records.
- Native normalized `SessionEvent` semantics.
- Rebuildable turn indexes, search results, and statistics as projections over canonical history.

### Does not own

The existing Session Event Pipeline is an ingestion/read subsystem within this broader context. Agent Execution owns live sessions; Memory & Learning owns durable learned knowledge.

## Invariants

- Raw streaming deltas are consolidated before canonical native event storage.
- Observational records do not own live Agent Session execution state.
- Cross-tool source adapters normalize foreign histories into canonical provenance records.
- Read indexes/projections remain rebuildable and cannot become the owner of raw identity.

## Consumes

- Native execution activity.
- External coding-agent histories.
- Repository/file context.
- Optional work/session references.

## Publishes

- History, replay, search, analytics, blame/diff/provenance views.
- Evidence references usable by Project & Work Management and Collaboration & Sharing.

## Representative implementation paths

- `src-tauri/crates/orgtrack-core/`
- `src-tauri/crates/orgtrack-core/src/canonical.rs`
- `src-tauri/src/agent_sessions/event_pipeline/`

## Context relationship notes

See [Entity ownership](ref-eng/domain-models/entity-ownership.md) and [Context relationships](ref-eng/domain-models/context-relationships.md) for the canonical cross-context contracts.
