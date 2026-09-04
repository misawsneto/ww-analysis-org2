---
type: domain-model
name: org2-entity-ownership
description: Canonical semantic ownership of important ORG2 entities and lifecycle concepts.
tags: [org2, domain-model, entity-ownership, bounded-contexts]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# ORG2 entity ownership

## Ownership rule

Every canonical product concept has one semantic owner. Other contexts may store IDs, snapshots, projections, caches, indexes, or foreign-key-like references without becoming the owner.

The source-observed entity inventory remains [Core entities](ref-eng/domain-models/core-entities.md). This table adds the Derived bounded-context classification.

| Canonical concept | Semantic owner | Notes |
| --- | --- | --- |
| `AgentDefinition` | Agent Configuration & Capability Catalog | Editable durable configuration identity. |
| `ResolvedAgent` | Agent Configuration & Capability Catalog | Launch-time resolved value, not separate persisted identity. |
| `AgentSkillsConfig` | Agent Configuration & Capability Catalog | Skill availability/loading configuration. |
| MCP server configuration | Agent Configuration & Capability Catalog | Native MCP configuration and capability source. |
| Agent capability selection | Agent Configuration & Capability Catalog | Declarative/resolved capability composition. |
| `AgentSession` | Agent Execution | Live execution aggregate. |
| `SessionRuntime` | Agent Execution | Session-scoped resolved runtime strategy bundle. |
| `DialogTurn` | Agent Execution | Active execution episode. |
| `TurnIntent` | Agent Execution | Durable logical submission identity. |
| Runtime tool registry/policy instance | Agent Execution | Session-scoped executable projection of configuration and infrastructure. |
| `AgentOrg` | Agent Team Coordination | Reusable agent-team composition. |
| `OrgMember` | Agent Team Coordination | Member identity within an Agent Org. |
| `AgentOrgRunRecord` | Agent Team Coordination | Durable coordinated-run envelope. |
| Org task | Agent Team Coordination | Run-scoped delegation primitive. |
| Agent-org inbox message/resolution | Agent Team Coordination | Run/member communication and resolution state. |
| `ProjectOrg` | Project & Work Management | Project-management namespace. |
| `ProjectData` / Project | Project & Work Management | Durable project identity. |
| `WorkItemData` / Work Item | Project & Work Management | Durable work aggregate. |
| `WorkItemRun` | Project & Work Management | Durable work execution attempt. |
| Work Item handoff | Project & Work Management | Work lifecycle state. |
| Work Item execution lock | Project & Work Management | Work-level execution coordination. |
| Routine / Routine Fire | Project & Work Management | Scheduled/repeated work semantics. |
| Team Inbox item | Project & Work Management | Work-management inbox item; distinct from agent-org inbox. |
| `Learning` | Memory & Learning | Structured durable knowledge record. |
| Learning status/category/source/evolution | Memory & Learning | Learning lifecycle vocabulary. |
| Consolidation run/trigger | Memory & Learning | Learning evolution process. |
| Workspace memory entry/index/surface state | Memory & Learning | Workspace-scoped memory and surfacing state. |
| `SessionRecord` | Trajectory & Provenance | Canonical cross-tool historical session record. |
| `ActivityRecord` / activity chunk | Trajectory & Provenance | Canonical/ingestion history representation. |
| File change/edit/diff/checkpoint/usage records | Trajectory & Provenance | Provenance and replay evidence. |
| `SessionEvent` | Trajectory & Provenance | Native normalized observational event; Agent Execution emits source activity but does not own the durable observational semantics. |
| Turn index / session statistics | Trajectory & Provenance | Rebuildable/read projections over history. |
| Pending plan approval | Human Interaction & Approval | Durable control obligation/resolution. |
| Permission request/rule | Human Interaction & Approval | Human/policy authorization state. |
| Question request/resolution | Human Interaction & Approval | Explicit interaction obligation. |
| Secret request/capture | Human Interaction & Approval | Controlled secret-resolution lifecycle. |
| Mode-switch request/resolution | Human Interaction & Approval | Control-plane interaction state. |
| Cloud organization | Collaboration & Sharing | Cloud membership/sharing identity. |
| Cloud membership / invitation | Collaboration & Sharing | Collaboration lifecycle. |
| Shared-session reference/import/fork | Collaboration & Sharing | Collaboration representation; native session ownership stays with Agent Execution or Trajectory & Provenance as applicable. |
| Collaboration comment/conversation | Collaboration & Sharing | Multi-user discussion/sharing semantics. |
| Channel account | Channel Gateway | Edge-context identity. |
| External chat | Channel Gateway | External conversation identity. |
| Chat-to-session binding | Channel Gateway | Mapping from external chat to native session. |
| Detected external artifact | External Artifact Import | Foreign-artifact candidate. |
| Per-item import report | External Artifact Import | Import attempt/outcome. |
| `Workspace` | Shared scope primitive | Referenced by several contexts; not promoted to an aggregate-owning context. |
| `Repository` | Infrastructure/shared reference | VCS resource referenced by work, execution, provenance, and collaboration. |

## Projection rules

- Agent Execution may cache resolved configuration; it does not own editable `AgentDefinition`.
- Project & Work Management may link an `AgentSession`; it does not own session execution.
- Agent Team Coordination may bind members to sessions; it does not own the session aggregate.
- Trajectory & Provenance may mirror session metadata; it does not own live execution.
- Collaboration & Sharing may expose project/session copies or references; it does not redefine the source context's canonical identity.
- Edge contexts may create native records through published contracts but do not take ownership of the created native entity.
