---
type: domain-context
name: org2-collaboration-sharing
description: Own cloud/multi-user organization membership, invitations, repository sharing scope, shared sessions, comments/conversations, and synchronization that exposes local ORG2 work/history to collaborators.
tags: [org2, domain-model, bounded-context]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# Collaboration & Sharing

## Purpose

Own cloud/multi-user organization membership, invitations, repository sharing scope, shared sessions, comments/conversations, and synchronization that exposes local ORG2 work/history to collaborators.

**Classification:** Supporting/product

The boundary is Derived. The listed source paths and entity/lifecycle facts are source-observed or UA-observed where cited by the accepted reference corpus.

## Boundary

### Owns

- Cloud organization identity.
- Cloud membership and invitation lifecycle.
- Repository sharing/scope eligibility.
- Shared-session/import/fork collaboration semantics.
- Collaboration comments/conversations.
- Cloud/local synchronization state owned by the collaboration feature surface.

### Does not own

Project and Work Item lifecycle remain owned by Project & Work Management. Canonical historical session records remain owned by Trajectory & Provenance.

## Invariants

- Cloud Org and Project Org remain distinct identities even when an alias maps them.
- Sharing a session does not transfer live Agent Session ownership.
- Synchronization translates between collaboration and local domain identities instead of creating one universal entity model.

## Consumes

- Project Org/Project/Work references from Project & Work Management.
- Session/history references from Agent Execution and Trajectory & Provenance.
- Repository scope references.

## Publishes

- Collaboration membership/sharing state to UI.
- Project/org synchronization operations.
- Shared history/session references.

## Representative implementation paths

- `src/features/Org2Cloud/`
- `src/features/TeamCollaboration/`
- `src/features/Org2Cloud/org2CloudProjectOrgAlias.ts`

## Context relationship notes

See [Entity ownership](ref-eng/domain-models/entity-ownership.md) and [Context relationships](ref-eng/domain-models/context-relationships.md) for the canonical cross-context contracts.
