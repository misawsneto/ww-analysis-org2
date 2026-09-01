---
type: specification
name: G-ORG2-REF-002-SPEC001
description: Requirements for the graph-guided ORG2 capability and execution atlas.
tags: [org2, implementation-reference, requirements, ua, graphify]
---

# G-ORG2-REF-002-SPEC001 — Capability and execution atlas requirements

**Goal:** G-ORG2-REF-002  
**Version:** 1  
**State:** active  
**Supersedes:** none

## Requirements

### G-ORG2-REF-002-SPEC001-REQ001 — UA-first contextualization

The analysis uses the accepted UA knowledge graph and domain graph to select semantic domains, architecture layers, candidate journeys, and source paths before any broad source traversal.

**Verified by:**
- G-ORG2-REF-002-VER001

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-002-SPEC001-REQ002 — Graphify structural traversal

The analysis uses Graphify to identify deterministic dependency, call, reference, hub, community, and cross-boundary paths that clarify each selected semantic journey.

**Verified by:**
- G-ORG2-REF-002-VER001

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-002-SPEC001-REQ003 — Accepted snapshot reuse

The work records the accepted source revision and graph artifact paths, reuses the accepted snapshots, and stops before analysis if their revision no longer matches the goal revision.

**Verified by:**
- G-ORG2-REF-002-VER001

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-002-SPEC001-REQ004 — Coverage-gap selection

A coverage matrix compares UA domains and candidate journeys with the existing `ref-eng/` corpus, identifies duplicate and missing coverage, and selects no more than four material journeys for deeper work.

**Verified by:**
- G-ORG2-REF-002-VER001

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-002-SPEC001-REQ005 — Capability mapping

The atlas maps each selected capability to its user entry point, frontend and Tauri boundary, Rust owners, domain entities, state transitions, persistence, tools or external systems, failure paths, and source evidence where applicable.

**Verified by:**
- G-ORG2-REF-002-VER002

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-002-SPEC001-REQ006 — Focused journey records

Each selected material gap has a focused record that explains control flow, data flow, user-harness-agent interaction, persistence or event behavior, extension points, trust boundaries, and implementation-specific tradeoffs supported by current source.

**Verified by:**
- G-ORG2-REF-002-VER002

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-002-SPEC001-REQ007 — Source authority

UA and Graphify guide navigation and coverage, while every material behavioral claim cites direct source at the accepted revision and labels derived or unresolved conclusions.

**Verified by:**
- G-ORG2-REF-002-VER002

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-002-SPEC001-REQ008 — Bounded verification

The work executes G-ORG2-REF-002-VER001 once after scope selection and G-ORG2-REF-002-VER002 once after publication, unless an accepted Decision records a material reason for another Run.

**Verified by:**
- G-ORG2-REF-002-VER002

**Waived by:** none  
**Supersedes:** none

## Interfaces

- `ref-eng/evidence/G-ORG2-REF-002-graph-coverage.md` records graph versions, UA-guided semantic coverage, Graphify structural coverage, existing-document coverage, selected gaps, and rejected duplicate topics.
- `ref-eng/architecture/capability-execution-atlas.md` is the main capability-to-component-to-entity-to-state-to-evidence map.
- Focused records live under the existing `ref-eng/architecture/`, `ref-eng/domain-models/`, `ref-eng/data-and-storage/`, `ref-eng/interfaces/`, or `ref-eng/runtime/` owner for the subject selected by the coverage matrix.
- Existing technical records can receive source-confirmed refinements when they own the selected subject; the work does not create a parallel document only to preserve the old file unchanged.
- [The reference index](ref-eng/README.md#org2-engineering-reference) links the accepted atlas and focused records after publication.
- Source references use repository-root-relative paths and stable symbols or focused line locators.

## Boundaries

- This Specification deepens the current implementation reference; it does not redesign ORG2 or define new product requirements.
- It does not merge, normalize, or copy UA and Graphify graph schemas into a combined graph.
- It does not repeat the existing C3/C4 topology, package map, core entity inventory, or state-lifecycle overview unless a focused journey needs a concise link to them.
- It does not require full-repository source traversal after the graphs and existing corpus establish a narrow path.
- It does not require runtime execution unless source evidence cannot resolve a material behavior claim.
