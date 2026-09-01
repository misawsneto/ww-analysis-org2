---
type: implementation-reference
name: org2-channel-gateway-routing
description: Inbound and outbound routing between external chat channels and the ORG2 agent runtime.
tags: [org2, runtime, channels, gateway, session]
source_revision: b315ba4f82fb1fe294496793d7322095e7efe262
status: active
claim_state: source-observed
---

# Channel gateway routing

## Scope and evidence

This record explains how ORG2 maps an external channel conversation to an agent session and returns the agent result through the same channel.

UA selected Channel Gateway as a missing journey. Graphify identified the gateway service, binding store, channel manager, shared session runtime, event bus, configuration, and frontend boundaries. All behavioral claims are Source-observed at revision `b315ba4f82fb1fe294496793d7322095e7efe262`.

## Boundary model

The gateway adapts transport-specific messages to the shared ORG2 runtime. It does not create a second agent engine.

```text
channel provider
  -> ChannelManager
  -> inbound gateway worker
  -> command or idle-reset policy
  -> BindingStore
  -> internal reinjection with original channel metadata
  -> shared AgentSession gateway pipeline
  -> outbound bus event
  -> delivery policy and ChannelManager
  -> channel provider
```

## Startup and configuration

The frontend edits integration configuration and can enable or disable a channel. `ensure_gateway_infra()` is idempotent. It hydrates persisted bindings and starts the gateway workers before the selected channel starts.

At application restore, the lifecycle path starts gateway infrastructure only when configuration contains an enabled channel. `GatewayService` owns the channel manager and the inbound and outbound processors. It registers enabled channels and spawns their workers.

The gateway model and account are explicit integration settings. A channel session uses the personal workspace and a registered agent session. Project or SDE routing can override the workspace only when the persisted session already carries that context.

## Conversation identity and binding

`BindingStore` maps an external conversation key to one ORG2 session. The key includes channel and chat identity and can include sender identity where the channel needs it.

```text
(channel, chat_id[, sender_id]) <-> session_id
```

The store loads bindings from the database at startup. Reads use the in-memory map on the hot path. A set or clear updates both memory and persistence.

The binding is routing state, not the conversation transcript. Session events remain under the normal session owner.

## Inbound route

1. A provider adapter creates an inbound channel message.
2. The gateway detects slash commands before ordinary agent dispatch.
3. Idle-reset policy can retire the old session before message delivery.
4. The dispatcher resolves an existing binding or creates a per-chat OS session.
5. Reinjection creates an internal inbound message and preserves the original channel, chat, message, and sender metadata.
6. Dispatch resolves the configured gateway model and account.
7. Tool contexts receive the original channel, chat, and sender values.
8. The message enters `session::gateway_pipeline::process_gateway_message`.

Reinjection is a deliberate seam. Internal processing can use the common message pipeline, but the dispatcher rewrites the original channel metadata before delivery. The outbound path therefore does not reply to the synthetic `gateway-reinject` transport.

## Commands and resets

The gateway handles `/new` and `/reset`, `/status`, `/model`, `/compact`, `/help`, and `/commands`. Slash-command replies publish through the outbound bus so they use normal channel delivery.

Idle reset follows conservative rules:

- no reset occurs while the session has an active turn;
- no reset occurs while an active child session exists;
- a database or activity-query failure counts as active;
- reset archives the old session on a best-effort basis;
- reset invalidates the runtime and clears the binding;
- the next inbound message creates the replacement session lazily;
- a pending reset notice joins the next reply or publishes alone when no agent reply exists.

The session ID uses a version after reset. If the version lookup fails, the code falls back to version 1 and logs the collision risk.

## Outbound route

The outbound worker subscribes to the application event bus. It ignores internal Tauri and automation events. It extracts media and sends the message through the channel manager with the delivery wrapper.

Delivery can strip unsupported Markdown, split long messages, retry transient failures, redact context, and send media. An empty text message is dropped unless it includes media. Provider-specific adapters own authentication and transport behavior.

## Trust and privacy boundaries

| Boundary | Variable input | Control |
| --- | --- | --- |
| Provider to gateway | Chat, sender, message, attachment, and provider event shape | Provider codec and channel adapter normalize it. |
| Gateway to agent | External text and channel identity | Access policy, session binding, context construction, and shared agent tool policy apply. |
| Identity context to prompt/tool | Chat and sender identifiers | Context-header code redacts sensitive values before use. |
| Agent output to provider | Rich text, media, size, and transient errors | Delivery wrapper strips, splits, retries, and validates nonempty output. |
| Stored integration settings | Credentials, model, and account | Channel configuration and the normal credential owners apply. |

A binding proves routing continuity. It does not prove that two external senders are the same human across channels.

## Failure behavior

| Failure | Response |
| --- | --- |
| Gateway startup or registration fails | The enable or restore path returns/logs the channel failure; it does not imply an active route. |
| Binding is missing | Ordinary inbound dispatch creates a session and persists a new binding. |
| Binding database lookup fails during reset checks | The path keeps the current session because it assumes activity. |
| Session version lookup fails | The path logs a warning and uses version 1. |
| Agent dispatch fails | The gateway can publish an error response through the outbound route. |
| Channel send fails | Delivery retry handles eligible failures; the provider error remains visible after the retry budget. |
| Process restarts | Enabled-channel restore restarts workers and the binding store reloads persisted routes. |

## Seams and tradeoffs

| Choice | Benefit | Cost or limit |
| --- | --- | --- |
| Reuse the shared session pipeline | Channel agents receive the same provider, tool, policy, and event behavior as local sessions. | Transport metadata must survive reinjection and return routing. |
| Keep hot bindings in memory and database | Routing avoids a database read for every message and survives restart. | Every mutation must keep the two views consistent. |
| Create one session per conversation key | Context remains stable across messages. | Group and sender semantics depend on each provider's key design. |
| Mint replacement sessions lazily | Reset avoids unused session creation. | The reset notice needs separate pending state. |
| Assume activity on reset-query failure | A transient database error cannot destroy an active conversation. | An idle session can remain bound longer than requested. |
| Use an outbound event bus | Commands and agent results share delivery. | Producers must retain correct channel metadata and filter internal events. |

## Source map

| Concern | Current source |
| --- | --- |
| Gateway composition and workers | [`src-tauri/crates/agent-core/src/integrations/gateway/service.rs`](src-tauri/crates/agent-core/src/integrations/gateway/service.rs), [`src-tauri/crates/agent-core/src/integrations/gateway/workers.rs`](src-tauri/crates/agent-core/src/integrations/gateway/workers.rs) |
| Conversation bindings | [`src-tauri/crates/agent-core/src/integrations/gateway/binding.rs`](src-tauri/crates/agent-core/src/integrations/gateway/binding.rs) |
| Slash-command model | [`src-tauri/crates/agent-core/src/integrations/gateway/commands.rs`](src-tauri/crates/agent-core/src/integrations/gateway/commands.rs), [`src-tauri/crates/agent-core/src/state/commands/channel_handler/slash.rs`](src-tauri/crates/agent-core/src/state/commands/channel_handler/slash.rs) |
| Startup and channel session creation | [`src-tauri/crates/agent-core/src/state/commands/channel_handler/lifecycle.rs`](src-tauri/crates/agent-core/src/state/commands/channel_handler/lifecycle.rs) |
| Inbound dispatch and reinjection | [`src-tauri/crates/agent-core/src/state/commands/channel_handler/dispatch.rs`](src-tauri/crates/agent-core/src/state/commands/channel_handler/dispatch.rs) |
| Idle reset | [`src-tauri/crates/agent-core/src/state/commands/channel_handler/idle_reset.rs`](src-tauri/crates/agent-core/src/state/commands/channel_handler/idle_reset.rs) |
| Channel manager and delivery | [`src-tauri/crates/agent-core/src/integrations/channels/manager.rs`](src-tauri/crates/agent-core/src/integrations/channels/manager.rs), [`src-tauri/crates/agent-core/src/integrations/channels/delivery/`](src-tauri/crates/agent-core/src/integrations/channels/delivery/) |
| Channel providers and configuration | [`src-tauri/crates/agent-core/src/integrations/channels/`](src-tauri/crates/agent-core/src/integrations/channels/), [`src-tauri/crates/agent-core/src/integrations/channels/config/`](src-tauri/crates/agent-core/src/integrations/channels/config/) |

## Known limits

This record did not connect to a live Telegram, Discord, Feishu, WeCom, or Weixin account. Provider-specific rate limits and delivery guarantees remain outside this source-only analysis.

