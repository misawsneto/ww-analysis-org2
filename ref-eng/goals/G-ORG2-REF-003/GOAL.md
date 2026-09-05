---
type: goal
name: G-ORG2-REF-003
description: Explain ORG2 prototyping, UI selection, source grounding, and webview diagnostic boundaries.
tags: [org2, implementation-reference, canvas, browser, ui-grounding]
---

# G-ORG2-REF-003 — Explain UI prototyping and grounding

**State:** completed  
**Confirmed by:** requester  
**Confirmed at:** 2026-09-05T03:42:00Z  
**Confirmation authority basis:** The requester asked to investigate prototyping/UI selection/grounding, accepted the verified direction, and instructed the agent to proceed.  
**Completed by:** agent:chatgpt:gpt-5.6-sol  
**Completed at:** 2026-09-05T03:42:00Z  
**Completion authority basis:** G-ORG2-REF-003-VER001-RUN001 and G-ORG2-REF-003-VER002-RUN001 satisfy the declared source, boundary, correction, and current-upstream checks.

## Outcome

The implementation reference now explains Canvas prototype rendering and revision, Canvas DOM selection, Browser inspected-webview selection and source hinting, active source-navigation fallback, native webview diagnostic boundaries, and the two material Canvas grounding limits.

## Success criteria

### SC001 — Prototype and revision path

Document all Canvas modes, render containment, event/revision identity, and validated localized revision behavior.

### SC002 — Selection and grounding path

Document how Canvas and Browser selection capture runtime identity and how that identity reaches source/artifact grounding.

### SC003 — Diagnostics boundary

Explicitly distinguish ORGII product selection/grounding from platform WKWebView/WebKitGTK/WebView2 DevTools.

### SC004 — Known limits and current verification

Record deterministic Canvas source-location absence, React iframe selection boundary, and re-check both against current upstream `develop`.

### SC005 — Correct stale ui-indexer inference

Record that active Browser source navigation uses bounded search and that the repository-wide `ui-indexer` path is retired/currently archived upstream.

## Boundaries

- Do not redesign ORG2 source.
- Author only in `ref-eng/`.
- Keep the accepted `b315...` source revision as the primary corpus anchor.
- Record current-upstream checks separately rather than silently repinning UA/Graphify evidence.
- Label cross-source architectural conclusions Derived.
- Label future source-anchor/postMessage ideas as design implications, not current behavior.

## Dependencies

- G-ORG2-REF-001 — source-grounded architecture baseline.
- G-ORG2-REF-002 — graph-guided capability/runtime atlas.
- G-ORG2-DOMAIN-001 — semantic context model used to keep Browser/Canvas infrastructure separate from domain ownership.

## Decisions

### DEC001 — Keep selection and DevTools separate

**State:** accepted  
**Statement:** Treat DOM/webview UI grounding as product instrumentation and native WebView DevTools as an orthogonal diagnostics channel.

### DEC002 — Preserve the React sandbox boundary

**State:** accepted  
**Statement:** Treat the opaque-origin React Canvas iframe as an intentional trust boundary; do not recommend weakening it merely to enable selection.

### DEC003 — Correct active source navigation

**State:** accepted  
**Statement:** Describe current Browser source navigation as source-hint detection followed by bounded filename/content search, not as active `ui-indexer` lookup.