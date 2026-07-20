# The Compound Operations Model

An open, source-available AI operations blueprint for consumer SMEs, published by Compai.

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-c9a667.svg)](LICENSE)
[![Built in public](https://img.shields.io/badge/built-in%20public-1a1a1a.svg)](https://usecompai.com)
[![Playbook](https://img.shields.io/badge/playbook-66%20chapters-1a1a1a.svg)](https://usecompai.com/playbook)
[![Release audit](https://github.com/usecompai/compound-operations-model/actions/workflows/parity.yml/badge.svg)](.github/workflows/parity.yml)

> **The operating layer behind an 8-figure consumer company running a Company Brain for an internal operating cost of EUR631/month.** This is not the price of Compai or an implementation quote. Read the method, inspect the evidence and adapt the kit.

This repository documents a real operating system: a Company Brain, authenticated tools, domain agents, governed skills, source coverage, action receipts and bounded execution. It is an educational implementation portfolio and source-available starter kit, not a hosted SaaS product.

## Current Release

**v5.1 - Runtime Truth - 20 July 2026**

This release refreshes the public evidence boundary after a deep runtime due diligence. It also removes unsupported legacy case-study claims, documents the current operating limits and adds stronger release gates against stale metrics and placeholder content.

| Surface | Verified public snapshot |
|---|---:|
| Brain documents indexed | 5,235 |
| Embedding vectors | 24,469 |
| Current embedding backlog | 112 pending |
| Skills available to the swarm | 374 |
| Company-governed canonical skills | 48 |
| Canonical skills with a recorded evaluation | 46 |
| Public, anonymized skills in this repo | 31 |
| Authenticated MCP tools | 98 |
| Production agent runtimes | 7 + founder command center |
| Connector smoke tests | 14/14 green + independent Google Workspace mail check |
| Recorded action receipts | 46,221 |
| MCP authentication | `enforce` |
| Dated Brain maturity assessment | 6.6/10 |

These figures were verified on 20 July 2026. They are a dated release snapshot, not live telemetry. [`release-manifest.json`](release-manifest.json) is the machine-readable source.

## What Changed In v5.1

- Refreshed Brain, skill, tool, connector and receipt inventories from the live reference runtime.
- Added the latest path-confinement, provider-recovery and health-monitoring controls to the public operating lessons.
- Replaced the old case study, which mixed projections and unsupported outcomes, with a dated evidence-first account.
- Made current limitations explicit: one degraded team channel, single-node concentration for several runtimes, a non-zero retrieval backlog and low broad autonomy.
- Clarified that the public website is deployed from a separate private delivery workspace; this repository contains the portable operating model, playbook, kit, skills and patterns.
- Extended the release audit to reject the superseded v5.0 metrics and placeholder contact details.

## What Is Actually Proven

The reference deployment has broad capture and retrieval, authenticated source-system access, on-demand tool execution, governed procedures and a substantial action ledger. Read-only retrieval and low-risk analysis can run automatically. Customer-facing, financial, legal, HR, destructive and other consequential actions remain bounded by identity, scope, policy, verification and explicit approval.

The system is useful, but it is not highly available or broadly autonomous. Several runtimes and semantic retrieval still share one physical node, one team channel was degraded at the release boundary, runtime backup coverage remains incomplete and 112 documents were waiting for embeddings. These are operating constraints, not footnotes.

No single company-wide autonomy percentage is claimed. Autonomy is granted per capability, and confidence never grants authority.

## What Is Inside

| Path | Contents |
|---|---|
| `chapters/` | 66 source chapters organized as an eight-section SME journey |
| `kit/` | v5.1 implementation kit with deployment, governance, evaluation, identity, storage and evidence templates |
| `skills/` | 31 anonymized public skills plus a catalog explaining the wider 374-skill capability layer |
| `pattern-library/` | 21 executable pattern definitions plus schema and documentation |
| `case-study/` | Anonymized, evidence-first reference case study |
| `release-manifest.json` | Dated public truth contract for the reference deployment |
| `scripts/release_audit.py` | Release parity, anonymity, count, stale-claim and archive-integrity gate |

The source for `usecompai.com` is maintained separately because it contains deployment and lead-delivery configuration. The website demonstrates the same public-safe capabilities, but its source code is not part of this package.

## Start Here

1. Read [`chapters/00-index.md`](chapters/00-index.md).
2. Read [`chapters/10aa-truth-and-evidence.md`](chapters/10aa-truth-and-evidence.md).
3. Read [`chapters/10ab-architecture-contract.md`](chapters/10ab-architecture-contract.md).
4. Read [`chapters/10ac-skill-governance.md`](chapters/10ac-skill-governance.md).
5. Read [`chapters/10ad-closure-first-execution.md`](chapters/10ad-closure-first-execution.md).
6. Inspect [`kit/README.md`](kit/README.md), then run the release audit before adapting the assets.

```bash
python3 scripts/release_audit.py --repo-root .
```

## Operating Model

1. **Brain** - sourced company memory, world model, tasks, outputs, health and artifact references.
2. **Tools** - authenticated MCP interfaces to operational systems.
3. **Agents** - domain-specific runtimes with independent identity and explicit authority.
4. **Skills** - governed procedures promoted through contracts, independent evaluation and evidence.
5. **Closure loop** - observe, act within authority, verify, record a receipt, then stop or escalate.

The important shift is bidirectionality with proof. Agents do not only read the Brain; they write decisions, gotchas, outputs and receipts back into it. An action without verification is activity, not completed work.

## Version Lineage

The first public release was developed internally under the OperAI working name. The product and public project are now Compai. Legacy URLs redirect for compatibility, while current code, service names, templates and documentation use Compai.

Earlier ROI and autonomy language has also been corrected. The current public ROI model is 16.2:1 under the assumptions in Chapter 12, with hard savings separated from strategic capacity. It is a model, not audited realized value. Replace every input with your own before making an investment decision.

## What Not To Copy Blindly

Never copy a reference deployment's private data, credentials, employee names, channels, accounts, HR records, customer records or source-system tokens.

Copy the contracts:

- dated claims with an evidence class
- source references on durable facts
- one identity per human and machine
- scoped authority and privacy hard stops
- independent skill evaluation
- reversible changes and explicit rollback
- action receipts and source coverage
- known gaps published next to strengths

## Live Site

- Product, Live demo and evidence: https://usecompai.com
- Contact: hello@usecompai.com

## Community

Fork it, test it against your own operating reality and publish what changed.

- [Share a deployment](https://github.com/usecompai/compound-operations-model/issues/new?template=share-what-you-built.md)
- [Ask a question](https://github.com/usecompai/compound-operations-model/issues/new?template=question.md)
- [Report a bug](https://github.com/usecompai/compound-operations-model/issues/new?template=bug-report.md)
- Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md)

## License

The repository is source-available under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International. You may inspect, share and adapt it under the terms in [`LICENSE`](LICENSE). The NonCommercial restriction means it should not be described as OSI-approved open source.

Commercial usage or implementation help: hello@usecompai.com.
