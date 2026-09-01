import json, math

INPUT = "/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate/batch-inputs/batch-2.input.json"
EXTRACT = "/home/misael/pj/gui-repos/ORG2/.understand-anything/tmp/ua-file-extract-results-2.json"

inp = json.load(open(INPUT))
ext = json.load(open(EXTRACT))
batchImportData = inp["batchImportData"]

results = {r["path"]: r for r in ext["results"]}

# ---------- FILE-LEVEL INFO ----------
FILES = {
"src-tauri/crates/agent-core/src/core/definitions/commands.rs": (
    "Defines Tauri IPC command handlers for CRUD operations on agent definitions and agent orgs (teams), including tool-state introspection, patch-based updates, builtin reset, and integrations config access.",
    ["api-handler","tauri-command","service","crud","agent-definitions"], "complex", None),
"src-tauri/crates/agent-core/src/core/definitions/learnings_lookup.rs": (
    "Resolves accumulated learnings text for a given agent/session context, providing a small lookup helper used during agent definition resolution.",
    ["utility","lookup","learnings"], "simple", None),
"src-tauri/crates/agent-core/src/core/definitions/mod.rs": (
    "Module root for the definitions subsystem that re-exports builtin agents, capabilities, commands, orgs, patch, prefix lookup, resolved/resolver, schema, and store submodules.",
    ["barrel","module-root","entry-point"], "simple", None),
"src-tauri/crates/agent-core/src/core/definitions/orgs.rs": (
    "Defines the org/team hierarchy data model (OrgDefinition, OrgMember, hierarchy modes, plan-approval policy) and the AgentOrgsStore responsible for loading, persisting, and validating orgs, including default SDE/DS template teams.",
    ["data-model","persistence","org-hierarchy","template"], "complex", None),
"src-tauri/crates/agent-core/src/core/definitions/patch.rs": (
    "Defines partial-update patch types (AgentPolicyPatch, SessionModelPatch, AgentToolSelectionPatch, AgentDefinitionPatch) with apply() methods that merge optional overrides onto an existing agent definition, gated by builtin-agent restrictions.",
    ["data-model","patch","partial-update","validation"], "complex", None),
"src-tauri/crates/agent-core/src/core/definitions/prefix_lookup.rs": (
    "Provides lookup helpers that map session IDs to builtin agent definition prefixes, including workspace-personal and wingman session detection.",
    ["utility","lookup","session-routing"], "moderate", None),
"src-tauri/crates/agent-core/src/core/definitions/resolved.rs": (
    "Resolves a raw AgentDefinition plus session overrides and integrations config into a fully-resolved ResolvedAgent runtime configuration, including tool selection and skills parameters.",
    ["data-model","resolver","agent-config"], "complex", None),
"src-tauri/crates/agent-core/src/core/definitions/resolver.rs": (
    "Implements recursive resolution and merging of agent definitions, combining a definition with its parent/base definitions across capabilities, session model, agent policy, tools, skills, and delegation config.",
    ["resolver","merge-logic","inheritance"], "complex", None),
"src-tauri/crates/agent-core/src/core/definitions/schema.rs": (
    "Declares the core serializable schema types for agent definitions (SessionMode, SessionModel, AgentPolicy, AgentToolSelection, DelegationConfig, AgentDefinition, learnings config) used across the definitions subsystem.",
    ["data-model","type-definition","schema","agent-definition"], "complex", None),
"src-tauri/crates/agent-core/src/core/definitions/store.rs": (
    "Implements AgentDefinitionsStore, the persistence layer that loads/saves agent definitions and override deltas to disk, composes builtins with overrides, and migrates legacy workspace settings.",
    ["persistence","store","crud","migration"], "complex", None),
"src-tauri/crates/agent-core/src/core/definitions/tests_extended.rs": (
    "Extended unit test suite for the definitions subsystem covering store, resolver, patch, and orgs behaviors.",
    ["test","unit-test","definitions"], "complex", None),
"src-tauri/crates/agent-core/src/core/mod.rs": (
    "Module root for the core crate that re-exports config, coordination, definitions, interaction, model_context, providers, session, side_query, tools, and turn_executor submodules.",
    ["barrel","module-root","entry-point"], "simple", None),
"src-tauri/crates/agent-core/src/core/model_context/cleanup.rs": (
    "Performs post-compaction cleanup of stale tool-call state by collecting and clearing tool_call_ids no longer referenced in the trimmed message history.",
    ["cleanup","post-processing","context-management"], "moderate", None),
"src-tauri/crates/agent-core/src/core/model_context/compaction.rs": (
    "Core context-window compaction engine (ContextCompactor) implementing trigger detection, adaptive keep-ratio calculation, forked/manual compaction attempts, summary acceptance, and prompt-too-long recovery/calibration.",
    ["context-compaction","algorithm","token-budget","core-logic"], "complex", None),
"src-tauri/crates/agent-core/src/core/model_context/file_reinjection.rs": (
    "Extracts recently-read files from conversation history and re-injects file-reference reminders into the message stream after compaction to preserve file-awareness.",
    ["context-management","file-tracking","compaction"], "complex", None),
"src-tauri/crates/agent-core/src/core/model_context/microcompact.rs": (
    "Implements lightweight 'microcompaction' that clears stale tool results and caps recent tool-call images to keep context size under a rolling token budget without a full LLM summarization pass.",
    ["context-compaction","token-budget","tool-results"], "complex", None),
"src-tauri/crates/agent-core/src/core/model_context/mod.rs": (
    "Module root for the model_context subsystem, re-exporting cleanup, compaction, file_reinjection, microcompact, plan_preservation, session_memory, summarization, and tokenizer.",
    ["barrel","module-root"], "simple", None),
"src-tauri/crates/agent-core/src/core/model_context/plan_preservation.rs": (
    "Detects plan-bearing messages and re-injects the active plan back into context after compaction so in-progress task plans survive summarization.",
    ["context-management","plan-tracking","compaction"], "moderate", None),
"src-tauri/crates/agent-core/src/core/model_context/session_memory/compact.rs": (
    "Implements session-memory-aware compaction (try_sm_compact) that computes a safe message-keep index around existing compact-boundary markers and API tool-call invariants.",
    ["session-memory","compaction","boundary-parsing"], "complex", None),
"src-tauri/crates/agent-core/src/core/model_context/session_memory/config.rs": (
    "Defines default configuration structs (SessionMemoryConfig, SessionMemoryCompactConfig) controlling thresholds for the session-memory compaction feature.",
    ["config","session-memory","defaults"], "moderate", None),
"src-tauri/crates/agent-core/src/core/model_context/session_memory/extract.rs": (
    "Extracts durable session-memory content from conversation history via an LLM side-query, deciding when extraction should run and finding a safe extraction boundary.",
    ["session-memory","llm-extraction","side-query"], "complex", None),
"src-tauri/crates/agent-core/src/core/model_context/session_memory/mod.rs": (
    "Module root for the session_memory subsystem, re-exporting compact, config, extract, sections, and state submodules.",
    ["barrel","module-root","session-memory"], "simple", None),
"src-tauri/crates/agent-core/src/core/model_context/session_memory/sections.rs": (
    "Analyzes session-memory section sizes against token budgets, generates section-size reminders, and truncates/flushes oversized sections.",
    ["session-memory","token-budget","sections"], "moderate", None),
"src-tauri/crates/agent-core/src/core/model_context/session_memory/state.rs": (
    "Defines SessionMemoryState, a small struct tracking tool-call activity used to gate session-memory extraction.",
    ["session-memory","state","tracking"], "simple", None),
"src-tauri/crates/agent-core/src/core/model_context/summarization.rs": (
    "Builds LLM summarization prompts from conversation history and drives summarize_messages/summarize_messages_forked via a side-query to produce compaction summaries, with validation of the returned summary.",
    ["summarization","llm","side-query","compaction"], "complex", None),
"src-tauri/crates/agent-core/src/core/model_context/tokenizer.rs": (
    "Provides token-counting utilities (count_tokens, count_message_tokens) backed by a per-model tokenizer encoder, used to size messages against context budgets.",
    ["tokenizer","token-counting","utility"], "moderate", None),
"src-tauri/crates/agent-core/src/core/providers/anthropic_native/messages.rs": (
    "Converts internal message representations into Anthropic-native wire format, extracting system blocks, applying prompt-cache-control markers, and producing sidecar sibling content blocks.",
    ["provider-adapter","anthropic","message-conversion","prompt-caching"], "complex", None),
"src-tauri/crates/agent-core/src/core/session/compaction/fork.rs": (
    "Implements attempt_fork, which forks session state during compaction by writing a new session record/file rather than mutating history in place.",
    ["session-fork","compaction","persistence"], "complex", None),
"src-tauri/crates/agent-core/src/core/session/compaction/manual.rs": (
    "Drives user-triggered manual compaction (run_manual_compact), producing a ManualCompactResult/Summary and persisting the outcome to session state.",
    ["compaction","manual-trigger","session"], "complex", None),
"src-tauri/crates/agent-core/src/core/session/compaction/mod.rs": (
    "Module root for the session compaction subsystem, re-exporting fork, manual, and persist submodules.",
    ["barrel","module-root","compaction"], "simple", None),
"src-tauri/crates/agent-core/src/core/session/compaction/persist.rs": (
    "Persists compact-boundary markers into the session file in place, splitting summary and tail content and detecting already-compacted sessions.",
    ["persistence","compaction","boundary-marker"], "moderate", None),
"src-tauri/crates/agent-core/src/core/session/exec_modes.rs": (
    "Defines security policy layers and system-prompt suffixes per execution mode (e.g., read-only), including the base set of denied tools.",
    ["security-policy","execution-mode","system-prompt"], "complex", None),
"src-tauri/crates/agent-core/src/core/session/file_registry.rs": (
    "Maintains a registry of active session files on disk, supporting registration, unregistration, listing, and cleanup of stale session entries.",
    ["session-registry","file-tracking","cleanup"], "moderate", None),
"src-tauri/crates/agent-core/src/core/session/gateway_pipeline.rs": (
    "Implements process_gateway_message, the central pipeline function that routes and processes incoming gateway messages for a session.",
    ["gateway","message-processing","pipeline"], "complex", None),
"src-tauri/crates/agent-core/src/core/session/goal_loop.rs": (
    "Implements the autonomous goal-loop feature: persists GoalState, evaluates turn-end via an LLM judge, parses judge verdicts, and enqueues continuation messages until the goal is satisfied.",
    ["goal-loop","autonomous-agent","llm-judge","orchestration"], "complex", None),
}
print("FILES entries:", len(FILES))

# ---------- FUNCTION-LEVEL INFO ----------
# key: (path, name) -> (summary, tags)
FUNCS = {}
def F(path, name, summary, tags):
    FUNCS[(path, name)] = (summary, tags)

P = "src-tauri/crates/agent-core/src/core/definitions/commands.rs"
F(P,"agent_definitions_list_all","Tauri command that lists all agent definitions currently registered in the definitions store, returning them as wire-format DTOs for the frontend.",["api-handler","tauri-command","crud"])
F(P,"agent_definitions_remove","Tauri command that removes an agent definition by id from the store and cleans up any org references, propagating the change to running sessions.",["api-handler","tauri-command","crud"])
F(P,"agent_org_run_list","Tauri command that lists recent org/team run summaries (InboxRunSummary) for display in the frontend inbox, capped to a limit.",["api-handler","tauri-command","inbox"])
F(P,"agent_def_tool_states","Tauri command that computes the enabled/disabled state of every tool for a given agent definition, returning AgentToolStateRow entries for the tool-configuration UI.",["api-handler","tauri-command","tool-configuration"])
F(P,"agent_def_update_patch","Tauri command that applies an AgentDefinitionPatch to an existing agent definition and persists the resulting override.",["api-handler","tauri-command","patch"])
F(P,"agent_def_reset_builtin","Tauri command that resets a builtin agent definition back to its default configuration, discarding any user overrides.",["api-handler","tauri-command","reset"])
F(P,"integrations_update_patch","Tauri command that applies a partial patch to the integrations configuration (web search, nodes, execution mode, etc.) and persists it.",["api-handler","tauri-command","integrations"])

P = "src-tauri/crates/agent-core/src/core/definitions/learnings_lookup.rs"
F(P,"resolve_learnings_for","Resolves the accumulated learnings text applicable to a given agent id by looking up stored learnings entries relevant to that agent.",["utility","learnings","lookup"])

P = "src-tauri/crates/agent-core/src/core/definitions/orgs.rs"
F(P,"orgs_store","Returns the process-wide lazily-initialized AgentOrgsStore singleton used to access org/team definitions.",["singleton","store-access","org-hierarchy"])
F(P,"parse_cli_agent_org_reference","Parses a CLI-style agent id string to extract an org/team reference (org name and optional member path), if the id follows the CLI org-reference convention.",["utility","parsing","org-hierarchy"])
F(P,"apply_overrides_to_member_tree","Recursively walks an org member tree applying launch overrides (e.g., model, workspace) to matching members and their descendants.",["org-hierarchy","recursion","overrides"])
F(P,"apply_overrides_to_members","Applies a set of member launch overrides to a flat list of org members, tracking which member ids were successfully matched.",["org-hierarchy","overrides"])
F(P,"ensure_default_template_team","Ensures the default template team orgs (e.g. SDE, DS) exist in the store, creating or refreshing them if missing or stale.",["org-hierarchy","defaults","bootstrap"])
F(P,"ensure_default_org","Generic helper that ensures a given default org exists and is up to date, using the provided builder and staleness-check closures.",["org-hierarchy","defaults","bootstrap"])
F(P,"default_sde_template_team_is_current","Checks whether an existing SDE (software engineering) template org matches the current default template shape, to decide if it needs regeneration.",["org-hierarchy","defaults","validation"])
F(P,"default_sde_template_team","Builds the default 'SDE' template org, a preconfigured hierarchy of software-engineering agent roles.",["org-hierarchy","defaults","template"])
F(P,"default_ds_template_team_is_current","Checks whether an existing DS (data science) template org matches the current default template shape.",["org-hierarchy","defaults","validation"])
F(P,"default_ds_template_team","Builds the default 'DS' (data science) template org, a preconfigured hierarchy of data-science agent roles.",["org-hierarchy","defaults","template"])
F(P,"load_from_disk","Loads the orgs store contents from a JSON file on disk, returning the deserialized set of org definitions.",["persistence","deserialization","org-hierarchy"])
F(P,"save_to_disk","Serializes and writes the current org definitions to disk at the given path.",["persistence","serialization","org-hierarchy"])

P = "src-tauri/crates/agent-core/src/core/definitions/prefix_lookup.rs"
F(P,"session_prefix_for_launch","Determines the session id prefix to use when launching a session for a given agent definition, factoring in whether a workspace path is present.",["session-routing","utility","lookup"])

P = "src-tauri/crates/agent-core/src/core/definitions/resolved.rs"
F(P,"skills_from_schema","Converts a schema-level AgentSkillsConfig into resolved SkillsParams used at runtime.",["conversion","skills","resolver"])

P = "src-tauri/crates/agent-core/src/core/definitions/resolver.rs"
F(P,"get_raw_definition","Fetches the raw, unresolved AgentDefinition for a given agent id from the definitions store.",["lookup","definitions","resolver"])
F(P,"resolve_with_depth","Recursively resolves an agent definition against its parent chain up to a maximum depth, guarding against cycles via a visited set.",["resolver","recursion","inheritance"])
F(P,"merge_definitions","Merges a child agent definition onto its parent, combining capabilities, session model, policy, tools, skills, and delegation config field-by-field.",["resolver","merge-logic","inheritance"])
F(P,"merge_capabilities","Merges parent and child capability sets (coding, desktop, browser, etc.) for a resolved agent definition.",["resolver","merge-logic","capabilities"])
F(P,"merge_coding_cap","Merges parent and child coding-capability configuration.",["resolver","merge-logic","capabilities"])
F(P,"merge_desktop_cap","Merges parent and child desktop-capability configuration.",["resolver","merge-logic","capabilities"])
F(P,"merge_browser_cap","Merges parent and child browser-capability configuration.",["resolver","merge-logic","capabilities"])
F(P,"merge_session_model","Merges parent and child SessionModel settings, letting the child override the parent's model/provider choice where specified.",["resolver","merge-logic","llm-config"])
F(P,"merge_agent_policy","Merges parent and child AgentPolicy settings such as autonomy level and risk rules.",["resolver","merge-logic","security-policy"])
F(P,"merge_tools","Merges parent and child tool-selection configuration, combining allow/deny lists.",["resolver","merge-logic","tool-configuration"])
F(P,"merge_skills_config","Merges parent and child skills configuration.",["resolver","merge-logic","skills"])
F(P,"merge_delegation_config","Merges parent and child sub-agent delegation configuration.",["resolver","merge-logic","delegation"])

P = "src-tauri/crates/agent-core/src/core/definitions/store.rs"
F(P,"definitions_store","Returns the process-wide lazily-initialized AgentDefinitionsStore singleton.",["singleton","store-access","persistence"])
F(P,"migrate_legacy_workspace_settings","Migrates legacy on-disk workspace-settings JSON shapes into the current agent-definition schema during load.",["migration","backward-compatibility"])
F(P,"migrate_stale_summary_max_tokens","Migrates stale/legacy summary-max-tokens configuration values found in persisted definitions to the current schema.",["migration","backward-compatibility"])
F(P,"load_from_disk","Loads the full set of agent definitions from disk, applying legacy migrations as needed.",["persistence","deserialization","migration"])
F(P,"save_to_disk","Serializes and writes the current set of agent definitions to disk.",["persistence","serialization"])
F(P,"load_overrides_from_disk","Loads the persisted override-delta file (user customizations layered on top of builtin agent definitions) from disk.",["persistence","deserialization","overrides"])
F(P,"compose_builtin_with_delta","Composes a builtin agent definition with a stored override delta to produce the effective definition for that id.",["merge-logic","overrides"])
F(P,"delta_against_builtin","Computes the override delta between an effective (current) agent definition and its builtin baseline, for persistence.",["diffing","overrides"])
F(P,"save_overrides_to_disk","Serializes and writes the override-delta map to disk.",["persistence","serialization","overrides"])

P = "src-tauri/crates/agent-core/src/core/model_context/cleanup.rs"
F(P,"post_compact_cleanup","Cleans up tool-call bookkeeping state after a compaction pass by removing entries for tool_call_ids no longer present in the trimmed message history.",["cleanup","context-management","post-compaction"])
F(P,"collect_tool_call_ids","Walks a message list and collects the set of tool_call_ids referenced within it, used to determine which tool-call state entries are still live.",["utility","tool-calls"])

P = "src-tauri/crates/agent-core/src/core/model_context/file_reinjection.rs"
F(P,"extract_recently_read_files","Scans recent messages for file-read tool results and extracts the set of file paths that were recently read, to preserve file-awareness across compaction.",["context-management","file-tracking"])
F(P,"is_excluded_from_reinjection","Determines whether a given file path should be excluded from post-compaction reinjection (e.g., binary files, excluded directories).",["filtering","utility"])
F(P,"message_text","Extracts plain text content from a message's value/output representation.",["utility","extraction"])
F(P,"truncate_at_boundary","Truncates file content to a maximum byte size at a safe character boundary, avoiding mid-character splits.",["utility","truncation"])
F(P,"build_file_reinjection_messages_with_preserved_tail","Builds the set of synthetic reminder messages that re-inject recently-read file references after compaction, while preserving the untouched message tail.",["context-management","message-building","compaction"])
F(P,"reinject_files_after_compaction","Top-level entry point that reinjects recently-read file reminders into the compacted message history based on what was read before compaction.",["context-management","compaction","entry-point"])

P = "src-tauri/crates/agent-core/src/core/model_context/microcompact.rs"
F(P,"evaluate_time_trigger","Evaluates whether a time-based microcompaction trigger should fire based on elapsed time and configured thresholds.",["trigger-evaluation","microcompaction"])
F(P,"microcompact_messages","Runs a microcompaction pass over the message list, clearing stale tool results and capping images per the configured budget.",["microcompaction","token-budget"])
F(P,"force_microcompact_messages","Forces a microcompaction pass regardless of normal trigger conditions, used for explicit/manual invocation.",["microcompaction","manual-trigger"])
F(P,"clear_old_tool_results","Clears the content of old tool-call results that fall outside the retention window, replacing them with lightweight placeholders to reduce token usage.",["microcompaction","token-budget"])
F(P,"cap_recent_tool_images","Caps the number/size of images retained in recent tool-call results to control image-heavy context bloat.",["microcompaction","image-handling"])
F(P,"enforce_aggregate_budget","Enforces an aggregate token budget across all tool results by progressively clearing older entries until under budget.",["microcompaction","token-budget"])
F(P,"enforce_group_budget","Enforces a per-group token budget on a specific subset of tool-result message indices.",["microcompaction","token-budget"])

P = "src-tauri/crates/agent-core/src/core/model_context/plan_preservation.rs"
F(P,"extract_active_plan","Scans recent messages for the most recent plan-bearing content (e.g., an active TODO/plan tool call) and extracts it.",["context-management","plan-tracking"])
F(P,"reinject_plan_after_compaction","Re-injects the most recent active plan into the message history after compaction so in-progress plans aren't lost.",["context-management","compaction","plan-tracking"])

P = "src-tauri/crates/agent-core/src/core/model_context/session_memory/compact.rs"
F(P,"try_sm_compact","Attempts session-memory-aware compaction: computes a safe keep index relative to prior compact boundaries and returns the resulting compacted message set.",["session-memory","compaction"])
F(P,"parse_compact_boundary_content","Parses the structured content of a compact-boundary marker message to recover its metadata.",["parsing","session-memory"])
F(P,"parse_compacted_count","Parses the count of previously-compacted messages from a compact-boundary header string.",["parsing","session-memory"])
F(P,"compact_boundary_text","Extracts the raw text of a compact-boundary marker from a message, if present.",["utility","session-memory"])
F(P,"calculate_messages_to_keep_index","Calculates the message index boundary marking which messages should be kept (not re-summarized) during session-memory compaction.",["session-memory","compaction","algorithm"])
F(P,"adjust_keep_index_for_api_invariants","Adjusts a candidate keep-index so it doesn't split a tool-call/tool-result pair, keeping the resulting message list API-valid.",["session-memory","compaction","validation"])
F(P,"is_text_message","Checks whether a message consists purely of text content (no tool calls/results).",["utility","predicate"])
F(P,"last_turn_has_tool_calls","Checks whether the most recent conversational turn contains tool calls, used to decide safe compaction boundaries.",["utility","predicate"])

P = "src-tauri/crates/agent-core/src/core/model_context/session_memory/extract.rs"
F(P,"should_extract","Decides whether session-memory extraction should run now, based on current token usage, prior state, and whether the last turn has pending tool calls.",["session-memory","trigger-evaluation"])
F(P,"extract_session_memory","Drives LLM-based extraction of durable session-memory content from the conversation, issuing a side-query to the given provider/model.",["session-memory","llm-extraction","side-query"])
F(P,"find_last_safe_boundary","Finds the latest message index that forms a safe extraction boundary (not splitting a tool-call/tool-result pair).",["session-memory","boundary-detection"])

P = "src-tauri/crates/agent-core/src/core/model_context/session_memory/sections.rs"
F(P,"analyze_section_sizes","Parses session-memory content into named sections and estimates the token size of each.",["session-memory","token-budget","analysis"])
F(P,"generate_section_reminders","Generates reminder text flagging session-memory sections that exceed their configured token budgets.",["session-memory","token-budget"])
F(P,"truncate_for_compact","Truncates session-memory content down to fit within a per-section token budget ahead of compaction.",["session-memory","truncation"])
F(P,"flush_section","Flushes an accumulated section's lines into a bounded-length text block under a header, splitting or truncating as needed.",["session-memory","utility"])

P = "src-tauri/crates/agent-core/src/core/model_context/summarization.rs"
F(P,"truncate_for_summary","Truncates arbitrary text to a maximum character length before including it in a summarization prompt.",["truncation","utility","summarization"])
F(P,"flatten_content_text","Flattens a structured message content block into a single plain-text string for summarization purposes.",["utility","extraction","summarization"])
F(P,"format_messages_for_summary_refs","Formats the conversation history into a compact textual representation used as input to the summarization prompt.",["summarization","formatting"])
F(P,"format_tool_calls","Formats a message's tool calls into readable text for inclusion in the summarization prompt.",["summarization","formatting"])
F(P,"build_summary_prompt","Builds the full LLM prompt used to request a conversation summary, optionally including custom instructions and the prior summary for continuity.",["summarization","prompt-building"])
F(P,"validate_summary","Validates an LLM-produced summary for completeness (e.g., checking finish_reason and output length against the configured cap).",["summarization","validation"])
F(P,"summarize_messages_forked","Runs LLM summarization for the forked-compaction path, issuing a side-query against the given provider and returning the summary result.",["summarization","side-query","forked-compaction"])
F(P,"summarize_messages","Top-level entry point that summarizes a message history via an LLM side-query, applying the configured token budget and custom instructions.",["summarization","side-query","entry-point"])

P = "src-tauri/crates/agent-core/src/core/model_context/tokenizer.rs"
F(P,"encoder_for_model","Selects and returns the appropriate token encoder for a given LLM model identifier.",["tokenizer","model-selection","utility"])
F(P,"count_with_encoder","Counts the number of tokens in a text string using a specific pre-selected encoder.",["tokenizer","token-counting"])
F(P,"count_content_tokens","Counts the tokens represented by a structured message content block (text, tool calls, etc.).",["tokenizer","token-counting"])
F(P,"count_message_tokens","Counts the total tokens in a single message including its content and metadata overhead.",["tokenizer","token-counting"])

P = "src-tauri/crates/agent-core/src/core/providers/anthropic_native/messages.rs"
F(P,"extract_system","Extracts and separates system-prompt content from the message list when converting to Anthropic's native wire format, handling cache-control markers.",["provider-adapter","anthropic","message-conversion"])
F(P,"render_system_blocks","Renders the extracted system-prompt parts into Anthropic's system-block wire format, applying prompt-cache-control where appropriate.",["provider-adapter","anthropic","prompt-caching"])
F(P,"stamp_trailing_cache_control","Stamps a cache_control marker on the trailing eligible content block(s) of the message list to enable Anthropic prompt caching.",["provider-adapter","anthropic","prompt-caching"])
F(P,"strip_cache_scope_markers","Strips internal cache-scope markers from messages before sending them to the Anthropic API.",["provider-adapter","anthropic","sanitization"])
F(P,"finalize_wire_hygiene","Performs final cleanup/normalization passes on the message list to ensure it is well-formed for the Anthropic wire format.",["provider-adapter","anthropic","sanitization"])
F(P,"anthropic_thinking_block","Converts an internal thinking/reasoning representation associated with a tool call into an Anthropic-native thinking content block.",["provider-adapter","anthropic","message-conversion"])
F(P,"convert_content_block","Converts a single internal content block into its Anthropic-native wire representation.",["provider-adapter","anthropic","message-conversion"])
F(P,"sidecar_to_anthropic_sibling_blocks","Converts internal 'sidecar' content (auxiliary data attached to a message) into the sibling content blocks expected by the Anthropic API.",["provider-adapter","anthropic","message-conversion"])

P = "src-tauri/crates/agent-core/src/core/session/compaction/fork.rs"
F(P,"attempt_fork","Attempts to fork the current session during compaction: writes a new forked session record so compaction can proceed without mutating the original session's history in place.",["session-fork","compaction"])
F(P,"build_forked_record","Builds the new session record metadata for a forked session, linking it back to the original session id.",["session-fork","record-building"])

P = "src-tauri/crates/agent-core/src/core/session/compaction/manual.rs"
F(P,"run_manual_compact","Drives a user-triggered manual compaction of a session: loads state, runs the compactor, persists the result, and returns a summary.",["compaction","manual-trigger","entry-point"])

P = "src-tauri/crates/agent-core/src/core/session/compaction/persist.rs"
F(P,"content_text","Extracts the plain-text content of a message for persistence/boundary-marker purposes.",["utility","extraction"])
F(P,"split_summary_and_tail","Splits a compacted message list into the summary portion and the preserved tail portion for persistence.",["compaction","persistence"])
F(P,"append_in_place_compact_boundary","Appends a compact-boundary marker to the session's persisted message log in place, recording the token delta from compaction.",["persistence","compaction","boundary-marker"])
F(P,"persist_session_memory_after_compact","Persists any extracted session-memory content to disk immediately after a compaction pass completes.",["persistence","session-memory","compaction"])

P = "src-tauri/crates/agent-core/src/core/session/exec_modes.rs"
F(P,"read_only_deny_base","Returns the base set of tools denied under read-only execution mode.",["security-policy","execution-mode"])
F(P,"policy_layer","Builds the security-policy layer (deny/ask rules) associated with the current execution mode.",["security-policy","execution-mode"])
F(P,"system_prompt_suffix","Builds the system-prompt suffix text describing the active execution mode's constraints, appended to the agent's system prompt.",["execution-mode","prompt-building"])

P = "src-tauri/crates/agent-core/src/core/session/file_registry.rs"
F(P,"register_session","Registers a new active session in the on-disk session registry, recording its metadata for crash-recovery/cleanup purposes.",["session-registry","file-tracking"])
F(P,"unregister_session","Removes a session's entry from the on-disk session registry once it has ended.",["session-registry","cleanup"])
F(P,"list_registered_sessions","Lists all sessions currently recorded in the on-disk registry.",["session-registry","listing"])
F(P,"cleanup_stale_sessions","Removes registry entries for sessions that are no longer active, given the current set of active session ids.",["session-registry","cleanup"])

P = "src-tauri/crates/agent-core/src/core/session/gateway_pipeline.rs"
F(P,"process_gateway_message","Central pipeline function that processes an incoming gateway message for a session -- dispatching by message type, handling IDE context and image attachments, and driving the appropriate session-state updates.",["gateway","message-processing","pipeline","entry-point"])

P = "src-tauri/crates/agent-core/src/core/session/goal_loop.rs"
F(P,"init_schema","Initializes the database schema/tables used to persist goal-loop state.",["goal-loop","schema-init","persistence"])
F(P,"load_state","Loads the persisted GoalState for a session from the database.",["goal-loop","persistence"])
F(P,"save_state","Persists the current GoalState for a session to the database.",["goal-loop","persistence"])
F(P,"on_user_message","Hook invoked when a user sends a message, used to detect and record a new goal for the goal-loop feature.",["goal-loop","event-handler"])
F(P,"parse_judge_verdict","Parses the raw LLM judge response text into a structured JudgeVerdict (continue/stop decision and reasoning).",["goal-loop","llm-judge","parsing"])
F(P,"build_judge_messages","Builds the prompt messages sent to the LLM judge to evaluate whether the current turn satisfied the stated goal.",["goal-loop","llm-judge","prompt-building"])
F(P,"spawn_turn_end_evaluation","Spawns an asynchronous task that evaluates the end of a turn against the active goal without blocking the main session loop.",["goal-loop","async","orchestration"])
F(P,"evaluate_turn_end","Evaluates whether the just-completed turn satisfies the active goal, invoking the LLM judge and deciding whether to continue or stop the goal loop.",["goal-loop","llm-judge","orchestration"])
F(P,"run_judge","Runs the LLM judge side-query to obtain a verdict on the current goal-loop turn.",["goal-loop","llm-judge","side-query"])
F(P,"session_has_pending_messages","Checks whether a session has pending/queued user messages, used to avoid auto-continuing the goal loop over a user who is mid-typing.",["goal-loop","predicate"])
F(P,"enqueue_continuation","Enqueues a synthetic continuation message to keep the goal loop running for another turn, up to the configured max-turns limit.",["goal-loop","orchestration"])
F(P,"broadcast_goal_event","Broadcasts a goal-loop status event (progress, turns used, message) to the frontend over the event bus.",["goal-loop","event-broadcast"])

print("FUNCS entries:", len(FUNCS))

# ---------- CLASS-LEVEL INFO ----------
CLASSES = {}
def C(path, name, summary, tags):
    CLASSES[(path, name)] = (summary, tags)

P = "src-tauri/crates/agent-core/src/core/definitions/commands.rs"
C(P,"InboxRunSummary","Wire DTO summarizing a single org/team run (status, timing, participants) for the inbox/run-history UI.",["data-model","dto","inbox"])
C(P,"AgentToolStateRow","Wire DTO representing whether a specific tool is enabled for an agent definition, used to render the tool-configuration table.",["data-model","dto","tool-configuration"])

P = "src-tauri/crates/agent-core/src/core/definitions/orgs.rs"
C(P,"HierarchyMode","Enum describing how an org's member hierarchy is structured (e.g., flat vs. nested reporting lines).",["data-model","enum","org-hierarchy"])
C(P,"PlanApprovalPolicy","Enum/struct describing the plan-approval policy for an org (e.g., who must approve a plan before execution), with an as_wire() conversion for the frontend.",["data-model","policy","org-hierarchy"])
C(P,"OrgMemberRuntimeConfig","Runtime configuration overrides for an individual org member (e.g., model, workspace, tool selection) applied at launch time.",["data-model","config","org-hierarchy"])
C(P,"OrgMemberLaunchOverride","Represents a single launch-time override targeted at a specific org member or subtree.",["data-model","overrides","org-hierarchy"])
C(P,"OrgMember","Represents one member (agent) within an org hierarchy, including its role and nested sub-members.",["data-model","org-hierarchy"])
C(P,"OrgDefinition","Top-level org/team definition containing the member hierarchy, hierarchy mode, and plan-approval policy, with helpers to count members recursively.",["data-model","org-hierarchy"])
C(P,"AgentOrgsStore","In-memory store for all org/team definitions, providing CRUD (insert/replace/remove), persistence, agent-reference validation, and launch-override application.",["store","crud","persistence","org-hierarchy"])

P = "src-tauri/crates/agent-core/src/core/definitions/patch.rs"
C(P,"AgentPolicyPatch","Partial-update patch for AgentPolicy fields (e.g., autonomy level, risk rules), applied on top of an existing policy via apply().",["patch","partial-update","security-policy"])
C(P,"SessionModelPatch","Partial-update patch for the SessionModel (LLM provider/model selection) fields, merged onto an existing session model via apply().",["patch","partial-update","llm-config"])
C(P,"AgentToolSelectionPatch","Partial-update patch for an agent's tool selection/allow-deny configuration, merged via apply().",["patch","partial-update","tool-configuration"])
C(P,"AgentDefinitionPatch","Top-level partial-update patch aggregating policy, model, and tool-selection patches for an AgentDefinition, with builtin-agent gating (gate_for_builtin) and an apply() that merges all sub-patches.",["patch","partial-update","agent-definition"])

P = "src-tauri/crates/agent-core/src/core/definitions/prefix_lookup.rs"
C(P,"BuiltinPrefixEntry","Maps a builtin agent definition id to its session-id prefix convention.",["data-model","builtin","session-routing"])

P = "src-tauri/crates/agent-core/src/core/definitions/resolved.rs"
C(P,"SkillsParams","Resolved runtime parameters controlling which skills are available to an agent and how they're loaded.",["data-model","skills","agent-config"])
C(P,"ResolvedToolSelection","Fully-resolved tool allow/deny selection for an agent, derived from schema-level AgentToolSelection via from_schema().",["data-model","tool-configuration","agent-config"])
C(P,"ResolveError","Error type returned when agent definition resolution fails (e.g., missing parent, invalid reference).",["error-handling","resolver"])
C(P,"ResolvedAgent","Fully-resolved runtime configuration for an agent, combining its definition, session overrides, and integrations config, with a resolve() constructor and workspace() accessor.",["data-model","agent-config","resolver"])

P = "src-tauri/crates/agent-core/src/core/definitions/schema.rs"
C(P,"SessionMode","Enum of the supported session execution modes (e.g. normal, read-only) used to gate tool access.",["data-model","enum","execution-mode"])
C(P,"SessionModel","Schema struct describing which LLM provider/model a session or agent should use, with sensible defaults.",["data-model","llm-config"])
C(P,"AgentTier","Enum classifying an agent's tier/role level within the system.",["data-model","enum"])
C(P,"AgentPolicy","Schema struct capturing an agent's autonomy level, command-risk rules, and other security policy fields, convertible to a runtime SecurityPolicy via to_runtime_security().",["data-model","security-policy"])
C(P,"SubAgentIsolation","Enum describing the isolation level applied to sub-agents spawned by this agent (e.g., shared vs isolated workspace).",["data-model","enum","sub-agent"])
C(P,"SubAgentRef","Reference to a sub-agent definition that this agent is permitted to delegate to.",["data-model","sub-agent"])
C(P,"AgentSkillsConfig","Schema struct configuring which skills are enabled/available for an agent and their loading behavior.",["data-model","skills"])
C(P,"AgentToolSelection","Schema struct describing an agent's allowed/denied tool set and related tool-use configuration.",["data-model","tool-configuration"])
C(P,"DelegationConfig","Schema struct configuring how and whether an agent may delegate work to sub-agents, with defaults.",["data-model","sub-agent","delegation"])
C(P,"AgentDefinition","The core serializable schema describing a full agent definition: identity, policy, session model, tools, skills, delegation, and capabilities. Central type of the definitions subsystem.",["data-model","agent-definition","core-type"])
C(P,"AgentLearningsConfig","Schema struct configuring how an agent's learnings (accumulated knowledge) are stored and surfaced, with defaults.",["data-model","learnings"])

P = "src-tauri/crates/agent-core/src/core/definitions/store.rs"
C(P,"AgentDefinitionsStore","In-memory store for all agent definitions (builtin + overrides), providing CRUD, snapshotting, overlay updates, builtin reset, and disk persistence.",["store","crud","persistence"])

P = "src-tauri/crates/agent-core/src/core/model_context/compaction.rs"
C(P,"CompactionConfig","Configuration for the compaction engine (trigger ratio, keep ratio, summary token budget, minimum messages, floor/reserved/buffer tokens), with defaults and an effective_budget() calculation.",["config","compaction","token-budget"])
C(P,"CompactionState","Tracks the current compaction-related state of a session (e.g., last compacted index, recompaction info).",["state","compaction"])
C(P,"RecompactionInfo","Metadata describing a prior recompaction event, used to decide whether/how to recompact.",["data-model","compaction"])
C(P,"CompactionOutcome","Result type describing the outcome of a compaction attempt (success, boundaries, token counts, or failure reason).",["data-model","compaction","result-type"])
C(P,"ContextCompactor","Core compaction engine: detects when compaction is needed (needs_compaction*), performs standard/forked/manual compaction attempts (compact, compact_with_fork, compact_manual_force, try_compact), accepts LLM-produced summaries, and recovers from prompt-too-long errors via budget calibration and truncation.",["core-logic","compaction","algorithm"])

P = "src-tauri/crates/agent-core/src/core/model_context/microcompact.rs"
C(P,"MicrocompactConfig","Configuration for the microcompaction feature (thresholds, retention windows), with defaults.",["config","microcompaction"])
C(P,"MicrocompactStats","Statistics produced by a microcompaction pass (e.g., messages cleared, tokens saved).",["data-model","microcompaction","metrics"])
C(P,"ReplacementState","Tracks which tool-result entries have already been cleared/replaced during microcompaction, to avoid re-processing.",["state","microcompaction"])

P = "src-tauri/crates/agent-core/src/core/model_context/session_memory/compact.rs"
C(P,"ParsedCompactBoundary","Parsed representation of a compact-boundary marker's metadata (e.g., compacted message count, timestamp).",["data-model","session-memory"])

P = "src-tauri/crates/agent-core/src/core/model_context/session_memory/config.rs"
C(P,"SessionMemoryConfig","Top-level configuration for the session-memory feature (extraction thresholds, enablement), with defaults.",["config","session-memory"])
C(P,"SessionMemoryCompactConfig","Configuration specific to session-memory-driven compaction (keep ratios, boundaries), with defaults.",["config","session-memory","compaction"])

P = "src-tauri/crates/agent-core/src/core/model_context/session_memory/sections.rs"
C(P,"SmSection","Represents a single named section of session-memory content along with its accumulated lines/size.",["data-model","session-memory"])

P = "src-tauri/crates/agent-core/src/core/model_context/session_memory/state.rs"
C(P,"SessionMemoryState","Tracks per-session state for the session-memory feature, including a record_tool_calls() method to note tool-call activity that gates extraction timing.",["state","session-memory"])

P = "src-tauri/crates/agent-core/src/core/model_context/summarization.rs"
C(P,"ForkSummaryInputs","Bundled inputs (messages, state, model) required to run the forked-compaction summarization path.",["data-model","summarization"])

P = "src-tauri/crates/agent-core/src/core/session/compaction/fork.rs"
C(P,"ForkOutcome","Result type describing the outcome of a fork attempt (success with new session id, or failure reason).",["data-model","session-fork","result-type"])
C(P,"ForkInputs","Bundled inputs required to attempt a session fork (original session id, messages, compaction context).",["data-model","session-fork"])

P = "src-tauri/crates/agent-core/src/core/session/compaction/manual.rs"
C(P,"ManualCompactResult","Result of a manual-compaction request, including the resulting summary/status returned to the frontend.",["data-model","compaction","result-type"])
C(P,"ManualCompactSummary","Summary statistics for a completed manual compaction (e.g., messages compacted, tokens saved).",["data-model","compaction","metrics"])

P = "src-tauri/crates/agent-core/src/core/session/compaction/persist.rs"
C(P,"AppendedCompactBoundary","Result describing the compact-boundary marker that was appended to a session's persisted log.",["data-model","compaction","persistence"])

P = "src-tauri/crates/agent-core/src/core/session/file_registry.rs"
C(P,"SessionRegistryEntry","A single entry in the session registry file, recording a session's id and associated metadata (e.g., process/workspace info).",["data-model","session-registry"])

P = "src-tauri/crates/agent-core/src/core/session/goal_loop.rs"
C(P,"GoalState","Persisted state for the goal-loop feature on a session: the active goal text, turns used, and status.",["data-model","goal-loop","state"])
C(P,"JudgeVerdict","Structured verdict returned by the LLM judge evaluating whether a goal-loop turn satisfied the goal (continue/stop plus reasoning).",["data-model","goal-loop","llm-judge"])
C(P,"GoalLoopTurnEnd","Input bundle describing the state at the end of a turn, passed to the goal-loop evaluation logic.",["data-model","goal-loop"])

print("CLASSES entries:", len(CLASSES))

# ---------- ASSEMBLE NODES ----------
def complexity_from_lines(n):
    if n < 15: return "simple"
    if n < 40: return "moderate"
    return "complex"

def pad_tags(tags):
    tags = list(dict.fromkeys(tags))  # dedupe preserve order
    fallback = ["rust","backend","agent-core"]
    i = 0
    while len(tags) < 3 and i < len(fallback):
        if fallback[i] not in tags:
            tags.append(fallback[i])
        i += 1
    return tags[:5]

nodes = []
node_ids = set()

def add_node(n):
    assert n["id"] not in node_ids, f"DUPLICATE NODE ID: {n['id']}"
    node_ids.add(n["id"])
    nodes.append(n)

for path, (summary, tags, complexity, langnotes) in FILES.items():
    n = {
        "id": f"file:{path}",
        "type": "file",
        "name": path.split("/")[-1],
        "filePath": path,
        "summary": summary,
        "tags": pad_tags(tags),
        "complexity": complexity,
    }
    if langnotes:
        n["languageNotes"] = langnotes
    add_node(n)

exports_by_path = {}
for path, r in results.items():
    exports_by_path[path] = set(e["name"] if isinstance(e, dict) else e for e in r.get("exports", []))

func_line_range = {}
for r in ext["results"]:
    for f in r.get("functions", []):
        func_line_range[(r["path"], f["name"])] = (f.get("startLine"), f.get("endLine"))
class_line_range = {}
for r in ext["results"]:
    for c in r.get("classes", []):
        class_line_range[(r["path"], c["name"])] = (c.get("startLine"), c.get("endLine"))

for (path, name), (summary, tags) in FUNCS.items():
    start, end = func_line_range[(path, name)]
    n_lines = end - start + 1
    file_tags = FILES[path][1]
    combined_tags = tags + [file_tags[0]] if file_tags else tags
    add_node({
        "id": f"function:{path}:{name}",
        "type": "function",
        "name": name,
        "filePath": path,
        "lineRange": [start, end],
        "summary": summary,
        "tags": pad_tags(tags),
        "complexity": complexity_from_lines(n_lines),
    })

for (path, name), (summary, tags) in CLASSES.items():
    start, end = class_line_range[(path, name)]
    n_lines = end - start + 1
    add_node({
        "id": f"class:{path}:{name}",
        "type": "class",
        "name": name,
        "filePath": path,
        "lineRange": [start, end],
        "summary": summary,
        "tags": pad_tags(tags),
        "complexity": complexity_from_lines(n_lines),
    })

print("TOTAL NODES:", len(nodes))

# ---------- ASSEMBLE EDGES ----------
edges = []

def add_edge(source, target, etype, weight):
    if source == target:
        return
    edges.append({"source": source, "target": target, "type": etype, "direction": "forward", "weight": weight})

# contains + exports edges
for (path, name) in FUNCS:
    add_edge(f"file:{path}", f"function:{path}:{name}", "contains", 1.0)
    if name in exports_by_path.get(path, set()):
        add_edge(f"file:{path}", f"function:{path}:{name}", "exports", 0.8)

for (path, name) in CLASSES:
    add_edge(f"file:{path}", f"class:{path}:{name}", "contains", 1.0)
    if name in exports_by_path.get(path, set()):
        add_edge(f"file:{path}", f"class:{path}:{name}", "exports", 0.8)

# imports edges - EXACT 1:1 from batchImportData
import_edge_count = 0
for path in FILES:
    targets = batchImportData.get(path, [])
    for t in targets:
        add_edge(f"file:{path}", f"file:{t}", "imports", 0.7)
        import_edge_count += 1

expected_imports = sum(len(v) for v in batchImportData.values())
assert import_edge_count == expected_imports, f"import mismatch {import_edge_count} vs {expected_imports}"

# tested_by: resolved.rs / store.rs / resolver.rs / orgs.rs / patch.rs are exercised by tests_extended.rs
# resolved.rs explicitly declares tests_extended as its test submodule (per batchImportData)
add_edge("file:src-tauri/crates/agent-core/src/core/definitions/resolved.rs",
         "file:src-tauri/crates/agent-core/src/core/definitions/tests_extended.rs", "tested_by", 0.5)

# high-confidence cross-batch calls edges (via neighborMap symbol matches)
add_edge("file:src-tauri/crates/agent-core/src/core/model_context/session_memory/extract.rs",
         "function:src-tauri/crates/agent-core/src/core/side_query.rs:side_query_typed", "calls", 0.8)
add_edge("file:src-tauri/crates/agent-core/src/core/model_context/summarization.rs",
         "function:src-tauri/crates/agent-core/src/core/side_query.rs:side_query_typed", "calls", 0.8)
add_edge("file:src-tauri/crates/agent-core/src/core/session/gateway_pipeline.rs",
         "function:src-tauri/crates/agent-core/src/foundation/persistence/images.rs:persist_images", "calls", 0.7)

print("TOTAL EDGES:", len(edges))
print("import edges:", import_edge_count, "expected:", expected_imports)

# sanity: every edge source/target must be a known node id, OR a file:path that exists in
# results/FILES/batchImportData targets, OR a function/class id we referenced explicitly (neighborMap-based)
allowed_external = set()
for v in batchImportData.values():
    for t in v:
        allowed_external.add(f"file:{t}")
allowed_external.add("function:src-tauri/crates/agent-core/src/core/side_query.rs:side_query_typed")
allowed_external.add("function:src-tauri/crates/agent-core/src/foundation/persistence/images.rs:persist_images")

bad = []
for e in edges:
    if e["source"] not in node_ids and e["source"] not in allowed_external:
        bad.append(("source", e))
    if e["target"] not in node_ids and e["target"] not in allowed_external:
        bad.append(("target", e))
print("BAD EDGES:", len(bad))
for b in bad[:20]:
    print(b)

import pickle
with open("/home/misael/pj/gui-repos/ORG2/.understand-anything/tmp/batch2_graph.pkl","wb") as fh:
    pickle.dump({"nodes": nodes, "edges": edges}, fh)

# ---------- SPLIT INTO PARTS ----------
import math, json

node_count = len(nodes)
edge_count = len(edges)
parts = max(1, math.ceil(max(node_count/60, edge_count/120)))
print("PARTS:", parts)

sorted_files = sorted(FILES.keys())
chunk_size = math.ceil(len(sorted_files) / parts)
file_chunks = [sorted_files[i:i+chunk_size] for i in range(0, len(sorted_files), chunk_size)]
print("chunk sizes:", [len(c) for c in file_chunks])

file_to_part = {}
for idx, chunk in enumerate(file_chunks, start=1):
    for f in chunk:
        file_to_part[f] = idx

# assign nodes to parts by filePath
node_part = {}
for n in nodes:
    fp = n.get("filePath")
    node_part[n["id"]] = file_to_part[fp]

part_nodes = {i: [] for i in range(1, len(file_chunks)+1)}
for n in nodes:
    part_nodes[node_part[n["id"]]].append(n)

part_edges = {i: [] for i in range(1, len(file_chunks)+1)}
for e in edges:
    src = e["source"]
    # source should always be a file: id belonging to our batch (contains/exports/imports/tested_by/calls all sourced from our files)
    part_idx = node_part.get(src)
    assert part_idx is not None, f"edge source not in batch: {src}"
    part_edges[part_idx].append(e)

OUTDIR = "/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate"
import os
os.makedirs(OUTDIR, exist_ok=True)

total_written_nodes = 0
total_written_edges = 0
if len(file_chunks) == 1:
    outpath = f"{OUTDIR}/batch-2.json"
    with open(outpath, "w") as fh:
        json.dump({"nodes": part_nodes[1], "edges": part_edges[1]}, fh, indent=2)
    total_written_nodes += len(part_nodes[1])
    total_written_edges += len(part_edges[1])
    print("WROTE", outpath, len(part_nodes[1]), len(part_edges[1]))
else:
    for i in range(1, len(file_chunks)+1):
        outpath = f"{OUTDIR}/batch-2-part-{i}.json"
        with open(outpath, "w") as fh:
            json.dump({"nodes": part_nodes[i], "edges": part_edges[i]}, fh, indent=2)
        total_written_nodes += len(part_nodes[i])
        total_written_edges += len(part_edges[i])
        print("WROTE", outpath, len(part_nodes[i]), len(part_edges[i]))

print("GRAND TOTAL nodes:", total_written_nodes, "edges:", total_written_edges)
assert total_written_nodes == node_count
assert total_written_edges == edge_count
