---
type: implementation-reference
name: org2-external-artifact-import-seams
description: Detection, translation, fidelity, and persistence boundaries for external agent artifacts.
tags: [org2, interfaces, import, agents, skills, policies, mcp]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: source-observed
---

# External artifact import seams

## Scope and evidence

This record explains the import boundary for policies, skills, MCP server definitions, and agent definitions from other coding-agent products.

UA selected External Artifact Import as a missing domain journey. Graphify identified the detector modules, Tauri commands, native target stores, and shared frontend wizard. All behavioral claims are Source-observed at revision `b315ba4f82fb1fe294496793d7322095e7efe262`.

## Contract

The pipeline has two explicit phases:

```text
foreign files
  -> detect and preview without writes
  -> user selects, renames, skips, or permits overwrite
  -> apply each selection to its native ORG2 owner
  -> per-item report and cache invalidation where required
```

Detection is advisory and loss-aware. Apply is the mutation boundary. A detected item does not become ORG2 state until the user submits an `ImportSelection`.

## Shared interface types

`DetectedItem` preserves source agent, source scope, artifact kind, absolute source path, suggested name, existing-target status, fidelity warnings, and a lossless preview. `ImportSelection` adds destination repository, final name, and overwrite authority.

```rust
enum ItemKind { Policy, Skill, Mcp, AgentDefinition }

struct ImportSelection {
    source_scope: SourceScope,
    kind: ItemKind,
    source_path: PathBuf,
    target_repo_path: Option<PathBuf>,
    target_name: String,
    overwrite: bool,
}
```

`SourceScope` separates user-global input from one repository's local input. `target_repo_path` separately states the destination. This prevents the detector's source location from silently deciding where a policy or skill will be written.

## Detection

`external_import_detect` moves filesystem scanning to a blocking task. `detect_all` runs source-specific detectors for Cursor IDE, Claude Code, Codex, Copilot, Kiro, and external MCP configurations.

Detectors follow these boundaries:

- Global detection reads known user configuration roots.
- Repository detection reads known local roots under the selected repository.
- Paths under `extensions`, `node_modules`, or `.git` are rejected.
- One policy file has a 1 MiB limit.
- One source-agent and item-kind batch has a 1,000-item limit.
- A malformed frontmatter block becomes a fidelity warning when the detector can still offer the body.
- Detection checks the relevant ORG2 target owner to report `already_imported`.
- The preview exposes the first useful body line, scalar frontmatter, and source size.

MCP detection parses `mcpServers` maps. It infers `stdio` when a server has a command and `streamableHttp` when it has a URL. It also translates an external `http` transport label to `streamableHttp` before the typed ORG2 parser runs.

## User interaction

The shared frontend hook scans global sources and each selected repository. It merges successful results, reports failed scans, lets the user select items and names, and sends one batch of selections to `external_import_apply`.

The same table and hook serve inline import surfaces for:

- Agent Orgs and external agent definitions;
- MCP integrations;
- Skills;
- Rules and memory evolution.

The result is per item. One failed item does not hide successful items in the same batch.

## Apply routes

| Kind | Destination and behavior | Important seam |
| --- | --- | --- |
| Policy | Personal or workspace policy directory plus policy configuration | Adds a provenance comment and creates the proper scope entry. |
| User-global skill | ORG2 global skill directory | Copies a complete skill bundle or creates `SKILL.md`, then invalidates skill caches. |
| Workspace-local skill | Original repository location | Skips the copy because ORG2 loads the skill in place. |
| MCP | Global or workspace MCP configuration | Parses the selected server into the typed config and saves through `McpConfigFile`. |
| Agent definition | Live `AgentDefinitionsStore` and its durable file | Updates memory and persistence together, so the definition appears without restart. |

Every target name must be nonempty, must not start with a dot, and can contain only ASCII letters, digits, dot, underscore, or hyphen. A slash or backslash is invalid. Existing targets fail unless the user set `overwrite=true`.

## Fidelity rules

The detector reports unmapped fields, frontmatter parse errors, large bundles, and read-only downgrades. These are warnings because the wizard owns the import decision.

A foreign `readonly: true` or `read_only: true` agent flag has no direct top-level `AgentDefinition` field. ORG2 translates it into excluded write-capable built-ins: edit file, delete file, and run shell. The imported agent remains a secondary custom agent and receives its Markdown body as `soul_content` with provenance.

Malformed agent frontmatter does not block the full batch. The apply path keeps the raw body and omits parsed frontmatter values.

## Persistence and consistency

The import pipeline has no generic imported-artifact table. Each artifact enters the store that already owns its runtime meaning.

This choice keeps downstream behavior native:

- policy selection reads policy configuration;
- skill prompt construction reads the skill loader;
- MCP runtime assembly reads typed MCP configuration;
- agent launch reads the live Agent Definitions store.

The batch is not one cross-store transaction. Each `ImportItemReport` can be `Imported`, `Skipped`, or `Failed`. This supports partial progress but means the user must interpret a mixed report.

## Trust boundaries

| Risk | Current control |
| --- | --- |
| Path traversal through a target name | Closed target-name character set and separator rejection. |
| Unplanned replacement | Overwrite defaults to false and requires an explicit selection flag. |
| Foreign semantic loss | Preview and fidelity warnings appear before apply. |
| Foreign write authority | Read-only agent input loses edit, delete, and shell tools. |
| Hidden skill assets | Bundle import copies the full directory when `SKILL.md` defines a bundle. |
| Repository-local skill drift | The loader uses the source in place instead of creating a second copy. |
| Unbounded scan | Source roots, denied ancestors, file size, and item count constrain detection. |

The importer does not establish that foreign instructions, scripts, MCP commands, or agent prompts are safe. Their normal ORG2 runtime policy and trust checks still apply after import.

## Tradeoffs

| Choice | Benefit | Cost or limit |
| --- | --- | --- |
| Detect before apply | The user can inspect name, scope, size, and fidelity loss. | The source can change between detection and apply. |
| Route to native stores | Imported values use normal ORG2 behavior immediately. | Apply needs one adapter per artifact kind. |
| Report each item | One bad item does not discard the batch. | The batch has no all-or-nothing transaction. |
| Keep workspace skills in place | No fork or stale duplicate appears under `.orgii`. | Removal or change in the source repository changes future loading. |
| Preserve provenance in Markdown | A maintainer can trace copied text to its source path. | A moved or deleted source path can become historical only. |
| Translate read-only into tool exclusions | A foreign safety constraint keeps practical meaning. | It covers the curated write-tool list, not every possible external effect. |

## Source map

| Concern | Current source |
| --- | --- |
| Shared import model and fidelity warnings | [`src-tauri/crates/agent-core/src/specialization/external_import/types.rs`](src-tauri/crates/agent-core/src/specialization/external_import/types.rs) |
| Detector composition and bounds | [`src-tauri/crates/agent-core/src/specialization/external_import/detect/mod.rs`](src-tauri/crates/agent-core/src/specialization/external_import/detect/mod.rs), [`src-tauri/crates/agent-core/src/specialization/external_import/detect/helpers.rs`](src-tauri/crates/agent-core/src/specialization/external_import/detect/helpers.rs) |
| MCP detection | [`src-tauri/crates/agent-core/src/specialization/external_import/detect/mcp.rs`](src-tauri/crates/agent-core/src/specialization/external_import/detect/mcp.rs) |
| Apply routes | [`src-tauri/crates/agent-core/src/specialization/external_import/commands.rs`](src-tauri/crates/agent-core/src/specialization/external_import/commands.rs) |
| Frontend API types and commands | [`src/api/types/externalImport.ts`](src/api/types/externalImport.ts), [`src/api/tauri/externalImport/index.ts`](src/api/tauri/externalImport/index.ts) |
| Shared wizard state and result handling | [`src/scaffold/WizardSystem/shared/externalImport/useExternalImport.tsx`](src/scaffold/WizardSystem/shared/externalImport/useExternalImport.tsx), [`src/scaffold/WizardSystem/shared/externalImport/ExternalImportTable.tsx`](src/scaffold/WizardSystem/shared/externalImport/ExternalImportTable.tsx) |

## Known limits

This record does not claim semantic equivalence between the foreign product and ORG2. The current import shape covers the stated artifact types and source layouts only. It did not apply artifacts to the local machine during this analysis.

