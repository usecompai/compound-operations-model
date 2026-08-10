# Reference Architecture

## Canonical Topology

Compai is packaged as a model-agnostic company operating layer. Domain agents and Claude, Codex or other model clients consume the same governed capabilities.

- Strategy hub
- Customer service
- Finance
- Retail
- Marketing
- Merchandising
- HR / people ops
- founder command center

## Hosting Pattern

### Primary host
- Linux VPS
- shared brain
- MCP server
- cron layer
- strategy hub / orchestration

### Secondary host
- optional but recommended
- domain agents with isolation
- local services requiring dedicated runtime or session handling

## MCP Transport

- Default: Streamable HTTP
- Legacy fallback: SSE only where compatibility is still required temporarily
- Public endpoint should be stable and documented before onboarding users

## Data Flow Principle

Each system remains source of truth in its own domain.

Agents do not replace Shopify, ERP, analytics, or helpdesk. They orchestrate across them.

The Brain is operational memory: context, entities, decisions, procedures and receipts. It is not a silent cache of current operational truth.

## Required Layers

### Execution layer
- agent runtime
- cron schedules
- watchdog / health checks
- audit logging

### Capability layer
- explicit source of truth, inputs and outputs
- read, write and approval boundaries
- owner, sensitivity and freshness SLA
- harmless smoke test and runtime readiness state
- a skill is discoverable procedure, not proof that a capability is available

### Decision and outcome layer
- schema-validated decision packs
- applied-action receipts linked to approval
- business metrics, baselines, guardrails and observation windows
- outcome receipts that distinguish causal, observational and not-measurable results

### Memory layer
- shared brain
- context tree / indexes
- session-to-knowledge distillation
- human-readable operating docs

### Interface layer
- Claude, Codex or another compatible model client for power users
- Slack / email / helpdesk where the team already works
- optional employee AI clients if you standardize them

## Security Defaults

- least privilege per agent
- write actions only where required
- explicit human approval for consequential actions
- hard escalation rules
- public telemetry must be governed and anonymized

## Deployment Goal

By day 30 you should have a working operating surface with verified capabilities and measured loops, not a pile of prompts.
