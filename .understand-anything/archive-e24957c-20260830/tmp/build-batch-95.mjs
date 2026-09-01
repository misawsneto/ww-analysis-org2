import fs from 'fs';

const BASE = "src/modules/WorkStation/Browser/Panels/BrowserSecondaryPanel/components/WebDevTools/components/";
const WDT = "src/modules/WorkStation/Browser/Panels/BrowserSecondaryPanel/components/WebDevTools/";
const WI = "src/modules/WorkStation/Browser/Panels/BrowserSecondaryPanel/components/WebInspector/index.tsx";
const SHARED = "src/modules/WorkStation/Browser/shared/SharedBrowserDevToolsPanel.tsx";

const p = {
  editableStyleRow: BASE + "CSSPanel/EditableStyleRow.tsx",
  styleSection: BASE + "CSSPanel/StyleSection.tsx",
  cssPanel: BASE + "CSSPanel/index.tsx",
  consoleTab: BASE + "ConsoleTab/index.tsx",
  domNodeRow: BASE + "DOMTreeContent/DOMTreeNodeRow.tsx",
  domIndex: BASE + "DOMTreeContent/index.tsx",
  domTypes: BASE + "DOMTreeContent/types.ts",
  domUtils: BASE + "DOMTreeContent/utils.ts",
  boxModel: BASE + "DesignPanel/BoxModelDiagram.tsx",
  collapsible: BASE + "DesignPanel/CollapsibleSection.tsx",
  editableField: BASE + "DesignPanel/EditableField.tsx",
  layoutButtons: BASE + "DesignPanel/LayoutButtons.tsx",
  linkedInput: BASE + "DesignPanel/LinkedInputPair.tsx",
  spacingIcons: BASE + "DesignPanel/SpacingIcons.tsx",
  designPanel: BASE + "DesignPanel/index.tsx",
  networkTab: BASE + "NetworkTab/index.tsx",
  sourcePanel: BASE + "SourcePanel/index.tsx",
  styleEditsFooter: BASE + "StyleEditsFooter.tsx",
  hook: WDT + "hooks/useWebDevToolsElementsPanel.ts",
  wdtIndex: WDT + "index.tsx",
  wdtTypes: WDT + "types.ts",
  webInspector: WI,
  shared: SHARED,
};

const nodes = [];
const edges = [];

function fileNode(path, name, summary, tags, complexity, languageNotes) {
  const n = {
    id: "file:" + path,
    type: "file",
    name,
    filePath: path,
    summary,
    tags,
    complexity,
  };
  if (languageNotes) n.languageNotes = languageNotes;
  nodes.push(n);
}

function fnNode(path, fnName, lineRange, summary, tags, complexity) {
  nodes.push({
    id: `function:${path}:${fnName}`,
    type: "function",
    name: fnName,
    filePath: path,
    lineRange,
    summary,
    tags,
    complexity,
  });
}

function edge(source, target, type, weight) {
  edges.push({ source, target, type, direction: "forward", weight });
}

// ---- File nodes ----
fileNode(p.editableStyleRow, "EditableStyleRow.tsx",
  "Renders a single editable CSS declaration row (property/value pair) in the DevTools CSS panel, allowing inline editing of a style value.",
  ["component", "css-panel", "dev-tools", "editable-field"], "moderate");

fileNode(p.styleSection, "StyleSection.tsx",
  "Groups a set of EditableStyleRow entries into a titled CSS rule section within the DevTools CSS panel.",
  ["component", "css-panel", "dev-tools", "container"], "moderate");

fileNode(p.cssPanel, "index.tsx",
  "Top-level CSS panel component that renders the matched/computed style sections for the currently selected DOM element in the embedded web inspector.",
  ["component", "css-panel", "dev-tools", "panel"], "moderate");

fileNode(p.consoleTab, "index.tsx",
  "Renders the Console tab of the embedded web DevTools, listing console log entries with expandable messages/stack traces, level-based styling, and copy-to-clipboard support.",
  ["component", "console", "dev-tools", "logging"], "complex");

fileNode(p.domNodeRow, "DOMTreeNodeRow.tsx",
  "Renders a single row of the DOM tree browser, showing tag name, attributes, and expand/collapse/select controls for one DOM node.",
  ["component", "dom-tree", "dev-tools", "row"], "moderate");

fileNode(p.domIndex, "index.tsx",
  "Virtualized DOM tree browser that flattens and renders the inspected page's DOM hierarchy, handling node selection, expansion, and auto-scroll-to-element.",
  ["component", "dom-tree", "dev-tools", "virtualization"], "complex");

fileNode(p.domTypes, "types.ts",
  "Type definitions for the DOM tree view (node shape, expansion state) shared between the DOM tree renderer and its row/utility helpers.",
  ["type-definition", "dom-tree", "dev-tools"], "simple");

fileNode(p.domUtils, "utils.ts",
  "Utility functions for flattening a nested DOM tree into a display list and computing xpath-based ancestor paths for auto-expansion/navigation.",
  ["utility", "dom-tree", "dev-tools"], "simple");

fileNode(p.boxModel, "BoxModelDiagram.tsx",
  "Visual box-model diagram (margin/border/padding/content) for the selected element, mirroring browser DevTools' box model inspector.",
  ["component", "design-panel", "dev-tools", "visualization"], "moderate");

fileNode(p.collapsible, "CollapsibleSection.tsx",
  "Reusable collapsible/expandable section container with an optional nested SubSection, used to organize groups of controls in the Design and Source panels.",
  ["component", "design-panel", "dev-tools", "layout"], "moderate");

fileNode(p.editableField, "EditableField.tsx",
  "Inline-editable text/number field control used throughout the Design panel for editing CSS property values.",
  ["component", "design-panel", "dev-tools", "editable-field"], "moderate");

fileNode(p.layoutButtons, "LayoutButtons.tsx",
  "Button group for toggling the CSS layout mode (e.g. flex/grid/block) on the selected element from the Design panel.",
  ["component", "design-panel", "dev-tools", "layout"], "moderate");

fileNode(p.linkedInput, "LinkedInputPair.tsx",
  "Paired numeric input control (e.g. horizontal/vertical spacing values) that can be linked to edit both values together, with directional spacing icons.",
  ["component", "design-panel", "dev-tools", "editable-field"], "complex");

fileNode(p.spacingIcons, "SpacingIcons.tsx",
  "Small SVG icon components representing top/bottom/left/right spacing directions, used by the spacing controls in the Design panel.",
  ["component", "icon", "design-panel", "dev-tools"], "moderate");

fileNode(p.designPanel, "index.tsx",
  "Main Design panel component composing the box-model diagram, spacing controls, and editable style fields into a visual CSS editor for the selected element.",
  ["component", "design-panel", "dev-tools", "panel"], "complex");

fileNode(p.networkTab, "index.tsx",
  "Renders the Network tab of the embedded DevTools, listing captured network requests with status, duration, and formatted size.",
  ["component", "network", "dev-tools", "table"], "moderate");

fileNode(p.sourcePanel, "index.tsx",
  "Displays source code location, component definition, and usage references for the selected element, linking DOM selection to project source files.",
  ["component", "source-panel", "dev-tools", "navigation"], "complex");

fileNode(p.styleEditsFooter, "StyleEditsFooter.tsx",
  "Footer bar showing a summary/count of unsaved CSS style edits made in the DevTools Design panel.",
  ["component", "css-panel", "dev-tools", "footer"], "moderate");

fileNode(p.hook, "useWebDevToolsElementsPanel.ts",
  "Central React hook orchestrating Elements panel state and effects — DOM tree fetching/expansion, source navigation, style editing, and codebase-index status — for the WebDevTools Components tab.",
  ["hook", "dev-tools", "state-management", "dom-tree"], "complex",
  "Composes several smaller hooks (source navigation, webview DOM tree, style editor, refresh spin) into one large stateful hook rather than a class or reducer.");

fileNode(p.wdtIndex, "index.tsx",
  "Default-exported WebDevTools component — the main hideable side panel that composes the Console, Network, Elements (DOM tree + Design/CSS), and Source tabs into the embedded browser DevTools UI.",
  ["entry-point", "component", "dev-tools", "panel"], "complex",
  "Default export (`export default WebDevTools`) is not captured by the structural extractor's exports list, which only picked up the re-exported `./types` type aliases.");

fileNode(p.wdtTypes, "types.ts",
  "Shared TypeScript type and interface definitions (console/network entry shapes, tab identifiers, panel props) used across all WebDevTools sub-components.",
  ["type-definition", "dev-tools"], "moderate");

fileNode(p.webInspector, "index.tsx",
  "Wraps the WebDevTools panel to provide the Web Inspector feature within the Browser secondary panel.",
  ["component", "dev-tools", "wrapper"], "moderate");

fileNode(p.shared, "SharedBrowserDevToolsPanel.tsx",
  "Shared wrapper component that renders the WebInspector panel within the Browser's secondary panel layout, decoupling panel placement from the DevTools implementation.",
  ["component", "dev-tools", "wrapper", "shared"], "simple");

// ---- Function nodes ----
fnNode(p.consoleTab, "getEntryStyles", [49, 63],
  "Returns Tailwind class names for styling a console entry row based on its log level.",
  ["utility", "styling", "console"], "simple");

fnNode(p.consoleTab, "getMessagePreviewLines", [67, 81],
  "Splits a console message into a truncated preview of lines for collapsed display.",
  ["utility", "formatting", "console"], "simple");

fnNode(p.consoleTab, "ConsoleLogEntryRow", [93, 207],
  "Renders a single console log entry row with expandable message/stack trace, timestamp, and copy-to-clipboard action.",
  ["component", "console", "dev-tools", "row"], "complex");

fnNode(p.domUtils, "flattenDOMTree", [12, 33],
  "Recursively flattens a nested DOM tree into a flat list of visible nodes based on which nodes are currently expanded.",
  ["utility", "dom-tree", "tree-traversal"], "moderate");

fnNode(p.domUtils, "findNodeIndex", [38, 43],
  "Finds the index of a DOM node with a given xpath within a flattened node list.",
  ["utility", "dom-tree", "search"], "simple");

fnNode(p.domUtils, "getParentXpaths", [48, 59],
  "Computes the list of ancestor xpaths for a given node xpath, used to auto-expand parent nodes.",
  ["utility", "dom-tree", "xpath"], "simple");

fnNode(p.designPanel, "CornerIcon", [22, 45],
  "Renders a small SVG corner indicator icon used to highlight a selected corner in the box-model/border-radius UI.",
  ["component", "icon", "design-panel"], "simple");

fnNode(p.sourcePanel, "getRelativePath", [74, 83],
  "Converts an absolute source file path into a shortened relative path (last few segments) for compact display.",
  ["utility", "formatting", "source-panel"], "simple");

fnNode(p.hook, "useWebDevToolsElementsPanel", [83, 391],
  "Custom hook that manages all Elements panel state and effects — DOM tree fetch/expansion, source navigation, style editing, and codebase-index status — for the WebDevTools Components tab.",
  ["hook", "state-management", "dom-tree", "dev-tools"], "complex");

// ---- contains edges ----
edge("file:" + p.consoleTab, "function:" + p.consoleTab + ":getEntryStyles", "contains", 1.0);
edge("file:" + p.consoleTab, "function:" + p.consoleTab + ":getMessagePreviewLines", "contains", 1.0);
edge("file:" + p.consoleTab, "function:" + p.consoleTab + ":ConsoleLogEntryRow", "contains", 1.0);
edge("file:" + p.domUtils, "function:" + p.domUtils + ":flattenDOMTree", "contains", 1.0);
edge("file:" + p.domUtils, "function:" + p.domUtils + ":findNodeIndex", "contains", 1.0);
edge("file:" + p.domUtils, "function:" + p.domUtils + ":getParentXpaths", "contains", 1.0);
edge("file:" + p.designPanel, "function:" + p.designPanel + ":CornerIcon", "contains", 1.0);
edge("file:" + p.sourcePanel, "function:" + p.sourcePanel + ":getRelativePath", "contains", 1.0);
edge("file:" + p.hook, "function:" + p.hook + ":useWebDevToolsElementsPanel", "contains", 1.0);

// ---- exports edges (only for exported function/class nodes we created) ----
edge("file:" + p.domUtils, "function:" + p.domUtils + ":flattenDOMTree", "exports", 0.8);
edge("file:" + p.domUtils, "function:" + p.domUtils + ":findNodeIndex", "exports", 0.8);
edge("file:" + p.domUtils, "function:" + p.domUtils + ":getParentXpaths", "exports", 0.8);
edge("file:" + p.hook, "function:" + p.hook + ":useWebDevToolsElementsPanel", "exports", 0.8);

// ---- imports edges (1:1 from batchImportData) ----
const importPairs = [
  [p.styleSection, p.editableStyleRow],
  [p.cssPanel, p.styleSection],
  [p.consoleTab, p.wdtTypes],
  [p.domIndex, p.domNodeRow],
  [p.domIndex, p.domTypes],
  [p.domIndex, p.domUtils],
  [p.domUtils, p.domTypes],
  [p.linkedInput, p.spacingIcons],
  [p.designPanel, p.boxModel],
  [p.designPanel, p.collapsible],
  [p.designPanel, p.editableField],
  [p.designPanel, p.layoutButtons],
  [p.designPanel, p.linkedInput],
  [p.networkTab, p.wdtTypes],
  [p.sourcePanel, p.collapsible],
  [p.hook, p.wdtTypes],
  [p.wdtIndex, p.consoleTab],
  [p.wdtIndex, p.cssPanel],
  [p.wdtIndex, p.designPanel],
  [p.wdtIndex, p.domIndex],
  [p.wdtIndex, p.networkTab],
  [p.wdtIndex, p.sourcePanel],
  [p.wdtIndex, p.styleEditsFooter],
  [p.wdtIndex, p.hook],
  [p.wdtIndex, p.wdtTypes],
  [p.webInspector, p.wdtIndex],
  [p.shared, p.webInspector],
];

for (const [src, tgt] of importPairs) {
  edge("file:" + src, "file:" + tgt, "imports", 0.7);
}

const output = { nodes, edges };
fs.writeFileSync(process.argv[2], JSON.stringify(output, null, 2));
console.log("nodes:", nodes.length, "edges:", edges.length, "imports:", importPairs.length);
