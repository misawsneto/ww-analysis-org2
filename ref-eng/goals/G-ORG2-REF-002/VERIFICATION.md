---
type: verification-register
name: G-ORG2-REF-002-VERIFICATIONS
description: Bounded verification definitions and runs for the graph-guided ORG2 capability and execution atlas.
tags: [org2, implementation-reference, verification, ua, graphify]
---

# Verifications — G-ORG2-REF-002

## G-ORG2-REF-002-VER001 — Verify graph-guided scope selection

**Version:** 1  
**State:** active  
**Supersedes:** none  
**Mode:** judgment  
**Evaluator mode:** agent_judgment  
**Waived by:** none

**Covers:**
- G-ORG2-REF-002-SC001
- G-ORG2-REF-002-SC004
- G-ORG2-REF-002-SPEC001-REQ001
- G-ORG2-REF-002-SPEC001-REQ002
- G-ORG2-REF-002-SPEC001-REQ003
- G-ORG2-REF-002-SPEC001-REQ004
- G-ORG2-REF-002-TASK001-AC001
- G-ORG2-REF-002-PLAN001-CHK001-CND001

**Subjects:**
- `ref-eng/evidence/G-ORG2-REF-002-graph-coverage.md`
- `.understand-anything/knowledge-graph.json`
- `.understand-anything/domain-graph.json`
- `graphify-out/graph.json`
- `ref-eng/README.md`

### Criteria

- The coverage matrix records the accepted source revision and graph artifact paths.
- It uses UA domains, layers, tours, or semantic nodes to select and explain candidate coverage.
- It uses Graphify structural evidence only where it clarifies candidate boundaries or paths.
- It identifies existing documents before it selects new work.
- It rejects duplicate topics and selects no more than four material gaps.
- It treats graphs as navigation evidence and direct source as the authority for later behavioral claims.

### Procedure

1. Compare the recorded source revision with G-ORG2-REINDEX-001 evidence and the goal boundary.
2. Inspect the coverage matrix mappings for the accepted UA artifacts, Graphify artifact, existing reference documents, and selected gaps.
3. Check that the selected gaps have semantic and structural evidence and do not repeat the existing corpus at the same depth.
4. Record one pass or fail Run and stop this Verification.

### Expected

The coverage matrix establishes a current, graph-guided, non-duplicative scope of no more than four capability journeys.

### Runs

#### G-ORG2-REF-002-VER001-RUN001

**Verification version:** 1  
**Result:** pass  
**Executed by:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-31T15:38:17Z  
**Authority basis:** The requester authorized the active goal, and G-ORG2-REF-002-PLAN001 assigns this Verification as the Task 001 exit proof.

##### Subject snapshots

- `ref-eng/evidence/G-ORG2-REF-002-graph-coverage.md` @ `f9060174f7d8d5ca30787c530c2fdbb340c4b71920060fc156d6d2ec3ad1c550`
- `.understand-anything/knowledge-graph.json` @ `c77472fa5dad35e4b1c8525297bde19988c62110437303c8988c9740f521efdd`
- `.understand-anything/domain-graph.json` @ `17d7d7ced5542a1bec91c55c8e81fdb438ffec31ffad70db4ea92e5a5da4fe13`
- `graphify-out/graph.json` @ `c5176303cb7d7036cb28ce144b58410122388299ba709177e65e3526c1cce62a`
- `ref-eng/README.md` @ `1912f090876f0d1021ab3c596c0bc2ca1e09a75f148970ae57c859f37a7ce9e5`
- ORG2 @ `b315ba4f82fb1fe294496793d7322095e7efe262`

##### Observed

The current source and all three graph artifacts match the accepted reindex revision and digests. The matrix uses five UA domains, 16 UA flows, 48 source-backed steps, UA layer and tour context, and bounded Graphify path evidence. It rejects the already documented Agent Session Runtime domain and selects four material gaps: Agent Org coordination, channel routing, external artifact import, and the session-event review pipeline. It keeps the graph schemas separate and assigns direct source as the authority for Task 2 claims.

##### Rationale

The matrix satisfies every Verification criterion. It establishes graph-guided contextualization, maps existing documents before new work, limits the selected scope to four non-duplicate journeys, and defines how Task 2 will refine the technical corpus.

##### Evidence

- `ref-eng/evidence/G-ORG2-REF-002-graph-coverage.md`
- G-ORG2-REINDEX-001-VER001-RUN001
- G-ORG2-REINDEX-001-VER002-RUN001

## G-ORG2-REF-002-VER002 — Review the published atlas once

**Version:** 1  
**State:** active  
**Supersedes:** none  
**Mode:** judgment  
**Evaluator mode:** agent_judgment  
**Waived by:** none

**Covers:**
- G-ORG2-REF-002-SC002
- G-ORG2-REF-002-SC003
- G-ORG2-REF-002-SC004
- G-ORG2-REF-002-SPEC001-REQ005
- G-ORG2-REF-002-SPEC001-REQ006
- G-ORG2-REF-002-SPEC001-REQ007
- G-ORG2-REF-002-SPEC001-REQ008
- G-ORG2-REF-002-TASK002-AC001
- G-ORG2-REF-002-TASK002-AC002
- G-ORG2-REF-002-TASK002-AC003
- G-ORG2-REF-002-PLAN001-CHK002-CND001

**Subjects:**
- `ref-eng/architecture/capability-execution-atlas.md`
- New or refined technical records selected by `ref-eng/evidence/G-ORG2-REF-002-graph-coverage.md`
- `ref-eng/README.md`
- `ref-eng/goals/G-ORG2-REF-002/GOAL.md`
- `ref-eng/goals/G-ORG2-REF-002/SPEC.md`
- `ref-eng/goals/G-ORG2-REF-002/PLAN.md`
- `ref-eng/goals/G-ORG2-REF-002/TASKS.md`

### Criteria

- The atlas maps selected capabilities to applicable components, entities, state, persistence, events, interfaces, failures, trust boundaries, and evidence.
- Focused records explain user-harness-agent interaction and implementation-specific choices at useful depth.
- Published behavioral claims resolve to current direct source, while graph-derived conclusions remain labeled.
- New records link existing architecture documents instead of repeating broad C3/C4 content.
- The reference index links all accepted outputs.
- The review reports unresolved contradictions or missing obligations directly.

### Procedure

1. Resolve the exact output list from the accepted coverage matrix and G-ORG2-REF-002-TASK002 evidence.
2. Check the atlas and each focused record against the active Requirements and Acceptance Criteria.
3. Sample each journey at its entry point, cross-boundary transition, state or persistence boundary, and terminal or failure behavior against direct source.
4. Validate local Markdown links and the accepted source revision.
5. Record one pass or fail Run and stop this Verification without a repeat pass.

### Expected

The published atlas and focused records satisfy every current obligation or name each unresolved required defect without hiding uncertainty.

### Runs

#### G-ORG2-REF-002-VER002-RUN001

**Result:** fail  
**Actor:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-31T16:05:36Z  
**Authority basis:** G-ORG2-REF-002-TASK002 assigned the declared final review to an authorized agent after publication.

##### Subject snapshots

| Subject | SHA-256 |
| --- | --- |
| `ref-eng/architecture/capability-execution-atlas.md` | `95b8512e5a2ec6905bcc1b90ded5b02784646cb0da9fd632aa883f2b3c1dcac0` |
| `ref-eng/runtime/agent-org-coordination.md` | `b345b84ffb3c5026ae732c9c33f482e74280be7c688a77d6c2a6f1b9f45a627e` |
| `ref-eng/runtime/channel-gateway-routing.md` | `27e7a96c964de6fd6b3df23ca2529948568c3e251dce6007e1f33bfb9d7fe93e` |
| `ref-eng/interfaces/external-artifact-import-seams.md` | `26b806e628fe377b93576cd9c22ac9f561128cd2c2b6609d003819cc67f95329` |
| `ref-eng/data-and-storage/session-event-pipeline.md` | `aec5ba724cfb3bb04d70b70ea8dd030f08fdbff203b0f3991b683b07e67d2a09` |
| `ref-eng/domain-models/core-entities.md` | `c06cb1f23b0611a6209dba5dfa3a7c9110d69562a01d635050486f5de17ef9eb` |
| `ref-eng/data-and-storage/state-lifecycles.md` | `2ec64f54804377c9ff48475882e7fad7e25e51f6710376681545c1c938375c79` |
| `ref-eng/architecture/system-topology.md` | `48624b38c6fa3e9a50c3d43052f73cd446360d7a413756eb3018b96f0186f32b` |
| `ref-eng/README.md` | `3496966ab0721b6ee00d17569bdd3658698a550e7d7dffeb7d7fc1867bdb0748` |
| `ref-eng/goals/G-ORG2-REF-002/GOAL.md` | `36224eddac30adafc45abcb6106f442af1df9dc70e41770141b14986766b5f9d` |
| `ref-eng/goals/G-ORG2-REF-002/SPEC.md` | `6467e46b641edb920d23b0a49b79378fef5e67f179ee2444cd4a117096e5255e` |
| `ref-eng/goals/G-ORG2-REF-002/PLAN.md` | `a7dcb805b56eb185593f845e00aa11f490f0b17334b35ea4c07342e118086831` |
| `ref-eng/goals/G-ORG2-REF-002/TASKS.md` | `656ec2d02cffa4cac7b66540217e8c7e674667f31f65acc059fad8ab6bb25710` |

##### Observed

- The accepted source revision, document frontmatter, `ctxq` parsing, and diff-hygiene checks passed.
- Direct-source samples passed for Agent Org launch/finality, channel binding/reinjection/reset, external import detection/apply/fidelity, and event ingestion/cache/search/analytics.
- The output set satisfies the capability, interaction, state, persistence, failure, trust, and evidence depth criteria.
- Local-link validation found one real missing heading target: both atlas and index used `#graph-guided-coverage-matrix` for the coverage record.
- The validator also reported existing goal/index anchors because its temporary slug function collapsed punctuation differently from `ctxq`; those reports need deterministic heading resolution before correction.

##### Rationale

The real coverage-link defect fails the requirement that the reference index and atlas resolve their accepted evidence. The procedure requires one result and no silent repeat, so this Run records `fail` before corrective work.

##### Evidence

- Direct source paths in each focused record
- `ctxq outline` results for published and governance records
- Local link-validation output for 179 links

#### G-ORG2-REF-002-VER002-RUN002

**Result:** pass  
**Actor:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-31T16:11:18Z  
**Authority basis:** G-ORG2-REF-002-DEC004 authorized one link-only corrective delta Run after RUN001 exposed a real broken link and a defective temporary slug check.

##### Subject snapshots

| Subject | SHA-256 |
| --- | --- |
| `ref-eng/architecture/capability-execution-atlas.md` | `644879f9d4e59f4a00c6476ca25ea92bb36e043ddf013d7dd34a7e0f7516aa45` |
| `ref-eng/runtime/agent-org-coordination.md` | `b345b84ffb3c5026ae732c9c33f482e74280be7c688a77d6c2a6f1b9f45a627e` |
| `ref-eng/runtime/channel-gateway-routing.md` | `27e7a96c964de6fd6b3df23ca2529948568c3e251dce6007e1f33bfb9d7fe93e` |
| `ref-eng/interfaces/external-artifact-import-seams.md` | `26b806e628fe377b93576cd9c22ac9f561128cd2c2b6609d003819cc67f95329` |
| `ref-eng/data-and-storage/session-event-pipeline.md` | `aec5ba724cfb3bb04d70b70ea8dd030f08fdbff203b0f3991b683b07e67d2a09` |
| `ref-eng/domain-models/core-entities.md` | `c06cb1f23b0611a6209dba5dfa3a7c9110d69562a01d635050486f5de17ef9eb` |
| `ref-eng/data-and-storage/state-lifecycles.md` | `2ec64f54804377c9ff48475882e7fad7e25e51f6710376681545c1c938375c79` |
| `ref-eng/architecture/system-topology.md` | `48624b38c6fa3e9a50c3d43052f73cd446360d7a413756eb3018b96f0186f32b` |
| `ref-eng/README.md` | `9bdb56507bb8988dd0697482098e8f421bf8be3490e10d042c9084396a83f44f` |
| `ref-eng/goals/G-ORG2-REF-002/GOAL.md` | `c59471ceb6294570fb0548fa7ac3bd4c19d8831b6a4195860c4591b58fef8f43` |
| `ref-eng/goals/G-ORG2-REF-002/SPEC.md` | `6467e46b641edb920d23b0a49b79378fef5e67f179ee2444cd4a117096e5255e` |
| `ref-eng/goals/G-ORG2-REF-002/PLAN.md` | `a7dcb805b56eb185593f845e00aa11f490f0b17334b35ea4c07342e118086831` |
| `ref-eng/goals/G-ORG2-REF-002/TASKS.md` | `c344ba12598e9ea627d86b9fb42e8ba20c841323aa3a7d03ae2205d2dba06e65` |

##### Observed

- `ctxq` supplied the canonical heading identities for every Markdown target.
- All 179 local links across the nine technical/index subjects resolved through 21 Markdown target files.
- The accepted source revision and diff-hygiene checks passed.
- The four focused technical records and three refined technical owners retain their RUN001 hashes, so RUN001's passed direct-source samples remain current.
- The atlas changed only its coverage-matrix anchor. The index changed heading anchors and final lifecycle status. Goal and Task changes settle the accepted result.
- No unresolved required contradiction or missing obligation remains.

##### Rationale

RUN001 established content depth and direct-source support but failed the local-link criterion. DEC004 bounded the correction to link identities and lifecycle settlement. This Run proves that delta without repeating source traversal. The combined RUN001 source evidence and RUN002 current subject states satisfy the covered criteria and checkpoint condition.

##### Evidence

- G-ORG2-REF-002-VER002-RUN001
- G-ORG2-REF-002-DEC004
- `ctxq outline` identities for 21 Markdown targets
- Local link-validation output for 179 links
