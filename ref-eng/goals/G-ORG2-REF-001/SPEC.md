---
type: specification
name: G-ORG2-REF-001-SPEC001
description: Requirements for the ORG2 implementation-reference corpus.
tags: [org2, implementation-reference, requirements]
---

# G-ORG2-REF-001-SPEC001 — ORG2 implementation-reference requirements

**Goal:** G-ORG2-REF-001  
**Version:** 1  
**State:** active  
**Supersedes:** none

## Requirements

### G-ORG2-REF-001-SPEC001-REQ001 — Evidence contract

Each technical record declares the governing source revision and labels material claims as source-observed, runtime-verified, derived, proposed, or unverified.

**Verified by:**
- G-ORG2-REF-001-VER001

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-001-SPEC001-REQ002 — Execution-kernel architecture

The first slice identifies the native agent kernel boundary, major collaborators, state owners, dependency direction, and the relationship between frontend session launch and backend execution.

**Verified by:**
- G-ORG2-REF-001-VER002

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-001-SPEC001-REQ003 — Interface and context seams

The first slice identifies callers, callees, inputs, outputs, invariants, failure behavior, and extension or interception points across the session launch, prompt, provider, tool, event, and persistence seams.

**Verified by:**
- G-ORG2-REF-001-VER003

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-001-SPEC001-REQ004 — Runtime branches

The first slice traces nominal execution plus work-item context, queueing, provider failure, tool calls, approval, cancellation, retry, compaction, persistence, and settlement branches where current source supports them.

**Verified by:**
- G-ORG2-REF-001-VER004

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-001-SPEC001-REQ005 — Corpus breadth

Later slices cover system topology, domain and state ownership, data and storage, cross-tool ingestion, external CLI integration, extension mechanisms, design patterns, trust boundaries, and build or delivery choices.

**Verified by:**
- G-ORG2-REF-001-VER006

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-001-SPEC001-REQ006 — Reproducible source trace

Each completed slice includes focused source references, concise pseudocode or diagrams where sequence or topology matters, known limits, and enough contract detail to support a focused implementation or integration.

**Verified by:**
- G-ORG2-REF-001-VER007

**Waived by:** none  
**Supersedes:** none

## Interfaces

- `ref-eng/README.md` is the corpus entry point and reading map.
- `architecture/` owns component, dependency, and state-ownership views.
- `interfaces/` owns caller-callee contracts and extension seams.
- `runtime/` owns end-to-end control flow, branches, and recovery behavior.
- `domain-models/`, `data-and-storage/`, `design-patterns/`, `technology/`, and `evidence/` are added only when a completed task produces a useful record for that concern.
- Source links use repository-root-relative paths and section anchors for Markdown sources; code references include paths and stable symbol names or line locators.

## Boundaries

- The corpus explains ORG2 as implemented at the pinned revision; it does not define product requirements.
- Generated Graphify and UA data can identify candidate paths and relationships, but it cannot establish runtime behavior.
- Existing product documentation is navigation evidence unless direct production source or controlled execution confirms the claim.
- Small code excerpts may demonstrate a contract, but the corpus does not copy large source blocks.
- Recommendations remain separate from current-state claims.
