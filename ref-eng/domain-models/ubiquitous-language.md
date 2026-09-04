---
type: domain-model
name: org2-ubiquitous-language
description: Canonical terminology and semantic collision rules for the ORG2 domain model.
tags: [org2, domain-model, ubiquitous-language, terminology]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# ORG2 ubiquitous language

## Purpose

ORG2 uses several nearby terms for different identities. This record makes those distinctions explicit so architecture and product discussions do not collapse separate lifecycles into one generic concept.

## Canonical terms

| Term | Meaning | Owner |
| --- | --- | --- |
| **Agent Definition** | Durable editable configuration identity for a native agent. | Agent Configuration & Capability Catalog |
| **Resolved Agent** | Launch-time closed value after defaults, inheritance, policy, tools, skills, and capability resolution. | Agent Configuration & Capability Catalog |
| **Agent Session** | Live execution aggregate for one native session identity. | Agent Execution |
| **Dialog Turn** | One active provider/tool execution episode inside a session. | Agent Execution |
| **Turn Intent** | Durable identity of one logical submission across admission, execution, and settlement. | Agent Execution |
| **Agent Org** | Reusable composition/hierarchy of agent members. | Agent Team Coordination |
| **Agent Org Run** | Durable execution envelope for one coordinated Agent Org launch. | Agent Team Coordination |
| **Org Task** | Run-scoped delegated task inside Agent Team Coordination. | Agent Team Coordination |
| **Project Org** | Project-management namespace that contains Projects. | Project & Work Management |
| **Project** | Durable work-management container with metadata and repository links. | Project & Work Management |
| **Work Item** | Durable unit of product/project work with history, handoff, execution linkage, and proof of work. | Project & Work Management |
| **Work Item Run** | Durable execution attempt associated with a Work Item. | Project & Work Management |
| **Workspace** | Filesystem/execution scope used by multiple contexts. | Shared scope primitive |
| **Repository** | Version-controlled code resource linked into execution or project context. | Infrastructure/shared reference |
| **Learning** | Structured durable knowledge with lifecycle and evolution state. | Memory & Learning |
| **Workspace Memory** | Workspace-scoped persisted memory surfaced into agent context. | Memory & Learning |
| **Session Event** | Canonical native observational record derived from execution activity. | Trajectory & Provenance |
| **Session Record** | Canonical cross-tool provenance record anchoring historical activity. | Trajectory & Provenance |
| **Cloud Org** | Cloud collaboration/membership identity. | Collaboration & Sharing |
| **Skill** | Reusable prompt/procedure capability definition. | Agent Configuration & Capability Catalog |
| **Tool** | Executable runtime operation exposed to an agent. | Agent Execution / execution infrastructure |
| **MCP Server** | Configured external Model Context Protocol capability provider. | Agent Configuration & Capability Catalog |
| **Capability** | Declared or resolved ability that influences what an agent can use or do. | Agent Configuration & Capability Catalog |

## Prohibited equivalences

### `Org Task` is not `Work Item`

An Org Task exists inside a coordinated agent run and is constrained by the agent hierarchy. A Work Item is durable project work with its own state, history, handoff, execution locks, runs, review, routines, and synchronization.

### `Agent Org` is not `Project Org` and is not `Cloud Org`

- Agent Org composes execution agents.
- Project Org namespaces projects and work.
- Cloud Org represents collaboration membership/sharing scope.

Any alias or mapping between Project Org and Cloud Org is an integration relationship, not identity equality.

### `Agent Session` is not `Session Record`

`AgentSession` owns live execution state. `SessionRecord` is an observational/provenance representation of a session. The latter can describe external coding-agent sessions that never existed as native ORG2 `AgentSession` aggregates.

### `Workspace` is not `Project` and is not `Repository`

A workspace is an execution/filesystem scope. A project is a durable product/work-management identity. A repository is a VCS resource. Runtime flows can bind them together without merging their semantics.

### `Agent Definition` is not `Resolved Agent`

The definition is editable durable configuration. The resolved agent is a launch-time value produced by resolution. Execution should consume the latter.

### `Turn Intent` is not `Dialog Turn`

A Turn Intent identifies the logical submission. A Dialog Turn identifies an active execution episode. Retries, queueing, coalescing, or failure can make the relationship non-trivial.

### `Skill`, `Tool`, `MCP Server`, and `Capability` are not synonyms

A Skill is a reusable instruction/procedure artifact. A Tool is an executable runtime operation. An MCP Server supplies external MCP capabilities. Capability is the higher-level declarative/resolved ability model.

### `Session Event` is not raw streaming activity

Provider deltas and activity chunks are ingestion material. Session Events are normalized observational records after consolidation and pairing logic.
