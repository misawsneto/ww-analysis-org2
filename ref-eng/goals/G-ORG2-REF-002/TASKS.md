---
type: task-register
name: G-ORG2-REF-002-TASKS
description: Ordered tasks for the graph-guided ORG2 capability and execution atlas.
tags: [org2, implementation-reference, tasks, ua, graphify]
---

# Tasks — G-ORG2-REF-002

## G-ORG2-REF-002-TASK001 — Select gaps through UA and Graphify

**State:** completed  
**Type:** investigation  
**Waived by:** none  
**Blocked by:** none
**Started by:** agent:codex:gpt-5.6-sol  
**Started at:** 2026-08-31T15:26:45Z  
**Completed by:** agent:codex:gpt-5.6-sol  
**Completed at:** 2026-08-31T15:38:17Z  
**Authority basis:** G-ORG2-REF-002-VER001-RUN001 passed the Task Acceptance Criterion and the first Plan Checkpoint condition.

Reuse the accepted UA knowledge graph and domain graph as the primary semantic navigation layer. Compare their domains, layers, tours, nodes, and candidate journeys with the completed `ref-eng/` corpus. Use Graphify to inspect structural boundaries for candidate gaps. Persist one coverage matrix that identifies accepted graph snapshots, existing coverage, rejected duplicate topics, and no more than four selected journeys.

### Requirements

- G-ORG2-REF-002-SPEC001-REQ001
- G-ORG2-REF-002-SPEC001-REQ002
- G-ORG2-REF-002-SPEC001-REQ003
- G-ORG2-REF-002-SPEC001-REQ004

### Acceptance criteria

#### G-ORG2-REF-002-TASK001-AC001 — The coverage matrix proves graph-guided contextualization and selects only material gaps

The matrix records the accepted revision and graph paths, distinguishes UA semantic evidence from Graphify structural evidence, maps existing documents to covered subjects, and selects no more than four journeys that add implementation depth.

**Verified by:**
- G-ORG2-REF-002-VER001

**Waived by:** none  
**Supersedes:** none

### Verifications

- G-ORG2-REF-002-VER001

### Outcome

#### G-ORG2-REF-002-TASK001-OUT001

**Kind:** investigation_result  
**Statement:** The accepted coverage matrix makes UA the primary semantic navigation layer, uses Graphify only for structural boundary evidence, rejects duplicate native-runtime analysis, and selects four deeper journeys: Agent Org coordination, channel routing, external artifact import, and the session-event review pipeline. It also assigns each journey to new or existing technical-document owners.  
**Produced by:** agent:codex:gpt-5.6-sol  
**Produced at:** 2026-08-31T15:38:17Z  
**Authority basis:** G-ORG2-REF-002-VER001-RUN001 passed.

**Resolves:**
- none

**Supports:**
- G-ORG2-REF-002-SC001
- G-ORG2-REF-002-SC004
- G-ORG2-REF-002-SPEC001-REQ001
- G-ORG2-REF-002-SPEC001-REQ002
- G-ORG2-REF-002-SPEC001-REQ003
- G-ORG2-REF-002-SPEC001-REQ004

**Evidence:**
- `ref-eng/evidence/G-ORG2-REF-002-graph-coverage.md`
- G-ORG2-REF-002-VER001-RUN001

## G-ORG2-REF-002-TASK002 — Publish the capability and execution atlas

**State:** completed  
**Type:** research  
**Waived by:** none  
**Blocked by:** none
**Started by:** agent:codex:gpt-5.6-sol  
**Started at:** 2026-08-31T15:39:54Z  
**Completed by:** agent:codex:gpt-5.6-sol  
**Completed at:** 2026-08-31T16:09:55Z  
**Authority basis:** G-ORG2-REF-002-VER001-RUN001 authorized publication, G-ORG2-REF-002-DEC004 bounded the corrective delta, and G-ORG2-REF-002-VER002-RUN002 passed the Task Acceptance Criteria.

Use UA to retain semantic context for every selected journey and Graphify to traverse its concrete dependencies, calls, references, hubs, and boundary crossings. Confirm material behavior against direct source. Publish the capability atlas, refine existing technical records that own uncovered information, add focused records only for subjects without an adequate owner, and update the reference index. Execute one bounded final review before this Task completes.

### Dependencies

- G-ORG2-REF-002-TASK001

### Requirements

- G-ORG2-REF-002-SPEC001-REQ005
- G-ORG2-REF-002-SPEC001-REQ006
- G-ORG2-REF-002-SPEC001-REQ007
- G-ORG2-REF-002-SPEC001-REQ008

### Acceptance criteria

#### G-ORG2-REF-002-TASK002-AC001 — The atlas connects capabilities, execution, entities, state, and evidence

The atlas maps each selected capability across applicable user, frontend, Tauri, Rust, persistence, tool, external-system, event, failure, and trust boundaries and links each material claim to direct source.

**Verified by:**
- G-ORG2-REF-002-VER002

**Waived by:** none  
**Supersedes:** none

#### G-ORG2-REF-002-TASK002-AC002 — Focused records add depth without repeating the accepted corpus

Each new or refined technical record addresses a gap selected by G-ORG2-REF-002-TASK001, explains the implementation-specific interaction and tradeoffs, and links existing reference records instead of reproducing their broad content.

**Verified by:**
- G-ORG2-REF-002-VER002

**Waived by:** none  
**Supersedes:** none

#### G-ORG2-REF-002-TASK002-AC003 — One final review supplies current proof

An authorized Actor executes G-ORG2-REF-002-VER002 once against the exact published subjects and creates a current passing Run before this Task completes.

**Verified by:**
- G-ORG2-REF-002-VER002

**Waived by:** none  
**Supersedes:** none

### Verifications

- G-ORG2-REF-002-VER002

### Outcome

#### G-ORG2-REF-002-TASK002-OUT001

**Kind:** documentation_result  
**Statement:** The ORG2 reference now contains one capability connector atlas, four source-grounded journey records, and refined entity, lifecycle, topology, and index owners. UA guided semantic scope and navigation, Graphify identified structural boundaries, and direct source proved the published behavior.  
**Produced by:** agent:codex:gpt-5.6-sol  
**Produced at:** 2026-08-31T16:09:55Z  
**Authority basis:** G-ORG2-REF-002-VER002-RUN002 passed after the single link-only correction authorized by G-ORG2-REF-002-DEC004.

**Resolves:**
- G-ORG2-REF-002

**Supports:**
- G-ORG2-REF-002-SC002
- G-ORG2-REF-002-SC003
- G-ORG2-REF-002-SC004
- G-ORG2-REF-002-SPEC001-REQ005
- G-ORG2-REF-002-SPEC001-REQ006
- G-ORG2-REF-002-SPEC001-REQ007
- G-ORG2-REF-002-SPEC001-REQ008

**Evidence:**
- `ref-eng/architecture/capability-execution-atlas.md`
- `ref-eng/runtime/agent-org-coordination.md`
- `ref-eng/runtime/channel-gateway-routing.md`
- `ref-eng/interfaces/external-artifact-import-seams.md`
- `ref-eng/data-and-storage/session-event-pipeline.md`
- G-ORG2-REF-002-VER002-RUN002
