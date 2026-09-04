---
type: goal
name: G-ORG2-DOMAIN-001
description: Establish a source-grounded bounded-context model for ORG2 without redesigning the product.
tags: [org2, domain-model, bounded-contexts, ua]
---

# G-ORG2-DOMAIN-001 — Build the ORG2 bounded-context model

**State:** completed
**Confirmed by:** requester
**Confirmed at:** 2026-09-04T01:18:16Z
**Confirmation authority basis:** The requester approved the proposed curated `ref-eng/domain-models/` structure and instructed the agent to proceed.
**Completed by:** agent:chatgpt:gpt-5.6-sol
**Completed at:** 2026-09-04T01:26:52Z
**Completion authority basis:** G-ORG2-DOMAIN-001-VER001-RUN001 and G-ORG2-DOMAIN-001-VER002-RUN001 passed the declared structure/evidence and model-consistency criteria.

## Outcome

ORG2 has a curated, source-grounded bounded-context model that distinguishes core/supporting contexts, edge contexts, shared scopes, and infrastructure; assigns one semantic owner to canonical entities; defines terminology and context contracts; and maps the logical model back to representative implementation paths.

## Success criteria

### G-ORG2-DOMAIN-001-SC001 — Evidence-bound context classification

The model records why UA's five promoted domains are insufficient as an exhaustive bounded-context model and derives the accepted context classification from the verified UA snapshot plus source-grounded reference records.

**Verified by:** G-ORG2-DOMAIN-001-VER001

### G-ORG2-DOMAIN-001-SC002 — Explicit semantic ownership

Canonical entities and lifecycle concepts have one semantic owner, and the model explicitly distinguishes references/projections from ownership.

**Verified by:** G-ORG2-DOMAIN-001-VER002

### G-ORG2-DOMAIN-001-SC003 — Stable ubiquitous language and relationships

The corpus prevents known collisions such as Org Task vs Work Item, Agent Org vs Project/Cloud Org, Agent Session vs Session Record, and Workspace vs Project vs Repository, and records the major context translation contracts.

**Verified by:** G-ORG2-DOMAIN-001-VER002

### G-ORG2-DOMAIN-001-SC004 — Architecture remains separate

The bounded-context model links to but does not restructure existing architecture/runtime/data records or generated UA/Graphify outputs.

**Verified by:** G-ORG2-DOMAIN-001-VER001

## Boundaries

- Pin the model to ORG2 source revision `b315ba4f82fb1fe294496793d7322095e7efe262`.
- Author only under `ref-eng/`.
- Do not mutate `.understand-anything/`, `graphify-out/`, or tracked product source.
- Treat context classification as Derived unless direct source explicitly defines the same boundary.
- Preserve `core-entities.md` as the source-grounded entity inventory; do not replace it with a monolithic new entity document.
- Do not infer that physical package placement equals logical domain ownership.
- Model current behavior before recommending source-code reorganization.

## Dependencies

- G-ORG2-REINDEX-001 — accepted UA/Graphify evidence.
- G-ORG2-REF-001 — source-grounded architecture/entity baseline.
- G-ORG2-REF-002 — graph-guided domain/runtime slices.

## Decisions

### G-ORG2-DOMAIN-001-DEC001 — Curate the model under ref-eng

**State:** accepted
**Statement:** Keep UA and Graphify generated outputs immutable and place the canonical interpretation under `ref-eng/domain-models/`.
**Accepted by:** requester
**Accepted at:** 2026-09-04T01:18:16Z

### G-ORG2-DOMAIN-001-DEC002 — Separate bounded contexts from edge contexts and infrastructure

**State:** accepted
**Statement:** Model the eight product contexts separately from Channel Gateway and External Artifact Import edge contexts, and keep Git/terminal/browser/LSP/search/storage/security capabilities below the domain boundary.
**Accepted by:** requester
**Accepted at:** 2026-09-04T01:18:16Z

### G-ORG2-DOMAIN-001-DEC003 — One semantic owner per canonical concept

**State:** accepted
**Statement:** Use explicit entity ownership and translation contracts rather than a global entity model that merges nearby identities.
**Accepted by:** requester
**Accepted at:** 2026-09-04T01:18:16Z
