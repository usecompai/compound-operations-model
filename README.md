# The Compound Operations Model

An open, source-available AI operations blueprint for consumer SMEs, published by Compai.

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-c9a667.svg)](LICENSE)
[![Built in public](https://img.shields.io/badge/built-in%20public-1a1a1a.svg)](https://usecompai.com)
[![Playbook](https://img.shields.io/badge/playbook-72%20chapters-1a1a1a.svg)](https://usecompai.com/playbook)
[![Release audit](https://github.com/usecompai/compound-operations-model/actions/workflows/parity.yml/badge.svg)](.github/workflows/parity.yml)

> **Give your company a brain it can operate through.** Compai connects company knowledge, live systems, people and AI runtimes through one governed operating layer. Read the method, inspect the evidence and adapt the kit.

This repository documents a real operating system: a Company Brain, authenticated tools, domain agents, governed skills, source coverage, action receipts and bounded execution. It is an educational implementation portfolio and source-available starter kit, not a hosted SaaS product.

## Current Release

**v6.0 - Operating Layer - 30 August 2026**

This release catches the public project up with the reference runtime built during August. The central object is no longer presented as a memory store with agents attached. It is a governed company runtime: compiled context, verified capabilities, identity and policy, a run ledger, Decision Packs, Outcome Receipts and human review.

| Surface | Verified public snapshot |
|---|---:|
| Core capabilities ready | 46/46 |
| Lexical retrieval canaries | 20/20 passing |
| Semantic retrieval canaries | 5/5 passing |
| Production domain agents online | 7/7 |
| Public, anonymized skills in this repo | 31 |
| MCP authentication and audience enforcement | `enforce` |
| Governed business loops | 3, proposal/shadow only |
| Automated source synchronization | degraded at audit time |
| Offsite backup and repository check | passing |

Capability readiness was verified on 28 August 2026. Retrieval, agent health, source-sync status and backups were independently checked on 30 August 2026. These are dated results, not live telemetry. [`release-manifest.json`](release-manifest.json) is the machine-readable source.

## What Changed In v6.0

- Added the six contracts of the Company Operating Layer: ContextPack, Capability Registry, policy engine, run ledger, Outcome Receipts and human review.
- Added public schemas for a Company Runtime and permission-aware ContextPack.
- Separated authenticated human work from unattended machine authority. Stable role permissions should not require one-use grants; autonomous external effects remain tightly bounded.
- Added durable workspaces, canonical internal publishing, version history and rollback to the implementation path.
- Added Decision Packs and Outcome Receipts so recommendations can be followed through approval, application and measured impact.
- Replaced July inventory metrics with independently rechecked August evidence and disclosed degraded automated source synchronization at the release boundary.

## What Is Actually Proven

The reference deployment has permission-aware retrieval, authenticated source-system access, verified capabilities, private workspaces, governed publishing and seven online domain agents. Read-only retrieval and low-risk analysis can run automatically. Customer-facing, financial, legal, HR, destructive and other consequential actions remain bounded by identity, scope, policy, verification and explicit approval.

The system is useful, but it is not broadly autonomous. Three business loops have contracts and shadow/proposal paths, but they do not yet have closed Outcome Receipts proving repeatable business impact. Automated Slack, Drive and meeting synchronization was degraded during the 30 August audit even though core retrieval, MCP access and production agents were healthy. This is an operating constraint, not a footnote.

No single company-wide autonomy percentage is claimed. Autonomy is granted per capability, and confidence never grants authority.

## What Is Inside

| Path | Contents |
|---|---|
| `chapters/` | 72 source chapters organized as an eight-section SME journey |
| `kit/` | v6.0 implementation kit with runtime, context, capability, governance, evaluation, storage and evidence contracts |
| `skills/` | 31 anonymized public skills plus a catalog explaining how skills differ from verified capabilities |
| `pattern-library/` | 21 executable pattern definitions plus schema and documentation |
| `case-study/` | Anonymized, evidence-first reference case study |
| `release-manifest.json` | Dated public truth contract for the reference deployment |
| `scripts/release_audit.py` | Release parity, anonymity, count, stale-claim and archive-integrity gate |

The source for `usecompai.com` is maintained separately because it contains deployment and lead-delivery configuration. The website demonstrates the same public-safe capabilities, but its source code is not part of this package.

## Start Here

1. Read [`chapters/00-index.md`](chapters/00-index.md).
2. Read [`chapters/23-operating-layer.md`](chapters/23-operating-layer.md).
3. Read [`chapters/24-context-compiler.md`](chapters/24-context-compiler.md).
4. Read [`chapters/25-capability-registry.md`](chapters/25-capability-registry.md).
5. Read [`chapters/26-human-work-mode.md`](chapters/26-human-work-mode.md).
6. Read [`chapters/28-decision-packs-outcome-receipts.md`](chapters/28-decision-packs-outcome-receipts.md).
7. Inspect [`kit/README.md`](kit/README.md), then run the release audit before adapting the assets.

```bash
python3 scripts/release_audit.py --repo-root .
```

## Operating Model

1. **Sources** - company knowledge and live operational systems.
2. **Context compiler** - the minimum sourced, permission-aware context for one job.
3. **Capability Registry** - the reads, analyses, drafts and actions that work now.
4. **Identity and policy** - who may use each capability and where approval begins.
5. **Models and agents** - interchangeable workers operating above those contracts.
6. **Run and outcome ledger** - observe, act within authority, verify, record the result, then stop or escalate.

The important shift is bidirectionality with proof. Agents do not only read the Brain; they write decisions, gotchas, outputs and receipts back into it. An action without verification is activity, not completed work.

## Version Lineage

The first public release was developed internally under the OperAI working name. The product and public project are now Compai. Legacy URLs redirect for compatibility, while current code, service names, templates and documentation use Compai.

Earlier ROI and autonomy language remains bounded. Chapter 12 contains a replaceable model, not audited realized value. The reference business loops remain proposal/shadow systems until closed Outcome Receipts support promotion.

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
