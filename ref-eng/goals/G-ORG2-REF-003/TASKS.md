---
type: tasks
name: G-ORG2-REF-003-tasks
description: Completed tasks for the ORG2 UI prototyping and grounding reference.
tags: [org2, implementation-reference, tasks, ui-grounding]
---

# Tasks — G-ORG2-REF-003

## TASK001 — Trace Canvas prototype execution

**State:** completed

- Identify Canvas modes and containment boundaries.
- Trace event identity and revision materialization.
- Record exact-edit validation behavior.

## TASK002 — Trace Canvas Design selection

**State:** completed

- Inspect pointer interception, Shadow DOM handling, region selection, geometry refresh, and DOM capture.
- Confirm Canvas `sourceLocation` behavior.
- Trace the model-facing `dom-component` revision payload.

## TASK003 — Trace Browser grounding

**State:** completed

- Inspect Browser host hook and Tauri commands.
- Inspect injected element/source-location scripts.
- Verify exact/partial source hint behavior.
- Verify the active source-navigation fallback.

## TASK004 — Verify current upstream limits

**State:** completed

- Re-check React Design availability.
- Re-check opaque iframe containment.
- Re-check Canvas `sourceLocation: null`.
- Confirm no verified Canvas cross-iframe selection bridge.
- Correct active `ui-indexer` classification.

## TASK005 — Publish and verify

**State:** completed

- Publish architecture, interface, evidence, goal, specification, plan, task, and verification records.
- Keep all mutations inside `ref-eng/`.