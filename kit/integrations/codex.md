# Codex Integration Guide

Use Codex to build and operate against the same authenticated MCP and Brain contracts as the other runtimes. Codex is a client and execution surface, not the system of record: durable knowledge, identity, permissions, capability state and receipts remain outside the model.

For the full implementation sequence, start with the Spanish [`Codex-first Company Brain guide`](../../guides/company-brain-with-codex.es.md) and its [`phase-gated bootstrap prompt`](../../guides/codex-company-brain-bootstrap-prompt.es.md).

## Prerequisites

- a currently supported Codex installation;
- an authenticated Compai MCP endpoint;
- an identity key scoped to the minimum required tools and Brain Spaces;
- a runtime registry entry naming the approved model and fallback;
- a repository or workspace owned by this client rather than shared mutable state.

Do not hard-code a model identifier from this document. Model names and account entitlements change faster than the integration. Select the current approved identifier from your runtime registry and record the actual provider/model in each consequential receipt.

## Configuration Shape

Adapt the current Codex configuration format to your installed version:

```toml
model = "<CURRENT_APPROVED_CODEX_MODEL>"

[mcp_servers.compai]
url = "https://mcp.example.com/mcp"
bearer_token_env_var = "COMPAI_MCP_TOKEN"
```

Store `COMPAI_MCP_TOKEN` in the operating system keychain, secret manager or a mode-600 environment file. Never commit it to the repository or place it in a URL.

Use `AGENTS.md` for durable repository instructions. Keep organization-wide rules at the workspace root and add narrower files only where a project needs them. In cloud environments, treat the checked-out repository and configured setup as an ephemeral work surface, not as a database, daemon or substitute for the Brain.

## Bootstrap Sequence

1. Choose one repetitive workflow with a named owner and measurable result.
2. Connect one read-only source and verify caller scope.
3. Ask Codex to produce research and an implementation plan before changing the runtime.
4. Require human approval between discovery, architecture, implementation and activation.
5. Run in proposal or shadow mode until tests, rollback and receipts pass.
6. Add another source or capability only after the first workflow is reviewable end to end.

## Verification

1. Call the authenticated status tool.
2. Run a Brain search and confirm citations respect the caller's scope.
3. Attempt a forbidden write and verify it is rejected.
4. Run one read-only source-system smoke test.
5. Produce a receipt that records identity, source references, provider/model and terminal state.

## Authority

Codex does not inherit founder authority merely because it runs on the founder's machine. The client identity still receives explicit read, propose, execute and administer grants. Financial, legal, HR, customer-facing and destructive actions remain human-gated unless a named capability has separately passed its promotion gate.

## Cross-Model Deliberation

For consequential analysis, create one decision packet with shared sources and acceptance criteria, then send independent copies to two different model/provider paths. Each model should critique the other against the same evidence. The final artifact records disagreements, convergence and the human decision; model agreement alone does not authorize execution.

## Failure Semantics

Report one of:

- `ok` - verified output and receipt exist;
- `blocked-provider` - model/provider unavailable;
- `blocked-reauth` - identity token invalid or expired;
- `failed-validation` - output or source check failed;
- `escalated` - authority or risk requires a human.

Never silently fall back to a different identity, unapproved model or broader tool scope.

## Current Codex References

- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli)
- [Cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environment)
- [`AGENTS.md` instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Model Context Protocol](https://learn.chatgpt.com/docs/extend/mcp)
- [Skills](https://learn.chatgpt.com/docs/build-skills)
- [Non-interactive execution](https://learn.chatgpt.com/docs/non-interactive-mode)
