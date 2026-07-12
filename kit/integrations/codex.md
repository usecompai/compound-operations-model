# Codex Integration Guide

Use Codex as a coding, operations or founder command client over the same authenticated MCP and Brain contracts as the other runtimes.

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
