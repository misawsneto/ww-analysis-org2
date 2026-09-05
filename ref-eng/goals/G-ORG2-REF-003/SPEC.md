---
type: specification
name: G-ORG2-REF-003-SPEC001
description: Requirements for the ORG2 prototyping and UI-grounding implementation reference.
tags: [org2, implementation-reference, specification, ui-grounding]
---

# G-ORG2-REF-003-SPEC001 — UI prototyping and grounding requirements

**Goal:** G-ORG2-REF-003  
**Version:** 1  
**State:** completed

## Requirements

### REQ001 — Canvas render model

Explain `html`, `a2ui`, `react`, and `url` rendering boundaries and Canvas event/revision identity.

### REQ002 — Canvas selection

Explain capture-phase pointer selection, Shadow DOM handling, element/region capture, and the runtime metadata emitted by Canvas Design mode.

### REQ003 — Model-facing grounding

Explain how event identity, selected DOM metadata, current Canvas source, preview material, and human instruction are composed into the revision request.

### REQ004 — Revision safety

Explain exact-match localized edits, ambiguity rejection, target-event validation, and full-source structural replacement.

### REQ005 — Browser inspected-webview path

Explain Browser Tauri inspect commands, injected inspector scripts, source-location detection methods, and host polling.

### REQ006 — Active source navigation

Verify the current source-navigation implementation and explicitly settle whether `ui-indexer` is active, historical, or both.

### REQ007 — Diagnostics boundary

Distinguish application-level UI grounding from platform browser/webview developer tools.

### REQ008 — Known-limit verification

Re-check the React iframe boundary and Canvas `sourceLocation` behavior against current upstream `develop` without mutating the pinned UA/Graphify evidence revision.

### REQ009 — Evidence discipline

Separate Source-observed, Derived, and future-design implications. Do not describe proposed source anchors or iframe bridges as current ORG2 behavior.