# Chapter 24: Compile Context Before Work

Giving every model the whole company archive is noisy, expensive and unsafe. Compai compiles the smallest useful context for the person, project and job in front of it.

## Inputs

- durable company knowledge and recent decisions;
- the current user's identity, role and audience;
- the active project and its approved sources;
- fresh records from source systems when the question is operational;
- relevant skills, constraints, open tasks and prior outcomes.

## Output: a ContextPack

A ContextPack separates facts from uncertainty. It includes source references, freshness, audience, current state, conflicts, missing evidence and the capabilities that may be used next.

The compiler should never hide an important gap. It emits explicit states:

- `conflict` — credible sources disagree;
- `stale` — the evidence is older than the job allows;
- `incomplete` — required fields or sources are missing;
- `no_evidence` — no approved source supports the claim;
- `blocked_permission` — useful context exists but this identity cannot read it.

## Knowledge is not live data

Documents, conversations and meeting notes explain context. They do not replace the system that owns today's number. Revenue comes from the commerce or accounting source of truth; stock comes from the inventory system; the ContextPack carries those live records alongside the durable knowledge that explains them.

## Ship it

- [ ] Context is compiled for a named identity and job, not copied wholesale.
- [ ] Every material fact has a source and freshness rule.
- [ ] Conflicts and permission blocks remain visible.
- [ ] Live operating figures are refreshed from their source system.
- [ ] The pack exposes the next permitted capabilities without granting new authority.
