---
type: plan
name: G-ORG2-REF-003-PLAN001
description: Bounded source investigation and publication plan for UI prototyping and grounding.
tags: [org2, implementation-reference, plan, ui-grounding]
---

# G-ORG2-REF-003-PLAN001 — Trace and publish UI grounding

**Goal:** G-ORG2-REF-003  
**Version:** 1  
**State:** completed

## Sequence

1. Trace Canvas tool → event → renderer → Design selection → model request → revision.
2. Trace Browser inspect toggle → injected webview inspector → selected element → source-location detection → source navigation.
3. Inspect React artifact containment and compare it with the parent Canvas selection boundary.
4. Verify whether `ui-indexer` is active in current upstream source.
5. Separate product grounding from native webview DevTools diagnostics.
6. Publish architecture, interface, and evidence records.
7. Run one structural/source check and one semantic/limit check.

## Stop conditions

- Stop before source-code mutation.
- Stop before repinning generated UA/Graphify artifacts.
- Do not infer cross-iframe reachability merely from Design mode availability.
- Correct prior exploratory conclusions when current source contradicts them.