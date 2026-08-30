# Chapter 25: From Skills To Verified Capabilities

A written skill proves that someone described a method. It does not prove that credentials, APIs, permissions, data shapes and verification still work.

The Capability Registry is the runtime contract for what the company can rely on now.

## Minimum record

Each capability names:

- business owner and technical owner;
- source of truth;
- inputs and outputs;
- read, write and approval permissions;
- sensitivity and authority scope;
- freshness requirement;
- harmless smoke test;
- verification method;
- terminal states and known blockers;
- linked skills or implementation assets.

## Readiness

Use explicit states such as `ready`, `degraded`, `blocked_auth`, `planned` and `deprecated`. Re-run harmless smoke tests on a schedule and after material changes. A failing optional connector should not make the whole platform red; a failing core dependency should not remain hidden behind an aggregate green score.

The registry is also the product boundary. A model may discover and invoke only capabilities allowed for its current identity and job. Model confidence never changes that authority.

## Ship it

- [ ] Every marketed capability has a current registry record.
- [ ] `ready` requires a passing dependency and smoke test, not a README.
- [ ] Core and optional capabilities are reported separately.
- [ ] A failed smoke test changes readiness and opens an owned follow-up.
- [ ] Models cannot bypass the registry through direct credentials.
