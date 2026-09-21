# Chapter 10c: MCP — One Governed Interface To The Company

MCP gives AI clients and agents a common protocol for company context and operating capabilities. The important result is not a large tool list. It is that a finance manager, retail operator or autonomous runtime can use the same underlying contracts under different identities and permissions.

## Architecture

```text
human or machine identity
          |
     authenticated MCP
          |
 identity -> audience -> capability -> policy
          |
 ContextPack + source systems + artifact storage
          |
 verification -> run ledger -> Outcome Receipt
```

Credentials stay server-side. Clients discover only the capabilities permitted for their identity and job. A model never receives a shared root token or direct permission to expand its own scope.

## Capability families

The reference layer connects:

- Brain retrieval and durable write-back;
- team communication, email, documents and meetings;
- commerce, inventory, accounting, expenses and logistics;
- customer care, CRM and lifecycle marketing;
- paid media, web analytics, SEO and retail traffic;
- private workspaces and governed internal publishing;
- health, audit, release history and rollback.

The dated 15 September 2026 registry reported **45 of 55 core capabilities ready**. Four were degraded, four awaited configuration, one was blocked by a dependency and one was configured but unverified. Optional, planned and deprecated connectors remain separate from that core distribution.

## A capability is more than a tool

Every capability declares:

1. source system and account scope;
2. input and output contract;
3. owner and sensitivity;
4. read, internal-write or approval-required authority;
5. freshness and failure semantics;
6. harmless smoke test;
7. verification and terminal states.

An API wrapper without these fields is plumbing, not an operating capability.

## Retrieval

`brain_search` and `brain_vsearch` return source paths rather than unsupported prose. Lexical Brain retrieval was ready at the 15 September live check. Operational figures still come from their live source system; the Brain supplies context and provenance.

## Human work mode

Each employee authenticates as themselves. Stable, role-permitted capabilities can run without a one-use administrator grant. The server evaluates identity, role, audience, source account and action risk on every call. Sensitive and consequential actions can still require approval.

## Autonomous work mode

Unattended runtimes receive narrower contracts: exact capability, bounded parameters, expiry, idempotency, stop conditions and source-system verification. Model confidence never grants authority.

## Failure semantics

Use states that explain why work stopped:

- `ok` — execution and verification passed;
- `blocked_permission` — identity lacks scope;
- `blocked_auth` — source credentials need repair;
- `blocked_source_unavailable` — dependency is down or stale;
- `failed_validation` — output or effect did not satisfy the contract.

A failure should update readiness and open an owned follow-up. It should not silently return stale data as current.

## Current boundary

At the 15 September 2026 release audit, authenticated MCP, caller identity, lexical retrieval and seven production domain agents were ready. Automated company-source ingestion and the Context Compiler were degraded. Direct source reads and most of the operating layer remained available, while each non-ready capability kept its own explicit state.

## Ship it

- [ ] Independent identities for every person and runtime.
- [ ] No credentials in clients, prompts or public artifacts.
- [ ] Capability discovery filtered by role and job.
- [ ] Live figures read from the source of truth.
- [ ] Explicit blocked and failed states.
- [ ] Every consequential effect verified and recorded.

---

Continue to [Chapter 25 — From Skills To Verified Capabilities](25-capability-registry.md).
