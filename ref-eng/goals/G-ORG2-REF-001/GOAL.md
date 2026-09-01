---
type: goal
name: G-ORG2-REF-001
description: Create a source-grounded ORG2 implementation reference for engineers who need to understand, change, or reproduce its architecture.
tags: [org2, implementation-reference, architecture, runtime]
---

# G-ORG2-REF-001 — Explain how ORG2 works

**State:** completed  
**Confirmed by:** requester  
**Confirmed at:** 2026-08-31T04:24:33Z  
**Confirmation authority basis:** The requester selected ORG2 for the implementation-reference program and instructed the agent to pursue the goal.  
**Completed by:** agent:codex:gpt-5.6-sol  
**Completed at:** 2026-08-31T05:05:26Z  
**Completion authority basis:** G-ORG2-REF-001-VER001-RUN001, G-ORG2-REF-001-VER005-RUN001, G-ORG2-REF-001-VER006-RUN001, and G-ORG2-REF-001-VER007-RUN002 passed all current success criteria.

## Outcome

ORG2 has a practical, source-grounded implementation reference that lets an engineer understand its architecture, trace important runtime behavior, locate ownership boundaries, and reproduce focused integrations without an unguided repository search.

## Success criteria

### G-ORG2-REF-001-SC001 — Navigable and evidence-bound corpus

The corpus has one entry index, states its source revision and evidence rules, and gives clear reading paths for maintainers, integrators, and system designers.

**Verified by:**
- G-ORG2-REF-001-VER001

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-001-SC002 — Source-grounded execution slice

The first slice explains the work-item and direct-message paths into the native agent execution kernel, including session creation, prompt and context boundaries, provider streaming, tool execution, event publication, persistence, cancellation, recovery, and frontend projection.

**Verified by:**
- G-ORG2-REF-001-VER002
- G-ORG2-REF-001-VER003
- G-ORG2-REF-001-VER004
- G-ORG2-REF-001-VER005

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-001-SC003 — Sufficient architecture breadth

The corpus covers ORG2 system topology, runtime workflows, interface seams, design patterns, domain and state ownership, persistence, extension points, trust boundaries, and build or delivery choices at a depth that supports focused implementation work.

**Verified by:**
- G-ORG2-REF-001-VER006

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-001-SC004 — Current and reviewable claims

Each material claim identifies direct source or controlled runtime evidence at the governing revision, and each completed slice records contradictions, known limits, and verification status.

**Verified by:**
- G-ORG2-REF-001-VER007

**Waived by:** none  
**Supersedes:** none

## Boundaries

- Pin the initial corpus to ORG2 revision `b315ba4f82fb1fe294496793d7322095e7efe262`.
- Keep tracked ORG2 product source read-only.
- Author only under `ref-eng/`.
- Use Graphify, UA, and [the existing dossier](ref-eng/summary-1.md#org2-reference-dossier--1) to locate evidence, but use direct source or controlled execution for material behavior claims.
- Keep Graphify and UA schemas separate.
- Add documents in useful vertical slices; do not create empty directory scaffolding or speculative records.
- Describe current implementation before recommendations or redesigns.

## Dependencies

### G-ORG2-REF-001-DEP001 — G-ORG2-REINDEX-001

The completed [ORG2 reindex goal](ref-eng/goals/G-ORG2-REINDEX-001/GOAL.md#g-org2-reindex-001--reindex-org2) supplies current navigation artifacts for the accepted source revision.

**Waived by:** none

## Decisions

### G-ORG2-REF-001-DEC001 — Build one verified vertical slice at a time

**State:** accepted  
**Statement:** Start with the native agent execution path, verify that slice, and expand the corpus only after each added record has a concrete reader purpose.  
**Accepted by:** agent:codex:gpt-5.6-sol  
**Accepted at:** 2026-08-31T04:24:33Z  
**Authority basis:** The requester authorized the ORG2 implementation-reference program and asked the agent to pursue it; this sequencing choice stays within that scope and avoids speculative documentation.

**Waives:**
- none

**Supersedes:** none

### G-ORG2-REF-001-DEC002 — Freeze accepted records and use one final breadth review

**State:** accepted  
**Statement:** Keep the accepted execution slice frozen, author the four remaining reader-focused records as one bounded breadth pass, and run one final source and coverage review. Reopen a frozen record only for a material source defect or source-revision change.  
**Accepted by:** requester  
**Accepted at:** 2026-08-31T04:53:00Z  
**Authority basis:** The requester instructed the agent not to enter endless verification loops.

**Waives:**
- none

**Supersedes:** none
