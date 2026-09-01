---
type: goal
name: G-ORG2-REINDEX-001
description: Rebuild the ORG2 Graphify and Understand Anything indexes at the accepted develop revision.
tags: [org2, indexing, graphify, understand-anything]
---

# G-ORG2-REINDEX-001 — Reindex ORG2

**State:** complete  
**Confirmed by:** requester  
**Confirmed at:** 2026-08-30T13:51:51Z  
**Confirmation authority basis:** The requester instructed the agent to proceed after aligning `develop` with `origin/develop`.  
**Completed by:** agent:codex:gpt-5.6-sol  
**Completed at:** 2026-08-30T16:17:41Z  
**Completion authority basis:** The requester authorized continuation of the active reindex goal, and the current deterministic verification runs passed all success criteria.

## Outcome

ORG2 has current, separate Graphify and Understand Anything indexes for commit `b315ba4f82fb1fe294496793d7322095e7efe262`.

## Success criteria

### G-ORG2-REINDEX-001-SC001 — Current structural index

`graphify-out/graph.json` and `graphify-out/GRAPH_REPORT.md` describe the accepted commit and pass the Graphify integrity checks.

**Verified by:**
- G-ORG2-REINDEX-001-VER001

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REINDEX-001-SC002 — Current semantic indexes

The legacy `.understand-anything/` directory contains a knowledge graph, domain graph, fingerprints, and metadata for the accepted commit, with complete approved file coverage and valid references.

**Verified by:**
- G-ORG2-REINDEX-001-VER002

**Waived by:** none  
**Supersedes:** none

### G-ORG2-REINDEX-001-SC003 — Recoverable replacement

The prior Graphify and UA outputs remain recoverable until their replacements pass the required checks.

**Verified by:**
- G-ORG2-REINDEX-001-VER003

**Waived by:** none  
**Supersedes:** none

## Boundaries

- Do not change tracked ORG2 product source.
- Keep Graphify and UA schemas separate.
- Use only toolkit-owned runtimes and target-local attachment links.
- Use only Haiku, Sonnet, Terra, or Luna for UA semantic passes.
- Exclude generated index outputs from all source scans.

## Decisions

### G-ORG2-REINDEX-001-DEC001 — Rebuild at the aligned revision

**State:** accepted  
**Statement:** Rebuild both indexes at `b315ba4f82fb1fe294496793d7322095e7efe262` after preserving the prior tracked state on `safety/pre-force-update-develop-20260828-e24957c`.  
**Accepted by:** requester  
**Accepted at:** 2026-08-30T13:51:51Z  
**Authority basis:** The requester approved hard alignment and then instructed the agent to proceed with reindexing.

**Waives:**
- none

**Supersedes:** none
