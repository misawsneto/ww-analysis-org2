---
type: goal
name: G-ORG2-REF-002
description: Build a graph-guided ORG2 capability and execution atlas from the accepted UA and Graphify indexes.
tags: [org2, implementation-reference, architecture, ua, graphify]
---

# G-ORG2-REF-002 — Build the ORG2 capability and execution atlas

**State:** completed  
**Confirmed by:** requester  
**Confirmed at:** 2026-08-31T14:40:46Z  
**Confirmation authority basis:** The requester approved the proposed scoped work and instructed the agent to persist it.  
**Completed by:** agent:codex:gpt-5.6-sol  
**Completed at:** 2026-08-31T16:09:55Z  
**Completion authority basis:** G-ORG2-REF-002-VER001-RUN001 passed graph-guided scope, and the authorized corrective G-ORG2-REF-002-VER002-RUN002 passed the published technical corpus after RUN001 exposed one link defect.

## Outcome

ORG2 has a graph-guided capability and execution atlas that connects semantic domains, structural dependencies, runtime journeys, domain entities, state ownership, persistence, extension points, and source evidence without repeating the completed architecture overview.

## Success criteria

### G-ORG2-REF-002-SC001 — Graph-guided scope

The analysis reuses the accepted UA knowledge graph and domain graph as its semantic navigation layer, uses Graphify for structural traversal, and identifies documentation gaps before it reads source in depth.

**Verified by:**
- G-ORG2-REF-002-VER001

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-002-SC002 — Capability and execution atlas

The atlas maps important ORG2 capabilities to components, domain entities, state owners, persistence boundaries, runtime transitions, external interfaces, and focused evidence paths.

**Verified by:**
- G-ORG2-REF-002-VER002

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-002-SC003 — Focused runtime depth

The corpus adds source-grounded journey records only for material gaps, including user-to-harness-to-agent interaction and the state, persistence, event, extension, trust, and failure behavior relevant to each selected journey.

**Verified by:**
- G-ORG2-REF-002-VER002

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REF-002-SC004 — Bounded and reviewable proof

Each published behavioral claim resolves to direct source at the accepted revision, and the work uses one scope verification and one final review without repeated verification loops.

**Verified by:**
- G-ORG2-REF-002-VER001
- G-ORG2-REF-002-VER002

**Waived by:** none  
**Supersedes:** none

## Boundaries

- Pin the work to ORG2 revision `b315ba4f82fb1fe294496793d7322095e7efe262` and the accepted artifacts from G-ORG2-REINDEX-001.
- Keep tracked ORG2 product source read-only and author only under `ref-eng/`.
- Start from [the existing reference index](ref-eng/README.md#org2-engineering-reference) and add only information that it does not explain at useful depth.
- Use `.understand-anything/knowledge-graph.json` and `.understand-anything/domain-graph.json` as the primary semantic navigation layer.
- Use `graphify-out/graph.json` for deterministic dependencies, calls, references, communities, hubs, and paths.
- Keep UA and Graphify schemas separate and relate their evidence only through source paths or documentation matrices.
- Treat direct source as the authority for behavioral claims; generated graph summaries guide navigation and coverage.
- Do not regenerate either graph unless its recorded source revision is stale.
- Select no more than four focused capability journeys in this goal.
- Run only the two declared Verifications unless a material source contradiction or revision change requires a new Decision.

## Dependencies

### G-ORG2-REF-002-DEP001 — G-ORG2-REF-001

The completed [ORG2 implementation-reference goal](ref-eng/goals/G-ORG2-REF-001/GOAL.md#g-org2-ref-001--explain-how-org2-works) supplies the accepted corpus and defines what this goal must not duplicate.

**Waived by:** none

### G-ORG2-REF-002-DEP002 — G-ORG2-REINDEX-001

The completed [ORG2 reindex goal](ref-eng/goals/G-ORG2-REINDEX-001/GOAL.md#g-org2-reindex-001--reindex-org2) supplies the accepted UA and Graphify snapshots for the pinned revision.

**Waived by:** none

## Decisions

### G-ORG2-REF-002-DEC001 — Use UA as the semantic navigation layer

**State:** accepted  
**Statement:** Reuse the accepted UA knowledge graph and domain graph for contextualization, semantic coverage selection, and traversal across this goal. Use Graphify for deterministic structural traversal. Confirm every published behavioral claim against direct source.  
**Accepted by:** requester  
**Accepted at:** 2026-08-31T14:40:46Z  
**Authority basis:** The requester required UA and Graphify, especially UA, to appear explicitly in relevant goals and tasks.

**Waives:**
- none

**Supersedes:** none

### G-ORG2-REF-002-DEC002 — Limit verification to two declared passes

**State:** accepted  
**Statement:** Run one bounded scope verification after graph-guided gap analysis and one bounded final review after publication. Do not repeat either pass without a material contradiction or source-revision change.  
**Accepted by:** requester  
**Accepted at:** 2026-08-31T14:40:46Z  
**Authority basis:** The requester instructed the agent not to enter endless verification loops.

**Waives:**
- none

**Supersedes:** none

### G-ORG2-REF-002-DEC003 — Refine the technical corpus instead of treating new files as the target

**State:** accepted  
**Statement:** Use UA to guide semantic coverage and code navigation, then evolve the architecture, domain-model, data, interface, seam, and runtime documentation under `ref-eng/`. Update an existing technical record when source-confirmed information deepens or corrects its subject; create a new record only when no current document owns the subject.  
**Accepted by:** requester  
**Accepted at:** 2026-08-31T15:34:57Z  
**Authority basis:** The requester clarified that refined ORG2 technical documentation is the target and that UA is the semantic navigation mechanism, not the deliverable.

**Waives:**
- none

**Supersedes:** none

### G-ORG2-REF-002-DEC004 — Permit one link-only corrective review

**State:** accepted  
**Statement:** Correct the broken local heading links found by G-ORG2-REF-002-VER002-RUN001, replace the temporary slug emulation with `ctxq` heading identities, and execute one delta review of links, revision, and changed subject hashes. Reuse RUN001's passed source samples and do not repeat the full content review.  
**Accepted by:** agent:codex:gpt-5.6-sol  
**Accepted at:** 2026-08-31T16:07:09Z  
**Authority basis:** The active Task authorizes publication corrections, V002 permits another Run after an accepted Decision records a material reason, and a single delta check preserves the requester's no-loop constraint.

**Waives:**
- The one-Run limit in G-ORG2-REF-002-SPEC001-REQ008 only for one corrective V002 delta Run.

**Supersedes:** none
