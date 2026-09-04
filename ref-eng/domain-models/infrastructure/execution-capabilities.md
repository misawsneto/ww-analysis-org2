---
type: domain-model
name: org2-execution-capabilities
description: Classification of reusable technical capabilities that support ORG2 domains without becoming bounded contexts.
tags: [org2, domain-model, infrastructure, capabilities]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# Execution capabilities

## Rule

A large or sophisticated subsystem is not automatically a bounded context. The following areas primarily provide reusable technical operations and do not own the canonical product lifecycles identified by the context map.

| Capability | Domain use | Why it remains infrastructure |
| --- | --- | --- |
| Git / Git API / worktrees / branches | Work execution, provenance, collaboration | Provides VCS operations; Work Item/Session/Project identities remain elsewhere. |
| Terminal/process execution | Agent Execution | Executes commands but does not own agent/work lifecycle. |
| Browser automation | Agent Execution | External action adapter. |
| LSP / IDE tooling | Agent Execution, UI | Code-intelligence adapter. |
| Search / semantic/code search | Execution, provenance, UI | Retrieval capability; query/index lifecycle is technical. |
| SQLite/database plumbing | All durable contexts | Persistence implementation. |
| Key vault / credential storage | Agent Execution, MCP, collaboration | Security infrastructure; control obligations remain Human Interaction & Approval. |
| Transport / IPC | UI/Tauri/runtime | Message transport, not product-domain ownership. |
| OS/system services | Desktop shell and execution | Platform adapter. |

## Dependency rule

Domain records may specify required capabilities abstractly. Physical implementations can change without renaming the owning domain entity. For example, a Work Item may require an isolated execution workspace; a Git worktree can satisfy that requirement without becoming part of the Work Item aggregate.
