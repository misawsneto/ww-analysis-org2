---
type: plan
name: G-ORG2-DOMAIN-001-PLAN001
description: Plan for deriving and publishing the ORG2 bounded-context model.
tags: [org2, domain-model, plan]
---

# G-ORG2-DOMAIN-001-PLAN001 — Publish the bounded-context model

**Goal:** G-ORG2-DOMAIN-001
**Version:** 1
**State:** completed

## Sequence

1. Reconcile UA's five domains with the source-grounded entity inventory and broader UA source coverage.
2. Publish the context map, terminology, entity ownership, relationships, and source map.
3. Publish one record for each product context, edge context, and infrastructure/shared-scope classification.
4. Update the reference index and preserve `core-entities.md` as source-observed inventory.
5. Run the two declared verifications and settle the goal.

## Stop conditions

- Stop before any generated UA/Graphify mutation.
- Stop before tracked product-source mutation.
- Mark a context conclusion Derived when source establishes behavior but not the context boundary itself.
