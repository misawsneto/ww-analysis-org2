---
type: task-register
name: G-ORG2-REF-001-TASKS
description: Ordered tasks for the ORG2 implementation-reference corpus.
tags: [org2, implementation-reference, tasks]
---

# Tasks — G-ORG2-REF-001

## G-ORG2-REF-001-TASK001 — Establish the corpus and current execution trace

**State:** completed  
**Type:** investigation  
**Waived by:** none  
**Blocked by:** none  
**Started by:** agent:codex:gpt-5.6-sol  
**Started at:** 2026-08-31T04:24:33Z  
**Completed by:** agent:codex:gpt-5.6-sol  
**Completed at:** 2026-08-31T04:31:46Z  
**Authority basis:** The requester selected ORG2 and instructed the agent to pursue the implementation-reference goal.

Create the corpus index and a bounded evidence baseline for the native session launch and execution path at the pinned revision. Resolve conflicts between current source and the existing dossier before later records depend on them.

### Requirements

- G-ORG2-REF-001-SPEC001-REQ001
- G-ORG2-REF-001-SPEC001-REQ006

### Acceptance criteria

#### G-ORG2-REF-001-TASK001-AC001 — The corpus index declares purpose, revision, evidence rules, scope, current slice, and reading paths

**Verified by:**
- G-ORG2-REF-001-VER001

**Waived by:** none  
**Supersedes:** none

#### G-ORG2-REF-001-TASK001-AC002 — The evidence baseline identifies the current source path and records stale or contradicted dossier claims

**Verified by:**
- G-ORG2-REF-001-VER001

**Waived by:** none  
**Supersedes:** none

### Verifications

- G-ORG2-REF-001-VER001

### Outcome

#### G-ORG2-REF-001-TASK001-OUT001

**Kind:** investigation_result  
**Statement:** The corpus index and source baseline now pin the first slice to the accepted revision. They replace the stale prompt-builder route with the current Session Creator launch path and distinguish readable work-item context, structured durable-run metadata, and turn-time linked-item prompt guidance.  
**Produced by:** agent:codex:gpt-5.6-sol  
**Produced at:** 2026-08-31T04:31:46Z  
**Authority basis:** The requester authorized the ORG2 implementation-reference program.

**Resolves:**
- none

**Supports:**
- G-ORG2-REF-001-SC001
- G-ORG2-REF-001-SPEC001-REQ001
- G-ORG2-REF-001-SPEC001-REQ006

**Evidence:**
- `ref-eng/evidence/G-ORG2-REF-001-first-slice-sources.md`
- G-ORG2-REF-001-VER001-RUN001

## G-ORG2-REF-001-TASK002 — Explain the native execution kernel

**State:** completed  
**Type:** research  
**Waived by:** none  
**Blocked by:** none  
**Started by:** agent:codex:gpt-5.6-sol  
**Started at:** 2026-08-31T04:31:46Z  
**Completed by:** agent:codex:gpt-5.6-sol  
**Completed at:** 2026-08-31T04:38:49Z  
**Authority basis:** G-ORG2-REF-001-VER001-RUN001 passed the first checkpoint, and the requester authorized continued pursuit of the goal.

Document the native kernel boundary, component responsibilities, state ownership, dependency direction, and frontend-to-backend launch path.

### Dependencies

- G-ORG2-REF-001-TASK001

### Requirements

- G-ORG2-REF-001-SPEC001-REQ002
- G-ORG2-REF-001-SPEC001-REQ006

### Acceptance criteria

#### G-ORG2-REF-001-TASK002-AC001 — The architecture record identifies concrete owning files and symbols for each material component and state boundary

**Verified by:**
- G-ORG2-REF-001-VER002

**Waived by:** none  
**Supersedes:** none

### Verifications

- G-ORG2-REF-001-VER002

### Outcome

#### G-ORG2-REF-001-TASK002-OUT001

**Kind:** investigation_result  
**Statement:** The architecture record now defines the native execution-kernel boundary, containers, state owners, construction path, principal collaborations, work-item context channels, invariants, tradeoffs, and limits at the pinned revision.  
**Produced by:** agent:codex:gpt-5.6-sol  
**Produced at:** 2026-08-31T04:38:49Z  
**Authority basis:** The requester authorized the ORG2 implementation-reference program.

**Resolves:**
- none

**Supports:**
- G-ORG2-REF-001-SPEC001-REQ002

**Evidence:**
- `ref-eng/architecture/native-agent-execution-kernel.md`
- G-ORG2-REF-001-VER002-RUN001

## G-ORG2-REF-001-TASK003 — Define execution seams and contracts

**State:** completed  
**Type:** research  
**Waived by:** none  
**Blocked by:** none  
**Started by:** agent:codex:gpt-5.6-sol  
**Started at:** 2026-08-31T04:38:49Z  
**Completed by:** agent:codex:gpt-5.6-sol  
**Completed at:** 2026-08-31T04:44:48Z  
**Authority basis:** G-ORG2-REF-001-VER002-RUN001 passed the architecture-record gate, and the requester authorized continued pursuit of the goal.

Document the session launch, prompt/context, provider, tool, event, persistence, and frontend projection contracts.

### Dependencies

- G-ORG2-REF-001-TASK002

### Requirements

- G-ORG2-REF-001-SPEC001-REQ003
- G-ORG2-REF-001-SPEC001-REQ006

### Acceptance criteria

#### G-ORG2-REF-001-TASK003-AC001 — Each seam names caller, callee, input, output, invariant, failure behavior, and extension or interception point where one exists

**Verified by:**
- G-ORG2-REF-001-VER003

**Waived by:** none  
**Supersedes:** none

### Verifications

- G-ORG2-REF-001-VER003

### Outcome

#### G-ORG2-REF-001-TASK003-OUT001

**Kind:** investigation_result  
**Statement:** The interface record now defines eleven source-grounded contracts from composer projection through frontend settlement, with explicit invariants, failure behavior, and supported variation points.  
**Produced by:** agent:codex:gpt-5.6-sol  
**Produced at:** 2026-08-31T04:44:48Z  
**Authority basis:** The requester authorized the ORG2 implementation-reference program.

**Resolves:**
- none

**Supports:**
- G-ORG2-REF-001-SPEC001-REQ003

**Evidence:**
- `ref-eng/interfaces/native-agent-execution-seams.md`
- G-ORG2-REF-001-VER003-RUN001

## G-ORG2-REF-001-TASK004 — Trace the interactive runtime

**State:** completed  
**Type:** research  
**Waived by:** none  
**Blocked by:** none  
**Started by:** agent:codex:gpt-5.6-sol  
**Started at:** 2026-08-31T04:44:48Z  
**Completed by:** agent:codex:gpt-5.6-sol  
**Completed at:** 2026-08-31T04:48:51Z  
**Authority basis:** G-ORG2-REF-001-VER003-RUN001 passed the interface-seam gate, and the requester authorized continued pursuit of the goal.

Trace nominal execution and the supported queue, work-item context, provider, tool, approval, cancellation, retry, compaction, persistence, and settlement branches.

### Dependencies

- G-ORG2-REF-001-TASK003

### Requirements

- G-ORG2-REF-001-SPEC001-REQ004
- G-ORG2-REF-001-SPEC001-REQ006

### Acceptance criteria

#### G-ORG2-REF-001-TASK004-AC001 — The runtime record includes a sequence view, labeled pseudocode, state transitions, failure paths, invariants, and source references

**Verified by:**
- G-ORG2-REF-001-VER004

**Waived by:** none  
**Supersedes:** none

### Verifications

- G-ORG2-REF-001-VER004

### Outcome

#### G-ORG2-REF-001-TASK004-OUT001

**Kind:** investigation_result  
**Statement:** The runtime record now traces the interactive native-agent path through launch, durable Work Item admission, queueing, prompt construction, provider and tool iterations, cancellation, recovery, persistence, and frontend settlement.  
**Produced by:** agent:codex:gpt-5.6-sol  
**Produced at:** 2026-08-31T04:48:51Z  
**Authority basis:** The requester authorized the ORG2 implementation-reference program.

**Resolves:**
- none

**Supports:**
- G-ORG2-REF-001-SPEC001-REQ004

**Evidence:**
- `ref-eng/runtime/interactive-native-agent-loop.md`
- G-ORG2-REF-001-VER004-RUN001

## G-ORG2-REF-001-TASK005 — Verify and review the first slice

**State:** completed  
**Type:** verification  
**Waived by:** none  
**Blocked by:** none  
**Started by:** agent:codex:gpt-5.6-sol  
**Started at:** 2026-08-31T04:48:51Z  
**Completed by:** agent:codex:gpt-5.6-sol  
**Completed at:** 2026-08-31T04:52:42Z  
**Authority basis:** G-ORG2-REF-001-VER004-RUN001 passed the runtime-record gate, and the requester authorized continued pursuit of the goal.

Check the first slice against the pinned source, record contradictions and limits, and judge whether its three technical records agree.

### Dependencies

- G-ORG2-REF-001-TASK002
- G-ORG2-REF-001-TASK003
- G-ORG2-REF-001-TASK004

### Requirements

- G-ORG2-REF-001-SPEC001-REQ001
- G-ORG2-REF-001-SPEC001-REQ002
- G-ORG2-REF-001-SPEC001-REQ003
- G-ORG2-REF-001-SPEC001-REQ004
- G-ORG2-REF-001-SPEC001-REQ006

### Acceptance criteria

#### G-ORG2-REF-001-TASK005-AC001 — Current verification runs pass or name each unmet obligation without hiding uncertainty

**Verified by:**
- G-ORG2-REF-001-VER005
- G-ORG2-REF-001-VER007

**Waived by:** none  
**Supersedes:** none

### Verifications

- G-ORG2-REF-001-VER005
- G-ORG2-REF-001-VER007

### Outcome

#### G-ORG2-REF-001-TASK005-OUT001

**Kind:** verification_result  
**Statement:** The frozen first slice passed its local and cross-record checks after two launch-order corrections. No required correctness or evidence finding remains in the slice.  
**Produced by:** agent:codex:gpt-5.6-sol  
**Produced at:** 2026-08-31T04:52:42Z  
**Authority basis:** The active Plan assigned first-slice verification to this Task.

**Resolves:**
- none

**Supports:**
- G-ORG2-REF-001-SC002
- G-ORG2-REF-001-SC004

**Evidence:**
- G-ORG2-REF-001-VER005-RUN001
- G-ORG2-REF-001-VER007-RUN001

## G-ORG2-REF-001-TASK006 — Expand the corpus by reader need

**State:** completed  
**Type:** research  
**Waived by:** none  
**Blocked by:** none  
**Started by:** agent:codex:gpt-5.6-sol  
**Started at:** 2026-08-31T04:52:42Z  
**Completed by:** agent:codex:gpt-5.6-sol  
**Completed at:** 2026-08-31T05:05:26Z  
**Authority basis:** G-ORG2-REF-001-VER005-RUN001 and G-ORG2-REF-001-VER007-RUN001 passed the frozen first-slice gate, and the requester authorized continued pursuit of the goal.

Add the remaining reader-focused architecture records as one bounded breadth pass, then run one final source and coverage review.

### Dependencies

- G-ORG2-REF-001-TASK005

### Requirements

- G-ORG2-REF-001-SPEC001-REQ005
- G-ORG2-REF-001-SPEC001-REQ006

### Acceptance criteria

#### G-ORG2-REF-001-TASK006-AC001 — The completed corpus covers each required area at implementation-useful depth without empty or speculative records

**Verified by:**
- G-ORG2-REF-001-VER006
- G-ORG2-REF-001-VER007

**Waived by:** none  
**Supersedes:** none

### Verifications

- G-ORG2-REF-001-VER006
- G-ORG2-REF-001-VER007

### Outcome

#### G-ORG2-REF-001-TASK006-OUT001

**Kind:** research_result  
**Statement:** Four source-grounded breadth records completed the ORG2 corpus. They cover topology, package dependencies, core entities, state lifecycles, cross-tool ingestion, external CLIs, extensions, trust boundaries, and build or delivery choices without empty scaffolding.  
**Produced by:** agent:codex:gpt-5.6-sol  
**Produced at:** 2026-08-31T05:05:26Z  
**Authority basis:** The active Plan assigned corpus expansion and final breadth review to this Task.

**Resolves:**
- none

**Supports:**
- G-ORG2-REF-001-SC003
- G-ORG2-REF-001-SC004

**Evidence:**
- G-ORG2-REF-001-VER006-RUN001
- G-ORG2-REF-001-VER007-RUN002
