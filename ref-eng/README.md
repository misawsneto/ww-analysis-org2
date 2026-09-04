---
type: implementation-reference-index
name: org2-implementation-reference
description: Entry point for the source-grounded ORG2 implementation reference.
tags: [org2, implementation-reference, architecture, runtime]
---

# ORG2 Implementation Reference

## Purpose

This corpus explains how ORG2 is organized, how its important runtime paths execute, and where an engineer must change or extend behavior.

The product source remains authoritative. These records organize direct evidence at ORG2 revision `b315ba4f82fb1fe294496793d7322095e7efe262`; they do not replace the source or define new product behavior.

## Intended outcome

An engineer who follows this corpus should be able to:

- Explain ORG2 system topology, native agent boundaries, session categories, and dependency direction.
- Trace user and work-item input through session launch, prompt construction, provider streaming, tools, events, persistence, and frontend projection.
- Identify state owners, interface contracts, extension seams, failure boundaries, and the source that owns each behavior.
- Understand the tradeoffs behind major design and persistence choices when source or controlled evidence establishes them.
- Reproduce a focused integration from documented contracts, sequence views, pseudocode, and source references.

## Evidence contract

Each material claim uses one of these states:

| State | Meaning |
| --- | --- |
| Source-observed | Current production source directly supports the claim. |
| Runtime-verified | A controlled execution supports the claim. |
| Derived | Several observed facts support the conclusion. |
| Proposed | The text describes a possible future design or improvement. |
| Unverified | Available evidence does not establish the claim. |

Use this evidence order:

1. Direct production source at the pinned revision.
2. Controlled runtime evidence at that revision.
3. Current product documentation with source confirmation.
4. Validated Graphify and UA artifacts for navigation and inventory.
5. Existing research notes for candidate claims that still need source confirmation.

Names, comments, graph edges, and generated summaries do not prove runtime behavior by themselves.

## First active slice

The first slice follows an interactive native-agent launch from the Session Creator through the backend turn loop. It includes the work-item attachment path because ORG2 carries work-item information through two separate channels:

- A composer pill expands readable work-item content into the model-facing user message.
- Structured launch fields bind the session to work management, durable run, prompt guidance, locking, and status machinery.

The current [source baseline](ref-eng/evidence/G-ORG2-REF-001-first-slice-sources.md#first-slice-source-baseline) corrects two stale claims in the earlier dossier before the technical records reuse them.

First-slice records:

1. [Native-agent execution kernel](ref-eng/architecture/native-agent-execution-kernel.md#native-agent-execution-kernel) defines the kernel boundary, major components, state ownership, construction path, and dependency direction.
2. [Native-agent execution seams](ref-eng/interfaces/native-agent-execution-seams.md#native-agent-execution-seams) defines caller-callee contracts, invariants, failure behavior, and variation points.
3. [Interactive native-agent loop](ref-eng/runtime/interactive-native-agent-loop.md#interactive-native-agent-loop) traces nominal execution and its work-item, provider, tool, approval, cancellation, retry, compaction, persistence, and settlement branches.

Breadth records:

1. [System topology](ref-eng/architecture/system-topology.md#org2-system-topology) maps system context, deployable boundaries, composition, external CLIs, extensions, trust boundaries, and delivery.
2. [Package dependencies](ref-eng/architecture/package-dependencies.md#org2-package-dependencies) explains direct Cargo dependencies, build layers, inversion points, and change impact.
3. [Core entities](ref-eng/domain-models/core-entities.md#org2-core-entities) defines agent, session, project, work, execution, event, and imported-history identities and relations.
4. [State lifecycles](ref-eng/data-and-storage/state-lifecycles.md#org2-state-lifecycles) explains state ownership, the database split, WAL, application history, projections, dispatch, and recovery.

Graph-guided depth records:

1. [Capability and execution atlas](ref-eng/architecture/capability-execution-atlas.md#org2-capability-and-execution-atlas) connects the four selected capabilities to execution, entities, state, persistence, interfaces, failure, trust, and evidence.
2. [Agent Org coordination](ref-eng/runtime/agent-org-coordination.md#agent-org-coordination) explains launch, member sessions, tasks, inbox routing, completion intent, finality, and recovery.
3. [Channel gateway routing](ref-eng/runtime/channel-gateway-routing.md#channel-gateway-routing) explains conversation binding, reinjection, shared agent dispatch, reset, and outbound delivery.
4. [External artifact import seams](ref-eng/interfaces/external-artifact-import-seams.md#external-artifact-import-seams) explains detection, fidelity, explicit apply, and native-store translation.
5. [Session event pipeline](ref-eng/data-and-storage/session-event-pipeline.md#session-event-pipeline) explains event ingestion, live and durable state, browse, search, replay, and analytics.

## Domain-model corpus

The curated [ORG2 domain model](ref-eng/domain-models/README.md) interprets the source-grounded entity inventory and accepted UA evidence as a bounded-context model. It does not modify UA/Graphify outputs and labels context classification as Derived.

Start with:

1. [Context map](ref-eng/domain-models/context-map.md) for the eight product contexts and two edge contexts.
2. [Entity ownership](ref-eng/domain-models/entity-ownership.md) for canonical semantic owners.
3. [Ubiquitous language](ref-eng/domain-models/ubiquitous-language.md) for collision rules.
4. [Context relationships](ref-eng/domain-models/context-relationships.md) for cross-context contracts.
5. [Source map](ref-eng/domain-models/source-map.md) for logical-to-physical implementation mapping.
6. [Domain classification evidence](ref-eng/evidence/G-ORG2-DOMAIN-001-context-classification.md) for why UA's five behavioral domains are not treated as exhaustive bounded contexts.

The original [Core entities](ref-eng/domain-models/core-entities.md) remains the source-observed entity inventory and evidence input.

## Corpus map

| Record | Purpose |
| --- | --- |
| [Bounded-context goal](ref-eng/goals/G-ORG2-DOMAIN-001/GOAL.md) | Records the accepted context model, boundaries, and completion evidence. |
| [Domain-model index](ref-eng/domain-models/README.md) | Entry point for contexts, edge contexts, ownership, language, relationships, and source mapping. |
| [Context map](ref-eng/domain-models/context-map.md) | Defines the logical topology and context classes. |
| [Entity ownership](ref-eng/domain-models/entity-ownership.md) | Assigns one semantic owner to canonical concepts and distinguishes projections/references. |
| [Ubiquitous language](ref-eng/domain-models/ubiquitous-language.md) | Prevents semantic collisions across work, agent teams, organizations, sessions, scopes, and capabilities. |
| [Domain source map](ref-eng/domain-models/source-map.md) | Maps logical contexts to representative implementation paths and UA coverage. |
| [Active goal](ref-eng/goals/G-ORG2-REF-002/GOAL.md#g-org2-ref-002-build-the-org2-capability-and-execution-atlas) | Defines the current graph-guided depth outcome, boundaries, and success criteria. |
| [Specification](ref-eng/goals/G-ORG2-REF-002/SPEC.md#g-org2-ref-002-spec001-capability-and-execution-atlas-requirements) | Defines the current atlas, journey, evidence, and bounded-review obligations. |
| [Plan](ref-eng/goals/G-ORG2-REF-002/PLAN.md#g-org2-ref-002-plan001-build-the-graph-guided-capability-and-execution-atlas) | Orders the scope selection, publication, and single final review. |
| [Tasks](ref-eng/goals/G-ORG2-REF-002/TASKS.md#tasks-g-org2-ref-002) | Tracks the graph-guided selection and technical publication work. |
| [Coverage matrix](ref-eng/evidence/G-ORG2-REF-002-graph-coverage.md#graph-guided-coverage-for-the-org2-capability-atlas) | Records UA and Graphify evidence, duplicate rejection, and the four selected journeys. |
| [Source baseline](ref-eng/evidence/G-ORG2-REF-001-first-slice-sources.md#first-slice-source-baseline) | Pins the current launch path, source owners, contradictions, and unverified limits. |
| [Capability and execution atlas](ref-eng/architecture/capability-execution-atlas.md#org2-capability-and-execution-atlas) | Maps selected capabilities across entry points, components, entities, state, persistence, interfaces, failures, and evidence. |
| [Agent Org coordination](ref-eng/runtime/agent-org-coordination.md#agent-org-coordination) | Traces coordinated run launch, member materialization, task and inbox flow, finality, and recovery. |
| [Channel gateway routing](ref-eng/runtime/channel-gateway-routing.md#channel-gateway-routing) | Traces external chat binding, reinjection, shared session execution, reset, and delivery. |
| [External artifact import seams](ref-eng/interfaces/external-artifact-import-seams.md#external-artifact-import-seams) | Defines foreign artifact detection, fidelity warnings, apply routes, trust, and persistence ownership. |
| [Session event pipeline](ref-eng/data-and-storage/session-event-pipeline.md#session-event-pipeline) | Defines activity ingestion, canonical events, live/durable stores, search, replay, and analytics. |
| [Native-agent execution kernel](ref-eng/architecture/native-agent-execution-kernel.md#native-agent-execution-kernel) | Defines the first slice's architecture, state ownership, construction path, collaborations, invariants, and tradeoffs. |
| [Native-agent execution seams](ref-eng/interfaces/native-agent-execution-seams.md#native-agent-execution-seams) | Defines the first slice's caller-callee contracts, invariants, failure behavior, and variation points. |
| [Interactive native-agent loop](ref-eng/runtime/interactive-native-agent-loop.md#interactive-native-agent-loop) | Traces launch, queueing, prompt construction, provider/tools, cancellation, recovery, persistence, and settlement. |
| [System topology](ref-eng/architecture/system-topology.md#org2-system-topology) | Maps system context, deployment shape, composition roots, integrations, extension seams, trust boundaries, and delivery. |
| [Package dependencies](ref-eng/architecture/package-dependencies.md#org2-package-dependencies) | Defines direct package direction, inversion points, build order, and change impact. |
| [Core entities](ref-eng/domain-models/core-entities.md#org2-core-entities) | Defines domain identities, ownership, relations, events, and cross-tool history entities. |
| [State lifecycles](ref-eng/data-and-storage/state-lifecycles.md#org2-state-lifecycles) | Defines live and durable state, SQLite/WAL roles, projections, dispatch, recovery, and persistence limits. |
| [Existing dossier](ref-eng/summary-1.md#org2-reference-dossier-1) | Preserves earlier discovery findings; current source must confirm each claim before reuse. |
| [Completed reindex goal](ref-eng/goals/G-ORG2-REINDEX-001/GOAL.md#g-org2-reindex-001-reindex-org2) | Records the current Graphify and UA index state. |

## Reading paths

### Maintainer

Read the active goal, system topology, package dependencies, the relevant domain or state record, and the first-slice record that owns the planned change.

Use the capability atlas to find the focused journey and its direct source path before broad source navigation.

### Integrator

Read the system topology, capability atlas, source baseline, interface seams, state failure boundaries, and the focused extension record that applies to the integration.

### System designer

Read the domain-model index and context map first, then system topology, package dependencies, capability atlas, core entities, state lifecycles, the execution kernel, and known limits together before comparing designs.

## Current state

[G-ORG2-REF-001](ref-eng/goals/G-ORG2-REF-001/GOAL.md#g-org2-ref-001-explain-how-org2-works), [G-ORG2-REF-002](ref-eng/goals/G-ORG2-REF-002/GOAL.md#g-org2-ref-002-build-the-org2-capability-and-execution-atlas), and [G-ORG2-DOMAIN-001](ref-eng/goals/G-ORG2-DOMAIN-001/GOAL.md) are complete. The corpus includes the frozen first slice, breadth records, four graph-selected journeys, one connector atlas, and the curated bounded-context model at the pinned revision.

The completed Graphify and UA indexes support navigation at the pinned revision. Their schemas remain separate, and their semantic summaries do not replace direct source evidence.

## Update rule

Before changing a source-grounded record, compare its declared revision with ORG2 `HEAD`. Refresh affected evidence when the revision changes, preserve contradictions and known limits, and never turn an assumption into an observed fact through repetition.
