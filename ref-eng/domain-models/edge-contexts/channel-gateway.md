---
type: domain-context
name: org2-channel-gateway
description: Edge context mapping external channel chats and commands to native Agent Execution.
tags: [org2, domain-model, edge-context, channels]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: derived
---

# Channel Gateway

## Classification

**Edge/integration context.**

UA promoted Channel Gateway as one of its five domains. This curated model retains its explicit entities and lifecycle but classifies it as an edge context because its primary purpose is to map external channel conversations onto native session semantics.

## Owns

- Channel account identity/configuration.
- External chat identity.
- Persisted chat-to-session binding.
- Inbound message/gateway command interpretation.
- Idle reset of the external chat binding.

## Invariants

- A channel chat maps to a persisted native session binding.
- Idle reset archives the stale session before minting a fresh one.
- Native session execution remains owned by Agent Execution.

## Published contract

Inbound content and gateway commands resolve a chat binding and dispatch through Agent Execution. Outbound delivery projects native execution responses back into the external channel.

## UA source-ranged evidence

- `src-tauri/crates/agent-core/src/integrations/gateway/service.rs`
- `src-tauri/crates/agent-core/src/integrations/gateway/channels_ops.rs`
- `src-tauri/crates/agent-core/src/integrations/gateway/binding.rs`
- `src-tauri/crates/agent-core/src/state/commands/channel_handler/dispatch.rs`
- `src-tauri/crates/agent-core/src/state/commands/channel_handler/idle_reset.rs`
