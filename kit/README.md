# Compai Implementation Kit v6.2

This kit is the portable asset layer behind the Compai playbook. It turns the architecture into templates, scripts, eval fixtures and deployment contracts that a technical operator can inspect and adapt.

It is not a hosted service, a compliance certification or a promise that every connector is production-ready in every environment. Run it first in an isolated pilot, replace the example values, and review consequential data flows with the appropriate security, privacy and legal owners.

## Operating layer contracts

- Capability Registry contract with source, inputs, outputs, permissions, freshness, owner and smoke-test state.
- Decision Pack and Outcome Receipt schemas for business-loop evaluation.
- Loop v0.2 template with explicit capability dependencies, business metrics, observation windows and promotion gates.
- Model adapters cannot change source-of-truth selection, permissions or authority.
- ContextPack and Company Runtime schemas for permission-aware context compilation.
- Separate authority contracts for authenticated human work and unattended runtimes.
- Durable workspace, governed publishing and rollback requirements.

## Release Contract

Version 6.2 adds a Codex-first build path and explicit degraded or blocked truth states while retaining the complete operating layer introduced in v6.0:

- `templates/configs/public-truth-manifest.schema.json` - dated claims, evidence classes and known gaps
- `templates/configs/source-coverage.yml` - source, account and artifact-type coverage matrix
- `templates/configs/architecture-contract.md` - runtime identity, workspace and change-control invariants
- `templates/configs/skill-evaluation.yml` - builder/judge separation and promotion evidence
- `templates/configs/approved-task.yml` - bounded closure-first execution object
- `templates/configs/artifact-storage.yml` - durable artifact ownership and retention
- `templates/configs/loop.yml` - observe, choose, act, verify, record and stop
- `templates/configs/governance.yml` - read, propose, execute and administer authority
- `templates/configs/audit-event.schema.json` - machine-readable execution receipt
- `templates/configs/context-pack.schema.json` - the minimum sourced context for one identity and job
- `templates/configs/company-runtime.schema.json` - the complete operating-layer contract
- `templates/configs/capability-registry.schema.json` - capabilities that are usable now, not merely documented
- `templates/configs/decision-pack.schema.json` - evidence and authority contract for a proposed decision
- `templates/configs/outcome-receipt.schema.json` - measured result after an approved action

## Contents

| Path | Purpose |
|---|---|
| `deployment/` | Prerequisites, reference architecture, activation path and 30-day rollout |
| `init/` | Bootstrap CLI, agent runner, MCP template, onboarding and compliance scaffolds |
| `templates/configs/` | Truth, coverage, identity, authority, storage, loop and receipt contracts |
| `templates/souls/` | Portable role prompts for seven agent domains |
| `scripts/` | Example monitors, operational utilities and audit logging |
| `evals/` | Negative fixtures for stale sources, wrong accounts, empty artifacts and missing approval |
| `integrations/` | Client integration notes |
| `memory-architecture/` | Shared-memory scaffolding and synchronization examples |
| `knowledge-base/` | Security, privacy, AI governance and operating templates |
| `patterns/` | Minimal runtime examples |

## Recommended Path

1. For a Codex-first build, read [`../guides/company-brain-with-codex.es.md`](../guides/company-brain-with-codex.es.md) and use its [`phase-gated bootstrap prompt`](../guides/codex-company-brain-bootstrap-prompt.es.md).
2. Read `deployment/prerequisites.md`.
3. Fill `templates/configs/architecture-contract.md` before installing a runtime.
4. Inventory sources in `templates/configs/source-coverage.yml`.
5. Complete `deployment/deployment-contract.md` and `deployment/activation-path.md`.
6. Compile one ContextPack for a real job and expose conflicts or missing evidence.
7. Mark only smoke-tested dependencies as `ready` in the Capability Registry.
8. Start with one domain agent in propose-only mode.
9. Run the negative eval fixtures.
10. Approve one task with `templates/configs/approved-task.yml`.
11. Require a valid audit receipt for every consequential run.
12. Promote authority only from reviewed Outcome Receipts with no authority violations.

## Installation

The repository includes an inspectable bootstrap path:

```bash
sudo kit/init/install.sh
```

Do not pipe a remote installer directly into a privileged shell without reviewing it. The public files are examples; credentials must live in a secret store or mode-600 environment file, never in source, markdown or generated public data.

## Governance Rules

- Model confidence does not grant authority.
- Every human and machine gets an independent identity. Authenticated people can use stable role-permitted capabilities without one-use grants; unattended runtimes receive narrower explicit contracts.
- Sensitive retrieval is deny-by-default.
- Customer-facing, financial, legal, HR and destructive actions remain human-gated unless a named capability has passed its promotion gate.
- Artifacts live in durable storage and are referenced from the Brain; they are not embedded as opaque blobs.
- A backup is not trusted until a restore has been verified.
- A connector is not "covered" unless the approved accounts and artifact types are explicit.
- Compliance templates are starting points for qualified review, not legal advice or certification.

## Verification

From the repository root:

```bash
python3 scripts/release_audit.py --repo-root .
```

The audit checks release counts, chapter/index parity, anonymization, stale claims, service naming and archive integrity.

See Chapters 23-28 for the current operating layer, then Chapter 10aa for the evidence contract, 10ab for the architecture contract, 10ac for skill governance and 10ad for closure-first execution.
