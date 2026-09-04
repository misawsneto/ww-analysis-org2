---
type: domain-model
name: org2-shared-scopes
description: Shared ORG2 scopes and identity boundaries that cross contexts without forming one aggregate.
tags: [org2, domain-model, scopes, identity]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# Shared scopes and identity boundaries

## Workspace, Project, Repository

| Scope | Semantic role | Owner |
| --- | --- | --- |
| Workspace | Filesystem/execution scope used for session runtime, memory, permissions, skills, and local tooling. | Shared primitive |
| Project | Durable work-management identity with metadata, work items, members, schedules, and repository links. | Project & Work Management |
| Repository | Version-controlled code resource used by execution, project, provenance, and collaboration. | Infrastructure/shared reference |

These scopes may point at the same directory or be bound in one runtime flow, but they must not be treated as equivalent identities.

## Organization identities

| Identity | Meaning | Owner |
| --- | --- | --- |
| Agent Org | Reusable hierarchy/composition of execution agents. | Agent Team Coordination |
| Project Org | Namespace for projects/work. | Project & Work Management |
| Cloud Org | Cloud collaboration/membership identity. | Collaboration & Sharing |

`org2CloudProjectOrgAlias.ts` is evidence that Cloud Org and Project Org require an explicit mapping. The existence of a bridge is evidence against collapsing them into one universal `Organization`.

## Session identities

- Native `AgentSession` is live execution identity.
- `SessionRecord` is canonical provenance/history identity.
- A shared/imported session reference is a collaboration representation.

References between them are explicit translations/projections rather than implicit equality.
