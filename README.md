# The Compound Operations Model

Open-source AI operations playbook for consumer SMEs, published by Compai.

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-c9a667.svg)](LICENSE)
[![Built in public](https://img.shields.io/badge/built-in%20public-1a1a1a.svg)](https://usecompai.com)
[![Playbook](https://img.shields.io/badge/playbook-66%20chapters-1a1a1a.svg)](https://usecompai.com/playbook)
[![Release audit](https://github.com/usecompai/compound-operations-model/actions/workflows/parity.yml/badge.svg)](.github/workflows/parity.yml)

> **The operating system pattern behind an 8-figure consumer brand running AI in production for EUR631/month.** Read it. Fork it. Build your own.

This repository documents a real operating system: a company Brain, authenticated tools, domain agents, governed skills, source coverage, action receipts, and bounded execution. It is an educational implementation portfolio, not a hosted SaaS product.

## Current Release

**v5.0 - Truth & Execution - 12 July 2026**

This release brings the public portfolio back into parity with the current reference deployment and adds a machine-checked evidence contract.

| Surface | Verified public snapshot |
|---|---:|
| Brain documents | 4,819 |
| Skills available to the swarm | 373 |
| Company-authored canonical skills | 47 |
| Public, anonymized skills in this repo | 31 |
| MCP tools | 97 |
| Production agent runtimes | 7 + founder command center |
| Connector smoke tests | 15 green |
| Action receipts | 42,000+ |
| MCP authentication | `enforce` |

These figures are a dated snapshot, not a promise that every surface updates continuously. [`release-manifest.json`](release-manifest.json) is the machine-readable source for this release.

## What Is Actually Proven

The reference deployment has broad capture and retrieval, source-system access, on-demand tool execution, and a substantial action ledger. It does **not** claim a single company-wide autonomy percentage.

Autonomy is granted per capability. Read-only retrieval and low-risk analysis can run automatically; customer-facing, financial, legal, HR, destructive, and other consequential actions remain bounded by identity, scope, policy, verification, and explicit approval. Broad unattended execution is a controlled closure-first pilot, not a production-wide claim.

Known coverage gaps stay visible. Generated meeting notes are covered, but the native transcript inventory is currently zero. Granola coverage is incomplete. Fine-grained Brain Spaces retrieval scoping is rolling out domain by domain even though per-identity MCP authentication is already enforced.

## What Is Inside

| Path | Contents |
|---|---|
| `chapters/` | 66 source chapters organized as an eight-section SME journey |
| `kit/` | v5.0 implementation kit with deployment, governance, eval, identity, storage and evidence templates |
| `skills/` | 31 anonymized public skills plus a catalog explaining the wider 373-skill capability layer |
| `pattern-library/` | 21 executable pattern definitions plus schema and documentation |
| `case-study/` | Anonymized reference case study |
| `scripts/release_audit.py` | Release parity, anonymity, count and archive-integrity gate |

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

Earlier ROI and autonomy language has also been corrected. The current public model is 16.2:1 under the assumptions in Chapter 12, with hard savings separated from strategic capacity. Replace those inputs with your own before making an investment decision.

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

- Playbook and evidence dashboard: https://usecompai.com
- Contact: hello@usecompai.com

## Community

Fork it, test it against your own operating reality, and publish what changed.

- [Share a deployment](../../issues/new?template=share-what-you-built.md)
- [Ask a question](../../issues/new?template=question.md)
- [Report a bug](../../issues/new?template=bug-report.md)
- Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md)

## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International. See [`LICENSE`](LICENSE).

Commercial usage or implementation help: hello@usecompai.com.
