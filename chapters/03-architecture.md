# Chapter 3: The Architecture — How a Multi-Agent System Actually Works

## Why One Agent Isn't Enough

The first mistake everyone makes: "I'll just set up one AI agent and have it do everything."

That's like hiring one person to do CS, accounting, marketing, inventory management, and wholesale sales. Even if they were brilliant, they'd be context-switching constantly and doing everything poorly.

The architecture that works is **specialized agents with a shared brain.**

## The Multi-Agent Architecture

```
                    ┌─────────────────────────────┐
                    │   🧠 STRATEGY AGENT (Central Hub)    │
                    │   Strategy + Orchestration    │
                    │   Cloud VPS (EU)       │
                    └───────────┬─────────────────┘
                                │ Tailscale Mesh
        ┌───────────┬───────────┼───────────┬───────────────┐
        │           │           │           │               │
   ┌────▼────┐ ┌────▼────┐ ┌────▼────┐ ┌────▼────┐ ┌───────▼───────┐
   │ CS Agent │ │ Finance Agent │ │ Retail Agent │ │Marketing│ │ Merchandising Agent       │
   │   CS    │ │ Finance │ │ Retail  │ │Digital  │ │Merchandising  │
   │         │ │         │ │         │ │Marketing│ │& Wholesale    │
   └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └───────┬───────┘
        │           │           │           │               │
        └───────────┴───────────┴───────────┴───────────────┘
                         Mac Mini (secondary host)
                    ┌─────────────────────────────┐
                    │     SHARED BRAIN (5,235 docs)    │
                    │   rsync ↔ every 30 minutes    │
                    │   + MCP Server (98 tools)     │
                    └─────────────────────────────┘
```

**The production topology:** Strategy Agent (hub/strategy) runs on a cloud VPS in the EU. The domain agents run on a dedicated secondary host. All connected through an encrypted private network. A shared brain syncs bidirectionally every 30 minutes. This is the reference deployment, not a requirement; the technical appendix shows the host-specific setup.

## Design Principles

### 1. Each Agent Has a Clear Domain

Every agent owns a specific area of the business. This means:
- **Clear responsibility:** If something goes wrong with inventory, you know which agent to look at
- **Focused context:** The CS agent doesn't need to know about wholesale pricing formulas
- **Independent scaling:** You can run the CS agent on a beefier model (Opus) while the reporting agent runs on a cheaper one (Sonnet/Flash)

### 2. Agents Communicate Through the Hub

In the ideal architecture, agents communicate through a central orchestrator — this prevents chaos and creates an audit trail. In practice, the coordination often flows through team messaging channels (Slack, WhatsApp) where both agents and humans participate. The key is that every cross-domain request is logged and traceable, whether it routes through the hub directly or through a shared channel.

Example flow:
1. **CS Agent** receives complaint: "My order hasn't arrived"
2. CS Agent checks Shopify order status → sees it's marked "fulfilled"
3. CS Agent escalates to **Ops Agent** via hub: "Order #4521 marked fulfilled but customer says not received"
4. **Ops Agent** checks 3PL tracking → finds package stuck in customs
5. Ops Agent responds to hub with status update
6. Hub routes back to **CS Agent** with full context
7. CS Agent drafts customer response with accurate tracking info and ETA

This can happen in seconds. Whether a human is required depends on the action's authority class, not just the model's confidence. A grounded stock lookup can run automatically; a refund, payment, legal commitment, or customer-facing exception remains bounded by policy and approval.

### 3. Shared Knowledge, Separate Personalities

All agents share:
- **Catalog data** (products, descriptions, pricing, inventory, bundles, subscriptions, warranties)
- **Brand voice guidelines** (tone, vocabulary, do's and don'ts)
- **Customer history** (past orders, past issues, lifetime value)
- **Business rules** (return policy, shipping times, discount limits)

But each agent has its own:
- **SOUL.md** — personality, expertise, communication style
- **Tools** — only the integrations it needs
- **Decision thresholds** — when to act autonomously vs. escalate to human

### 4. Authority Is Capability-Specific

There is no honest company-wide "autonomy percentage." Autonomy is granted per capability after the evidence exists to support it:

| Capability class | Default authority | Promotion evidence |
|------------------|-------------------|--------------------|
| Read and retrieve | Execute | Source access, citations, freshness checks |
| Analyse and recommend | Execute with receipt | Reproducible inputs and validation rules |
| Draft internal or external work | Propose | Human review until a sampled quality gate passes |
| Change operational systems | Human-gated | Explicit scope, rollback, idempotency, audit receipt |
| Money, legal, HR, destructive actions | Human approval | Named approver; no confidence-only bypass |

The current reference deployment is strong at capture, retrieval, analysis, and on-demand tool execution. Broad unattended execution is deliberately a controlled pilot. The next promotion gate is ten reviewed closure-first runs with at least 80% verified completion and no authority violations.

### 5. Everything is Logged and Auditable

Every agent action is logged:
- What decision was made
- What data was used
- What confidence level was assigned
- Whether a human reviewed it
- What the outcome was

This isn't just good practice — it's a GDPR requirement if you're operating in Europe, and it's how the system learns and improves.

## The Technology Stack

At the core, the reference system runs on **OpenClaw** — an open-source AI agent framework that connects LLMs to real-world actions. You can fork the repo and swap this layer if another runtime fits your team better.

| Component | What We Use | Why |
|-----------|------------|-----|
| **Agent Runtime** | OpenClaw | Open source, local-first, 50+ integrations, active community |
| **Primary LLM** | Frontier model selected by role | Models change faster than the architecture; route by task quality, latency, privacy, and cost |
| **Secondary LLMs** | Provider fallbacks + coding and research runtimes | Resilience and specialization without coupling the brain to one vendor |
| **Hosting** | Dedicated server (Hetzner) | €40/mo, full control, EU data residency |
| **Agent-to-Agent** | ACP (Agent Communication Protocol) | Native cross-agent coordination |
| **Messaging** | WhatsApp, Slack, Email | Meet teams where they already work |
| **Memory** | Local files + structured knowledge base | No vendor lock-in, full data ownership |
| **Monitoring** | Built-in heartbeats + cron jobs | Self-healing, auto-restart |
| **ERP / Accounting** | the accounting system | Invoicing, payment reconciliation, ledger |
| **Expense Management** | the expense platform | Corporate cards, expense tracking, bank statements |
| **Knowledge Base** | Notion + Brain Context Tree | 5,235 docs organized by domain and indexed at the release boundary |
| **Social Listening** | Agent-Reach + bird CLI | Twitter/X monitoring, multi-platform scanning |
| **Semantic Search** | Exa | Better than Google for competitive research |
| **Image Generation** | Krea AI | Product shots, creative assets |
| **Power-User Layer** | Claude Code + MCP | Founder's direct interface — 98 tools, slash commands, subagents |

**Total system cost:** €631/month all-in (infrastructure + LLM access + subscriptions). See Ch.12 for the complete cost breakdown.

The current two-layer ROI model produces a 16.2:1 ratio under the documented assumptions. Chapter 12 separates hard savings from strategic capacity so readers can replace every input with their own numbers.

## What You Need to Get Started

**Minimum viable setup (1 agent):**
- A Linux server or VPS (€20-40/month)
- An LLM API key (Anthropic, OpenAI, or similar)
- OpenClaw installed and configured
- One channel connection (Slack, WhatsApp, email, helpdesk, or team chat)
- 2-4 hours for initial setup

**Full reference deployment (7 agent runtimes + founder command center):**
- VPS (€15/month) + Mac Mini as secondary compute (~€22/month amortized)
- Approved provider routes for each task class, plus an independently tested second-provider fallback
- All channel connections configured
- Integrations with your existing tools (Shopify, Klaviyo, etc.)
- 2-4 weeks for full implementation and tuning
- A second compute node (Mac Mini, NUC, VPS, or equivalent) for agent isolation

> **A note on agent roles:** The current reference deployment has seven production agent runtimes plus a founder-facing command center. Roles cover strategy/orchestration and the operating domains that warrant dedicated context. Your count should follow accountability boundaries, not a marketing target: start with the domains that hurt most, then split or merge as the evidence demands.

### 6. Confidence Is Evidence, Not Authority

Agents may report confidence, but confidence never grants permission by itself. The execution policy combines four independent checks:

1. **Identity:** which human or machine is calling.
2. **Scope:** which data and tools that identity may reach.
3. **Capability:** read, propose, execute, or administer.
4. **Risk:** reversible vs. irreversible, and internal vs. external impact.

A high-confidence answer can still require approval. A deterministic, low-risk lookup can execute even when the model is not the decision-maker at all.

### 7. Audit Logging

Every agent action is logged to a structured JSONL audit trail:

```json
{"timestamp":"2026-03-28T21:21:14+00:00","agent":"cs_agent","action":"cs_ticket_response","confidence":"94%","data":"order_tracking","human_review":false}
```

Logs are retained and rotated under the deployment's data policy. The action ledger is the foundation for replay, quality sampling, incident review, and capability-specific promotion decisions; logging alone does not establish GDPR compliance.

The next eight chapters walk through each agent in detail — what it does, how it's configured, and the specific results it delivers.

---

*Next: [Chapter 4 — Agent #1: Customer Service →](04-agent-cs.md)*
