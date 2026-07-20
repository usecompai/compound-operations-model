# Compai Implementation Kit v5.1

This kit is the portable asset layer behind the Compai playbook. It turns the architecture into templates, scripts, eval fixtures and deployment contracts that a technical operator can inspect and adapt.

It is not a hosted service, a compliance certification or a promise that every connector is production-ready in every environment. Run it first in an isolated pilot, replace the example values, and review consequential data flows with the appropriate security, privacy and legal owners.

## Release Contract

Version 5.1 refreshes the evidence boundary and keeps the controls introduced in v5.0:

- `templates/configs/public-truth-manifest.schema.json` - dated claims, evidence classes and known gaps
- `templates/configs/source-coverage.yml` - source, account and artifact-type coverage matrix
- `templates/configs/architecture-contract.md` - runtime identity, workspace and change-control invariants
- `templates/configs/skill-evaluation.yml` - builder/judge separation and promotion evidence
- `templates/configs/approved-task.yml` - bounded closure-first execution object
- `templates/configs/artifact-storage.yml` - durable artifact ownership and retention
- `templates/configs/loop.yml` - observe, choose, act, verify, record and stop
- `templates/configs/governance.yml` - read, propose, execute and administer authority
- `templates/configs/audit-event.schema.json` - machine-readable execution receipt

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

1. Read `deployment/prerequisites.md`.
2. Fill `templates/configs/architecture-contract.md` before installing a runtime.
3. Inventory sources in `templates/configs/source-coverage.yml`.
4. Complete `deployment/deployment-contract.md` and `deployment/activation-path.md`.
5. Start with one domain agent in propose-only mode.
6. Run the negative eval fixtures.
7. Approve one task with `templates/configs/approved-task.yml`.
8. Require a valid audit receipt for every consequential run.
9. Promote authority only after ten reviewed runs reach at least 80% verified closure with no authority violations.

## Installation

The repository includes an inspectable bootstrap path:

```bash
sudo kit/init/install.sh
```

Do not pipe a remote installer directly into a privileged shell without reviewing it. The public files are examples; credentials must live in a secret store or mode-600 environment file, never in source, markdown or generated public data.

## Governance Rules

- Model confidence does not grant authority.
- Every human and machine gets an independent identity.
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

See Chapter 10aa for the evidence contract, 10ab for the architecture contract, 10ac for skill governance and 10ad for closure-first execution.
