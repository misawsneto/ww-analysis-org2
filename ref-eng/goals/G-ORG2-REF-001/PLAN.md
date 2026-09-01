---
type: plan
name: G-ORG2-REF-001-PLAN001
description: Incremental plan for the ORG2 implementation-reference corpus.
tags: [org2, implementation-reference, plan]
---

# G-ORG2-REF-001-PLAN001 — Build the ORG2 implementation reference

**Goal:** G-ORG2-REF-001  
**Version:** 1  
**State:** active  
**Supersedes:** none

## Strategy

Build one reader-useful vertical slice at a time. Use current Graphify, UA, and the existing dossier to select candidate paths, trace claims to direct source, write the architecture, interface, and runtime views together, and verify the slice before broadening the corpus.

## Sequence

- G-ORG2-REF-001-TASK001
- G-ORG2-REF-001-TASK002
- G-ORG2-REF-001-TASK003
- G-ORG2-REF-001-TASK004
- G-ORG2-REF-001-TASK005
- G-ORG2-REF-001-TASK006

## Checkpoints

### G-ORG2-REF-001-PLAN001-CHK001 — Evidence baseline accepted

**Waived by:** none

#### Conditions

##### G-ORG2-REF-001-PLAN001-CHK001-CND001 — The index and first-slice evidence manifest identify the pinned revision, claim states, source precedence, and known stale findings

**Kind:** deterministic  
**Verification:** G-ORG2-REF-001-VER001  
**Waived by:** none

### G-ORG2-REF-001-PLAN001-CHK002 — First vertical slice accepted

**Waived by:** none

#### Conditions

##### G-ORG2-REF-001-PLAN001-CHK002-CND001 — Architecture, interface, and runtime records agree on the same current execution path

**Kind:** deterministic  
**Verification:** G-ORG2-REF-001-VER005  
**Waived by:** none

##### G-ORG2-REF-001-PLAN001-CHK002-CND002 — A source-grounded review finds no unresolved required contradiction in the first slice

**Kind:** judgment  
**Verification:** G-ORG2-REF-001-VER007  
**Waived by:** none

### G-ORG2-REF-001-PLAN001-CHK003 — Corpus breadth accepted

**Waived by:** none

#### Conditions

##### G-ORG2-REF-001-PLAN001-CHK003-CND001 — The corpus covers all areas required by G-ORG2-REF-001-SPEC001-REQ005 at useful implementation depth

**Kind:** judgment  
**Verification:** G-ORG2-REF-001-VER006  
**Waived by:** none

## Risks

- Existing notes can describe an earlier ORG2 path; mitigate this by tracing every material claim at the pinned revision before reuse.
- Generated semantic summaries can sound precise while remaining generic; use them only to locate direct source.
- ORG2 has several session categories and launch routes; name the route and category for each claim instead of generalizing across all sessions.
- Broad documentation can become shallow; complete and verify one vertical slice before adding new areas.

## Stop conditions

- Stop a claim when direct source contradicts the dossier or product documentation; record the contradiction and follow current source.
- Stop a slice when its source revision differs from the goal revision; refresh the evidence baseline before authoring.
- Stop before any tracked product-source mutation.

## Rollback

- Remove only new files created under `ref-eng/goals/G-ORG2-REF-001/` and new corpus records if the requester cancels this goal before accepting them.
- Preserve the completed reindex goal, generated indexes, existing dossier, and all tracked ORG2 source.
