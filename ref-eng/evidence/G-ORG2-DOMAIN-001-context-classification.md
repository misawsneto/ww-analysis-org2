---
type: evidence
name: G-ORG2-DOMAIN-001-context-classification
description: Evidence and rationale for the curated ORG2 bounded-context model.
tags: [org2, domain-model, ua, evidence, bounded-contexts]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# ORG2 domain context classification

## Question

Does UA's current five-domain graph represent ORG2's complete bounded-context model?

## Accepted evidence baseline

- G-ORG2-REINDEX-001 verified UA at `b315ba4f82fb1fe294496793d7322095e7efe262` with 6,911 approved files, 29,271 knowledge-graph nodes, 50,036 edges, 9 architecture layers, 5 domain nodes, 16 domain flows, and 48 source-ranged domain steps.
- [Core entities](ref-eng/domain-models/core-entities.md) provides source-observed identities for agent configuration, Agent Org, sessions/turns, project/work, and cross-tool history.
- UA `domain-graph.json` explicitly promotes Agent Session Runtime, Agent Organization Coordination, Channel Gateway, External Artifact Import, and Session Event Pipeline.

## Classification test

A candidate is promoted to a bounded context when the accepted evidence shows several of:

1. distinct domain vocabulary and identity;
2. lifecycle/state transitions independent of adjacent contexts;
3. durable state or dedicated stores;
4. policies/invariants that are not generic infrastructure;
5. a coherent source ownership area;
6. explicit translation/contracts with neighboring areas.

An area is classified as an **edge context** when its primary role is protocol/foreign-model translation. An area remains **infrastructure** when it provides reusable technical capability without owning ORG2 product identity.

## UA five-domain reassessment

| UA domain | Curated classification | Reason |
| --- | --- | --- |
| Agent Session Runtime | Agent Execution — Core | Owns session/turn execution semantics and runtime continuity. |
| Agent Organization Coordination | Agent Team Coordination — Core | Owns hierarchy, coordinated runs, delegated tasks/inbox, and finality. |
| Channel Gateway | Edge context | Owns external chat/binding semantics whose purpose is dispatch into native sessions. |
| External Artifact Import | Edge/anti-corruption context | Translates foreign artifacts into native configuration identities. |
| Session Event Pipeline | Subsystem inside Trajectory & Provenance | Ingestion/search/analytics behavior is observational and sits beside the broader canonical provenance model. |

## Omitted bounded-context candidates

UA's approved file scan shows substantial source ownership outside the five promoted behavioral slices:

| Candidate | Representative prefixes | Approved files under prefixes | Classification |
| --- | --- | ---: | --- |
| Project & Work Management | `src-tauri/crates/project-management/` | 173 | Core |
| Memory & Learning | `agent-core/src/specialization/memory/` | 46 | Core |
| Trajectory & Provenance | `orgtrack-core/` + native event pipeline | 251 | Core |
| Agent Configuration & Capability Catalog | definitions + skills + MCP | 101 | Supporting/core-enabling |
| Human Interaction & Approval | `agent-core/src/core/interaction/` | 20 | Supporting/control |
| Collaboration & Sharing | `src/features/Org2Cloud/` + `TeamCollaboration/` | 214 | Supporting/product |

The counts are coverage signals, not the classification basis by themselves.

## Representative semantic evidence

### Project & Work Management

The existing source-observed entity record identifies Project Org, Project, Work Item, Work Item Run, dispatch records, routines, handoff/lock/history, and execution linkage. These are distinct from Agent Org tasks and native sessions.

### Memory & Learning

UA summaries identify `Learning`, `LearningCategory`, `EvolutionType`, `LearningStatus`, `LearningSource`, workspace-memory surface state, and dedicated extraction/consolidation behavior under `agent-core/src/specialization/memory/`.

### Trajectory & Provenance

`orgtrack-core/src/canonical.rs` contains canonical session provenance identity, while the native event pipeline consolidates activity into searchable/analytic `SessionEvent` records. This is broader than one event-pipeline journey.

### Agent Configuration & Capability Catalog

UA identifies the central `AgentDefinition` schema, recursive definition resolution, definition storage/override behavior, `AgentSkillsConfig`, MCP wiring/configuration, and capability selection. This authoring/resolution lifecycle precedes session execution.

### Human Interaction & Approval

UA identifies permission management, persisted plan approvals, questions, presence policy, secrets, and mode switching. These are explicit control obligations with resolution semantics.

### Collaboration & Sharing

UA architecture coverage includes Cloud Org, membership/sharing surfaces, Team Collaboration, and an explicit `org2CloudProjectOrgAlias.ts` bridge between Cloud Org and local Project Org identity spaces.

## Infrastructure rejection

Git, terminal, browser, LSP, search, database plumbing, key vault, transport, and system services remain infrastructure because they provide technical capability to several contexts without owning the canonical work/session/memory/provenance/collaboration lifecycles.

## Conclusion

UA's five domains are valid, source-ranged behavioral slices but are not an exhaustive ORG2 bounded-context model. The curated reference therefore adopts eight product contexts, two edge contexts, and a separate infrastructure/shared-scope classification while preserving UA and Graphify as upstream evidence.
