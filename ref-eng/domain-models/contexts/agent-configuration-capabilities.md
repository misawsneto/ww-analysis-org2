---
type: domain-context
name: org2-agent-configuration-capabilities
description: Define what a native agent is and what it may use: durable definitions, inheritance/patching, policy, model/session settings, tools, skills, MCP configuration, capabilities, delegation, and launch-time resolution.
tags: [org2, domain-model, bounded-context]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# Agent Configuration & Capability Catalog

## Purpose

Define what a native agent is and what it may use: durable definitions, inheritance/patching, policy, model/session settings, tools, skills, MCP configuration, capabilities, delegation, and launch-time resolution.

**Classification:** Supporting/core-enabling

The boundary is Derived. The listed source paths and entity/lifecycle facts are source-observed or UA-observed where cited by the accepted reference corpus.

## Boundary

### Owns

- `AgentDefinition` durable configuration.
- `ResolvedAgent` launch-time resolved value.
- Definition inheritance, patches, built-in overrides, and definition store semantics.
- `AgentSkillsConfig` and skill catalog/configuration.
- MCP server configuration and capability discovery configuration.
- Declarative capability/tool selection and delegation configuration.

### Does not own

Runtime tool instances and provider/tool execution belong to Agent Execution. External Artifact Import is an edge context that creates/updates native configuration through this boundary.

## Invariants

- Editable definition and resolved launch value are distinct.
- Resolution closes defaults, inheritance, overrides, capabilities, policy, model settings, tools, and skills before execution.
- Built-in overrides preserve one agent identity rather than creating a second active identity.
- Foreign imports must translate into native configuration semantics.

## Consumes

- Persisted/custom definition sources.
- Skills and MCP integration configuration.
- External Artifact Import translations.
- Account/model configuration.

## Publishes

- Resolved agent/runtime configuration to Agent Execution.
- Agent/member selection to Agent Team Coordination.
- Configuration/status projections to UI.

## Representative implementation paths

- `src-tauri/crates/agent-core/src/core/definitions/`
- `src-tauri/crates/agent-core/src/core/definitions/schema.rs`
- `src-tauri/crates/agent-core/src/core/definitions/resolver.rs`
- `src-tauri/crates/agent-core/src/core/definitions/store.rs`
- `src-tauri/crates/agent-core/src/specialization/skills/`
- `src-tauri/crates/agent-core/src/specialization/mcp/`

## Context relationship notes

See [Entity ownership](ref-eng/domain-models/entity-ownership.md) and [Context relationships](ref-eng/domain-models/context-relationships.md) for the canonical cross-context contracts.
