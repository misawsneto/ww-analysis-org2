---
type: evidence-manifest
name: G-ORG2-REF-002-graph-coverage
description: UA-guided semantic coverage and Graphify structural scope for the ORG2 capability and execution atlas.
tags: [org2, implementation-reference, evidence, ua, graphify]
---

# Graph-guided coverage for the ORG2 capability atlas

**Goal:** G-ORG2-REF-002  
**Source revision:** `b315ba4f82fb1fe294496793d7322095e7efe262`  
**Status:** Ready for G-ORG2-REF-002-VER001  
**Evidence role:** UA guides semantic coverage and navigation; Graphify clarifies deterministic structure; direct source will prove published behavior

## Purpose

This matrix selects the next ORG2 technical-documentation work without another broad repository search. It starts from UA's semantic domains, subtracts the accepted `ref-eng/` corpus, and uses Graphify only to confirm that a candidate crosses enough structural boundaries to warrant a focused journey.

The selected outputs can refine an existing architecture, domain, data, seam, or runtime record. A new file is appropriate only when no existing record owns the deeper subject.

## Accepted snapshots

| Subject | Accepted state | Role in this goal |
| --- | --- | --- |
| ORG2 source | `b315ba4f82fb1fe294496793d7322095e7efe262` | Authority for the implementation that Task 2 will document. |
| UA knowledge graph | `.understand-anything/knowledge-graph.json`, commit `b315ba4f82fb1fe294496793d7322095e7efe262`, 29,271 nodes, 50,036 edges, nine layers, ten tour steps | Semantic file and symbol navigation, layer context, summaries, tags, and tour context. |
| UA domain graph | `.understand-anything/domain-graph.json`, commit `b315ba4f82fb1fe294496793d7322095e7efe262`, five domains, 16 flows, 48 source-backed steps | Primary domain, flow, vocabulary, and journey selection. |
| Graphify graph | `graphify-out/graph.json`, `built_at_commit` `b315ba4f82fb1fe294496793d7322095e7efe262`, 73,483 nodes, 180,803 edges, 2,134 communities | Deterministic file, symbol, call, reference, import, community, and boundary evidence. |
| Existing corpus | [ORG2 Implementation Reference](ref-eng/README.md#org2-implementation-reference), completed by G-ORG2-REF-001 | Defines accepted coverage and prevents duplicate analysis. |

G-ORG2-REINDEX-001 recorded the accepted graph digests and complete file coverage. Its semantic review also recorded 639 orphan-node warnings and generic or repeated summaries for 2,430 file paths. This goal therefore uses UA paths, domain structure, and specific summaries as navigation evidence, not as behavioral proof.

## UA semantic coverage

| UA domain | UA flows | Current `ref-eng/` depth | Scope decision |
| --- | --- | --- | --- |
| Agent Session Runtime | Start Workspace Session; Execute Agent Turn; Compact Session Context | Deep coverage exists in the execution kernel, execution seams, interactive loop, core entities, and state lifecycles. | Reject a new journey. Use these records as the shared runtime boundary for the selected slices. |
| Agent Organization Coordination | Create Agent Org Run; Route Organization Task; Finalize Agent Org Run | Core entities identifies Agent Orgs and Runs, but no record traces creation, hierarchy routing, inbox delivery, member sessions, finality, persistence, and frontend notification as one execution path. | Select. |
| Channel Gateway | Start Channel Gateway; Route Inbound Channel Message; Reset Idle Channel Session | No accepted technical record explains channel lifecycle, persistent chat binding, slash-command handling, singleton OS sessions, reinjection, idle reset, or outbound workers. | Select. |
| External Artifact Import | Detect External Artifacts; Apply External Selections; Import Specialized Artifacts | System topology names extension mechanisms, but no source-grounded seam record explains detection, preview, user selection, parsing, trust, collision handling, and writes into policies, skills, MCP configuration, and agent definitions. | Select. |
| Session Event Pipeline | Ingest Session Activity; Browse Session Events; Search Session Events; Compute Session Analytics | State lifecycles explains canonical session events and persistence, but it does not trace raw-chunk consolidation, tool-call pairing, query filters, search snippets, analytics, or the review-facing read path. | Select. |

UA's three `cross_domain` edges support the selected connections: Channel Gateway to Agent Session Runtime, Agent Organization Coordination to Agent Session Runtime, and Agent Session Runtime to Session Event Pipeline. External Artifact Import connects indirectly by writing definitions and integrations that later runtime assembly consumes.

## UA layer and path guidance

The following file counts are navigation scopes from the UA knowledge graph. They do not measure implementation size and must not be compared with Graphify node counts.

| Selected journey | UA file scope | Main UA layers | High-value semantic path |
| --- | ---: | --- | --- |
| Agent Org coordination | 110 files | Frontend UI, Rust Agent Runtime, Configuration | Organization UI and definitions → run context and hierarchy → routing and inbox → member session runtime → finality and frontend run events. |
| Channel message routing | 42 files | Configuration, Frontend UI, Rust Agent Runtime | Channel configuration → gateway service and workers → persistent chat binding → inbound dispatch and slash commands → session reinjection or new turn → idle reset. |
| External artifact import | 13 files | Rust Agent Runtime | Tauri detect command → per-tool detectors → preview and selection → typed item dispatch → policy, skill, MCP, or agent-definition store. |
| Session event review pipeline | 57 files | Tauri Shell | Raw activity chunks → consolidation and tool-pair merge → canonical events → filters, pagination, search, extraction, statistics, and frontend review consumers. |

The UA tour already covers the application entry, agent runtime, state/event flow, integrations/imports, persistence, and frontend shell. Task 2 can use those tour nodes for orientation, but the selected domain flows define the deeper traversal.

## Graphify structural boundaries

The Graphify counts below come from bounded path-prefix selection over the accepted graph. `Internal edges` connect selected-path nodes to the same journey. `Boundary edges` connect them to another path. These values establish navigation breadth; they do not establish runtime order or criticality.

| Selected journey | Files | Structural nodes | Internal edges | Boundary edges | Main boundary evidence |
| --- | ---: | ---: | ---: | ---: | --- |
| Agent Org coordination | 76 | 785 | 1,858 | 1,426 | References, imports, and calls connect coordination to the database writer and bridge, inbox records, agent definitions, session task views, and frontend organization configuration. |
| Channel message routing | 42 | 203 | 422 | 370 | References and imports connect gateway and channel-handler code to bus events, unified app state, channel management, frontend channel hooks, and connection configuration. |
| External artifact import | 13 | 111 | 300 | 260 | References and calls connect import orchestration to MCP configuration, the agent-definition store, and policy ownership. |
| Session event review pipeline | 57 | 627 | 1,254 | 1,096 | References and imports connect the pipeline to canonical session-event types, extracted payloads, session persistence, turn indexes, Tauri transport, Orgtrack canonical data, and diff extraction. |

The large boundary counts justify focused seam analysis. They do not justify reading every selected file. Task 2 will begin at UA flow steps, follow only Graphify edges that cross an owning boundary, and stop when direct source establishes the contract.

## Existing-document coverage

| Existing record | Strong accepted coverage | Refinement opportunity from selected journeys |
| --- | --- | --- |
| [Native-agent execution kernel](ref-eng/architecture/native-agent-execution-kernel.md#native-agent-execution-kernel) | Native session construction, provider/tool loop, scheduler, events, and persistence. | Link Agent Org and channel entry paths to the shared runtime without restating the kernel. |
| [Native-agent execution seams](ref-eng/interfaces/native-agent-execution-seams.md#native-agent-execution-seams) | Interactive launch, prompt, provider, tool, persistence, and frontend seams. | Add links to separate channel and import seam records; do not expand its native-interactive contract table beyond its declared scope. |
| [Interactive native-agent loop](ref-eng/runtime/interactive-native-agent-loop.md#interactive-native-agent-loop) | User and Work Item launch through terminal turn settlement, including compaction. | Retain as the common execution continuation after Agent Org or channel admission. |
| [System topology](ref-eng/architecture/system-topology.md#org2-system-topology) | Context, containers, composition, CLIs, extensions, trust, and delivery. | Refine cross-links or concise boundaries for channel gateways and external import after their focused seams are source-confirmed. |
| [Package dependencies](ref-eng/architecture/package-dependencies.md#org2-package-dependencies) | Cargo package direction, inversion points, build order, and change impact. | No planned content expansion; use it to explain crate ownership when needed. |
| [Core entities](ref-eng/domain-models/core-entities.md#org2-core-entities) | Agent, session, project, Work Item, Run, event, and cross-tool identities and relations. | Refine Agent Org run, member, inbox, task, and finality relations if direct source establishes details missing from the current model. |
| [State lifecycles](ref-eng/data-and-storage/state-lifecycles.md#org2-state-lifecycles) | SQLite/WAL, session events, Turn Intents, Work Item Runs, projections, outboxes, replay, and recovery. | Refine the distinction between event storage and the review pipeline, then link its ingestion and query record. |

## Selected Task 2 outputs

| Priority | Journey and reader question | Planned technical owner | Required boundary depth |
| ---: | --- | --- | --- |
| 1 | Agent Org coordination: How does a user-defined organization become a persisted run, route work through hierarchy and inbox state into member sessions, and reach consistent finality? | New `ref-eng/runtime/agent-org-coordination.md`; refine `ref-eng/domain-models/core-entities.md` and other owning records only where source adds material facts. | UI and definition → run persistence → hierarchy and task routing → inbox and member session → plan or completion gates → finality → frontend events and recovery. |
| 2 | Channel message routing: How does an external chat become or reenter one OS-agent session, and how do binding, commands, workers, idle reset, and failure handling preserve user continuity? | New `ref-eng/runtime/channel-gateway-routing.md`; refine topology and state records only where the focused analysis adds an owning boundary. | Channel config and process lifecycle → inbound worker → binding and command policy → session admission or steering → outbound response → reset and restart persistence. |
| 3 | External artifact import: How does ORG2 detect and safely translate another tool's instructions, skills, MCP servers, and agent definitions into ORG2-owned primitives? | New `ref-eng/interfaces/external-artifact-import-seams.md`; refine topology's extension and trust sections when needed. | Filesystem/config trust → per-tool detection → preview and selection → parse and validation → collision policy → target stores → later runtime consumption. |
| 4 | Session event review pipeline: How does raw agent activity become canonical, searchable, paginated, analytic review data without turning the read model into the source of execution truth? | New `ref-eng/data-and-storage/session-event-pipeline.md`; refine state lifecycles where the data-owner distinction needs a precise link. | Raw chunks and sources → consolidation and pairing → canonical event shape → persistence or cache → filters/search/analytics → review consumers and rebuild boundaries. |

`ref-eng/architecture/capability-execution-atlas.md` will connect these four journeys to the already documented native runtime, entities, state owners, and structural boundaries.

## Rejected duplicate or deferred topics

- Native interactive execution is rejected as a new slice because three focused records already cover it at implementation depth.
- Manual and forked compaction are rejected as a separate slice because the interactive loop already covers compaction and the UA steps do not expose a broader missing boundary.
- Durable Work Item execution is rejected as a new slice because the execution kernel, interactive loop, core entities, and state lifecycles already cover its launch, run, dispatch, and settlement roles.
- Broad C3/C4 topology, package layering, entity inventory, and SQLite/WAL explanation are rejected because the accepted corpus already owns them.
- Cross-tool history ingestion through Orgtrack is deferred because state lifecycles already explains its main normalization and index boundary, while UA selected the distinct external-artifact import domain.
- Project sync is deferred because the accepted UA domain graph does not model it as one of the five primary domains in this snapshot; a later goal can select it through direct evidence if a reader need emerges.

## Task 2 navigation rule

For each selected journey:

1. Start with the UA domain, flows, and source-backed steps.
2. Use the UA knowledge graph to identify the owning layer, adjacent semantic files, and shared vocabulary.
3. Use Graphify to follow only calls, references, imports, hubs, and community bridges that clarify an ownership or interface boundary.
4. Confirm material behavior and tradeoffs against direct source at the pinned revision.
5. Update the existing technical owner when one exists; otherwise create the focused record named above.
6. Label any graph-derived inference and unresolved contradiction; never promote it to Source-observed through repetition.

This rule makes UA the contextualization mechanism while keeping refined ORG2 technical documentation as the goal output.
