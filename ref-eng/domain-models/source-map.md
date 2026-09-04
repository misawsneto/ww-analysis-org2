---
type: domain-model
name: org2-domain-source-map
description: Mapping from logical ORG2 contexts to representative implementation paths and UA coverage.
tags: [org2, domain-model, source-map, ua]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# ORG2 domain source map

## Method

Counts below are unique approved files under representative source prefixes in UA's accepted 6,911-file scan. They are a **physical-footprint signal**, not the size or authority of a bounded context. Context classification comes from vocabulary, lifecycle, state, policy, and interaction evidence.

| Logical context | Representative source ownership | UA files under prefixes |
| --- | --- | ---: |
| Agent Execution | `src-tauri/crates/agent-core/src/core/session/`, `core/turn_executor/`, `init/` | 130 |
| Agent Team Coordination | `src-tauri/crates/agent-core/src/core/coordination/` | 51 |
| Project & Work Management | `src-tauri/crates/project-management/` | 173 |
| Memory & Learning | `src-tauri/crates/agent-core/src/specialization/memory/` | 46 |
| Trajectory & Provenance | `src-tauri/crates/orgtrack-core/`, `src-tauri/src/agent_sessions/event_pipeline/` | 251 |
| Agent Configuration & Capability Catalog | `core/definitions/`, `specialization/skills/`, `specialization/mcp/` | 101 |
| Human Interaction & Approval | `src-tauri/crates/agent-core/src/core/interaction/` | 20 |
| Collaboration & Sharing | `src/features/Org2Cloud/`, `src/features/TeamCollaboration/` | 214 |
| Channel Gateway | `agent-core/src/integrations/gateway/`, `state/commands/channel_handler/` | 13 |
| External Artifact Import | `agent-core/src/specialization/external_import/` | 13 |

## UA-promoted behavioral slices

UA's current domain graph explicitly promotes only five domains:

1. Agent Session Runtime.
2. Agent Organization Coordination.
3. Channel Gateway.
4. External Artifact Import.
5. Session Event Pipeline.

Those five domains contain 16 flows and 48 source-ranged steps. This curated map keeps their evidence but changes abstraction level:

- Agent Session Runtime → **Agent Execution**.
- Agent Organization Coordination → **Agent Team Coordination**.
- Channel Gateway → edge context.
- External Artifact Import → edge/anti-corruption context.
- Session Event Pipeline → implementation/read pipeline inside **Trajectory & Provenance**.

## Representative source evidence

### Agent Execution

- `src-tauri/crates/agent-core/src/core/session/project_init.rs`
- `src-tauri/crates/agent-core/src/init/runtime_assemble.rs`
- `src-tauri/crates/agent-core/src/core/turn_executor/execute/iteration_input.rs`
- `src-tauri/crates/agent-core/src/core/turn_executor/execute/provider_iteration.rs`
- `src-tauri/crates/agent-core/src/core/session/compaction/`
- `src-tauri/crates/agent-core/src/core/model_context/plan_preservation.rs`

### Agent Team Coordination

- `src-tauri/crates/agent-core/src/core/coordination/agent_org_runs/`
- `src-tauri/crates/agent-core/src/core/session/turn/processor/inbox_drain/routing.rs`

### Project & Work Management

- `src-tauri/crates/project-management/`
- Source-observed entities and lifecycles are summarized in [Core entities](ref-eng/domain-models/core-entities.md).

### Memory & Learning

- `src-tauri/crates/agent-core/src/specialization/memory/learnings/types.rs`
- `src-tauri/crates/agent-core/src/specialization/memory/workspace_memory/`
- Built-in memory extractor/consolidator definitions under `agent-core/src/core/definitions/builtin/`.

### Trajectory & Provenance

- `src-tauri/crates/orgtrack-core/src/canonical.rs`
- `src-tauri/src/agent_sessions/event_pipeline/`
- Cross-tool history is summarized in [Core entities](ref-eng/domain-models/core-entities.md).

### Agent Configuration & Capability Catalog

- `src-tauri/crates/agent-core/src/core/definitions/schema.rs`
- `src-tauri/crates/agent-core/src/core/definitions/resolver.rs`
- `src-tauri/crates/agent-core/src/core/definitions/store.rs`
- `src-tauri/crates/agent-core/src/specialization/skills/`
- `src-tauri/crates/agent-core/src/specialization/mcp/`

### Human Interaction & Approval

- `src-tauri/crates/agent-core/src/core/interaction/permission.rs`
- `src-tauri/crates/agent-core/src/core/interaction/plan_approval/`
- Other question, secret, presence, and mode-control modules under `core/interaction/`.

### Collaboration & Sharing

- `src/features/Org2Cloud/`
- `src/features/TeamCollaboration/`
- `src/features/Org2Cloud/org2CloudProjectOrgAlias.ts` is a concrete boundary between Cloud Org and local Project Org identities.

### Edge contexts

Channel Gateway source-ranged UA steps live under `integrations/gateway/` and `state/commands/channel_handler/`. External Artifact Import steps live under `specialization/external_import/commands.rs` and `detect/`.
