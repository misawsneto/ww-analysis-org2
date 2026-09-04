---
type: domain-context
name: org2-external-artifact-import
description: Anti-corruption context translating foreign agent artifacts into native ORG2 configuration.
tags: [org2, domain-model, edge-context, import]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# External Artifact Import

## Classification

**Edge/anti-corruption context.**

UA promoted External Artifact Import as one of its five domains. Its behavior is real and source-ranged, but its purpose is translation from foreign ecosystems into ORG2-owned configuration concepts.

## Owns

- Detected foreign artifact candidates.
- Already-imported/deduplication observations.
- User import selection.
- Per-item import attempt/report.
- Type-specific translation dispatch.

## Produces native records

- Agent definitions.
- Skills.
- MCP server configuration.
- Policy/rule artifacts where supported.

The produced native entities are owned by Agent Configuration & Capability Catalog after successful translation.

## Invariants

- Already-imported artifacts are identified during detection.
- Each selected item receives a per-item result.
- Foreign naming/schema does not become the canonical ORG2 domain language merely because it was imported.

## UA source-ranged evidence

- `src-tauri/crates/agent-core/src/specialization/external_import/commands.rs`
- `src-tauri/crates/agent-core/src/specialization/external_import/detect/mod.rs`
- `src-tauri/crates/agent-core/src/specialization/external_import/detect/mcp.rs`
