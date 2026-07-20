# Chapter 10: The Technology Stack

## The Stack Is A Contract, Not A Vendor List

Models, APIs and product names move quickly. The durable system is the contract between identity, memory, tools, skills, authority, verification and receipts. The reference deployment uses OpenClaw-compatible runtimes, plain files, git, MCP and multiple model providers, but none of those choices should become an excuse to hard-code a fast-expiring model SKU into the architecture.

**Verified reference snapshot: 20 July 2026.**

| Layer | Current evidence |
|---|---|
| Runtime topology | Seven production agent runtimes plus a founder command center |
| Brain | 5,235 QMD documents; 24,469 vectors; 112 pending embeddings |
| Skills | 374 available; 48 canonical; 46 with a recorded evaluation |
| Tools | 98 authenticated MCP tools |
| Identity | Authentication in `enforce`; independent human and machine identities |
| Source systems | 14/14 read-only connector smoke tests plus an independent Google Workspace mail check green |
| Audit | 46,221 action receipts |
| Infrastructure | EU cloud hub, dedicated secondary host and encrypted private mesh |
| Public portfolio | 66 chapters, 31 anonymized skills, 21 patterns and a 220-file kit |

## Reference Architecture

```text
team AI clients + founder command center
                 |
          authenticated MCP
                 |
      identity -> scope -> authority
                 |
    company Brain + skill registry
                 |
  source systems / artifact storage
                 |
       verification + receipt
```

The system has two classes of compute:

1. **Cloud hub:** orchestration, authenticated MCP, shared indexes, public-safe publishing and central health checks.
2. **Independent agent workspaces:** domain runtimes with their own identity, workspace, logs and minimum viable tool scope.

The secondary host is not a shared home directory with several personalities. Each production runtime owns its operating state. Shared knowledge is synchronized through declared Brain and artifact contracts, not by letting every process mutate every folder.

## Model Routing

Choose models through a runtime registry rather than through prose copied into every prompt.

| Work class | Selection criteria |
|---|---|
| Frontier reasoning | Decision quality, context handling, tool reliability and adversarial review |
| Customer-facing drafting | Tone quality, privacy terms, latency and sampled acceptance rate |
| Structured extraction | Schema adherence, deterministic validation, throughput and cost |
| Coding and operations | Repository access, test execution, rollback and handoff quality |
| Fallback | Different provider failure domain, tested against the same output contract |

Record the provider, model identifier and runtime version in each receipt. That preserves reproducibility without pretending today's model name is a permanent architectural fact.

Provider OAuth or team subscriptions can reduce incremental cost, but only where machine use is supported and operationally reliable. A cheap route that silently rate-limits or loses tool support is not cheaper after incidents. Keep at least one independently tested fallback for critical paths.

## The Brain

The Brain is plain, versioned operating memory with four storage roles:

- **source captures:** immutable or append-only evidence with provenance;
- **canonical knowledge:** owned, dated documents and domain indexes;
- **work lifecycle:** tasks, outputs, decisions, health and capability gaps;
- **artifact references:** metadata and checksums pointing to durable binary or structured storage.

Do not put large datasets, videos, credentials or opaque binaries into the markdown tree. Rows belong in the structured-data sidecar. Large artifacts belong in object or file storage. Secrets belong in a secret manager or mode-600 environment file.

Queue depth is a first-class metric. The current release found 112 documents pending embedding: lexical and semantic search both passed, but the non-zero queue remains visible beside the document headline. A healthy retrieval layer reports and drains that queue; it does not hide it behind a cumulative count.

## MCP And Source Systems

MCP gives clients and agents one authenticated protocol for reading the Brain and reaching operating systems. The current tool inventory is 98. Tool count is not the objective; useful, scoped and testable capabilities are.

Every connector must declare:

1. source system and account scope;
2. read, propose, execute or administer authority;
3. freshness and failure semantics;
4. validation and rollback behavior;
5. receipt fields;
6. a dated smoke test.

The source system remains authoritative for live operational facts. The Brain stores meaning, decisions, contracts and provenance. A copied revenue number does not outrank commerce or accounting; a copied absence does not outrank the HR source.

## Identity, Scope And Authority

Authentication is currently in `enforce`: unauthenticated MCP calls are rejected. Each human, machine and runtime receives an independent identity so a receipt can answer who acted.

Fine-grained Brain Spaces retrieval scoping is still rolling out by sensitive domain. That distinction matters:

- identity enforcement is deployed;
- the Spaces architecture contract is published;
- universal tree-level retrieval enforcement is not yet claimed.

Confidence never grants authority. Read-only retrieval can execute with citations. Analysis can execute with a receipt. External drafts default to propose. Money, employment, legal and destructive actions require a named human unless a narrowly defined capability has separately passed its promotion gate.

## Skills

The swarm can discover 374 available skills, but only 48 are company-governed canonical procedures. Forty-six of those have a recorded evaluation. Availability, ownership and production approval are separate states.

A canonical skill needs stable inputs, authority, output contract, verification, stop conditions, rollback, an owner and an independent judge. See Chapter 10ac for the promotion lifecycle.

## Health And Recovery

The reference deployment uses:

- git-versioned Brain changes and a change ledger;
- layered Brain backups in separate failure domains;
- restore verification by checksum;
- host-level service supervision;
- connector smoke tests;
- queue-depth and freshness monitoring;
- batch rollback for bad automated writes;
- action receipts for consequential work.

"Online" is not one boolean. Runtime readiness and channel readiness are reported separately. A runtime can be healthy while a messaging token is invalid; collapsing those states creates false confidence.

## Current Cost Model

| Item | EUR/month |
|---|---:|
| Team AI subscriptions used by the operating layer | 460 |
| Additional model/runtime subscription | 20 |
| Provider API usage and fallbacks | 93 |
| EU cloud host and offsite backup | 19 |
| Secondary host amortization | 22 |
| Private mesh networking | 17 |
| **Total** | **631** |

Annual cost is EUR7,572. The Chapter 12 model estimates EUR122,944/year of reclaimed labor capacity under its stated assumptions, or 16.2:1. This is an auditable model, not a guaranteed return.

## Known Gaps

- broad autonomous execution remains a controlled pilot;
- fine-grained Brain Spaces enforcement is staged, not universal;
- complete native meeting-transcript coverage is not claimed even though generated notes are covered;
- 112 documents were pending embedding at the release boundary;
- several agent runtimes and semantic retrieval share one physical node;
- one team channel was degraded while its runtime remained available;
- Brain backups are layered, but runtime-home and session backup coverage remains incomplete;
- two canonical skills had not yet received a recorded evaluation.

These gaps do not erase the deployed system. Publishing them makes the strengths credible and gives the next release a measurable acceptance test.

## Porting Checklist

- [ ] Put identity in front of every tool call.
- [ ] Give each runtime an independent workspace and minimum viable scope.
- [ ] Keep source systems authoritative for live facts.
- [ ] Store credentials outside source and public data.
- [ ] Record model/provider versions in receipts, not permanent architecture prose.
- [ ] Keep a tested provider fallback for critical paths.
- [ ] Separate available, canonical, evaluated and public skills.
- [ ] Monitor queues and freshness, not just totals.
- [ ] Verify backup restores and rollback.
- [ ] Publish known gaps next to current evidence.

---

*Next: [Chapter 10b — Memory Architecture →](10b-memory-architecture.md)*
