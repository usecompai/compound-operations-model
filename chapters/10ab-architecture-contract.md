# Chapter 10ab: The Architecture Contract — What the System Is Not Allowed to Forget

## Architecture is the part that survives the model

Models change. Hosts move. Connectors are replaced. A company operating system still needs a small set of decisions that remain true through those changes.

We call that set the **Architecture Contract**: the load-bearing decisions, invariants and re-verification commands an operator reads before touching the brain, MCP, sync, auth or agent runtime.

It is not a diagram and it is not a roadmap. It is the answer to: *what would silently break the company if an agent "cleaned it up" without understanding why it exists?*

## The reference contract

The reference deployment currently protects these invariants:

1. **One shared tool plane.** Agents and human AI clients reach company systems through one authenticated MCP surface. This keeps policy, attribution and connector behavior in one place.
2. **Company memory is portable.** Durable memory lives in readable files with Git history. Search is an index over that memory, not the source of truth.
3. **Every material write is attributable.** Caller identity, tool, target, risk class, result and rollback hint enter an append-only ledger.
4. **Backups and rollback are part of runtime.** Frequent Git snapshots, daily encrypted backup and integrity checks are operating requirements, not disaster-recovery decoration.
5. **Authentication is enforced.** Every human and machine uses an identity. Anonymous access is rejected; sensitive scopes become narrower as identity improves.
6. **Credentials belong to runtimes, not shared files.** OAuth and refresh tokens are created independently per runtime and remain in approved secret stores.
7. **Search can lag.** A document may be true on disk before the index catches up. Absence from search does not prove absence from the brain.
8. **Heavy artifacts live outside compute.** The brain stores context, metadata and links; reusable media, PDFs, decks and delivery packs live in the company's file archive.
9. **Agents do not receive the whole brain by default.** Retrieval scope follows role, sensitivity and workflow need.
10. **Autonomy is capability-specific.** A system can be highly autonomous for one low-risk workflow and human-gated for payments, people, legal or customer-facing actions.

## Contracts need executable checks

An invariant without a check becomes folklore. Each contract row should include:

```yaml
invariant: "Every material write is attributable"
verify: "query the action ledger for actor, tool, target and result"
failure_state: "blocked_missing_attribution"
owner: platform
change_gate: "human approval"
rollback: "restore the last known-good service/config snapshot"
```

The check does not need to be sophisticated. It needs to be repeatable by someone who did not build the system.

## Cloud workspaces without credential sharing

One practical consequence is a server-first workspace model. Long-running engineering and agent work happens in a dedicated cloud workspace with its own Unix identity, HOME, source control and OAuth session. Laptops and phones reconnect to that workspace; they do not copy refresh-token files between machines.

This gives the company:

- session continuity across devices;
- one auditable working tree;
- independent identity per runtime;
- fewer "works on my laptop" failures;
- clean rollback through source control;
- no need to keep a founder laptop awake for production work.

## The asset boundary

Compute is not an archive. Large reusable artifacts belong in a durable company file system. The runtime may download, transform and render them, but completion means:

1. upload the final reusable artifact;
2. verify name and size, and checksum when available;
3. record the canonical link in the brain/task output;
4. remove temporary originals, extraction trees and superseded packages;
5. confirm storage headroom remains healthy.

This boundary matters because a full disk does not merely slow the system. It can stop snapshots, indexes and event writes at the same time.

## Change control

Different changes deserve different gates:

| Change | Minimum gate |
|---|---|
| Knowledge document | source + owner + write receipt |
| Canonical skill | authoring standard + separate evaluation |
| Agent prompt/governance | human approval + fleet propagation check |
| MCP/auth/runtime | backup + human approval + health smoke |
| Public release | anonymity + parity + link + package verification |
| Deletion | explicit scope + rollback + verification on every synced copy |

## Porting checklist

- [ ] Write ten or fewer load-bearing decisions in one canonical contract.
- [ ] Give every invariant a live verification method.
- [ ] State which changes require human approval.
- [ ] Keep search/index behavior separate from source truth.
- [ ] Create independent runtime identities; never copy OAuth state between machines.
- [ ] Version brain changes and keep an append-only action ledger.
- [ ] Put heavy reusable artifacts in the company archive, not the compute root.
- [ ] Re-read the contract before changing auth, sync, MCP or agent topology.

## For Compai readers

The model is rented. The architecture contract is owned. It is the small document that stops a future model, employee or maintainer from optimizing away the exact thing that made the system dependable.

