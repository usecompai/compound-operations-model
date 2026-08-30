# Chapter 16: Agentic Governance — Authority Outside The Model

Governance is not another model watching the first model. The hard boundary must live in identity, policy, capability contracts, server-side enforcement and receipts. A critic can improve a proposal; it cannot grant itself permission.

## Five independent controls

### 1. Identity

Every human, agent and service has its own authenticated identity. Shared tokens make attribution and revocation impossible.

### 2. Context scope

The Context Compiler includes only information this identity may use for this job. Sensitive retrieval is deny-by-default and permission blocks remain visible.

### 3. Capability scope

The Capability Registry separates what is installed from what works now. Each capability declares source accounts, inputs, outputs, sensitivity, authority, freshness, verification and terminal states.

### 4. Policy and approval

Authenticated people can use stable capabilities permitted by their role. Unattended runtimes receive narrower, explicit contracts. Financial, legal, HR, destructive and customer-facing effects stop at a named human boundary unless a specific promoted policy says otherwise.

### 5. Verification and receipts

Every consequential run records the actor, sources, model/runtime, policy decision, attempted effect, source-system verification and final state. Confidence never substitutes for evidence.

## Where model review helps

Cross-model criticism is useful for high-impact reasoning, ambiguous interpretation and adversarial review. It can return `accept`, `revise` or `escalate`, with reasons. That verdict remains advisory unless the server-side policy contract explicitly consumes it.

Deterministic checks should handle deterministic risks first:

- identity and account scope;
- duplicate and idempotency checks;
- parameter limits and expiry;
- required approval state;
- destination allowlists;
- schema and source freshness;
- rollback availability.

## Human and machine modes

Putting one-use authorization in front of every normal employee task creates a human bottleneck without meaningfully restricting an autonomous runtime. Use durable role permissions for authenticated people and exact, expiring authority for unattended external mutations. See Chapter 26.

## Promotion ladder

1. **Read-only** — gather and cite evidence.
2. **Propose** — produce a Decision Pack for review.
3. **Approved canary** — apply a tightly bounded action after approval.
4. **Production** — execute only the promoted capability contract.

Promotion requires reviewed Outcome Receipts, no authority violations and a rollback path. Activity volume is not promotion evidence.

## Current reference boundary

At the 30 August 2026 audit, authentication, RBAC, audience enforcement, retrieval and seven production domain agents were healthy. Three business loops had governed proposal/shadow contracts. Broad unattended execution was not deployed, and automated source synchronization was degraded. The release publishes both sides of that boundary.

## Ship it

- [ ] One identity per human and machine.
- [ ] Sensitive context is scoped before the model sees it.
- [ ] Only `ready` capabilities can be invoked.
- [ ] Approval and mutation rules are enforced outside prompts.
- [ ] Every external effect is verified and recorded.
- [ ] Authority is promoted from outcomes, not confidence or demos.

---

Back to [Chapter 15 — The Five Pillars](15-five-pillars.md) · Continue to [Chapter 26 — Human Work Mode](26-human-work-mode.md)
