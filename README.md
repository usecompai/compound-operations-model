# The Compound Operations Model

An open, source-available AI operations blueprint for consumer SMEs, published by Compai.

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-c9a667.svg)](LICENSE)
[![Built in public](https://img.shields.io/badge/built-in%20public-1a1a1a.svg)](https://usecompai.com)
[![Playbook](https://img.shields.io/badge/playbook-72%20chapters-1a1a1a.svg)](https://usecompai.com/playbook)
[![Release audit](https://github.com/usecompai/compound-operations-model/actions/workflows/parity.yml/badge.svg)](.github/workflows/parity.yml)

> **Give your company a brain it can operate through.** Compai connects company knowledge, live systems, people and AI runtimes through one governed operating layer. Read the method, inspect the evidence and adapt the kit.

This repository documents a real operating system: a Company Brain, authenticated tools, domain agents, governed skills, source coverage, action receipts and bounded execution. The new Codex-first path makes that architecture easier to reproduce while keeping memory, permissions and operational state outside any one model. It is an educational implementation portfolio and source-available starter kit, not a hosted SaaS product.

## Current Release

**v6.2 - Codex-First Bootstrap - 15 September 2026**

This release adds a practical Codex-first route for building the same governed operating layer. Start with one workflow and one read-only source, approve each phase, then expand only when the evidence and controls hold. Codex is one builder and operating surface; the Company Brain, identity, permissions, capability state and receipts remain model-independent.

| Surface | Verified public snapshot |
|---|---:|
| Core capability registry | 45/55 ready; 4 degraded; 4 awaiting configuration; 1 blocked dependency; 1 configured but unverified |
| Brain lexical retrieval | ready |
| Context Compiler | degraded, with incomplete states exposed |
| Production domain agents online | 7/7 |
| Public, anonymized skills in this repo | 31 |
| Authenticated MCP | ready; caller identity verified |
| Governed business loops | 3, proposal/shadow only |
| Automated company-source ingestion | degraded at audit time |
| Full offsite restore | passed in isolation; one inherited ledger warning remains |

Capabilities, MCP and agents were checked on 15 September 2026. The isolated full-restore drill ran on 9 September 2026. These are dated results, not live telemetry. [`release-manifest.json`](release-manifest.json) is the machine-readable source.

## What Changed In v6.2

- Added a Spanish Codex-first implementation guide and a phase-gated discovery prompt that can be used without exposing company data.
- Made one workflow, one read-only source and explicit human approval the default bootstrap path.
- Updated the Codex integration for current `AGENTS.md`, cloud-environment, skill and authenticated MCP conventions.
- Expanded the public truth contract beyond `deployed`, `pilot` and `pattern` so degraded, blocked, stale, planned and deprecated states can be reported honestly.
- Replaced the stale all-ready headline with the current registry distribution and a verified recovery-drill result.

## What Is Actually Proven

The reference deployment has permission-aware retrieval, authenticated source-system access, 45 ready core capabilities out of 55, private workspaces, governed publishing and seven online domain agents. Read-only retrieval and low-risk analysis can run automatically. Customer-facing, financial, legal, HR, destructive and other consequential actions remain bounded by identity, scope, policy, verification and explicit approval.

The system is useful, but it is not broadly autonomous. Three business loops have contracts and shadow/proposal paths, but they do not yet have closed Outcome Receipts proving repeatable business impact. Company-source ingestion and the Context Compiler were degraded at the 15 September boundary even though Brain retrieval, MCP access and production agents were healthy. Those states remain visible until their gates pass again.

No single company-wide autonomy percentage is claimed. Autonomy is granted per capability, and confidence never grants authority.

## What Is Inside

| Path | Contents |
|---|---|
| `chapters/` | 72 source chapters organized as an eight-section SME journey |
| `guides/` | 2 Spanish Codex-first guides: implementation method and copy-ready bootstrap prompt |
| `kit/` | v6.2 implementation kit with runtime, context, capability, governance, evaluation, storage and evidence contracts |
| `skills/` | 31 anonymized public skills plus a catalog explaining how skills differ from verified capabilities |
| `pattern-library/` | 21 executable pattern definitions plus schema and documentation |
| `case-study/` | Anonymized, evidence-first reference case study |
| `release-manifest.json` | Dated public truth contract for the reference deployment |
| `scripts/release_audit.py` | Release parity, anonymity, count, stale-claim and archive-integrity gate |

The source for `usecompai.com` is maintained separately because it contains deployment and lead-delivery configuration. The website demonstrates the same public-safe capabilities, but its source code is not part of this package.

## Start Here

1. If you are building with Codex, start with [`guides/company-brain-with-codex.es.md`](guides/company-brain-with-codex.es.md) and its [`phase-gated bootstrap prompt`](guides/codex-company-brain-bootstrap-prompt.es.md).
2. Read [`chapters/00-index.md`](chapters/00-index.md).
3. Read [`chapters/23-operating-layer.md`](chapters/23-operating-layer.md).
4. Read [`chapters/24-context-compiler.md`](chapters/24-context-compiler.md).
5. Read [`chapters/25-capability-registry.md`](chapters/25-capability-registry.md).
6. Read [`chapters/26-human-work-mode.md`](chapters/26-human-work-mode.md).
7. Read [`chapters/28-decision-packs-outcome-receipts.md`](chapters/28-decision-packs-outcome-receipts.md).
8. Inspect [`kit/README.md`](kit/README.md), then run the release audit before adapting the assets.

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
