#!/usr/bin/env python3
import json

OUT_DIR = "/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate"

# ---------------------------------------------------------------------------
# File node definitions
# ---------------------------------------------------------------------------
FILES = [
    dict(path="src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/index.tsx",
         name="index.tsx",
         summary="React hook that aggregates local and Linear-synced projects, work items, and orgs into sidebar menu rows for the Projects/Work Items navigation section, handling async loading, pagination, and tab-opening actions.",
         tags=["hook", "sidebar", "work-items", "linear-integration", "api-handler"],
         complexity="complex"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/linearHelpers.ts",
         name="linearHelpers.ts",
         summary="Small utility functions for deriving Linear org identifiers and display names and normalizing Linear API errors.",
         tags=["utility", "linear-integration", "error-handling"],
         complexity="simple"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx",
         name="menuRows.tsx",
         summary="Builder functions that construct individual sidebar menu row objects (separators, org rows, project rows, work item rows, load-more rows) for the Projects/Work Items sidebar section.",
         tags=["utility", "sidebar", "menu-builder", "work-items"],
         complexity="moderate"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/types.ts",
         name="types.ts",
         summary="Type definitions for the Projects/Work Items sidebar hook, including local/Linear project, org, and work item shapes plus hook parameter and result types.",
         tags=["type-definition", "sidebar", "work-items"],
         complexity="moderate"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/workItemMapping.tsx",
         name="workItemMapping.tsx",
         summary="Maps and validates work item status/priority values, renders status icons, and provides sorting/grouping helpers used when building work item sidebar rows.",
         tags=["utility", "work-items", "mapping", "data-model"],
         complexity="moderate"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useRenameSessionModal.ts",
         name="useRenameSessionModal.ts",
         summary="React hook that manages the state and submit flow for the session rename modal, persisting the new name via the session store and backend RPC.",
         tags=["hook", "modal", "session-management", "api-handler"],
         complexity="moderate"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useSessionMenuItems.tsx",
         name="useSessionMenuItems.tsx",
         summary="Barrel file re-exporting the useSessionMenuItems hook and its helpers from the useSessionMenuItems directory.",
         tags=["barrel", "re-export", "sidebar"],
         complexity="simple"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/dateGroupingHelpers.ts",
         name="dateGroupingHelpers.ts",
         summary="Defines date-based grouping keys and a helper to bucket a session into a date group (today, yesterday, this week, etc.) for the sidebar session list.",
         tags=["utility", "sidebar", "date-grouping"],
         complexity="simple"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/index.tsx",
         name="index.tsx",
         summary="Core hook that builds the full set of sidebar menu items for chat sessions, handling subagent child-session fetching, benchmark session filtering, search, org filtering, grouping (time/agent/workspace), and pagination.",
         tags=["hook", "sidebar", "session-management", "complex-logic", "api-handler"],
         complexity="complex"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/menuItemBuilders.tsx",
         name="menuItemBuilders.tsx",
         summary="Helper predicates and a builder function that construct an individual session sidebar row, including read/unread and pending-ask status.",
         tags=["utility", "sidebar", "menu-builder", "session-management"],
         complexity="moderate"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/menuSectionBuilders.ts",
         name="menuSectionBuilders.ts",
         summary="Builds grouped sidebar menu item sections for sessions organized by time, coordinating agent, or workspace, inserting separators and per-group load-more rows.",
         tags=["utility", "sidebar", "menu-builder", "grouping"],
         complexity="moderate"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/orgFilter.ts",
         name="orgFilter.ts",
         summary="Resolves which organization ids a sidebar session list should match against, supporting both local and Linear/collab org selections.",
         tags=["utility", "sidebar", "filtering", "org-scope"],
         complexity="simple"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx",
         name="paginationHelpers.tsx",
         summary="Builds load-more and unified load-more sidebar rows, tracks per-category and cross-workspace pagination state, and renders group visibility.",
         tags=["utility", "sidebar", "pagination", "menu-builder"],
         complexity="moderate"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/sessionGroupHelpers.ts",
         name="sessionGroupHelpers.ts",
         summary="Converts a session sidebar group key into the wire-level session list category used by pagination requests.",
         tags=["utility", "sidebar", "mapping"],
         complexity="simple"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/statusIndicators.tsx",
         name="statusIndicators.tsx",
         summary="Renders small animated and static status dot indicators (loading/breathing pulse, colored tone dot) used on sidebar load-more and pagination rows.",
         tags=["component", "sidebar", "status-indicator", "ui"],
         complexity="simple"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/types.ts",
         name="types.ts",
         summary="Type definitions for the session sidebar hook, including its parameters, pagination state, and grouped menu item results.",
         tags=["type-definition", "sidebar", "session-management"],
         complexity="moderate"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useWorkstationSidebarContextMenu.ts",
         name="useWorkstationSidebarContextMenu.ts",
         summary="React hook that builds and pops native Tauri right-click context menus for sidebar drafts and sessions, wiring rename, delete, pin, export, move, and cloud sync/share actions.",
         tags=["hook", "sidebar", "context-menu", "tauri", "api-handler"],
         complexity="complex"),
    dict(path="src/scaffold/NavigationSidebar/connectors/useWorkstationSidebarHandlers.ts",
         name="useWorkstationSidebarHandlers.ts",
         summary="React hook centralizing the workstation sidebar's action handlers: session deletion (local and cloud), markdown export, draft/new-session creation, load-more pagination, and chat-panel tab navigation.",
         tags=["hook", "sidebar", "event-handler", "session-management", "api-handler"],
         complexity="complex"),
    dict(path="src/scaffold/NavigationSidebar/connectors/workstationSidebarData.ts",
         name="workstationSidebarData.ts",
         summary="Pure data-shaping utilities for the workstation sidebar: sorting sessions by activity, mapping repo paths to display names, and resolving the currently selected sidebar/section id.",
         tags=["utility", "sidebar", "data-model"],
         complexity="moderate"),
    dict(path="src/scaffold/NavigationSidebar/connectors/workstationSidebarMenuItems.tsx",
         name="workstationSidebarMenuItems.tsx",
         summary="Builds the pinned menu items (new session, work items, Kanban, projects actions) and session-creator draft rows shown at the top of the workstation sidebar.",
         tags=["utility", "sidebar", "menu-builder"],
         complexity="moderate"),
    dict(path="src/scaffold/NavigationSidebar/contexts/ForceVisibleContext.tsx",
         name="ForceVisibleContext.tsx",
         summary="React context and provider that force nested sidebars to render as visible even while collapsed, used by the floating hover sidebar.",
         tags=["context", "sidebar", "provider", "react"],
         complexity="simple"),
    dict(path="src/scaffold/NavigationSidebar/types.ts",
         name="types.ts",
         summary="Centralized TypeScript type definitions for the unified sidebar system, covering item, group, section, theme, and props shapes shared across all sidebar variants and blocks.",
         tags=["type-definition", "sidebar", "shared-types"],
         complexity="complex"),
    dict(path="src/scaffold/NavigationSidebar/utils/menuFromRoutes.ts",
         name="menuFromRoutes.ts",
         summary="Converts a route configuration entry into a navigation menu item, resolving labels and icons, for deriving sidebar menus directly from the route table.",
         tags=["utility", "sidebar", "routing", "menu-builder"],
         complexity="simple"),
    dict(path="src/scaffold/NavigationSidebar/utils/renderIcon.tsx",
         name="renderIcon.tsx",
         summary="Renders a sidebar icon (Lucide component, string name, or React node) with optional hover-triggered animation classes.",
         tags=["utility", "sidebar", "icon", "rendering"],
         complexity="moderate"),
    dict(path="src/scaffold/NavigationSidebar/variants/EconomySidebar.tsx",
         name="EconomySidebar.tsx",
         summary="Compact sidebar variant that renders a page-level sidebar wrapper used in space-constrained ('economy') layouts.",
         tags=["component", "sidebar", "variant", "react"],
         complexity="moderate"),
    dict(path="src/scaffold/NavigationSidebar/variants/HomeSidebar.tsx",
         name="HomeSidebar.tsx",
         summary="Primary application sidebar shown on the home/workstation screen, combining navigation menu items derived from routes with the workstation session list, spotlight search entry point, and a native right-click settings menu.",
         tags=["component", "sidebar", "variant", "navigation", "react"],
         complexity="complex"),
    dict(path="src/scaffold/NavigationSidebar/variants/NavigationSidebar.tsx",
         name="NavigationSidebar.tsx",
         summary="Reusable, memoized base sidebar component rendering navigation and pinned menu items with icons, submenus, search filtering, and collapse/expand behavior; underlies the Home, Page-level, and Settings sidebar variants.",
         tags=["component", "sidebar", "navigation", "react", "memoized"],
         complexity="complex"),
    dict(path="src/scaffold/NavigationSidebar/variants/PageLevelSidebar.tsx",
         name="PageLevelSidebar.tsx",
         summary="Sidebar variant for secondary/detail pages that shows a back button plus a flat list of navigable items, built on top of the shared NavigationSidebar component.",
         tags=["component", "sidebar", "variant", "react"],
         complexity="moderate"),
    dict(path="src/scaffold/NavigationSidebar/variants/SettingsSidebar.tsx",
         name="SettingsSidebar.tsx",
         summary="Sidebar variant for the Settings screen, rendering either the settings navigation menu or (at the settings root) a two-tier list of app and core setting sections with icons and integration links.",
         tags=["component", "sidebar", "variant", "settings", "react"],
         complexity="complex"),
]

FILE_TYPE = "file"

# ---------------------------------------------------------------------------
# Function node definitions: (filePath, funcName, start, end, exported, summary, tags, complexity)
# ---------------------------------------------------------------------------
FUNCS = [
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/index.tsx", "useProjectsWorkItemMenuItems", 66, 446, True,
     "Fetches and combines local project/org/work-item data with Linear-synced projects and issues, then builds grouped, paginated sidebar menu rows and tab-opening callbacks for the Projects/Work Items sidebar section.",
     ["hook", "api-handler", "work-items", "linear-integration"], "complex"),

    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/linearHelpers.ts", "getLinearOrgId", 6, 8, True,
     "Derives a stable Linear org id string from a connection id and team id.", ["utility", "linear-integration"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/linearHelpers.ts", "getLinearTeamOrgName", 10, 12, True,
     "Formats a Linear team name into the display name used for the org sidebar row.", ["utility", "linear-integration"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/linearHelpers.ts", "getErrorMessage", 14, 16, True,
     "Normalizes an unknown error value to a string message.", ["utility", "error-handling"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/linearHelpers.ts", "isLinearConnection", 18, 20, True,
     "Type guard that checks whether a value is a Linear connection record.", ["utility", "type-guard", "linear-integration"], "simple"),

    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "separator", 23, 25, True,
     "Builds a visual separator row for the Projects/Work Items sidebar menu.", ["utility", "menu-builder"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "localOrgMenuRow", 27, 36, False,
     "Internal builder for a local-org sidebar menu row entry, used by localOrgRow.", ["utility", "menu-builder"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "localOrgRow", 38, 40, True,
     "Builds a sidebar menu row representing a local (non-Linear) organization.", ["utility", "menu-builder", "work-items"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "linearOrgRow", 42, 51, True,
     "Builds a sidebar menu row representing a connected Linear organization.", ["utility", "menu-builder", "linear-integration"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "groupLoadMoreRow", 53, 65, True,
     "Builds a 'load more' row appended to a group of project/work-item menu rows.", ["utility", "menu-builder", "pagination"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "linearLoadRow", 67, 84, True,
     "Builds the row prompting the user to load Linear issues for an org, including a loading state.", ["utility", "menu-builder", "linear-integration"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "createWorkItemRow", 86, 100, True,
     "Builds the 'create work item' action row scoped to a given org.", ["utility", "menu-builder", "work-items"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "buildProjectOverviewRow", 102, 122, True,
     "Builds the sidebar row linking to a project's overview page.", ["utility", "menu-builder", "work-items"], "moderate"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "pendingSyncIndicator", 124, 136, True,
     "Renders a small pending-sync badge/tooltip shown on project rows awaiting collab sync.", ["utility", "ui", "sync-status"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "buildProjectRow", 138, 160, True,
     "Builds the sidebar row for a single project, including its overview link and pending-sync indicator.", ["utility", "menu-builder", "work-items"], "moderate"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "buildWorkItemRow", 162, 190, True,
     "Builds the sidebar row for a single work item, including status icon, Linear linkage, and pending-sync indicator.", ["utility", "menu-builder", "work-items"], "moderate"),

    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/workItemMapping.tsx", "toWorkItemStatus", 16, 18, True,
     "Coerces an arbitrary string into a known WorkItemStatus, defaulting when invalid.", ["utility", "mapping", "work-items"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/workItemMapping.tsx", "toWorkItemPriority", 24, 26, True,
     "Coerces an arbitrary string into a known WorkItemPriority, defaulting when invalid.", ["utility", "mapping", "work-items"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/workItemMapping.tsx", "statusIconElement", 28, 38, True,
     "Renders the icon element representing a given work item status.", ["utility", "ui", "work-items"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/workItemMapping.tsx", "sortWorkItemsByActivity", 40, 50, True,
     "Sorts work items by most recent update/creation activity, most recent first.", ["utility", "sorting", "work-items"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/workItemMapping.tsx", "pushGroupedItems", 52, 63, True,
     "Appends a work item into the appropriate bucket of a grouped-items map, creating the bucket if needed.", ["utility", "grouping", "work-items"], "simple"),

    ("src/scaffold/NavigationSidebar/connectors/useRenameSessionModal.ts", "useRenameSessionModal", 24, 86, True,
     "Hook powering the session rename modal: tracks visibility and the editable name, and submits the new name to the session store and backend RPC on confirm.", ["hook", "modal", "session-management", "api-handler"], "moderate"),

    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/dateGroupingHelpers.ts", "getDateGroup", 13, 15, True,
     "Buckets a session into its date group (today, yesterday, earlier, etc.) based on its timestamp.", ["utility", "date-grouping", "sidebar"], "simple"),

    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/index.tsx", "childRecordToSession", 99, 118, False,
     "Converts a fetched child-session record from the backend into the sidebar Session shape, deriving its subagent display name.", ["utility", "mapping", "session-management"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/index.tsx", "buildChildSessionMenuItem", 120, 134, False,
     "Builds a nested sidebar menu row for a subagent child session, indented under its parent.", ["utility", "menu-builder", "session-management"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/index.tsx", "insertExpandedSubagentRows", 136, 162, False,
     "Inlines child-session rows immediately after their parent row for parents whose subagent list is expanded.", ["utility", "menu-builder", "session-management"], "moderate"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/index.tsx", "useSessionMenuItems", 164, 630, True,
     "Builds the sidebar's full session menu item tree: fetches subagent child sessions on demand, filters by search/org/benchmark visibility, groups sessions by time/agent/workspace, and appends pagination rows.", ["hook", "sidebar", "session-management", "complex-logic"], "complex"),

    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/menuItemBuilders.tsx", "isSessionCompletedUnread", 22, 29, True,
     "Determines whether a completed session should show an unread indicator based on the visited-sessions set.", ["utility", "session-management", "status"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/menuItemBuilders.tsx", "buildSessionMenuItem", 46, 87, True,
     "Builds a single sidebar session row, combining its display name, live status indicator, and read/pending state.", ["utility", "menu-builder", "session-management"], "moderate"),

    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/menuSectionBuilders.ts", "buildByTimeMenuItems", 33, 64, True,
     "Groups unpinned sessions into date-based sections (today, yesterday, etc.) and appends pinned rows, group rows, and trailing load-more items.", ["utility", "menu-builder", "grouping", "date-grouping"], "moderate"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/menuSectionBuilders.ts", "buildByAgentMenuItems", 73, 148, True,
     "Groups unpinned sessions by coordinating agent/org, building nested agent-org sections with their own load-more rows for the sidebar's agent grouping mode.", ["utility", "menu-builder", "grouping", "session-management"], "complex"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/menuSectionBuilders.ts", "buildByWorkspaceMenuItems", 159, 205, True,
     "Groups unpinned sessions by repository/workspace path into labeled sections for the sidebar's workspace grouping mode.", ["utility", "menu-builder", "grouping"], "moderate"),

    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/orgFilter.ts", "buildSessionOrgFilterIds", 14, 27, True,
     "Expands a selected sidebar org id into the full set of org ids to match against, including the corresponding local org id for a Linear selection.", ["utility", "filtering", "org-scope"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/orgFilter.ts", "sessionMatchesOrgFilter", 30, 36, True,
     "Checks whether a session's org tag matches the currently selected sidebar org filter set.", ["utility", "filtering", "org-scope"], "simple"),

    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx", "loadMoreRow", 33, 48, True,
     "Builds a per-category 'load more' sidebar row with an optional loading status dot.", ["utility", "menu-builder", "pagination"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx", "groupLoadMoreRow", 50, 65, True,
     "Builds a 'load more' row scoped to a specific session group.", ["utility", "menu-builder", "pagination"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx", "unifiedLoadMoreRow", 67, 81, True,
     "Builds the combined 'load more' row shown when multiple session categories still have more pages.", ["utility", "menu-builder", "pagination"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx", "getUnifiedLoadMoreState", 98, 124, True,
     "Computes which session categories are still loadable and rolls them into a single unified pagination state.", ["utility", "pagination", "state"], "moderate"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx", "loadUnifiedReadyCategories", 126, 135, True,
     "Triggers loading of all pagination categories that are currently ready to load more.", ["utility", "pagination", "async"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx", "appendSessionGroup", 146, 162, True,
     "Appends a visible slice of a session group's rows to the menu item list, followed by a load-more row if more remain.", ["utility", "menu-builder", "pagination", "grouping"], "simple"),

    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/sessionGroupHelpers.ts", "groupKeyToWireCategory", 8, 18, True,
     "Maps a sidebar agent-group key to the session-list category string expected by the pagination/load-more backend API.", ["utility", "mapping", "pagination"], "simple"),

    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/statusIndicators.tsx", "renderBreathingStatusDot", 7, 21, True,
     "Renders an animated 'breathing' status dot used to indicate an in-progress loading state on sidebar rows.", ["component", "ui", "status-indicator"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/statusIndicators.tsx", "renderStatusDot", 23, 44, True,
     "Renders a static colored status dot for a given tone, used on sidebar pagination/status rows.", ["component", "ui", "status-indicator"], "simple"),

    ("src/scaffold/NavigationSidebar/connectors/useWorkstationSidebarContextMenu.ts", "useWorkstationSidebarContextMenu", 49, 230, True,
     "Builds and displays native Tauri context menus for sidebar drafts and sessions, wiring rename, delete, export, pin, move-to-org, and cloud sync/share menu actions based on session type and eligibility.", ["hook", "context-menu", "tauri", "sidebar"], "complex"),

    ("src/scaffold/NavigationSidebar/connectors/useWorkstationSidebarHandlers.ts", "useWorkstationSidebarHandlers", 110, 388, True,
     "Centralizes the workstation sidebar's action handlers for deleting sessions (local and cloud), exporting markdown, creating new sessions/drafts, navigating chat panel tabs, and driving load-more pagination.", ["hook", "event-handler", "session-management", "api-handler"], "complex"),

    ("src/scaffold/NavigationSidebar/connectors/workstationSidebarData.ts", "sortSessionsByActivity", 16, 28, True,
     "Sorts sessions by most recent activity timestamp, most recent first.", ["utility", "sorting", "session-management"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/workstationSidebarData.ts", "buildRepoPathToName", 30, 39, True,
     "Builds a map from repository path to display name for use in workspace-grouped sidebar sections.", ["utility", "mapping"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/workstationSidebarData.ts", "getSelectedDraftMenuItemId", 41, 54, True,
     "Resolves the sidebar menu item id that should be shown as selected for the active session-creator draft.", ["utility", "selection-state"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/workstationSidebarData.ts", "getSelectedMenuItemId", 56, 71, True,
     "Resolves which sidebar menu item id should currently be highlighted as selected, preferring an explicit pinned selection, then the active session, then the active draft.", ["utility", "selection-state"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/workstationSidebarData.ts", "getAllSectionIds", 73, 83, True,
     "Collects the ids of all collapsible section rows within a sidebar menu item tree.", ["utility", "menu-builder"], "simple"),
    ("src/scaffold/NavigationSidebar/connectors/workstationSidebarData.ts", "findSidebarSectionIdForMenuItem", 93, 106, True,
     "Finds which collapsible section id contains a given target sidebar menu item id, searching recursively.", ["utility", "menu-builder", "search"], "simple"),

    ("src/scaffold/NavigationSidebar/connectors/workstationSidebarMenuItems.tsx", "buildPinnedMenuItems", 36, 72, True,
     "Builds the pinned action rows (new session, work items, Kanban) shown at the top of the workstation sidebar.", ["utility", "menu-builder", "sidebar"], "moderate"),
    ("src/scaffold/NavigationSidebar/connectors/workstationSidebarMenuItems.tsx", "buildProjectsPinnedMenuItems", 74, 107, True,
     "Builds the pinned action rows specific to the Projects sidebar view (create project, create work item, import GitHub issues).", ["utility", "menu-builder", "work-items"], "moderate"),
    ("src/scaffold/NavigationSidebar/connectors/workstationSidebarMenuItems.tsx", "buildDraftMenuItems", 114, 144, True,
     "Builds sidebar rows for in-progress session-creator drafts, including preview text and relative timestamps.", ["utility", "menu-builder", "session-management"], "moderate"),

    ("src/scaffold/NavigationSidebar/contexts/ForceVisibleContext.tsx", "useForceVisibleSidebar", 29, 32, True,
     "Hook returning whether the current sidebar is being force-shown via the ForceVisibleSidebarContext, used to keep collapsed sidebars rendered while hovered.", ["hook", "context", "sidebar"], "simple"),
    ("src/scaffold/NavigationSidebar/contexts/ForceVisibleContext.tsx", "ForceVisibleSidebarProvider", 45, 53, True,
     "Provider component that marks nested sidebars as force-visible for consumers of useForceVisibleSidebar.", ["component", "context", "provider", "sidebar"], "simple"),

    ("src/scaffold/NavigationSidebar/utils/menuFromRoutes.ts", "routeToMenuItem", 29, 49, True,
     "Converts a route table entry into a NavigationMenuItem, resolving its label and icon with optional overrides.", ["utility", "routing", "menu-builder"], "simple"),

    ("src/scaffold/NavigationSidebar/utils/renderIcon.tsx", "renderSidebarIcon", 30, 66, True,
     "Renders a sidebar icon from a Lucide component, icon name, or React node, applying hover-triggered animation classes when configured.", ["utility", "rendering", "icon"], "moderate"),

    ("src/scaffold/NavigationSidebar/variants/EconomySidebar.tsx", "EconomySidebar", 20, 67, True,
     "Compact page-level sidebar variant component used in economy/space-constrained layouts, wrapping PageLevelSidebar.", ["component", "sidebar", "variant", "entry-point"], "moderate"),

    ("src/scaffold/NavigationSidebar/variants/HomeSidebar.tsx", "HomeSidebar", 55, 228, True,
     "Top-level home sidebar component: derives navigation menu items from the route table, embeds the workstation session list and spotlight search trigger, and shows a native settings context menu.", ["component", "sidebar", "variant", "navigation", "entry-point"], "complex"),

    ("src/scaffold/NavigationSidebar/variants/NavigationSidebar.tsx", "filterMenuItem", 121, 137, False,
     "Recursively tests whether a menu item (or any of its submenu items) matches a normalized search query.", ["utility", "search", "filtering"], "moderate"),
    ("src/scaffold/NavigationSidebar/variants/NavigationSidebar.tsx", "filterMenuItems", 139, 165, False,
     "Filters a list of menu items (recursively through submenus) down to those matching a search query.", ["utility", "search", "filtering"], "moderate"),
    ("src/scaffold/NavigationSidebar/variants/NavigationSidebar.tsx", "NavigationSidebar", 171, 556, True,
     "Shared, memoized base sidebar component that renders navigation and pinned menu items with icons, collapsible submenus, and optional search filtering; the common rendering core reused by the Home, Page-level, and Settings sidebar variants.", ["component", "sidebar", "navigation", "memoized", "entry-point"], "complex"),

    ("src/scaffold/NavigationSidebar/variants/PageLevelSidebar.tsx", "PageLevelSidebar", 46, 89, True,
     "Sidebar variant for secondary pages showing a back button and a flat, non-collapsible list of navigable items.", ["component", "sidebar", "variant", "navigation", "entry-point"], "moderate"),

    ("src/scaffold/NavigationSidebar/variants/SettingsSidebar.tsx", "SettingsFooterBackButton", 74, 93, False,
     "Renders the animated back-to-app button shown in the settings sidebar footer.", ["component", "ui", "navigation"], "simple"),
    ("src/scaffold/NavigationSidebar/variants/SettingsSidebar.tsx", "SettingsSidebar", 140, 191, True,
     "Sidebar variant for the Settings screen: shows the settings navigation menu, or (at the settings root path) delegates to SettingsRootBody for the two-tier section list.", ["component", "sidebar", "variant", "settings", "entry-point"], "moderate"),
    ("src/scaffold/NavigationSidebar/variants/SettingsSidebar.tsx", "SettingsRootBody", 195, 315, False,
     "Renders the settings root's two-tier list of app sections and core setting items, including icons, integration counts, and click-through navigation.", ["component", "sidebar", "settings", "navigation"], "complex"),
]

# ---------------------------------------------------------------------------
# batchImportData (copied verbatim from batch input)
# ---------------------------------------------------------------------------
with open("/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate/batch-inputs/batch-60.input.json") as fh:
    batch_input = json.load(fh)
IMPORTS = batch_input["batchImportData"]

# ---------------------------------------------------------------------------
# Cross-batch calls (function -> function in another batch, per neighborMap)
# ---------------------------------------------------------------------------
CROSS_CALLS = [
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "localOrgRow",
     "src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/idHelpers.ts", "getLocalOrgMenuItemId"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "linearOrgRow",
     "src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/idHelpers.ts", "getLinearOrgMenuItemId"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "buildProjectOverviewRow",
     "src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/idHelpers.ts", "getProjectOverviewMenuItemId"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "buildProjectRow",
     "src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/idHelpers.ts", "getProjectOverviewMenuItemId"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "buildWorkItemRow",
     "src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/idHelpers.ts", "getWorkItemMenuItemId"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "buildWorkItemRow",
     "src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/idHelpers.ts", "getLinearWorkItemMenuItemId"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/index.tsx", "useProjectsWorkItemMenuItems",
     "src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/groupingBuilders.ts", "buildByOrgMenuItems"),

    ("src/scaffold/NavigationSidebar/connectors/useWorkstationSidebarContextMenu.ts", "useWorkstationSidebarContextMenu",
     "src/scaffold/NavigationSidebar/connectors/sidebarConnectorUtils.ts", "isDraftMenuItemId"),
    ("src/scaffold/NavigationSidebar/connectors/useWorkstationSidebarContextMenu.ts", "useWorkstationSidebarContextMenu",
     "src/scaffold/NavigationSidebar/connectors/sidebarConnectorUtils.ts", "getDraftIdFromMenuItemId"),
    ("src/scaffold/NavigationSidebar/connectors/useWorkstationSidebarHandlers.ts", "useWorkstationSidebarHandlers",
     "src/scaffold/NavigationSidebar/connectors/sidebarConnectorUtils.ts", "getDraftIdFromMenuItemId"),
    ("src/scaffold/NavigationSidebar/connectors/workstationSidebarData.ts", "getSelectedDraftMenuItemId",
     "src/scaffold/NavigationSidebar/connectors/sidebarConnectorUtils.ts", "getDraftMenuItemId"),
    ("src/scaffold/NavigationSidebar/connectors/workstationSidebarMenuItems.tsx", "buildDraftMenuItems",
     "src/scaffold/NavigationSidebar/connectors/sidebarConnectorUtils.ts", "getDraftMenuItemId"),
    ("src/scaffold/NavigationSidebar/connectors/workstationSidebarMenuItems.tsx", "buildDraftMenuItems",
     "src/scaffold/NavigationSidebar/connectors/sidebarConnectorUtils.ts", "getDraftPreviewText"),
    ("src/scaffold/NavigationSidebar/variants/SettingsSidebar.tsx", "SettingsFooterBackButton",
     "src/scaffold/NavigationSidebar/components/HoverAnimatedIcon.tsx", "triggerIconAnimation"),
]

# ---------------------------------------------------------------------------
# Within-batch calls (function -> function, both defined in this batch)
# ---------------------------------------------------------------------------
LOCAL_CALLS = [
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/index.tsx", "useProjectsWorkItemMenuItems",
     "src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/workItemMapping.tsx", "toWorkItemStatus"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/index.tsx", "useProjectsWorkItemMenuItems",
     "src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/workItemMapping.tsx", "toWorkItemPriority"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "buildWorkItemRow",
     "src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/workItemMapping.tsx", "statusIconElement"),
    ("src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/menuRows.tsx", "buildWorkItemRow",
     "src/scaffold/NavigationSidebar/connectors/useProjectsWorkItemMenuItems/workItemMapping.tsx", "toWorkItemStatus"),

    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/index.tsx", "useSessionMenuItems",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/orgFilter.ts", "sessionMatchesOrgFilter"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/index.tsx", "useSessionMenuItems",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/menuItemBuilders.tsx", "buildSessionMenuItem"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/index.tsx", "useSessionMenuItems",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx", "loadMoreRow"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/index.tsx", "useSessionMenuItems",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx", "getUnifiedLoadMoreState"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/index.tsx", "useSessionMenuItems",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx", "unifiedLoadMoreRow"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/index.tsx", "useSessionMenuItems",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx", "appendSessionGroup"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/index.tsx", "useSessionMenuItems",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/menuSectionBuilders.ts", "buildByTimeMenuItems"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/index.tsx", "useSessionMenuItems",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/menuSectionBuilders.ts", "buildByAgentMenuItems"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/index.tsx", "useSessionMenuItems",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/menuSectionBuilders.ts", "buildByWorkspaceMenuItems"),

    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx", "loadMoreRow",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/statusIndicators.tsx", "renderBreathingStatusDot"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx", "groupLoadMoreRow",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/statusIndicators.tsx", "renderBreathingStatusDot"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx", "unifiedLoadMoreRow",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/statusIndicators.tsx", "renderBreathingStatusDot"),

    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/menuSectionBuilders.ts", "buildByTimeMenuItems",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/dateGroupingHelpers.ts", "getDateGroup"),
    ("src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/menuSectionBuilders.ts", "buildByAgentMenuItems",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/sessionGroupHelpers.ts", "groupKeyToWireCategory"),

    ("src/scaffold/NavigationSidebar/connectors/useWorkstationSidebarHandlers.ts", "useWorkstationSidebarHandlers",
     "src/scaffold/NavigationSidebar/connectors/useSessionMenuItems/paginationHelpers.tsx", "loadUnifiedReadyCategories"),

    ("src/scaffold/NavigationSidebar/variants/HomeSidebar.tsx", "HomeSidebar",
     "src/scaffold/NavigationSidebar/utils/menuFromRoutes.ts", "routeToMenuItem"),
]

# ---------------------------------------------------------------------------
# Build nodes
# ---------------------------------------------------------------------------
file_index = {f["path"]: f for f in FILES}

def file_node(f):
    return {
        "id": f"file:{f['path']}",
        "type": FILE_TYPE,
        "name": f["name"],
        "filePath": f["path"],
        "summary": f["summary"],
        "tags": f["tags"],
        "complexity": f["complexity"],
    }

def func_node(path, name, start, end, summary, tags, complexity):
    return {
        "id": f"function:{path}:{name}",
        "type": "function",
        "name": name,
        "filePath": path,
        "lineRange": [start, end],
        "summary": summary,
        "tags": tags,
        "complexity": complexity,
    }

FUNC_LOOKUP = {}
for (path, name, start, end, exported, summary, tags, complexity) in FUNCS:
    FUNC_LOOKUP[(path, name)] = dict(path=path, name=name, start=start, end=end,
                                      exported=exported, summary=summary, tags=tags,
                                      complexity=complexity)

# Group files into 3 parts (10, 10, 9) by alphabetical order (already matches batchFiles order)
paths_sorted = [f["path"] for f in FILES]
assert len(paths_sorted) == 29
PART_FILES = [paths_sorted[0:10], paths_sorted[10:20], paths_sorted[20:29]]

part_of_file = {}
for idx, group in enumerate(PART_FILES, start=1):
    for p in group:
        part_of_file[p] = idx

# ---------------------------------------------------------------------------
# Assemble nodes and edges per part
# ---------------------------------------------------------------------------
parts_nodes = {1: [], 2: [], 3: []}
parts_edges = {1: [], 2: [], 3: []}

# File nodes
for f in FILES:
    p = part_of_file[f["path"]]
    parts_nodes[p].append(file_node(f))

# Function nodes + contains/exports edges
for (path, name, start, end, exported, summary, tags, complexity) in FUNCS:
    p = part_of_file[path]
    node = func_node(path, name, start, end, summary, tags, complexity)
    parts_nodes[p].append(node)
    parts_edges[p].append({
        "source": f"file:{path}",
        "target": node["id"],
        "type": "contains",
        "direction": "forward",
        "weight": 1.0,
    })
    if exported:
        parts_edges[p].append({
            "source": f"file:{path}",
            "target": node["id"],
            "type": "exports",
            "direction": "forward",
            "weight": 0.8,
        })

# Import edges (1:1 from batchImportData)
for path, targets in IMPORTS.items():
    p = part_of_file[path]
    for t in targets:
        parts_edges[p].append({
            "source": f"file:{path}",
            "target": f"file:{t}",
            "type": "imports",
            "direction": "forward",
            "weight": 0.7,
        })

# Local (within-batch) calls edges
for (src_path, src_name, dst_path, dst_name) in LOCAL_CALLS:
    p = part_of_file[src_path]
    parts_edges[p].append({
        "source": f"function:{src_path}:{src_name}",
        "target": f"function:{dst_path}:{dst_name}",
        "type": "calls",
        "direction": "forward",
        "weight": 0.8,
    })

# Cross-batch calls edges
for (src_path, src_name, dst_path, dst_name) in CROSS_CALLS:
    p = part_of_file[src_path]
    parts_edges[p].append({
        "source": f"function:{src_path}:{src_name}",
        "target": f"function:{dst_path}:{dst_name}",
        "type": "calls",
        "direction": "forward",
        "weight": 0.8,
    })

# ---------------------------------------------------------------------------
# Write output files
# ---------------------------------------------------------------------------
total_nodes = 0
total_edges = 0
for idx in (1, 2, 3):
    out = {"nodes": parts_nodes[idx], "edges": parts_edges[idx]}
    out_path = f"{OUT_DIR}/batch-60-part-{idx}.json"
    with open(out_path, "w") as fh:
        json.dump(out, fh, indent=2)
    print(f"part {idx}: nodes={len(parts_nodes[idx])} edges={len(parts_edges[idx])} -> {out_path}")
    total_nodes += len(parts_nodes[idx])
    total_edges += len(parts_edges[idx])

print(f"TOTAL nodes={total_nodes} edges={total_edges}")
