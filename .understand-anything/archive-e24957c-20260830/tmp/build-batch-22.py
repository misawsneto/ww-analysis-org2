import json

P = "src/engines/ChatPanel/InputArea/components/"

def fid(p): return f"file:{p}"
def fnid(p, name): return f"function:{p}:{name}"

nodes = []
edges = []

def add_file(path, summary, tags, complexity, lang_notes=None):
    n = {
        "id": fid(path),
        "type": "file",
        "name": path.split("/")[-1],
        "filePath": path,
        "summary": summary,
        "tags": tags,
        "complexity": complexity,
    }
    if lang_notes:
        n["languageNotes"] = lang_notes
    nodes.append(n)

def add_fn(path, name, line_range, summary, tags, complexity, exported=False):
    n = {
        "id": fnid(path, name),
        "type": "function",
        "name": name,
        "filePath": path,
        "lineRange": list(line_range),
        "summary": summary,
        "tags": tags,
        "complexity": complexity,
    }
    nodes.append(n)
    edges.append({"source": fid(path), "target": fnid(path, name), "type": "contains", "direction": "forward", "weight": 1.0})
    if exported:
        edges.append({"source": fid(path), "target": fnid(path, name), "type": "exports", "direction": "forward", "weight": 0.8})

def add_import(src_path, targets):
    for t in targets:
        edges.append({"source": fid(src_path), "target": fid(t), "type": "imports", "direction": "forward", "weight": 0.7})

def add_call(src_path, src_fn, dst_path, dst_fn):
    edges.append({"source": fnid(src_path, src_fn), "target": fnid(dst_path, dst_fn), "type": "calls", "direction": "forward", "weight": 0.8})

# ============ FILE NODES ============

add_file(P+"InputActions.tsx",
    "Renders the composer's primary action button (send/stop/retry/resume) implementing a priority-ordered state machine based on agent working, pending-cancel, and terminal session states.",
    ["component", "ui", "state-machine", "button"], "complex")

add_file(P+"InputAreaChrome.tsx",
    "Provides layout chrome for the composer: top row with pinned-actions bar and plan-todo pill, a quiet-edit status banner, an edit-mode image preview strip, and style-variant helpers for the composer shell.",
    ["component", "layout", "ui", "composer"], "moderate")

add_file(P+"InputAreaPortals.tsx",
    "Aggregates and renders the floating/portal UI surfaces attached to the input area -- context menu, at-mention menu, and slash-command menu -- from a single component.",
    ["component", "portal", "ui", "composer"], "moderate")

add_file(P+"InputComposerBars.tsx",
    "Defines the composer bar layouts for edit mode and normal chat mode, wiring together the input editor, action buttons, prefix chips (cited code / reply info), and mode/model pills.",
    ["component", "composer", "ui", "layout"], "complex")

add_file(P+"InputEditor.tsx",
    "Wraps ComposerInput with drag-drop image attachment, paste, and keyboard-menu-trigger handling to provide the rich text editing surface for chat messages.",
    ["component", "editor", "drag-drop", "ui"], "moderate")

add_file(P+"MiniCpmCompactCard.tsx",
    "Renders a compact status card summarizing background agent progress or error state inline in the composer, including an error-message normalization helper.",
    ["component", "ui", "status-card"], "moderate")

add_file(P+"ModePill.tsx",
    "Compact selector pill for choosing the agent execution mode, reading from and writing to controlled, session-creator-default, or per-session state depending on usage context.",
    ["component", "dropdown", "ui", "mode-selector"], "complex")

add_file(P+"ModelPill.tsx",
    "Compact selector pill for choosing the active AI model for the current session, backed by a searchable dropdown panel.",
    ["component", "dropdown", "ui", "model-selector"], "complex")

add_file(P+"PinnedActionsBar/PinActionsPanel.tsx",
    "Renders the expandable panel of pinned quick-actions and slash commands, with helpers to derive a stable key for an action and to convert a slash item into a pinned action.",
    ["component", "panel", "ui", "actions"], "complex")

add_file(P+"PinnedActionsBar/index.tsx",
    "Renders the pinned actions bar shown above the composer, including individual action pill buttons and the trigger that opens the full PinActionsPanel.",
    ["component", "toolbar", "ui", "actions"], "complex")

add_file(P+"PlanTodoPill.tsx",
    "Renders a pill showing plan/todo progress for the active session, with per-status icon rendering and a helper to count completed todos.",
    ["component", "ui", "todo", "progress"], "moderate")

add_file(P+"ProgressRing.tsx",
    "Renders an SVG circular progress ring used to visualize context-usage percentage in the composer.",
    ["component", "ui", "svg", "progress-indicator"], "simple")

add_file(P+"PromptPolishButton.tsx",
    "Renders a button that triggers AI-assisted prompt polishing/rewriting for the current composer input.",
    ["component", "ui", "button"], "simple")

add_file(P+"QueueEditModeCard.tsx",
    "Renders a small informational card in the composer indicating the input is currently in queue-edit mode.",
    ["component", "ui", "banner"], "simple")

add_file(P+"QueuedMessageItem.tsx",
    "Renders a single queued message row within the message queue list, displaying a not-yet-sent message and its available actions.",
    ["component", "ui", "list-item", "queue"], "moderate")

add_file(P+"QueuedMessages.tsx",
    "Renders the stack of queued (not-yet-sent) messages above the composer using QueuedMessageItem rows and a header, tracking drag-reorder activity via a module-level ref.",
    ["component", "ui", "queue", "list"], "moderate")

add_file(P+"ReplyInfoDisplay.tsx",
    "Renders a compact chip showing which message is currently being replied to, with a button to clear the reply target.",
    ["component", "ui", "chip"], "simple")

add_file(P+"SessionReadOnlyBar.tsx",
    "Renders a bar indicating the current session is read-only, shown in place of the normal composer controls.",
    ["component", "ui", "banner"], "simple")

add_file(P+"SlashCommandPortal/AddressCommentsFlyout.tsx",
    "Renders a flyout panel for selecting review-comment threads to address, grouped by scope (session/round) with select-all and per-scope toggling.",
    ["component", "flyout", "ui", "code-review"], "complex")

add_file(P+"SlashCommandPortal/FlyoutSubmenu.tsx",
    "Renders a grouped submenu flyout (used for mode/model selection) that lists items by category with keyboard highlight support and outside-click dismissal.",
    ["component", "flyout", "ui", "menu"], "moderate")

add_file(P+"SlashCommandPortal/MenuRows.tsx",
    "Provides the individual row renderer components used inside the slash-command menu: section headers, image rows, mode rows, flyout triggers, slash-item rows, and dividers.",
    ["component", "ui", "menu", "list-item"], "moderate")

add_file(P+"SlashCommandPortal/SlashCommandMenu.tsx",
    "Implements the full slash-command dropdown menu: search/filter input, keyboard navigation, category flyouts, and selection handling for slash items and modes.",
    ["component", "menu", "ui", "keyboard-navigation"], "complex")

add_file(P+"SlashCommandPortal/constants.ts",
    "Defines the flyout categories, ordering, labels, and icons used by the slash-command menu's grouped flyouts.",
    ["constants", "config", "ui"], "simple")

add_file(P+"SlashCommandPortal/index.tsx",
    "Public entry point for the SlashCommandPortal module; a thin wrapper that renders SlashCommandMenu only when visible, preserving component identity across visibility toggles.",
    ["entry-point", "component", "barrel"], "simple")

add_file(P+"SlashCommandPortal/slashItemUtils.ts",
    "Utility functions for normalizing skill descriptions, resolving a skill's group/origin label from its path, and building MCP tool slash-command strings.",
    ["utility", "mapper"], "simple")

add_file(P+"SlashCommandPortal/types.ts",
    "Type definitions for the SlashCommandPortal module's public props, search mode, and related shared types.",
    ["type-definition"], "moderate")

add_file(P+"SlashCommandPortal/useEntries.ts",
    "Hook that builds the filtered, categorized, and search-matched list of slash-command menu entries (modes, images, sections, items) from raw slash items and a search query.",
    ["hook", "utility", "search"], "complex")

add_file(P+"SlashCommandPortal/useKeyboard.ts",
    "Hook implementing keyboard navigation (arrow keys, enter, escape) across the slash-command menu's flat entry list and nested category flyouts.",
    ["hook", "keyboard-navigation"], "complex")

add_file(P+"TurnCollapsePinBar.tsx",
    "Renders a bar for collapsing/pinning a conversation turn group in the chat history, related to GroupHeaderRenderer.",
    ["component", "ui", "chat-history"], "moderate")

add_file(P+"UserActionButton.tsx",
    "Renders a small titled action button with optional left/right icons and an optional close affordance, used for user-facing quick actions.",
    ["component", "ui", "button"], "simple")

add_file(P+"compactFileChangesHelpers.ts",
    "Utility functions mapping final-diff and edit-artifact data into normalized FileChangeInfo records, plus helpers for counting chat rounds and building a cache-invalidation key for the compact file-changes view.",
    ["utility", "mapper", "data-transform"], "moderate")

add_file(P+"contextInfoTypes.ts",
    "Shared constants and a helper for the context-usage ring/panel UI: stroke-color-by-percentage lookup plus ring and panel sizing constants.",
    ["constants", "utility", "ui"], "simple")

add_file(P+"floatingPlacement.ts",
    "Geometry utilities for positioning floating/portal UI elements (menus, flyouts) relative to an anchor element within the viewport, including viewport clamping and above/below placement resolution.",
    ["utility", "geometry", "positioning"], "moderate")

# ============ FUNCTION NODES (Part 1 files) ============

add_fn(P+"InputActions.tsx", "InputActions", (55, 240),
    "Memoized send-button component implementing a priority-ordered state machine (submit/stop/retry/resume) based on agent working, pending-cancel, and terminal session states.",
    ["component", "state-machine", "event-handler"], "complex", exported=True)

add_fn(P+"InputAreaChrome.tsx", "InputAreaTopRows", (24, 52),
    "Renders the composer's top row: optional chat header, pinned-actions bar, and plan-todo pill, unless suppressed for edit mode.",
    ["component", "layout"], "simple", exported=True)
add_fn(P+"InputAreaChrome.tsx", "QuietEditStatus", (61, 87),
    "Renders a subdued status label shown while in \"quiet\" edit mode instead of the full edit header.",
    ["component", "ui"], "simple", exported=True)
add_fn(P+"InputAreaChrome.tsx", "EditImagePreviews", (96, 125),
    "Renders the thumbnail strip of images attached while editing a message, with per-image removal handlers.",
    ["component", "ui", "image-preview"], "simple", exported=True)
add_fn(P+"InputAreaChrome.tsx", "getComposerShellVariant", (127, 141),
    "Derives the visual variant (default/edit/quiet) of the composer shell background based on edit-mode state.",
    ["utility", "styling"], "simple", exported=True)
add_fn(P+"InputAreaChrome.tsx", "getComposerShellClassName", (143, 164),
    "Computes the composer shell's Tailwind class name, accounting for drag-over, edit mode, quiet surface, and breathing-animation flags.",
    ["utility", "styling"], "simple", exported=True)

add_fn(P+"InputAreaPortals.tsx", "InputAreaPortals", (57, 161),
    "Renders the input area's floating surfaces (context menu, at-mention menu, slash-command menu) based on visibility and query state props.",
    ["component", "portal", "ui"], "complex", exported=True)

add_fn(P+"InputComposerBars.tsx", "ComposerPrefixes", (73, 100),
    "Renders the prefix chips shown above the input editor -- cited code snippet preview and reply-target chip -- with clear handlers.",
    ["component", "ui", "chip"], "simple", exported=False)
add_fn(P+"InputComposerBars.tsx", "EditComposerBar", (102, 262),
    "Renders the full composer layout used when editing an existing message, wiring the input editor, context/slash menus, action buttons, and cancel/send-now controls.",
    ["component", "composer", "edit-mode"], "complex", exported=True)
add_fn(P+"InputComposerBars.tsx", "NormalComposerContent", (288, 455),
    "Renders the full composer layout used for normal (non-edit) message composition, wiring the input editor, image previews, action buttons, and mode/model pills.",
    ["component", "composer", "ui"], "complex", exported=True)

add_fn(P+"InputEditor.tsx", "InputEditor", (80, 207),
    "Memoized rich-text input component wrapping ComposerInput, handling drag-drop image attachment, paste, focus/blur, and keyboard-driven menu triggers.",
    ["component", "editor", "drag-drop"], "complex", exported=True)

add_fn(P+"MiniCpmCompactCard.tsx", "MiniCpmCompactCard", (28, 109),
    "Memoized compact status card rendering progress or error state for a background agent task inline within the composer.",
    ["component", "ui", "status-card"], "moderate", exported=True)

add_fn(P+"ModePill.tsx", "ModePill", (64, 244),
    "Memoized dropdown pill for selecting the AgentExecMode, resolving its value from a controlled prop, the session-creator default atom, or the per-session field depending on usage context.",
    ["component", "dropdown", "state-management"], "complex", exported=True)

add_fn(P+"ModelPill.tsx", "ModelPill", (53, 279),
    "Memoized dropdown pill for selecting the active AI model for the session, rendering a searchable list of available models in a portal-based dropdown.",
    ["component", "dropdown", "ui"], "complex", exported=True)

add_fn(P+"PinnedActionsBar/PinActionsPanel.tsx", "actionKey", (44, 56),
    "Derives a stable, unique key string for a pinned action or slash item for use in React lists and pinned-key comparisons.",
    ["utility"], "simple", exported=True)
add_fn(P+"PinnedActionsBar/PinActionsPanel.tsx", "slashItemToAction", (58, 67),
    "Converts a SlashItem into a normalized PinnedAction object for display in the pinned actions panel.",
    ["utility", "mapper"], "simple", exported=True)
add_fn(P+"PinnedActionsBar/PinActionsPanel.tsx", "PinActionsPanel", (104, 372),
    "Memoized panel component rendering the searchable, sectioned list of pinnable actions/slash commands with keyboard navigation and pin/unpin toggling.",
    ["component", "panel", "keyboard-navigation"], "complex", exported=True)

add_fn(P+"PinnedActionsBar/index.tsx", "ActionPill", (66, 98),
    "Renders a single pinned action as a small pill button within the pinned actions bar.",
    ["component", "ui", "button"], "simple", exported=False)
add_fn(P+"PinnedActionsBar/index.tsx", "PinnedActionsBar", (117, 401),
    "Memoized toolbar rendering the row of pinned action pills above the composer plus the trigger that opens the full PinActionsPanel.",
    ["component", "toolbar", "ui"], "complex", exported=True)

add_fn(P+"PlanTodoPill.tsx", "TodoStatusIcon", (24, 55),
    "Renders the status icon (pending/in-progress/completed/blocked) for a single plan todo item.",
    ["component", "ui", "icon"], "simple", exported=False)
add_fn(P+"PlanTodoPill.tsx", "countCompletedTodos", (61, 64),
    "Counts how many todo items in a list have a completed status.",
    ["utility"], "simple", exported=True)
add_fn(P+"PlanTodoPill.tsx", "PlanTodoPill", (70, 206),
    "Memoized pill component showing plan/todo progress for the active session, expanding to a detail list on interaction.",
    ["component", "ui", "progress"], "complex", exported=True)

add_fn(P+"ProgressRing.tsx", "ProgressRing", (24, 64),
    "Memoized SVG ring component that visualizes a percentage value with tone-based coloring for context-usage display.",
    ["component", "ui", "svg"], "simple", exported=True)

add_fn(P+"PromptPolishButton.tsx", "PromptPolishButton", (13, 72),
    "Memoized button component that triggers prompt-polishing and reflects its loading/disabled state.",
    ["component", "ui", "button"], "simple", exported=True)

add_fn(P+"QueueEditModeCard.tsx", "QueueEditModeCard", (8, 31),
    "Renders an informational banner card indicating the composer is currently in queue-edit mode, reading the relevant atom for context.",
    ["component", "ui", "banner"], "simple", exported=True)

add_fn(P+"QueuedMessageItem.tsx", "QueuedMessageItem", (36, 145),
    "Memoized row component rendering a single queued (unsent) message with its content and available actions.",
    ["component", "ui", "list-item"], "moderate", exported=True)

add_fn(P+"QueuedMessages.tsx", "QueuedMessages", (60, 177),
    "Memoized component rendering the stack of queued messages above the composer with a header and reorderable item list.",
    ["component", "ui", "queue"], "complex", exported=True)

add_fn(P+"ReplyInfoDisplay.tsx", "ReplyInfoDisplay", (29, 48),
    "Memoized chip component displaying the message currently being replied to, with a clear/close action.",
    ["component", "ui", "chip"], "simple", exported=True)

# ============ FUNCTION NODES (Part 2 files) ============

add_fn(P+"SessionReadOnlyBar.tsx", "SessionReadOnlyBar", (31, 62),
    "Memoized bar component indicating the current session is read-only, replacing normal composer controls.",
    ["component", "ui", "banner"], "simple", exported=True)

add_fn(P+"SlashCommandPortal/AddressCommentsFlyout.tsx", "AddressCommentsFlyout", (29, 254),
    "Renders the flyout for selecting review-comment threads to address, grouped by scope with select-all/per-scope/per-thread toggling and outside-click dismissal.",
    ["component", "flyout", "code-review"], "complex", exported=True)

add_fn(P+"SlashCommandPortal/FlyoutSubmenu.tsx", "FlyoutSubmenu", (33, 175),
    "Renders a grouped submenu flyout listing items by category with keyboard-highlight scrolling and outside-click dismissal.",
    ["component", "flyout", "menu"], "complex", exported=True)

add_fn(P+"SlashCommandPortal/MenuRows.tsx", "DividerRow", (212, 214),
    "Renders a thin horizontal divider row between menu sections.",
    ["component", "ui"], "simple", exported=True)
add_fn(P+"SlashCommandPortal/MenuRows.tsx", "SectionHeaderRow", (44, 53),
    "Renders a labeled section-header row within the slash-command menu.",
    ["component", "ui", "list-item"], "simple", exported=True)
add_fn(P+"SlashCommandPortal/MenuRows.tsx", "ImageRow", (60, 90),
    "Renders the menu row offering image upload/attachment as a slash-menu action.",
    ["component", "ui", "list-item"], "moderate", exported=True)
add_fn(P+"SlashCommandPortal/MenuRows.tsx", "ModeRow", (99, 131),
    "Renders a selectable agent-execution-mode row within the slash-command menu.",
    ["component", "ui", "list-item"], "moderate", exported=True)
add_fn(P+"SlashCommandPortal/MenuRows.tsx", "FlyoutTriggerRow", (141, 174),
    "Renders a menu row that opens a category flyout (e.g., mode or model selection) on click.",
    ["component", "ui", "list-item"], "moderate", exported=True)
add_fn(P+"SlashCommandPortal/MenuRows.tsx", "SlashItemRow", (182, 211),
    "Renders a single selectable slash-command item row with icon, label, and active/selected styling.",
    ["component", "ui", "list-item"], "moderate", exported=True)

add_fn(P+"SlashCommandPortal/SlashCommandMenu.tsx", "SlashCommandMenu", (48, 518),
    "Implements the full slash-command dropdown menu including entry building via useEntries, keyboard navigation via useKeyboard, category flyouts, positioning, and selection handling.",
    ["component", "menu", "keyboard-navigation"], "complex", exported=True)

add_fn(P+"SlashCommandPortal/constants.ts", "categoryIcon", (22, 33),
    "Returns the icon component associated with a given flyout category (mode or models).",
    ["utility", "ui"], "simple", exported=True)

add_fn(P+"SlashCommandPortal/index.tsx", "SlashCommandPortal", (15, 21),
    "Thin wrapper component that renders SlashCommandMenu only when visible, preserving stable component identity across visibility toggles.",
    ["component", "entry-point", "wrapper"], "simple", exported=True)

add_fn(P+"SlashCommandPortal/slashItemUtils.ts", "normalizeSkillDescription", (17, 22),
    "Returns a skill's description, falling back to a placeholder string when none is provided.",
    ["utility"], "simple", exported=True)
add_fn(P+"SlashCommandPortal/slashItemUtils.ts", "resolveSkillGroup", (37, 78),
    "Resolves a human-readable group/origin label for a skill by parsing its filesystem path (home directory, repo-relative, or well-known prefixes).",
    ["utility", "path-parsing"], "complex", exported=True)
add_fn(P+"SlashCommandPortal/slashItemUtils.ts", "buildMcpToolCommand", (84, 90),
    "Builds the slash-command string identifying an MCP server tool from its server and tool names.",
    ["utility", "string-formatting"], "simple", exported=True)

add_fn(P+"SlashCommandPortal/useEntries.ts", "useEntries", (42, 231),
    "Hook that builds the filtered, categorized list of slash-command menu entries (modes, image action, section headers, flyout triggers, items) from raw slash items and a fuzzy search query.",
    ["hook", "search", "data-transform"], "complex", exported=True)

add_fn(P+"SlashCommandPortal/useKeyboard.ts", "useKeyboard", (37, 194),
    "Hook implementing arrow/enter/escape keyboard navigation across the slash-command menu's flat entry list and nested category flyouts.",
    ["hook", "keyboard-navigation"], "complex", exported=True)

add_fn(P+"TurnCollapsePinBar.tsx", "TurnCollapsePinBar", (54, 159),
    "Memoized bar component for collapsing/pinning a conversation turn group in the chat history.",
    ["component", "ui", "chat-history"], "complex", exported=True)

add_fn(P+"UserActionButton.tsx", "UserActionButton", (12, 48),
    "Renders a small titled action button with optional left/right icons and an optional close affordance.",
    ["component", "ui", "button"], "simple", exported=True)

add_fn(P+"compactFileChangesHelpers.ts", "mapFinalDiffToFileChangeInfo", (45, 57),
    "Maps a final-diff record into a normalized list of FileChangeInfo entries for the compact file-changes view.",
    ["utility", "mapper"], "simple", exported=True)
add_fn(P+"compactFileChangesHelpers.ts", "mapEditArtifactsToFileChangeInfo", (59, 97),
    "Maps a collection of edit artifacts into deduplicated, normalized FileChangeInfo entries keyed by file path.",
    ["utility", "mapper", "data-transform"], "complex", exported=True)
add_fn(P+"compactFileChangesHelpers.ts", "countChatRounds", (111, 119),
    "Counts the number of completed chat rounds from a list of chat events.",
    ["utility"], "simple", exported=True)
add_fn(P+"compactFileChangesHelpers.ts", "buildCompactFilesReloadKey", (127, 133),
    "Builds a cache-invalidation key combining session id, round count, and agent-working state for the compact file-changes view.",
    ["utility"], "simple", exported=True)

add_fn(P+"contextInfoTypes.ts", "ringToneForPercentage", (25, 30),
    "Returns the stroke color/tone to use for the context-usage ring based on a usage percentage.",
    ["utility", "styling"], "simple", exported=True)

add_fn(P+"floatingPlacement.ts", "resolveFloatingPlacement", (48, 61),
    "Resolves whether a floating element should be placed above or below its anchor, given the requested strategy and available space.",
    ["utility", "geometry"], "simple", exported=False)
add_fn(P+"floatingPlacement.ts", "computeFloatingPosition", (63, 114),
    "Computes the final clamped screen position for a floating/portal element relative to an anchor rect, viewport size, and placement strategy.",
    ["utility", "geometry", "positioning"], "complex", exported=True)

# ============ IMPORT EDGES (from batchImportData, 1:1) ============

add_import(P+"InputAreaChrome.tsx", [
    "src/engines/ChatPanel/InputArea/ChatHeader/index.tsx",
    "src/engines/ChatPanel/InputArea/components/EditModeImageThumbnail.tsx",
    "src/engines/ChatPanel/InputArea/components/ImageAttachmentPreview.tsx",
    "src/engines/ChatPanel/InputArea/components/PinnedActionsBar/index.tsx",
    "src/engines/ChatPanel/InputArea/components/PlanTodoPill.tsx",
])
add_import(P+"InputAreaPortals.tsx", [
    "src/engines/ChatPanel/InputArea/components/ContextMenuPortal.tsx",
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/index.tsx",
])
add_import(P+"InputComposerBars.tsx", [
    "src/engines/ChatPanel/InputArea/components/CiteCodePreview.tsx",
    "src/engines/ChatPanel/InputArea/components/ImageAttachmentPreview.tsx",
    "src/engines/ChatPanel/InputArea/components/InputActions.tsx",
    "src/engines/ChatPanel/InputArea/components/InputEditor.tsx",
    "src/engines/ChatPanel/InputArea/components/PromptPolishButton.tsx",
    "src/engines/ChatPanel/InputArea/components/ReplyInfoDisplay.tsx",
])
add_import(P+"PinnedActionsBar/index.tsx", [
    "src/engines/ChatPanel/InputArea/components/PinnedActionsBar/PinActionsPanel.tsx",
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/slashItemUtils.ts",
])
add_import(P+"ProgressRing.tsx", [
    "src/engines/ChatPanel/InputArea/components/contextInfoTypes.ts",
])
add_import(P+"QueuedMessages.tsx", [
    "src/engines/ChatPanel/InputArea/components/ComposerStackHeader.tsx",
    "src/engines/ChatPanel/InputArea/components/QueuedMessageItem.tsx",
])
add_import(P+"ReplyInfoDisplay.tsx", [
    "src/engines/ChatPanel/InputArea/components/UserActionButton.tsx",
])
add_import(P+"SessionReadOnlyBar.tsx", [
    "src/engines/ChatPanel/InputArea/components/ContextInfoButton.tsx",
])
add_import(P+"SlashCommandPortal/FlyoutSubmenu.tsx", [
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/constants.ts",
])
add_import(P+"SlashCommandPortal/MenuRows.tsx", [
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/constants.ts",
])
add_import(P+"SlashCommandPortal/SlashCommandMenu.tsx", [
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/AddressCommentsFlyout.tsx",
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/FlyoutSubmenu.tsx",
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/MenuRows.tsx",
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/types.ts",
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/useEntries.ts",
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/useKeyboard.ts",
    "src/engines/ChatPanel/InputArea/components/useFloatingPortalPosition.ts",
])
add_import(P+"SlashCommandPortal/index.tsx", [
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/SlashCommandMenu.tsx",
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/types.ts",
])
add_import(P+"SlashCommandPortal/types.ts", [
    "src/engines/ChatPanel/InputArea/components/floatingPlacement.ts",
])
add_import(P+"SlashCommandPortal/useEntries.ts", [
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/constants.ts",
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/types.ts",
])
add_import(P+"SlashCommandPortal/useKeyboard.ts", [
    "src/engines/ChatPanel/InputArea/components/SlashCommandPortal/types.ts",
])

# ============ CALLS EDGES (grounded in source / callGraph) ============

add_call(P+"InputComposerBars.tsx", "ComposerPrefixes", P+"ReplyInfoDisplay.tsx", "ReplyInfoDisplay")
add_call(P+"InputComposerBars.tsx", "EditComposerBar", P+"InputEditor.tsx", "InputEditor")
add_call(P+"InputComposerBars.tsx", "EditComposerBar", P+"InputActions.tsx", "InputActions")
add_call(P+"InputComposerBars.tsx", "NormalComposerContent", P+"InputEditor.tsx", "InputEditor")
add_call(P+"InputComposerBars.tsx", "NormalComposerContent", P+"PromptPolishButton.tsx", "PromptPolishButton")
add_call(P+"InputComposerBars.tsx", "NormalComposerContent", P+"InputActions.tsx", "InputActions")
add_call(P+"InputAreaPortals.tsx", "InputAreaPortals", P+"SlashCommandPortal/index.tsx", "SlashCommandPortal")
add_call(P+"InputAreaChrome.tsx", "InputAreaTopRows", P+"PinnedActionsBar/index.tsx", "PinnedActionsBar")
add_call(P+"InputAreaChrome.tsx", "InputAreaTopRows", P+"PlanTodoPill.tsx", "PlanTodoPill")
add_call(P+"PinnedActionsBar/index.tsx", "PinnedActionsBar", P+"PinnedActionsBar/PinActionsPanel.tsx", "PinActionsPanel")

add_call(P+"SlashCommandPortal/index.tsx", "SlashCommandPortal", P+"SlashCommandPortal/SlashCommandMenu.tsx", "SlashCommandMenu")
add_call(P+"SlashCommandPortal/FlyoutSubmenu.tsx", "FlyoutSubmenu", P+"SlashCommandPortal/constants.ts", "categoryIcon")
add_call(P+"SlashCommandPortal/SlashCommandMenu.tsx", "SlashCommandMenu", P+"SlashCommandPortal/useEntries.ts", "useEntries")
add_call(P+"SlashCommandPortal/SlashCommandMenu.tsx", "SlashCommandMenu", P+"SlashCommandPortal/useKeyboard.ts", "useKeyboard")
edges.append({
    "source": fnid(P+"SlashCommandPortal/SlashCommandMenu.tsx", "SlashCommandMenu"),
    "target": "function:src/engines/ChatPanel/InputArea/components/useFloatingPortalPosition.ts:useFloatingPortalPosition",
    "type": "calls", "direction": "forward", "weight": 0.8
})

# ============ Partition into parts ============

part1_files = {
    P+"InputActions.tsx", P+"InputAreaChrome.tsx", P+"InputAreaPortals.tsx", P+"InputComposerBars.tsx",
    P+"InputEditor.tsx", P+"MiniCpmCompactCard.tsx", P+"ModePill.tsx", P+"ModelPill.tsx",
    P+"PinnedActionsBar/PinActionsPanel.tsx", P+"PinnedActionsBar/index.tsx", P+"PlanTodoPill.tsx",
    P+"ProgressRing.tsx", P+"PromptPolishButton.tsx", P+"QueueEditModeCard.tsx", P+"QueuedMessageItem.tsx",
    P+"QueuedMessages.tsx", P+"ReplyInfoDisplay.tsx",
}

def node_file_path(n):
    if n["type"] == "file":
        return n["filePath"]
    return n.get("filePath")

part1_nodes = [n for n in nodes if node_file_path(n) in part1_files]
part2_nodes = [n for n in nodes if node_file_path(n) not in part1_files]

part1_ids = {n["id"] for n in part1_nodes}
part2_ids = {n["id"] for n in part2_nodes}

def edge_source_file(e):
    src = e["source"]
    # source is always file: or function: with a path component
    parts = src.split(":", 2)
    if parts[0] == "file":
        return parts[1]
    elif parts[0] == "function":
        return parts[1]
    return None

part1_edges = [e for e in edges if edge_source_file(e) in part1_files]
part2_edges = [e for e in edges if edge_source_file(e) not in part1_files]

print("Total nodes:", len(nodes), "Total edges:", len(edges))
print("Part1 nodes:", len(part1_nodes), "Part1 edges:", len(part1_edges))
print("Part2 nodes:", len(part2_nodes), "Part2 edges:", len(part2_edges))

# sanity check: no dup node ids
ids = [n["id"] for n in nodes]
assert len(ids) == len(set(ids)), "duplicate node ids!"

# sanity: no self edges
for e in edges:
    assert e["source"] != e["target"], f"self edge {e}"

out1 = {"nodes": part1_nodes, "edges": part1_edges}
out2 = {"nodes": part2_nodes, "edges": part2_edges}

with open("/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate/batch-22-part-1.json", "w") as f:
    json.dump(out1, f, indent=2)
with open("/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate/batch-22-part-2.json", "w") as f:
    json.dump(out2, f, indent=2)

print("Written.")
