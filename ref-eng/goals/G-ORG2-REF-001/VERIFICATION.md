---
type: verification-register
name: G-ORG2-REF-001-VERIFICATIONS
description: Verification definitions and runs for the ORG2 implementation-reference corpus.
tags: [org2, implementation-reference, verification]
---

# Verifications — G-ORG2-REF-001

## G-ORG2-REF-001-VER001 — Verify the corpus and evidence baseline

**Version:** 1  
**State:** active  
**Supersedes:** none  
**Mode:** deterministic  
**Evaluator mode:** deterministic  
**Waived by:** none

**Covers:**
- G-ORG2-REF-001-SC001
- G-ORG2-REF-001-SPEC001-REQ001
- G-ORG2-REF-001-TASK001-AC001
- G-ORG2-REF-001-TASK001-AC002
- G-ORG2-REF-001-PLAN001-CHK001-CND001

**Subjects:**
- `ref-eng/README.md`
- `ref-eng/evidence/G-ORG2-REF-001-first-slice-sources.md`
- ORG2 source revision

### Procedure

1. Confirm that ORG2 `HEAD` equals the source revision declared by both subjects.
2. Confirm that both subjects have the required frontmatter and expected heading structure.
3. Resolve each Markdown file target linked from the index and goal.
4. Search `src/` and `src-tauri/` for the three stale-path symbols named by the baseline.
5. Confirm that the baseline labels unexecuted behavior as source-observed or unverified, not runtime-verified.

### Expected

The revision matches, document structure and link targets pass, current production source supports each stated correction, and the baseline does not claim runtime proof.

### Runs

#### G-ORG2-REF-001-VER001-RUN001

**Verification version:** 1  
**Result:** pass  
**Executed by:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-31T04:31:46Z  
**Authority basis:** none

##### Subject snapshots

- ORG2 `HEAD` @ `b315ba4f82fb1fe294496793d7322095e7efe262`
- `ref-eng/README.md` @ SHA-256 `68934ba669dcf0b95a8baf04dd5bd034dd7193c87e378c21f72c7220768a0838`
- `ref-eng/evidence/G-ORG2-REF-001-first-slice-sources.md` @ SHA-256 `93bd4f7e6ffc569ec205ce5a50afc2006225e8dc34884b4178fff805a5d986ba`

##### Observed

The subjects declared the accepted revision, contained the required frontmatter and bounded heading structure, and had no missing linked-file target. Production-source search found one `buildSdeTaskPrompt` reference, which is its definition, and found zero `StartAgentButton` or `useWorkItemOrchestrator` references. The baseline explicitly withheld runtime verification.

##### Evidence

- `ctxq scan ref-eng/goals/G-ORG2-REF-001`
- `ctxq outline ref-eng/README.md`
- `ctxq outline ref-eng/evidence/G-ORG2-REF-001-first-slice-sources.md`
- `/usr/bin/rg -n 'buildSdeTaskPrompt|StartAgentButton|useWorkItemOrchestrator' src src-tauri`
- `sha256sum ref-eng/README.md ref-eng/evidence/G-ORG2-REF-001-first-slice-sources.md`

## G-ORG2-REF-001-VER002 — Verify the execution-kernel architecture record

**Version:** 1  
**State:** active  
**Supersedes:** none  
**Mode:** deterministic  
**Evaluator mode:** deterministic  
**Waived by:** none

**Covers:**
- G-ORG2-REF-001-SPEC001-REQ002
- G-ORG2-REF-001-TASK002-AC001

**Subjects:**
- `ref-eng/architecture/native-agent-execution-kernel.md`

### Procedure

1. Confirm the declared revision equals ORG2 `HEAD`.
2. Check the required boundary, container, state-owner, construction, collaboration, invariant, tradeoff, limit, source-map, and conformance sections.
3. Resolve each cited repository path and internal Markdown target.
4. Confirm that diagrams and pseudocode are labeled as derived and that the record claims no unexecuted runtime proof.

### Expected

The architecture record has the required forms, resolves its evidence paths, and stays within the native interactive session boundary.

### Runs

#### G-ORG2-REF-001-VER002-RUN001

**Verification version:** 1  
**Result:** pass  
**Executed by:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-31T04:38:49Z  
**Authority basis:** none

##### Subject snapshots

- ORG2 `HEAD` @ `b315ba4f82fb1fe294496793d7322095e7efe262`
- `ref-eng/architecture/native-agent-execution-kernel.md` @ SHA-256 `265d472e1aaf6733e13a46f9c29c19e339511ffb4f081f6f32932bb64b9f1cf7`

##### Observed

The record declared the accepted revision, contained each required section, resolved every linked repository path, labeled diagrams and pseudocode as derived, and made no Runtime-verified claim.

##### Evidence

- `ctxq outline ref-eng/architecture/native-agent-execution-kernel.md`
- Linked-target existence check over `ref-eng/architecture/native-agent-execution-kernel.md`
- `git rev-parse HEAD`
- `sha256sum ref-eng/architecture/native-agent-execution-kernel.md`

## G-ORG2-REF-001-VER003 — Verify the execution-seam record

**Version:** 1  
**State:** active  
**Supersedes:** none  
**Mode:** deterministic  
**Evaluator mode:** deterministic  
**Waived by:** none

**Covers:**
- G-ORG2-REF-001-SPEC001-REQ003
- G-ORG2-REF-001-TASK003-AC001

**Subjects:**
- `ref-eng/interfaces/native-agent-execution-seams.md`

### Procedure

1. Confirm the declared revision equals ORG2 `HEAD`.
2. Check that each seam names caller, callee, input, output, invariant, failure behavior, and variation point where one exists.
3. Resolve each cited repository path and internal Markdown target.
4. Confirm that unsupported runtime behavior remains unverified.

### Expected

Every required seam has a complete, source-grounded contract row and no missing evidence path.

### Runs

#### G-ORG2-REF-001-VER003-RUN001

**Verification version:** 1  
**Result:** pass  
**Executed by:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-31T04:44:48Z  
**Authority basis:** none

##### Subject snapshots

- ORG2 `HEAD` @ `b315ba4f82fb1fe294496793d7322095e7efe262`
- `ref-eng/interfaces/native-agent-execution-seams.md` @ SHA-256 `0d6a26fdbd86f317f0cdc65433426dae4419cbde3f3b52d3f52ca7ecb855b2d8`

##### Observed

The record declared the accepted revision, contained eleven seam rows with every required contract field, resolved every linked repository path, and withheld runtime verification.

##### Evidence

- Required-heading and eleven-row contract-table check over `ref-eng/interfaces/native-agent-execution-seams.md`
- Linked-target existence check over `ref-eng/interfaces/native-agent-execution-seams.md`
- `git rev-parse HEAD`
- `sha256sum ref-eng/interfaces/native-agent-execution-seams.md`

#### G-ORG2-REF-001-VER003-RUN002

**Verification version:** 1  
**Result:** pass  
**Executed by:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-31T04:51:08Z  
**Authority basis:** none

##### Subject snapshots

- ORG2 `HEAD` @ `b315ba4f82fb1fe294496793d7322095e7efe262`
- `ref-eng/interfaces/native-agent-execution-seams.md` @ SHA-256 `4a02cac5a093dbcccb42ad70328b3896b55e6d3c5b38d9c39c75ad31d23143d2`

##### Observed

The current record passed the contract and evidence checks after it distinguished ordinary spawned submission from durable scheduler acceptance. This run replaces RUN001 as current proof for the changed subject.

##### Evidence

- Required-heading and eleven-row contract-table check over `ref-eng/interfaces/native-agent-execution-seams.md`
- Linked-target existence check over `ref-eng/interfaces/native-agent-execution-seams.md`
- `git rev-parse HEAD`
- `sha256sum ref-eng/interfaces/native-agent-execution-seams.md`

## G-ORG2-REF-001-VER004 — Verify the interactive runtime record

**Version:** 1  
**State:** active  
**Supersedes:** none  
**Mode:** deterministic  
**Evaluator mode:** deterministic  
**Waived by:** none

**Covers:**
- G-ORG2-REF-001-SPEC001-REQ004
- G-ORG2-REF-001-TASK004-AC001

**Subjects:**
- `ref-eng/runtime/interactive-native-agent-loop.md`

### Procedure

1. Confirm the declared revision equals ORG2 `HEAD`.
2. Check the nominal sequence, state transitions, pseudocode, work-item, queue, provider, tool, approval, cancellation, retry, compaction, persistence, settlement, invariant, and limit sections.
3. Resolve each cited repository path and internal Markdown target.
4. Confirm that execution order agrees with cited source and that runtime verification is not implied.

### Expected

The runtime record covers each required current-source branch with no missing evidence path or unsupported execution claim.

### Runs

#### G-ORG2-REF-001-VER004-RUN001

**Verification version:** 1  
**Result:** pass  
**Executed by:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-31T04:48:51Z  
**Authority basis:** none

##### Subject snapshots

- ORG2 `HEAD` @ `b315ba4f82fb1fe294496793d7322095e7efe262`
- `ref-eng/runtime/interactive-native-agent-loop.md` @ SHA-256 `7416a1e2e2058b7d72cbcf0bc36964915505f0eb67bfe2e8f3cbce25b4b655c5`

##### Observed

The record declared the accepted revision, contained every required runtime section, resolved every linked repository path, preserved source execution order, and withheld runtime verification.

##### Evidence

- Required-heading check over `ref-eng/runtime/interactive-native-agent-loop.md`
- Linked-target existence check over `ref-eng/runtime/interactive-native-agent-loop.md`
- `git rev-parse HEAD`
- `sha256sum ref-eng/runtime/interactive-native-agent-loop.md`

#### G-ORG2-REF-001-VER004-RUN002

**Verification version:** 1  
**Result:** pass  
**Executed by:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-31T04:51:08Z  
**Authority basis:** none

##### Subject snapshots

- ORG2 `HEAD` @ `b315ba4f82fb1fe294496793d7322095e7efe262`
- `ref-eng/runtime/interactive-native-agent-loop.md` @ SHA-256 `35e7236dbfd3c2e4f178328410890593eeea4ae9516821623559090d7ea8aada`

##### Observed

The current record passed the runtime and evidence checks after its sequence view made ordinary spawned submission distinct from durable awaited submission. This run replaces RUN001 as current proof for the changed subject.

##### Evidence

- Required-heading check over `ref-eng/runtime/interactive-native-agent-loop.md`
- Linked-target existence check over `ref-eng/runtime/interactive-native-agent-loop.md`
- `git rev-parse HEAD`
- `sha256sum ref-eng/runtime/interactive-native-agent-loop.md`

## G-ORG2-REF-001-VER005 — Verify first-slice consistency

**Version:** 1  
**State:** active  
**Supersedes:** none  
**Mode:** deterministic  
**Evaluator mode:** deterministic  
**Waived by:** none

**Covers:**
- G-ORG2-REF-001-SC002
- G-ORG2-REF-001-TASK005-AC001
- G-ORG2-REF-001-PLAN001-CHK002-CND001

**Subjects:**
- `ref-eng/architecture/native-agent-execution-kernel.md`
- `ref-eng/interfaces/native-agent-execution-seams.md`
- `ref-eng/runtime/interactive-native-agent-loop.md`

### Procedure

1. Confirm that all three subjects passed their local deterministic verification.
2. Compare component names, ownership, execution order, state transitions, and stated limits across the subjects.
3. Resolve cross-links among the subjects and from `ref-eng/README.md`.

### Expected

The three records describe one consistent path and have no unresolved cross-record contradiction.

### Runs

#### G-ORG2-REF-001-VER005-RUN001

**Verification version:** 1  
**Result:** pass  
**Executed by:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-31T04:51:56Z  
**Authority basis:** none

##### Subject snapshots

- ORG2 `HEAD` @ `b315ba4f82fb1fe294496793d7322095e7efe262`
- `ref-eng/architecture/native-agent-execution-kernel.md` @ SHA-256 `265d472e1aaf6733e13a46f9c29c19e339511ffb4f081f6f32932bb64b9f1cf7`
- `ref-eng/interfaces/native-agent-execution-seams.md` @ SHA-256 `4a02cac5a093dbcccb42ad70328b3896b55e6d3c5b38d9c39c75ad31d23143d2`
- `ref-eng/runtime/interactive-native-agent-loop.md` @ SHA-256 `35e7236dbfd3c2e4f178328410890593eeea4ae9516821623559090d7ea8aada`
- `ref-eng/README.md` @ SHA-256 `654b95e06c26dad67ed7d129d7c6380455b8a3beb559f379b95a2df845274a08`

##### Observed

All three subjects had current local proof, one source revision, consistent component ownership, aligned Work Item channels, the same durable-versus-ordinary launch distinction, compatible state transitions, and explicit category and runtime limits. README and cross-record targets resolved. No cross-record contradiction remained.

##### Corrected findings

- The first interface draft implied that every launch waited for initial-turn acceptance. S4 and S5 now distinguish an ordinary spawned submission from durable awaited scheduler acceptance.
- The first runtime sequence drew ordinary and durable submission as one strict order. The diagram now has separate branches.

##### Evidence

- Current subject-hash and local-proof check
- Linked-target and cross-link resolution over the three subjects and `ref-eng/README.md`
- `ctxq show` comparison of Work Item, invariant, and known-limit sections
- Direct source comparison with `launch_rust_agent_run`, `send_message_impl`, `DialogScheduler`, `UnifiedMessageProcessor`, `execute_turn`, `UnifiedEventHandler`, and frontend terminal handlers

## G-ORG2-REF-001-VER006 — Review corpus breadth

**Version:** 1  
**State:** active  
**Supersedes:** none  
**Mode:** judgment  
**Evaluator mode:** agent_judgment  
**Waived by:** none

**Covers:**
- G-ORG2-REF-001-SC003
- G-ORG2-REF-001-SPEC001-REQ005
- G-ORG2-REF-001-TASK006-AC001
- G-ORG2-REF-001-PLAN001-CHK003-CND001

**Subjects:**
- `ref-eng/README.md`
- Completed technical records linked from the corpus map

### Criteria

- Each required area has a reader-useful record or a justified explicit limit.
- Records provide enough implementation depth to support focused change or integration work.
- The corpus has no empty scaffolding or repeated overview text that substitutes for evidence.

### Procedure

1. Map each active breadth requirement to completed records.
2. Review explanatory forms, source depth, cross-links, and known limits for each area.
3. Record each missing or shallow area before judging the result.

### Expected

Every required area has sufficient current coverage, and no unresolved required breadth finding remains.

### Runs

#### G-ORG2-REF-001-VER006-RUN001

**Verification version:** 1  
**Result:** pass  
**Executed by:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-31T05:05:26Z  
**Authority basis:** The active Plan assigns corpus breadth judgment to G-ORG2-REF-001-TASK006.

##### Subject snapshots

- ORG2 `HEAD` @ `b315ba4f82fb1fe294496793d7322095e7efe262`
- `ref-eng/README.md` @ SHA-256 `1912f090876f0d1021ab3c596c0bc2ca1e09a75f148970ae57c859f37a7ce9e5`
- `ref-eng/architecture/system-topology.md` @ SHA-256 `e8b4ff8b26e1055f48481190918dac9f1e010f8a5dc46195db54900ba5e34c3f`
- `ref-eng/architecture/package-dependencies.md` @ SHA-256 `6d297924b0eb6b8beb8d3f11e5b3dff29289e18fac5db369a95e65743bebf58a`
- `ref-eng/domain-models/core-entities.md` @ SHA-256 `1948b86dac4c26330ca855f3992d7c278c1f419a5fd0dc7919785a32bc8a2cce`
- `ref-eng/data-and-storage/state-lifecycles.md` @ SHA-256 `223f4b2b4351b16f0ec0c0d8e580b03fbb049ad627a0a73408c36c04ef665e9e`

##### Requirement mapping

- System topology, external CLI integration, extension mechanisms, trust boundaries, and build or delivery choices: `ref-eng/architecture/system-topology.md`.
- Package direction, dependency inversion, design choices, and change impact: `ref-eng/architecture/package-dependencies.md`.
- Domain and state ownership, identity, relations, events, and cross-tool ingestion: `ref-eng/domain-models/core-entities.md`.
- Data and storage, WAL, application history, projections, dispatch, concurrency, and recovery: `ref-eng/data-and-storage/state-lifecycles.md`.
- Runtime workflows and interface seams: the frozen execution-kernel, interface, and runtime records.

##### Judgment

Accept corpus breadth. Every area in G-ORG2-REF-001-SPEC001-REQ005 has an implementation-useful record. The records use system, dependency, entity, and lifecycle views where those forms clarify the source. Each record names direct owners, design tradeoffs, and known limits. No empty scaffold or unresolved required breadth finding remains.

##### Evidence

- The final review parsed all eight corpus/index files with `ctxq`, resolved every local Markdown link target, found no placeholder markers, and matched every technical record to the pinned revision.
- Cargo metadata reported 43 local Rust packages and supported the selected direct dependency graph.
- Direct source checks confirmed database PRAGMAs, Turn Intent terminals, Work Item Run states, and the `org2-pm` and `orgtrack` binary names.

## G-ORG2-REF-001-VER007 — Review source-grounded quality

**Version:** 1  
**State:** active  
**Supersedes:** none  
**Mode:** judgment  
**Evaluator mode:** agent_judgment  
**Waived by:** none

**Covers:**
- G-ORG2-REF-001-SC004
- G-ORG2-REF-001-SPEC001-REQ006
- G-ORG2-REF-001-TASK005-AC001
- G-ORG2-REF-001-TASK006-AC001
- G-ORG2-REF-001-PLAN001-CHK002-CND002

**Subjects:**
- Completed technical records linked from `ref-eng/README.md`

### Criteria

- Direct source supports each material source-observed claim.
- Derived, proposed, runtime-verified, and unverified claims have accurate labels.
- Diagrams and pseudocode preserve current control order and do not masquerade as source.
- Records expose contradictions, trust boundaries, failure behavior, and current limits where relevant.
- The corpus uses consistent component names and avoids unsupported generalization across session categories.

### Procedure

1. Select every material claim in the completed slice.
2. Compare it with the cited current source or controlled runtime evidence.
3. Review correctness, clarity, architecture, trust boundaries, and unmeasured performance claims.
4. Record contradictions or missing evidence before judging the result.

### Expected

No unresolved required correctness or evidence finding remains in the completed slice.

### Runs

#### G-ORG2-REF-001-VER007-RUN001

**Verification version:** 1  
**Result:** pass  
**Executed by:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-31T04:51:56Z  
**Authority basis:** The active Plan assigns first-slice quality judgment to G-ORG2-REF-001-TASK005.

##### Subject snapshots

- ORG2 `HEAD` @ `b315ba4f82fb1fe294496793d7322095e7efe262`
- `ref-eng/README.md` @ SHA-256 `654b95e06c26dad67ed7d129d7c6380455b8a3beb559f379b95a2df845274a08`
- `ref-eng/architecture/native-agent-execution-kernel.md` @ SHA-256 `265d472e1aaf6733e13a46f9c29c19e339511ffb4f081f6f32932bb64b9f1cf7`
- `ref-eng/interfaces/native-agent-execution-seams.md` @ SHA-256 `4a02cac5a093dbcccb42ad70328b3896b55e6d3c5b38d9c39c75ad31d23143d2`
- `ref-eng/runtime/interactive-native-agent-loop.md` @ SHA-256 `35e7236dbfd3c2e4f178328410890593eeea4ae9516821623559090d7ea8aada`

##### Judgment

Accept the completed first slice. Direct source supports its material source-observed claims. Derived diagrams and pseudocode preserve current control order after two launch-order corrections. The records expose trust boundaries, failure behavior, contradicted older claims, category limits, and unverified runtime behavior. No required correctness or evidence finding remains.

##### Evidence

- G-ORG2-REF-001-VER002-RUN001
- G-ORG2-REF-001-VER003-RUN002
- G-ORG2-REF-001-VER004-RUN002
- G-ORG2-REF-001-VER005-RUN001

#### G-ORG2-REF-001-VER007-RUN002

**Verification version:** 1  
**Result:** pass  
**Executed by:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-31T05:05:26Z  
**Authority basis:** The active Plan assigns the completed-corpus quality judgment to G-ORG2-REF-001-TASK006.

##### Subject snapshots

- ORG2 `HEAD` @ `b315ba4f82fb1fe294496793d7322095e7efe262`
- `ref-eng/README.md` @ SHA-256 `1912f090876f0d1021ab3c596c0bc2ca1e09a75f148970ae57c859f37a7ce9e5`
- `ref-eng/architecture/native-agent-execution-kernel.md` @ SHA-256 `265d472e1aaf6733e13a46f9c29c19e339511ffb4f081f6f32932bb64b9f1cf7`
- `ref-eng/interfaces/native-agent-execution-seams.md` @ SHA-256 `4a02cac5a093dbcccb42ad70328b3896b55e6d3c5b38d9c39c75ad31d23143d2`
- `ref-eng/runtime/interactive-native-agent-loop.md` @ SHA-256 `35e7236dbfd3c2e4f178328410890593eeea4ae9516821623559090d7ea8aada`
- `ref-eng/architecture/system-topology.md` @ SHA-256 `e8b4ff8b26e1055f48481190918dac9f1e010f8a5dc46195db54900ba5e34c3f`
- `ref-eng/architecture/package-dependencies.md` @ SHA-256 `6d297924b0eb6b8beb8d3f11e5b3dff29289e18fac5db369a95e65743bebf58a`
- `ref-eng/domain-models/core-entities.md` @ SHA-256 `1948b86dac4c26330ca855f3992d7c278c1f419a5fd0dc7919785a32bc8a2cce`
- `ref-eng/data-and-storage/state-lifecycles.md` @ SHA-256 `223f4b2b4351b16f0ec0c0d8e580b03fbb049ad627a0a73408c36c04ef665e9e`

##### Judgment

Accept the completed corpus at the pinned revision. Direct source supports the material source-observed claims reviewed in the breadth pass. Derived diagrams and groupings identify themselves as Derived. The records distinguish SQLite WAL from application history, native sessions from imported histories, and product work from execution episodes. They expose trust boundaries, failure behavior, unmeasured properties, and category limits. No unresolved required correctness or evidence finding remains.

##### Evidence

- G-ORG2-REF-001-VER005-RUN001
- G-ORG2-REF-001-VER006-RUN001
- The bounded final source, structure, link, coverage, and placeholder review recorded for G-ORG2-REF-001-TASK006.
