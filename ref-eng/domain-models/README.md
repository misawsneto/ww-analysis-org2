---
type: domain-model-index
name: org2-domain-model
description: Canonical bounded-context model for ORG2, derived from source-grounded entities plus the accepted UA semantic index.
tags: [org2, domain-model, bounded-contexts, ddd]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# ORG2 domain model

## Purpose

This corpus defines the logical domain boundaries of ORG2 without changing product source or the generated UA and Graphify artifacts.

The context classification is **Derived**. Entity identities and lifecycle facts reuse source-observed records where available, especially [Core entities](ref-eng/domain-models/core-entities.md). UA supplies semantic coverage, source paths, and evidence-backed behavioral slices; it does not by itself define the canonical bounded contexts.

## Modeling rules

1. A bounded context owns a distinct vocabulary, lifecycle, policy set, or durable state that can change independently of neighboring contexts.
2. An edge context primarily translates an external protocol or foreign model into ORG2 semantics.
3. Infrastructure provides reusable technical capability but does not own product-domain identity.
4. Every canonical entity has one semantic owner. Other contexts hold references, projections, snapshots, or adapters.
5. Physical crate/module placement does not by itself determine logical context ownership.
6. `Workspace`, `Project`, and `Repository` remain distinct scope concepts even when one runtime path binds them together.

## Canonical contexts

| Context | Classification | Primary responsibility |
| --- | --- | --- |
| [Agent Execution](ref-eng/domain-models/contexts/agent-execution.md) | Core | Execute a resolved agent session and its turns. |
| [Agent Team Coordination](ref-eng/domain-models/contexts/agent-team-coordination.md) | Core | Coordinate a hierarchy of agents, delegated tasks, inbox traffic, and run finality. |
| [Project & Work Management](ref-eng/domain-models/contexts/project-work-management.md) | Core | Own projects, durable work, work runs, handoff, routines, review, and execution linkage. |
| [Memory & Learning](ref-eng/domain-models/contexts/memory-learning.md) | Core | Preserve workspace memory and evolve durable learnings across executions. |
| [Trajectory & Provenance](ref-eng/domain-models/contexts/trajectory-provenance.md) | Core | Normalize execution history, file/change provenance, replay, usage, and observational records. |
| [Agent Configuration & Capability Catalog](ref-eng/domain-models/contexts/agent-configuration-capabilities.md) | Supporting/core-enabling | Define agents, capabilities, skills, MCP configuration, inheritance, and launch-time resolution. |
| [Human Interaction & Approval](ref-eng/domain-models/contexts/human-interaction-approval.md) | Supporting/control | Own permission, question, plan-approval, secret, and mode-control obligations. |
| [Collaboration & Sharing](ref-eng/domain-models/contexts/collaboration-sharing.md) | Supporting/product | Own cloud organization membership, sharing, comments/conversations, and collaboration synchronization. |

## Edge contexts

| Context | Role |
| --- | --- |
| [Channel Gateway](ref-eng/domain-models/edge-contexts/channel-gateway.md) | Maps external chats and commands onto native agent sessions. |
| [External Artifact Import](ref-eng/domain-models/edge-contexts/external-artifact-import.md) | Translates foreign agent artifacts into native definitions, skills, and MCP configuration. |

## Infrastructure and shared scopes

- [Execution capabilities](ref-eng/domain-models/infrastructure/execution-capabilities.md) classifies Git, terminal, browser, LSP, search, database, key vault, transport, and OS services as technical capabilities rather than product domains.
- [Shared scopes and identity boundaries](ref-eng/domain-models/infrastructure/shared-scopes.md) defines the non-equivalence of Workspace, Project, Repository, Agent Org, Project Org, and Cloud Org.

## Canonical cross-cutting records

1. [Context map](ref-eng/domain-models/context-map.md) — compact logical topology.
2. [Ubiquitous language](ref-eng/domain-models/ubiquitous-language.md) — terminology and prohibited conflations.
3. [Entity ownership](ref-eng/domain-models/entity-ownership.md) — one semantic owner per canonical concept.
4. [Context relationships](ref-eng/domain-models/context-relationships.md) — published/consumed contracts.
5. [Source map](ref-eng/domain-models/source-map.md) — logical contexts mapped to representative implementation paths.
6. [Core entities](ref-eng/domain-models/core-entities.md) — source-observed entity inventory retained as evidence, not as the bounded-context map.

## Evidence

The classification rationale and UA coverage audit live in [G-ORG2-DOMAIN-001 context classification](ref-eng/evidence/G-ORG2-DOMAIN-001-context-classification.md).

## Update rule

When ORG2 source changes, revalidate the entity owner and published contracts before changing a context boundary. Do not edit `.understand-anything/` or `graphify-out/` to make generated evidence agree with this curated model.
