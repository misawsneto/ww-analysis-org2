import json

P = "src/scaffold/GlobalSpotlight/"

def fid(p): return f"file:{p}"
def fnid(p, n): return f"function:{p}:{n}"

# ---------------- FILE NODES ----------------
files = [
  dict(id=fid(P+"palettes/UnifiedModelPalette/useUnifiedModelPaletteItems.ts"), type="file",
       name="useUnifiedModelPaletteItems.ts", filePath=P+"palettes/UnifiedModelPalette/useUnifiedModelPaletteItems.ts",
       summary="Hook that derives the sectioned SpotlightItem list (models, recents, sources) shown by the UnifiedModelPalette, combining pinned/default variants, account compatibility, and recent-entry matching.",
       tags=["hook","model-selection","palette","spotlight"], complexity="complex"),
  dict(id=fid(P+"palettes/UnifiedModelPalette/useUnifiedModelPaletteSelection.ts"), type="file",
       name="useUnifiedModelPaletteSelection.ts", filePath=P+"palettes/UnifiedModelPalette/useUnifiedModelPaletteSelection.ts",
       summary="Hook managing the UnifiedModelPalette's two-column selection state (models/sources columns, active/preview model, source switching) and commits the chosen model/variant back to AdvancedConfig.",
       tags=["hook","state-management","model-selection","palette"], complexity="complex"),
  dict(id=fid(P+"palettes/UnifiedModelPalette/variantReselect.ts"), type="file",
       name="variantReselect.ts", filePath=P+"palettes/UnifiedModelPalette/variantReselect.ts",
       summary="Tiny decision helper that determines whether editing the currently selected model's variant should update the active selection.",
       tags=["utility","model-selection"], complexity="simple"),
  dict(id=fid(P+"palettes/WorkspacePalette/WorkspaceDropdown.tsx"), type="file",
       name="WorkspaceDropdown.tsx", filePath=P+"palettes/WorkspacePalette/WorkspaceDropdown.tsx",
       summary="Anchored, compact dropdown variant of WorkspacePalette for quickly switching repos/workspaces from a 320px panel, omitting the add/manage flows of the full Spotlight palette.",
       tags=["component","dropdown","workspace-switching","spotlight"], complexity="complex"),
  dict(id=fid(P+"palettes/WorkspacePalette/index.tsx"), type="file",
       name="index.tsx", filePath=P+"palettes/WorkspacePalette/index.tsx",
       summary="Flat palette component listing repos, folders, and multi-repo workspaces as selectable peers, composing add/manage/multi-repo-workspace-editing flows from local hooks.",
       tags=["component","palette","workspace-switching","entry-point"], complexity="complex"),
  dict(id=fid(P+"palettes/WorkspacePalette/pathActionItem.ts"), type="file",
       name="pathActionItem.ts", filePath=P+"palettes/WorkspacePalette/pathActionItem.ts",
       summary="Builds the \"open path\" SpotlightItem shown when the search query looks like a filesystem path candidate.",
       tags=["utility","spotlight-item","workspace"], complexity="simple"),
  dict(id=fid(P+"palettes/WorkspacePalette/pathImport.ts"), type="file",
       name="pathImport.ts", filePath=P+"palettes/WorkspacePalette/pathImport.ts",
       summary="Filesystem-path helpers for the workspace add flow: path validation, home-dir expansion, and the import routine that stats a candidate path and either imports it or shows an invalid-path dialog.",
       tags=["utility","filesystem","tauri","workspace-import"], complexity="moderate"),
  dict(id=fid(P+"palettes/WorkspacePalette/pinnedActions.ts"), type="file",
       name="pinnedActions.ts", filePath=P+"palettes/WorkspacePalette/pinnedActions.ts",
       summary="Builds the pinned action row (open, create workspace, add, bulk delete, manage toggle) shown at the top of the WorkspacePalette.",
       tags=["utility","spotlight-item","actions"], complexity="simple"),
  dict(id=fid(P+"palettes/WorkspacePalette/types.ts"), type="file",
       name="types.ts", filePath=P+"palettes/WorkspacePalette/types.ts",
       summary="Type definitions and section-key constants for the WorkspacePalette, including component props and the shape of its localized text bundle.",
       tags=["type-definition","workspace-switching"], complexity="simple"),
  dict(id=fid(P+"palettes/WorkspacePalette/useWorkspacePaletteNavigation.ts"), type="file",
       name="useWorkspacePaletteNavigation.ts", filePath=P+"palettes/WorkspacePalette/useWorkspacePaletteNavigation.ts",
       summary="Hook that manages back-navigation and modal-stage transitions across the WorkspacePalette's add-menu, manage-mode, and clone/create sub-flows.",
       tags=["hook","navigation","state-management"], complexity="moderate"),
  dict(id=fid(P+"palettes/WorkspacePalette/useWorkspacePaletteWorkspace.tsx"), type="file",
       name="useWorkspacePaletteWorkspace.tsx", filePath=P+"palettes/WorkspacePalette/useWorkspacePaletteWorkspace.tsx",
       summary="Hook encapsulating saved-workspace CRUD (activate, edit, bulk delete) and deriving the manage-mode-aware SpotlightItem list for multi-repo workspaces.",
       tags=["hook","workspace-management","state-management"], complexity="complex"),
  dict(id=fid(P+"palettes/WorkspacePalette/workspacePaletteItems.ts"), type="file",
       name="workspacePaletteItems.ts", filePath=P+"palettes/WorkspacePalette/workspacePaletteItems.ts",
       summary="Builds the sectioned SpotlightItem list (current/recent/repo/workspace/system/external groups) rendered by WorkspacePalette, and the add-menu item list.",
       tags=["utility","spotlight-item","sectioning"], complexity="complex"),
  dict(id=fid(P+"palettes/adapters/branchAdapter.ts"), type="file",
       name="branchAdapter.ts", filePath=P+"palettes/adapters/branchAdapter.ts",
       summary="Converts BranchItem domain objects into SpotlightItem rows (single and batch), shared by the branch selector and main spotlight.",
       tags=["adapter","spotlight-item","branch"], complexity="simple"),
  dict(id=fid(P+"palettes/adapters/index.ts"), type="file",
       name="index.ts", filePath=P+"palettes/adapters/index.ts",
       summary="Barrel re-exporting the repo, branch, and workspace-folder adapters plus the systemPathRepoItem predicate for shared item-builder access.",
       tags=["barrel","adapter","entry-point"], complexity="simple"),
  dict(id=fid(P+"palettes/adapters/repoAdapter.ts"), type="file",
       name="repoAdapter.ts", filePath=P+"palettes/adapters/repoAdapter.ts",
       summary="Converts RepoItem domain objects into SpotlightItem rows (with manage-mode selection/action affordances) and provides current-selection-first sorting.",
       tags=["adapter","spotlight-item","repo"], complexity="moderate"),
  dict(id=fid(P+"palettes/adapters/workspaceFolderAdapter.ts"), type="file",
       name="workspaceFolderAdapter.ts", filePath=P+"palettes/adapters/workspaceFolderAdapter.ts",
       summary="Converts WorkspaceFolder domain objects into SpotlightItem rows for multi-root workspace display, including per-folder git status badges.",
       tags=["adapter","spotlight-item","workspace"], complexity="simple"),
  dict(id=fid(P+"palettes/config.ts"), type="file",
       name="config.ts", filePath=P+"palettes/config.ts",
       summary="Single source of truth for palette path/template configs (repo, model, dispatch-category, branch, editor) plus small accessor helpers for mode paths, labels, and icons.",
       tags=["config","palette","single-source-of-truth"], complexity="complex"),
  dict(id=fid(P+"palettes/core/index.ts"), type="file",
       name="index.ts", filePath=P+"palettes/core/index.ts",
       summary="Barrel exposing the shared selector kernel hook (useSelectorKernel) and its option/return types used by every palette.",
       tags=["barrel","entry-point","kernel"], complexity="simple"),
  dict(id=fid(P+"palettes/index.ts"), type="file",
       name="index.ts", filePath=P+"palettes/index.ts",
       summary="Public barrel re-exporting every palette component and its prop types (Workspace, Branch, Worktree, Database, UnifiedModel, DispatchCategory, Editor, ContentSearch, and session/agent palettes).",
       tags=["barrel","entry-point","palette"], complexity="simple"),
  dict(id=fid(P+"shared/SpotlightInput.tsx"), type="file",
       name="SpotlightInput.tsx", filePath=P+"shared/SpotlightInput.tsx",
       summary="Reusable search input for spotlight-style interfaces with a clear button, Tauri select-all shortcut handling, and an optional trailing slot.",
       tags=["component","input","shared"], complexity="moderate"),
  dict(id=fid(P+"shared/index.ts"), type="file",
       name="index.ts", filePath=P+"shared/index.ts",
       summary="Barrel exporting the shared SpotlightInput component and base palette/item type definitions.",
       tags=["barrel","entry-point","shared"], complexity="simple"),
  dict(id=fid(P+"shell/PaletteBody.tsx"), type="file",
       name="PaletteBody.tsx", filePath=P+"shell/PaletteBody.tsx",
       summary="Pure-content palette body composing the search bar/input, top/hint slots, and item list without any chrome, portal, or footer concerns (owned by SpotlightShell).",
       tags=["component","shell","palette-body"], complexity="moderate"),
  dict(id=fid(P+"shell/ShellFooterAction.tsx"), type="file",
       name="ShellFooterAction.tsx", filePath=P+"shell/ShellFooterAction.tsx",
       summary="Portal component letting palettes inject a footer action pill next to SpotlightShell's keyboard-hint footer, using useSyncExternalStore to track the host element.",
       tags=["component","portal","shell"], complexity="simple"),
  dict(id=fid(P+"shell/SpotlightShell.tsx"), type="file",
       name="SpotlightShell.tsx", filePath=P+"shell/SpotlightShell.tsx",
       summary="The single shared visual chrome for all spotlight palettes — portal, backdrop, keyboard-hint footer, and footer-action-slot context provider — so palette content stays chrome-free.",
       tags=["component","shell","chrome","entry-point"], complexity="moderate"),
  dict(id=fid(P+"shell/SpotlightShellChrome.tsx"), type="file",
       name="SpotlightShellChrome.tsx", filePath=P+"shell/SpotlightShellChrome.tsx",
       summary="Low-level chrome rendering the spotlight panel, optional portal/backdrop, viewport-centered positioning, escape handling, and refocus-on-click behavior.",
       tags=["component","shell","chrome","portal"], complexity="moderate"),
  dict(id=fid(P+"shell/footerActionContext.ts"), type="file",
       name="footerActionContext.ts", filePath=P+"shell/footerActionContext.ts",
       summary="React context carrying the footer-action host subscription slot (useSyncExternalStore shape) shared between SpotlightShell and ShellFooterAction.",
       tags=["context","shell"], complexity="simple"),
  dict(id=fid(P+"shell/index.ts"), type="file",
       name="index.ts", filePath=P+"shell/index.ts",
       summary="Barrel exporting the public shell surface — SpotlightShell, PaletteBody, ShellFooterAction — for palette consumers.",
       tags=["barrel","entry-point","shell"], complexity="simple"),
  dict(id=fid(P+"styles.ts"), type="file",
       name="styles.ts", filePath=P+"styles.ts",
       summary="Raw CSS string for spotlight visuals that can't be expressed with Tailwind utilities (shadow, hidden scrollbar, refresh-spin animation, hover/selection states).",
       tags=["styles","css"], complexity="simple"),
  dict(id=fid(P+"types.ts"), type="file",
       name="types.ts", filePath=P+"types.ts",
       summary="Core domain and prop types for GlobalSpotlight — path segments, action definitions, RepoItem/BranchItem shapes, and the top-level GlobalSpotlightProps.",
       tags=["type-definition","domain-model"], complexity="simple"),
  dict(id=fid(P+"utils/branchUtils.ts"), type="file",
       name="branchUtils.ts", filePath=P+"utils/branchUtils.ts",
       summary="Categorizes a branch list into Recent/Worktrees/Default/Other buckets with priority ordering for the branch selector UI.",
       tags=["utility","branch","categorization"], complexity="moderate"),
  dict(id=fid(P+"views/SpotlightConfirmationView.tsx"), type="file",
       name="SpotlightConfirmationView.tsx", filePath=P+"views/SpotlightConfirmationView.tsx",
       summary="Renders the confirmation page (action header, parameter list, back/confirm buttons) shown before executing an action without a dedicated modal.",
       tags=["component","confirmation","view"], complexity="simple"),
  dict(id=fid(P+"views/SpotlightModalView.tsx"), type="file",
       name="SpotlightModalView.tsx", filePath=P+"views/SpotlightModalView.tsx",
       summary="Dispatches to the correct add-workspace form (new folder, GitHub clone, URL clone, create multi-repo workspace) based on the active path segment.",
       tags=["component","view","form-dispatch","workspace"], complexity="moderate"),
  dict(id=fid(P+"views/index.ts"), type="file",
       name="index.ts", filePath=P+"views/index.ts",
       summary="Barrel exporting the SpotlightModalView and SpotlightConfirmationView components and their prop types.",
       tags=["barrel","entry-point","view"], complexity="simple"),
]

# ---------------- FUNCTION NODES ----------------
funcs = [
  dict(path=P+"palettes/UnifiedModelPalette/useUnifiedModelPaletteItems.ts", name="useUnifiedModelPaletteItems", lineRange=[59,364],
       summary="Memoized hook building recent/model/source SpotlightItem sections for the UnifiedModelPalette, resolving default variants, group-by-model lookups, and active-model matching.",
       tags=["hook","model-selection","memoization"], complexity="complex", exported=True),
  dict(path=P+"palettes/UnifiedModelPalette/useUnifiedModelPaletteSelection.ts", name="useUnifiedModelPaletteSelection", lineRange=[31,267],
       summary="Manages selection state and callbacks (model select/preview, source select, recent select, variant reselect) for the two-column UnifiedModelPalette, committing changes via onConfigChange.",
       tags=["hook","state-management","model-selection"], complexity="complex", exported=True),
  dict(path=P+"palettes/UnifiedModelPalette/variantReselect.ts", name="resolveVariantReselection", lineRange=[10,17],
       summary="Returns the next model id when a variant edit should update the current selection, or null when it's a no-op.",
       tags=["utility","decision-logic"], complexity="simple", exported=True),
  dict(path=P+"palettes/WorkspacePalette/WorkspaceDropdown.tsx", name="RepoRow", lineRange=[106,145],
       summary="Renders a single repo row in the WorkspaceDropdown list with icon, current-selection check, and keyboard navigation props.",
       tags=["component","list-item"], complexity="simple", exported=False),
  dict(path=P+"palettes/WorkspacePalette/WorkspaceDropdown.tsx", name="WorkspaceRow", lineRange=[147,174],
       summary="Renders a single saved-workspace row in the WorkspaceDropdown list.",
       tags=["component","list-item"], complexity="simple", exported=False),
  dict(path=P+"palettes/WorkspacePalette/WorkspaceDropdown.tsx", name="OpenPathRow", lineRange=[176,197],
       summary="Renders the \"open path\" action row shown when the dropdown search query matches a filesystem path candidate.",
       tags=["component","list-item"], complexity="simple", exported=False),
  dict(path=P+"palettes/WorkspacePalette/WorkspaceDropdown.tsx", name="WorkspaceDropdown", lineRange=[215,671],
       summary="Anchored dropdown component that assembles repo/workspace/system-path sections, filters by search query and recency, and handles keyboard navigation and selection via useDropdownEngine.",
       tags=["component","dropdown","workspace-switching"], complexity="complex", exported=True),
  dict(path=P+"palettes/WorkspacePalette/index.tsx", name="WorkspacePalette", lineRange=[59,666],
       summary="Top-level flat palette component wiring together repo/workspace listing, add-workspace flow, manage-mode bulk actions, and navigation across search/add/manage/confirmation stages.",
       tags=["component","palette","entry-point"], complexity="complex", exported=True),
  dict(path=P+"palettes/WorkspacePalette/pathActionItem.ts", name="buildOpenPathItem", lineRange=[14,35],
       summary="Builds the SpotlightItem representing an \"open this path\" action for a path-like search query.",
       tags=["utility","spotlight-item"], complexity="simple", exported=True),
  dict(path=P+"palettes/WorkspacePalette/pathImport.ts", name="looksLikeWorkspacePath", lineRange=[14,16],
       summary="Tests whether a string looks like an absolute filesystem path (POSIX, UNC, or Windows drive letter).",
       tags=["utility","validation"], complexity="simple", exported=True),
  dict(path=P+"palettes/WorkspacePalette/pathImport.ts", name="getWorkspacePathCandidate", lineRange=[18,21],
       summary="Trims a value and returns it only if it looks like a workspace path, otherwise null.",
       tags=["utility","validation"], complexity="simple", exported=True),
  dict(path=P+"palettes/WorkspacePalette/pathImport.ts", name="getWorkspacePathDisplayName", lineRange=[23,28],
       summary="Extracts the trailing folder name from a normalized filesystem path for display purposes.",
       tags=["utility","formatting"], complexity="simple", exported=True),
  dict(path=P+"palettes/WorkspacePalette/pathImport.ts", name="expandHomePath", lineRange=[30,36],
       summary="Expands a leading \"~/\" in a path to the OS home directory via the Tauri path API.",
       tags=["utility","tauri","filesystem"], complexity="simple", exported=True),
  dict(path=P+"palettes/WorkspacePalette/pathImport.ts", name="showInvalidWorkspacePathDialog", lineRange=[38,47],
       summary="Shows a Tauri native error dialog when a candidate workspace path is invalid.",
       tags=["utility","tauri","dialog"], complexity="simple", exported=True),
  dict(path=P+"palettes/WorkspacePalette/pathImport.ts", name="importWorkspacePath", lineRange=[49,78],
       summary="Validates, expands, and stats a candidate path, then imports it as a workspace or shows an invalid-path dialog on failure.",
       tags=["utility","tauri","workspace-import","filesystem"], complexity="moderate", exported=True),
  dict(path=P+"palettes/WorkspacePalette/pinnedActions.ts", name="buildPinnedWorkspaceActions", lineRange=[19,86],
       summary="Builds the pinned action list (open, create workspace, add, bulk delete, manage toggle) shown above the palette's item list, varying by manage-mode and selection state.",
       tags=["utility","spotlight-item","actions"], complexity="moderate", exported=True),
  dict(path=P+"palettes/WorkspacePalette/useWorkspacePaletteNavigation.ts", name="useWorkspacePaletteNavigation", lineRange=[24,156],
       summary="Hook implementing back-navigation semantics across the WorkspacePalette's modal stages (add menu, clone/create forms, manage mode), including parent-palette handoff via onGoBackToParent.",
       tags=["hook","navigation"], complexity="moderate", exported=True),
  dict(path=P+"palettes/WorkspacePalette/useWorkspacePaletteWorkspace.tsx", name="buildWorkspaceRepoNameResolver", lineRange=[75,97],
       summary="Builds a lookup function resolving a workspace folder's display name from its repoId or normalized filesystem path against the current repo list.",
       tags=["utility","lookup"], complexity="moderate", exported=False),
  dict(path=P+"palettes/WorkspacePalette/useWorkspacePaletteWorkspace.tsx", name="useWorkspacePaletteWorkspace", lineRange=[103,431],
       summary="Hook exposing derived workspace SpotlightItems and bulk-delete handling, backed by the saved-workspaces atom and workspace CRUD API calls.",
       tags=["hook","workspace-management","state-management"], complexity="complex", exported=True),
  dict(path=P+"palettes/WorkspacePalette/workspacePaletteItems.ts", name="buildSectionHeader", lineRange=[17,30],
       summary="Builds a non-interactive SpotlightItem header row for a workspace-palette section.",
       tags=["utility","spotlight-item"], complexity="simple", exported=False),
  dict(path=P+"palettes/WorkspacePalette/workspacePaletteItems.ts", name="buildSectionedWorkspaceItems", lineRange=[63,237],
       summary="Assembles the full sectioned item list (current/recent/repo/multi-repo-workspace/folder-workspace/system-path/external-recent) for the WorkspacePalette, deduplicating items already surfaced under \"current\" or \"recent\".",
       tags=["utility","spotlight-item","sectioning"], complexity="complex", exported=True),
  dict(path=P+"palettes/WorkspacePalette/workspacePaletteItems.ts", name="buildSectionedAddItems", lineRange=[239,243],
       summary="Passthrough that returns the add-workspace item list unchanged (kept for symmetry with buildSectionedWorkspaceItems).",
       tags=["utility"], complexity="simple", exported=True),
  dict(path=P+"palettes/adapters/branchAdapter.ts", name="buildBranchSpotlightItem", lineRange=[23,52],
       summary="Converts a single BranchItem into a SpotlightItem with type/status badges and relative-time description.",
       tags=["adapter","spotlight-item"], complexity="simple", exported=True),
  dict(path=P+"palettes/adapters/branchAdapter.ts", name="buildBranchSpotlightItems", lineRange=[57,62],
       summary="Maps an array of BranchItems to SpotlightItems via buildBranchSpotlightItem.",
       tags=["adapter","spotlight-item"], complexity="simple", exported=True),
  dict(path=P+"palettes/adapters/repoAdapter.ts", name="buildRepoSpotlightItem", lineRange=[34,70],
       summary="Converts a single RepoItem into a SpotlightItem, including manage-mode selection state and right-side action rendering.",
       tags=["adapter","spotlight-item"], complexity="moderate", exported=True),
  dict(path=P+"palettes/adapters/repoAdapter.ts", name="buildRepoSpotlightItems", lineRange=[75,80],
       summary="Maps an array of RepoItems to SpotlightItems via buildRepoSpotlightItem.",
       tags=["adapter","spotlight-item"], complexity="simple", exported=True),
  dict(path=P+"palettes/adapters/repoAdapter.ts", name="sortRepoItemsSelectedFirst", lineRange=[85,93],
       summary="Sorts a SpotlightItem array so the currently-selected repo item appears first.",
       tags=["utility","sorting"], complexity="simple", exported=True),
  dict(path=P+"palettes/adapters/workspaceFolderAdapter.ts", name="buildWorkspaceFolderItems", lineRange=[19,52],
       summary="Converts WorkspaceFolder domain objects into SpotlightItems, computing per-folder git change counts from a status map.",
       tags=["adapter","spotlight-item"], complexity="moderate", exported=True),
  dict(path=P+"palettes/config.ts", name="buildPathSegment", lineRange=[79,91],
       summary="Builds a navigation PathSegment (id, label, icon, template) from a PathConfig for use in the spotlight search bar.",
       tags=["utility","config"], complexity="simple", exported=True),
  dict(path=P+"palettes/config.ts", name="getModePath", lineRange=[96,101],
       summary="Looks up the PathConfig for a given palette mode id within a SelectorConfig.",
       tags=["utility","config"], complexity="simple", exported=True),
  dict(path=P+"palettes/config.ts", name="getLabel", lineRange=[106,108],
       summary="Looks up a label from a SelectorConfig's labels map, falling back to the key itself.",
       tags=["utility","config"], complexity="simple", exported=True),
  dict(path=P+"palettes/config.ts", name="getIcon", lineRange=[113,118],
       summary="Looks up an icon from a SelectorConfig's icons map.",
       tags=["utility","config"], complexity="simple", exported=True),
  dict(path=P+"shared/SpotlightInput.tsx", name="SpotlightInput", lineRange=[37,111],
       summary="Reusable spotlight search input with icon, placeholder, clear button, and Tauri select-all shortcut wiring.",
       tags=["component","input"], complexity="moderate", exported=True),
  dict(path=P+"shell/PaletteBody.tsx", name="PaletteBody", lineRange=[61,135],
       summary="Composes the palette's search bar/input variant, top/hint slots, and item list (or content override) into the chrome-free palette body.",
       tags=["component","palette-body"], complexity="moderate", exported=True),
  dict(path=P+"shell/ShellFooterAction.tsx", name="ShellFooterAction", lineRange=[24,37],
       summary="Portals its children into the SpotlightShell's footer-action host element, rendering nothing if no shell is present.",
       tags=["component","portal"], complexity="simple", exported=True),
  dict(path=P+"shell/SpotlightShell.tsx", name="SpotlightShell", lineRange=[52,119],
       summary="Provides the shared spotlight chrome (portal/backdrop/footer) and a footer-action-slot context so palette content and ShellFooterAction stay decoupled.",
       tags=["component","shell","chrome"], complexity="moderate", exported=True),
  dict(path=P+"shell/SpotlightShellChrome.tsx", name="SpotlightShellChrome", lineRange=[35,165],
       summary="Renders the low-level spotlight panel with optional portal/backdrop, viewport-centered placement, escape-to-close handling, and click-to-refocus behavior.",
       tags=["component","chrome","portal"], complexity="complex", exported=True),
  dict(path=P+"utils/branchUtils.ts", name="categorizeBranches", lineRange=[25,111],
       summary="Sorts and buckets branches into Recent/Worktrees/Default/Other categories with well-defined priority ordering for the branch selector.",
       tags=["utility","branch","categorization"], complexity="moderate", exported=True),
  dict(path=P+"views/SpotlightConfirmationView.tsx", name="SpotlightConfirmationView", lineRange=[30,95],
       summary="Renders the confirmation-page UI (header, parameter list, back/confirm buttons) for the active confirmation-page hook state.",
       tags=["component","confirmation"], complexity="simple", exported=True),
  dict(path=P+"views/SpotlightModalView.tsx", name="SpotlightModalView", lineRange=[38,173],
       summary="Switches on the active path segment id to render the matching add-workspace form (new folder, GitHub clone, URL clone, create multi-repo workspace).",
       tags=["component","form-dispatch"], complexity="moderate", exported=True),
]

func_nodes = []
for f in funcs:
    func_nodes.append(dict(
        id=fnid(f["path"], f["name"]), type="function", name=f["name"],
        filePath=f["path"], lineRange=f["lineRange"], summary=f["summary"],
        tags=f["tags"], complexity=f["complexity"]
    ))

with open('/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate/batch-inputs/batch-28.input.json') as fh:
    inp = json.load(fh)
bid = inp["batchImportData"]

import_edges = []
for src_path, targets in bid.items():
    for t in targets:
        import_edges.append(dict(source=fid(src_path), target=fid(t), type="imports", direction="forward", weight=0.7))

contains_edges = []
exports_edges = []
for f in funcs:
    contains_edges.append(dict(source=fid(f["path"]), target=fnid(f["path"], f["name"]), type="contains", direction="forward", weight=1.0))
    if f["exported"]:
        exports_edges.append(dict(source=fid(f["path"]), target=fnid(f["path"], f["name"]), type="exports", direction="forward", weight=0.8))

calls_edges = [
  dict(source=fnid(P+"palettes/UnifiedModelPalette/useUnifiedModelPaletteItems.ts","useUnifiedModelPaletteItems"),
       target=fnid(P+"palettes/UnifiedModelPalette/modelSection.ts","buildGroupByModel"), type="calls", direction="forward", weight=0.8),
  dict(source=fnid(P+"palettes/UnifiedModelPalette/useUnifiedModelPaletteItems.ts","useUnifiedModelPaletteItems"),
       target=fnid(P+"palettes/UnifiedModelPalette/modelSection.ts","getActiveModelId"), type="calls", direction="forward", weight=0.8),
  dict(source=fnid(P+"palettes/UnifiedModelPalette/useUnifiedModelPaletteItems.ts","useUnifiedModelPaletteItems"),
       target=fnid(P+"palettes/UnifiedModelPalette/modelSection.ts","entryMatchesActiveConfig"), type="calls", direction="forward", weight=0.8),
  dict(source=fnid(P+"palettes/UnifiedModelPalette/useUnifiedModelPaletteItems.ts","useUnifiedModelPaletteItems"),
       target=fnid(P+"palettes/UnifiedModelPalette/modelSelectionItems.tsx","buildModelSelectionSpotlightItem"), type="calls", direction="forward", weight=0.8),
  dict(source=fnid(P+"palettes/UnifiedModelPalette/useUnifiedModelPaletteItems.ts","useUnifiedModelPaletteItems"),
       target=fnid(P+"palettes/UnifiedModelPalette/modelSelectionItems.tsx","buildAllModelItems"), type="calls", direction="forward", weight=0.8),
  dict(source=fnid(P+"palettes/UnifiedModelPalette/useUnifiedModelPaletteSelection.ts","useUnifiedModelPaletteSelection"),
       target=fnid(P+"palettes/UnifiedModelPalette/variantReselect.ts","resolveVariantReselection"), type="calls", direction="forward", weight=0.8),
  dict(source=fnid(P+"palettes/WorkspacePalette/index.tsx","WorkspacePalette"),
       target=fnid(P+"palettes/WorkspacePalette/pathActionItem.ts","buildOpenPathItem"), type="calls", direction="forward", weight=0.8),
  dict(source=fnid(P+"palettes/WorkspacePalette/index.tsx","WorkspacePalette"),
       target=fnid(P+"palettes/WorkspacePalette/pathImport.ts","importWorkspacePath"), type="calls", direction="forward", weight=0.8),
  dict(source=fnid(P+"palettes/WorkspacePalette/index.tsx","WorkspacePalette"),
       target=fnid(P+"palettes/WorkspacePalette/pinnedActions.ts","buildPinnedWorkspaceActions"), type="calls", direction="forward", weight=0.8),
  dict(source=fnid(P+"palettes/WorkspacePalette/index.tsx","WorkspacePalette"),
       target=fnid(P+"palettes/WorkspacePalette/useWorkspacePaletteNavigation.ts","useWorkspacePaletteNavigation"), type="calls", direction="forward", weight=0.8),
  dict(source=fnid(P+"palettes/WorkspacePalette/index.tsx","WorkspacePalette"),
       target=fnid(P+"palettes/WorkspacePalette/useWorkspacePaletteWorkspace.tsx","useWorkspacePaletteWorkspace"), type="calls", direction="forward", weight=0.8),
  dict(source=fnid(P+"palettes/WorkspacePalette/index.tsx","WorkspacePalette"),
       target=fnid(P+"palettes/WorkspacePalette/workspacePaletteItems.ts","buildSectionedWorkspaceItems"), type="calls", direction="forward", weight=0.8),
  dict(source=fnid(P+"palettes/WorkspacePalette/index.tsx","WorkspacePalette"),
       target=fnid(P+"palettes/WorkspacePalette/workspacePaletteItems.ts","buildSectionedAddItems"), type="calls", direction="forward", weight=0.8),
  dict(source=fnid(P+"palettes/WorkspacePalette/WorkspaceDropdown.tsx","WorkspaceDropdown"),
       target=fnid(P+"palettes/WorkspacePalette/pathActionItem.ts","buildOpenPathItem"), type="calls", direction="forward", weight=0.8),
  dict(source=fnid(P+"palettes/WorkspacePalette/WorkspaceDropdown.tsx","WorkspaceDropdown"),
       target=fnid(P+"palettes/WorkspacePalette/pathImport.ts","importWorkspacePath"), type="calls", direction="forward", weight=0.8),
]

all_nodes = files + func_nodes
all_edges = import_edges + contains_edges + exports_edges + calls_edges

print("TOTAL nodes:", len(all_nodes), "TOTAL edges:", len(all_edges))
print("imports:", len(import_edges), "contains:", len(contains_edges), "exports:", len(exports_edges), "calls:", len(calls_edges))

# ---- partition into 2 parts by sorted file path (17 / 16 files) ----
sorted_paths = sorted([f["filePath"] for f in files])
part1_files = set(sorted_paths[:17])
part2_files = set(sorted_paths[17:])

def node_file(n):
    return n.get("filePath") or n["id"].split(":",2)[1]  # function/class ids: type:path:name -> path via filePath key already set for func nodes

part1_nodes = [n for n in all_nodes if n["filePath"] in part1_files]
part2_nodes = [n for n in all_nodes if n["filePath"] in part2_files]

part1_ids = set(n["id"] for n in part1_nodes)
part2_ids = set(n["id"] for n in part2_nodes)

def source_file_of_edge(e):
    # source is always file:... or function:path:name
    src = e["source"]
    if src.startswith("file:"):
        return src[len("file:"):]
    elif src.startswith("function:"):
        rest = src[len("function:"):]
        # path:name -- path itself may contain colons? no. split on last ':'
        return rest.rsplit(":",1)[0]
    return None

part1_edges = [e for e in all_edges if source_file_of_edge(e) in part1_files]
part2_edges = [e for e in all_edges if source_file_of_edge(e) in part2_files]

print("part1 nodes:", len(part1_nodes), "part1 edges:", len(part1_edges))
print("part2 nodes:", len(part2_nodes), "part2 edges:", len(part2_edges))
assert len(part1_edges) + len(part2_edges) == len(all_edges)
assert len(part1_nodes) + len(part2_nodes) == len(all_nodes)

with open('/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate/batch-28-part-1.json','w') as fh:
    json.dump({"nodes": part1_nodes, "edges": part1_edges}, fh, indent=1)
with open('/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate/batch-28-part-2.json','w') as fh:
    json.dump({"nodes": part2_nodes, "edges": part2_edges}, fh, indent=1)

print("WROTE part1 and part2")
