---
type: verification
name: G-ORG2-REINDEX-001-verifications
description: Deterministic proof for the completed ORG2 Graphify and Understand Anything reindex.
tags: [org2, indexing, verification, graphify, understand-anything]
---

# Verifications — G-ORG2-REINDEX-001

## G-ORG2-REINDEX-001-VER001 — Verify the current structural index

**Version:** 1  
**State:** active  
**Supersedes:** none  
**Mode:** deterministic  
**Evaluator mode:** deterministic  
**Waived by:** none

**Covers:**
- G-ORG2-REINDEX-001-SC001

**Subjects:**
- `graphify-out/graph.json`
- `graphify-out/GRAPH_REPORT.md`

### Criteria

- The graph records the accepted commit, has unique nodes and valid edge endpoints, and excludes generated index and `ref-eng/` paths.

### Procedure

1. Parse the graph and compare `built_at_commit` with the accepted commit.
2. Check node identity, edge endpoints, self-loops, excluded paths, graph counts, and artifact digests.

### Expected

The structural graph passes all checks and its report exists at the verified digest.

### Runs

#### G-ORG2-REINDEX-001-VER001-RUN001

**Verification version:** 1  
**Result:** pass  
**Executed by:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-30T16:17:41Z  
**Authority basis:** none

##### Subject snapshots

- `graphify-out/graph.json` @ `c5176303cb7d7036cb28ce144b58410122388299ba709177e65e3526c1cce62a`
- `graphify-out/GRAPH_REPORT.md` @ `6ee6202cf73fe4d4a104154c962a5942e29c39f6782ff8c4cfd3e7c6b840e3bd`
- ORG2 @ `b315ba4f82fb1fe294496793d7322095e7efe262`

##### Observed

The graph has 73,483 nodes, 180,803 edges, 2,134 communities, no dangling edges, no self-loops, and no forbidden index or bookkeeping paths.

##### Rationale

The deterministic checks matched the structural-index criterion.

##### Evidence

- `ref-eng/goals/G-ORG2-REINDEX-001/artifacts/verification-run-001.json`

## G-ORG2-REINDEX-001-VER002 — Verify the current semantic indexes

**Version:** 1  
**State:** active  
**Supersedes:** none  
**Mode:** deterministic  
**Evaluator mode:** deterministic  
**Waived by:** none

**Covers:**
- G-ORG2-REINDEX-001-SC002

**Subjects:**
- `.understand-anything/knowledge-graph.json`
- `.understand-anything/domain-graph.json`
- `.understand-anything/fingerprints.json`
- `.understand-anything/meta.json`

### Criteria

- The semantic artifacts record the accepted commit, cover every approved file, and contain valid node, edge, layer, tour, domain, flow, step, fingerprint, and import references.

### Procedure

1. Compare semantic metadata and file coverage with the canonical 6,911-file scan.
2. Validate graph identities, edge endpoints, deterministic imports, layer assignments, tour references, fingerprints, and the domain hierarchy.

### Expected

All semantic artifacts pass the required checks with no missing approved files or invalid references.

### Runs

#### G-ORG2-REINDEX-001-VER002-RUN001

**Verification version:** 1  
**Result:** pass  
**Executed by:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-30T16:17:41Z  
**Authority basis:** none

##### Subject snapshots

- `.understand-anything/knowledge-graph.json` @ `c77472fa5dad35e4b1c8525297bde19988c62110437303c8988c9740f521efdd`
- `.understand-anything/domain-graph.json` @ `17d7d7ced5542a1bec91c55c8e81fdb438ffec31ffad70db4ea92e5a5da4fe13`
- `.understand-anything/fingerprints.json` @ `8f7630061db016dd1a5f59f66dc4258c48db5fdbc3b8051da21c3f74baf50af4`
- `.understand-anything/meta.json` @ `47d616c247c1672bc608f427f8b3e8093922f62321dcd5139bbac5c31265b699`
- ORG2 @ `b315ba4f82fb1fe294496793d7322095e7efe262`

##### Observed

The knowledge graph has 29,271 nodes, 50,036 edges, 9 layers, 10 tour steps, all 6,911 approved files, and all 8,552 canonical imports. The domain graph has 5 domains, 16 flows, and 48 graph-backed steps. All 6,911 files have fingerprints. The deterministic reviews found no issues.

The review recorded 639 orphan-node warnings. The bulk Luna pass also produced generic or repeated summaries for 2,430 file paths. These limits do not remove file coverage, symbol data, import edges, layer assignments, tour references, or domain evidence.

##### Rationale

The required semantic coverage and reference checks passed. The recorded quality limits do not violate this goal's completion criterion.

##### Evidence

- `ref-eng/goals/G-ORG2-REINDEX-001/artifacts/verification-run-001.json`
- `.understand-anything/intermediate/review.json`
- `.understand-anything/intermediate/domain-review.json`

## G-ORG2-REINDEX-001-VER003 — Verify recoverable replacement

**Version:** 1  
**State:** active  
**Supersedes:** none  
**Mode:** deterministic  
**Evaluator mode:** deterministic  
**Waived by:** none

**Covers:**
- G-ORG2-REINDEX-001-SC003

**Subjects:**
- `ref-eng/index-archives/e24957c-20260830/graphify-out/graph.json`
- `.understand-anything/archive-e24957c-20260830/`
- `safety/pre-force-update-develop-20260828-e24957c`

### Criteria

- The prior index files retain their pre-move digests, and the safety branch remains available.

### Procedure

1. Compare the archived Graphify and UA graph digests with the recorded pre-move values.
2. Confirm that the safety branch still exists.

### Expected

The prior index state remains recoverable after the replacement passes verification.

### Runs

#### G-ORG2-REINDEX-001-VER003-RUN001

**Verification version:** 1  
**Result:** pass  
**Executed by:** agent:codex:gpt-5.6-sol  
**Executed at:** 2026-08-30T16:17:41Z  
**Authority basis:** none

##### Subject snapshots

- Archived Graphify graph @ `fd93b079fed3878eced7b2caa017e6489df6eb01feea1ec935a6ad5626ac2935`
- Archived UA knowledge graph @ `2d5663b73b3357238060ec8ab990b8d70ca4207e77ccc31bbcf9411dd205bd95`
- Archived UA domain graph @ `c2993e3e2c750d9d342b2d60c1e8e4d85c0bcfc99dcf61ec48abce6f2b8a80e5`

##### Observed

All archive digests match, and `safety/pre-force-update-develop-20260828-e24957c` exists.

##### Rationale

The previous index and tracked source states remain available for recovery.

##### Evidence

- `ref-eng/goals/G-ORG2-REINDEX-001/artifacts/verification-run-001.json`
- `ref-eng/index-archives/e24957c-20260830/pre-move-sha256.txt`
