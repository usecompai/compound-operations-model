# Skills Catalog

**Compai v6.0 release snapshot: 30 August 2026**

The public package contains **31 anonymized skills**. The reference runtime no longer uses a raw skill count as proof of capability: each operational capability must declare its dependencies, permissions, owner, verification and smoke-test state in the Capability Registry.

| State | Count | Meaning |
|---|---:|---|
| Public in this repo | 31 | Anonymized, portable procedures published with Compai v6.0 |
| Core runtime capabilities | 46/46 ready | Live dependencies passed the dated readiness gate on 28 August 2026 |
| Governed business loops | 3 | Contracted and available in proposal/shadow mode; not promoted as autonomous outcomes |

The remaining available skills are mostly installed vendor/community capabilities or internal procedures that are private, source-specific, not yet anonymized, or not yet ready for a public contract. The latest canonical addition is an attributed adaptation of an external prospect-research workflow; it remains outside this package until its supporting assets and licence are packaged cleanly. We do not republish third-party packages as our own.

## Brain And Execution Operations

- `brain-due-diligence` - audits brain claims, infrastructure, coverage and closure
- `check-brain-health` - checks raw/source gaps, loose captures and lifecycle hygiene
- `create-task-card` - turns evidence into an owned executable task
- `handoff-task` - delegates a task with source context and acceptance criteria
- `review-output` - validates an output and advances its lifecycle
- `log-capability-gap` - records missing data, access, process or tooling
- `refresh-world-model` - regenerates current state from verified operating artifacts
- `suggest-skills` - identifies repeated work worth packaging
- `failure-archaeology` - searches prior failures before starting a new investigation
- `skill-authoring-standards` - defines the canonical skill contract
- `skill-evaluation` - evaluates a skill independently from its builder
- `spec-driven-execution` - converts an approved specification into verified execution
- `session-handoff` - compresses context without losing sources or open risks
- `swarm-propagation` - packages an approved capability for multiple runtimes

## Research And Deliberation

- `adversarial-deliberation` - cross-model critique for consequential decisions
- `autoresearch` - bounded research with source and stop conditions
- `cross-model-handoff` - transfers a decision packet between model runtimes
- `research-prompting` - creates evidence-oriented research briefs
- `visual-review` - evaluates rendered artifacts against explicit criteria

## Commerce And Customer Operations

- `agent-payments` - prepares governed payment actions and receipts
- `cs-fashion-triage` - classifies fashion customer-service cases
- `cs-triage-finalization` - closes escalations and verifies the final customer state
- `employee-onboarding` - creates an auditable team onboarding packet
- `klaviyo-fashion` - analyses lifecycle marketing in a fashion context
- `omnichannel-foot-traffic-attribution` - estimates store halo from traffic and media evidence
- `omnichannel-growth-loop` - diagnoses and proposes cross-channel growth actions
- `pinterest-ads-integration` - connects Pinterest Ads through a bounded integration contract
- `restock-trigger` - proposes restocks from stock, velocity and forecast evidence
- `sell-through-dashboard-sync` - computes and publishes merchandising health metrics
- `shopify-inventory-sync` - reconciles inventory through a controlled sync
- `weekly-top5-digital` - produces a sourced weekly digital performance brief

## Promotion Contract

A reusable prompt is not automatically a production skill. Canonical promotion requires:

1. stable inputs and an explicit authority boundary;
2. a deterministic or reviewable output contract;
3. verification and stop conditions;
4. failure modes and rollback behavior;
5. an independent judge, distinct from the builder;
6. a recorded evaluation result and named owner.

See [`../chapters/10ac-skill-governance.md`](../chapters/10ac-skill-governance.md) for the full lifecycle.
