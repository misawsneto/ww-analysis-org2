---
type: domain-model
name: org2-context-relationships
description: Published and consumed semantic contracts among ORG2 bounded and edge contexts.
tags: [org2, domain-model, context-relationships, contracts]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# ORG2 context relationships

## Contract map

| Upstream / caller | Downstream / owner | Contract | Relationship rule |
| --- | --- | --- | --- |
| Agent Configuration & Capability Catalog | Agent Execution | Resolved agent, model/tool/skill/capability policy | Execution consumes a closed launch-time view rather than repeatedly interpreting editable definitions. |
| Project & Work Management | Agent Execution | Work binding, execution request, run/session link | Work remains durable project state; sessions remain execution state. |
| Agent Team Coordination | Agent Execution | Member session identity, delegated input, run/member context | Member execution uses native sessions while coordination owns hierarchy, task, inbox, and finality. |
| Agent Execution | Human Interaction & Approval | Permission/question/plan/secret/mode obligation | Execution blocks or branches on a control obligation without owning its durable resolution policy. |
| Human Interaction & Approval | Agent Execution | Approved/rejected/answered/cancelled resolution | Resolution lets execution continue, change behavior, or terminate the blocked action. |
| Agent Execution | Memory & Learning | Experience, extraction input, recall opportunity | Runtime activity can create or reinforce memory; memory lifecycle remains separate. |
| Memory & Learning | Agent Execution | Recalled workspace memory / learnings | Execution consumes relevant memory as context, not as session-owned state. |
| Agent Execution | Trajectory & Provenance | Native activity, event material, session metadata | Observation records execution without becoming the live session owner. |
| Project & Work Management | Trajectory & Provenance | Proof-of-work and historical references | Work can retain evidence references while provenance owns canonical history. |
| Collaboration & Sharing | Project & Work Management | Cloud-org/project-org mapping, project/work synchronization | Mapping does not equate Cloud Org and Project Org identities. |
| Collaboration & Sharing | Trajectory & Provenance | Shared/imported/forked session references | Sharing exposes or transfers history without redefining provenance ownership. |
| Channel Gateway | Agent Execution | Chat-bound inbound command/message dispatch | Gateway owns external chat/binding; execution owns native session behavior. |
| External Artifact Import | Agent Configuration & Capability Catalog | Translated agent definition, skill, MCP server config | Foreign concepts are normalized into native configuration semantics. |

## Translation boundaries

### Configuration → execution

The canonical seam is **resolution**. Agent Execution should depend on resolved, executable configuration rather than on the mutable authoring model.

### Work → execution

A Work Item or Work Item Run may cause session launch/resume and may hold session references. The execution outcome can settle work state, but neither identity replaces the other.

### Coordination → execution

Agent Team Coordination creates/addresses member execution through sessions. Hierarchy and finality remain coordination semantics even though turn execution happens in Agent Execution.

### Execution ↔ control

Human Interaction & Approval is a control-loop context. It owns outstanding obligations and their resolution; Agent Execution owns the action that requested control.

### Execution ↔ memory

Execution supplies experience; Memory & Learning decides persistence/evolution and later returns relevant context. Memory is not merely transcript history.

### Execution → provenance

Trajectory & Provenance is observational. It may consolidate raw activity, maintain replay/search/analytics projections, and ingest external histories.

### Collaboration ↔ local domains

Cloud and multi-user collaboration can map to Project Org, Project, Work Item, or session/history concepts. Those mappings are explicit integration seams rather than a single global entity model.

## Coupling constraint

A context may depend on another context's **published semantic contract**, but the domain model does not authorize direct cross-context mutation of the downstream owner's internal state.
