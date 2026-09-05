---
type: interface-record
name: org2-ui-grounding-seams
description: Caller-callee and trust contracts for Canvas selection/revision and Browser DOM-to-source inspection.
tags: [org2, interfaces, canvas, browser, ui-grounding]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
current_upstream_revision: 6f56a34036d7cd2443da0fc8acb9a5ad0e208b40
status: active
---

# ORG2 UI grounding seams

## 1. Agent → Canvas event

**Caller:** native agent tool execution  
**Callee:** Canvas event/projection pipeline

Contract:

- `render_inline_canvas` creates an addressable Canvas version.
- the returned event id is the revision identity for later `revise_inline_canvas` calls;
- tool acceptance does not assert visual success;
- source-backed modes are `html`, `a2ui`, and `react`; `url` is an external action.

## 2. Canvas renderer → execution containment

| Mode | Render boundary | Inspection consequence |
| --- | --- | --- |
| HTML | open ShadowRoot in application document | parent inspector can traverse through `composedPath()` / open shadow roots |
| A2UI | application React tree | parent inspector sees rendered DOM |
| React | sandboxed iframe, scripts only, opaque origin | parent Canvas inspector cannot directly traverse artifact internals |
| URL | external-open action | Canvas Design mode is unavailable |

The React containment boundary is intentional security architecture. Source grounding must not require `allow-same-origin` or Tauri exposure to the artifact.

## 3. Pointer → CanvasDesignSelection

**Caller:** user pointer in Canvas Design mode  
**Callee:** `useCanvasDesignInspector` / `canvasDomCapture`

Inputs:

- root-local pointer event;
- current Canvas DOM;
- optional drag region.

Outputs:

- element or region selection;
- runtime rect/selector/XPath/role/text/style metadata;
- optional preview HTML;
- target summaries for a region.

Invariant: inspection consumes the click while active; artifact handlers should not execute as a side effect of selecting a target.

Limit: `sourceLocation` is null in Canvas capture.

## 4. Canvas selection → model-facing design request

**Caller:** `CanvasDesignPrompt`  
**Callee:** workspace chat / agent execution

The agent receives a compound grounding envelope:

```text
human instruction
+ Canvas event/session identity
+ runtime DOM selection
+ current Canvas source
+ optional sanitized preview
```

The display message contains a `dom-component` pill; the model-facing message removes preview-only HTML and explicitly labels the current Canvas source as untrusted data.

Invariant: the request targets one existing Canvas event and tells the agent to call `revise_inline_canvas` rather than create an unrelated Canvas.

## 5. Agent → revise_inline_canvas

Localized revision contract:

- `find` must match current materialized source;
- default requires exactly one match;
- `all=true` is an explicit opt-in to replace every occurrence;
- structural changes can supply complete replacement content instead;
- target event must belong to the current session and identify a Canvas event.

This turns the agent's inferred DOM-to-source association into a bounded, validated source mutation rather than an unrestricted patch.

## 6. Browser UI → inspected webview

**Caller:** `useWebviewInspector`  
**Callee:** Browser crate Tauri commands / inspected webview

Commands include enabling/disabling/toggling inspect mode, clearing selection, and reading selected element info.

The Browser crate injects ORGII-owned inspector scripts into the inspected page. The page-side inspector owns hover/select overlays and exports bounded element metadata for retrieval by the host.

This is application instrumentation of a webview, not invocation of the native WebKit/Chromium DevTools element picker.

## 7. Browser DOM element → source hint

`getSourceLocation` applies ordered strategies:

1. explicit `data-insp-path`;
2. common debug/source attributes;
3. React fiber development metadata and component stack;
4. Vue file metadata;
5. Svelte development metadata;
6. styled-component naming hints.

A result can be exact (`path`, `line`, `column`) or partial (`componentName`, `searchHint`). Consumers must preserve that distinction.

## 8. Source hint → repository candidate

Active `useSourceNavigation` no longer invokes the retired repository-wide `ui-indexer`.

When exact source is unavailable it performs bounded filename and content search in the selected repository, ranks candidates, and returns a small candidate set. Opening a file uses the resolved repository-relative/absolute path and best available line.

**Invariant:** a component-name match is a navigation candidate, not proof that the selected DOM node originated from that file.

## 9. Diagnostics seam

Native WKWebView/WebKitGTK/WebView2 developer tools may inspect console/network/runtime/layout behavior, but those tools are not a semantic contract between ORG2 selection and source ownership.

Keep diagnostics and grounding separate:

```text
Grounding: rendered target → semantic/source target
Diagnostics: runtime/webview → failure/performance evidence
```

## Failure boundaries

- missing framework debug metadata → sourceLocation can be partial or null;
- no bounded repository match → Browser cannot offer a reliable source candidate;
- React Canvas iframe → parent Canvas selector cannot inspect artifact descendants;
- stale Canvas source → exact revision edit is rejected when `find` no longer matches;
- ambiguous edit → non-`all` revision is rejected when `find` matches multiple occurrences.

## Extension constraint

A future cross-iframe Canvas inspector should use a narrow message/anchor protocol from the sandboxed artifact to the parent. Relaxing the opaque-origin boundary merely to obtain DOM access would couple source grounding to a weaker security posture.