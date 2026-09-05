---
type: evidence-record
name: G-ORG2-REF-003-ui-grounding
description: Source observations and current-upstream verification for ORG2 Canvas prototyping, UI selection, Browser grounding, and webview diagnostics.
tags: [org2, evidence, canvas, browser, ui-grounding]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
current_upstream_revision: 6f56a34036d7cd2443da0fc8acb9a5ad0e208b40
status: accepted
---

# G-ORG2-REF-003 — UI grounding evidence

## Question

How does ORG2 ground a user-selected prototype/browser UI element, and does it rely on WebKit/DevTools for selection or source mapping?

## Observation matrix

| Finding | State | Representative evidence |
| --- | --- | --- |
| Canvas supports html/url/a2ui/react prototype modes | Source-observed | `render_inline_canvas.rs`, `CanvasPreviewSurface.tsx` |
| Static HTML renders in an open ShadowRoot | Source-observed | `CanvasPreviewSurface.tsx` |
| React Canvas executes in a scripts-only sandboxed iframe with opaque origin | Source-observed | `ReactArtifactRunner.tsx` |
| Canvas Design selection uses capture-phase DOM pointer handlers and `composedPath()` | Source-observed | `useCanvasDesignInspector.ts` |
| Canvas capture includes selector/XPath/geometry/styles/text but emits `sourceLocation: null` | Source-observed | `canvasDomCapture.ts` |
| Canvas design requests combine selection metadata, event identity, and current Canvas source | Source-observed | `CanvasDesignSurface.tsx`, `domComponentPayload.ts` |
| `revise_inline_canvas` validates exact source edits | Source-observed | `render_inline_canvas.rs` |
| Browser inspect mode is implemented through ORGII Tauri commands and injected scripts | Source-observed | `useWebviewInspector.ts`, browser crate inspector scripts |
| Browser source detection probes explicit instrumentation and framework debug metadata | Source-observed | `inspector-source-loc.js` |
| Active Browser source navigation uses bounded filename/content search | Source-observed/current-upstream | `useSourceNavigation.ts` |
| repository-wide `ui-indexer` is retired from the active Browser navigation path | Source-observed/current-upstream | comment and implementation in `useSourceNavigation.ts`; archived implementation remains under `.archive` |
| Native webview DevTools is not the product UI-grounding authority | Derived | Canvas and Browser selection are implemented by ORGII code independent of platform DevTools |
| React Canvas Design cannot inspect iframe descendants through the parent selector | Derived | Design is offered for React; renderer is opaque iframe; selector is attached to parent Canvas DOM; no verified bridge |

## Correction to earlier analysis

An earlier exploratory reading treated `ui-indexer` as the current Browser source-grounding backend because the Rust workspace still contained/documented the crate at the pinned mirror revision. Current upstream source shows that the repository-wide component index has since been retired from the active Browser navigation path and preserved under `.archive`.

The current architecture is therefore:

```text
runtime source metadata when available
        ↓
component/search hint when necessary
        ↓
bounded filename + content search
        ↓
ranked source candidates
```

This correction is material and is reflected in the architecture and interface records created by this goal.

## Current-upstream verification

Checked upstream ORG2 `develop` at `6f56a34036d7cd2443da0fc8acb9a5ad0e208b40`.

The following remained true:

1. `CanvasApp` permits Design mode for non-URL, non-streaming React Canvas.
2. `canvasDomCapture` still sets `sourceLocation: null`.
3. `ReactArtifactRunner` still uses an opaque-origin sandboxed iframe.
4. active `useSourceNavigation` uses bounded search and states that the repository-wide component index is retired.
5. Browser source-location detection still uses explicit debug attributes/framework metadata before search fallback.

No later source change was found that closes the React Canvas iframe-selection gap or adds deterministic Canvas source spans.

## Source paths

Pinned mirror/current upstream representative paths:

- `src/engines/Simulator/apps/canvas/CanvasApp.tsx`
- `src/engines/Simulator/apps/canvas/design/CanvasDesignSurface.tsx`
- `src/engines/Simulator/apps/canvas/design/useCanvasDesignInspector.ts`
- `src/engines/Simulator/apps/canvas/design/canvasDomCapture.ts`
- `src/engines/ChatPanel/blocks/CanvasInlineCard/CanvasPreviewSurface.tsx`
- `src/engines/ChatPanel/blocks/CanvasInlineCard/ReactArtifactRunner.tsx`
- `src/features/DomSelection/domComponentPayload.ts`
- `src/modules/WorkStation/Browser/hooks/useWebviewInspector.ts`
- `src/modules/WorkStation/Browser/hooks/useSourceNavigation.ts`
- `src-tauri/crates/browser/src/scripts/js/inspector-element-info.js`
- `src-tauri/crates/browser/src/scripts/js/inspector-source-loc.js`
- `src-tauri/crates/agent-core/src/specialization/tools/render_inline_canvas.rs`

## Accepted conclusion

ORG2 uses **product-level DOM/webview instrumentation** for UI selection and grounding. Platform WebKit/WebView DevTools are diagnostics, not the semantic grounding protocol. Canvas has strong runtime/artifact grounding but lacks deterministic source-location mapping; React Canvas additionally crosses an isolation boundary that the parent Canvas selector cannot traverse in the verified implementation.