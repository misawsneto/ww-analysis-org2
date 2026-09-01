---
type: plan
name: G-ORG2-REF-002-PLAN001
description: Bounded plan for the graph-guided ORG2 capability and execution atlas.
tags: [org2, implementation-reference, plan, ua, graphify]
---

# G-ORG2-REF-002-PLAN001 — Build the graph-guided capability and execution atlas

**Goal:** G-ORG2-REF-002  
**Version:** 1  
**State:** active  
**Supersedes:** none

## Strategy

Start from the accepted UA domain and knowledge graphs, then subtract coverage already present in `ref-eng/`. Use Graphify only on the selected semantic paths to expose structural dependencies and boundary crossings. Read direct source along those bounded paths, publish the atlas and focused journey records, and execute each declared Verification once. G-ORG2-REF-002-TASK001 exits only after an authorized Actor executes G-ORG2-REF-002-VER001 against its exact subjects and creates a current passing Run. G-ORG2-REF-002-TASK002 exits only after an authorized Actor executes G-ORG2-REF-002-VER002 against its exact subjects and creates a current passing Run.

## Sequence

- G-ORG2-REF-002-TASK001
- G-ORG2-REF-002-TASK002

## Checkpoints

### G-ORG2-REF-002-PLAN001-CHK001 — Graph-guided scope accepted

**Waived by:** none

#### Conditions

##### G-ORG2-REF-002-PLAN001-CHK001-CND001 — The coverage matrix proves accepted snapshot reuse, separates UA and Graphify evidence, identifies existing coverage, and selects no more than four material gaps

**Kind:** judgment  
**Verification:** G-ORG2-REF-002-VER001  
**Waived by:** none

### G-ORG2-REF-002-PLAN001-CHK002 — Capability and execution atlas accepted

**Waived by:** none

#### Conditions

##### G-ORG2-REF-002-PLAN001-CHK002-CND001 — The atlas and focused records satisfy the active requirements and contain no unresolved required source contradiction

**Kind:** judgment  
**Verification:** G-ORG2-REF-002-VER002  
**Waived by:** none

## Risks

- UA summaries can sound authoritative; mitigate this by using UA for semantic navigation and direct source for behavioral claims.
- Graphify can expose high-degree paths that lack product meaning; retain only paths that clarify a selected UA-guided capability.
- The prior corpus already covers broad architecture; reject topics that add wording but no new implementation depth.
- A broad journey list can dilute depth; cap the selected set at four and prefer fewer when the evidence warrants it.

## Stop conditions

- Stop before analysis if the ORG2 source revision differs from the accepted graph revision.
- Stop a claim when UA, Graphify, and direct source disagree; record the conflict and use direct source before publication.
- Stop a proposed journey when the existing corpus already explains it at implementation-useful depth.
- Stop before any tracked product-source change or graph regeneration.
- Stop after each declared Verification Run; do not repeat it without a material contradiction, revision change, or accepted Decision.

## Rollback

- Remove only incomplete files created for G-ORG2-REF-002 if the requester cancels the active goal.
- Preserve the accepted G-ORG2-REF-001 corpus, G-ORG2-REINDEX-001 records, UA artifacts, Graphify artifacts, and tracked ORG2 source.
