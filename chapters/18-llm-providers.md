# Chapter 18: LLM Provider Abstraction

## Models Expire Faster Than Operating Systems

A provider abstraction is not a dropdown with several brand names. It is a stable execution contract that survives model renames, pricing changes, outages, quota shifts and account-policy changes.

Do not copy model identifiers or prices from a playbook and call the integration current. Keep a dated runtime registry, verify identifiers against official provider documentation during deployment, and record the model actually used in each consequential receipt.

## Provider Contract

Every adapter should implement the same request:

```json
{
  "task_class": "customer_draft",
  "messages": [],
  "tools": [],
  "output_schema": {},
  "data_class": "internal",
  "max_latency_ms": 30000,
  "max_cost_eur": 0.05,
  "required_capabilities": ["tool_calling", "structured_output"]
}
```

And return the same receipt fields:

```json
{
  "provider": "provider-id",
  "model": "model-id",
  "runtime_version": "adapter-version",
  "input_tokens": 0,
  "output_tokens": 0,
  "estimated_cost_eur": 0,
  "latency_ms": 0,
  "terminal_state": "ok",
  "validation": "passed"
}
```

## Runtime Registry

Keep model selection outside agent prose:

```yaml
registry_version: "2026-07-12"

task_classes:
  frontier_reasoning:
    primary: provider_a/frontier_model
    fallback: provider_b/frontier_model
    requires: [tool_calling, long_context]

  structured_extraction:
    primary: provider_b/fast_structured_model
    fallback: provider_a/fast_model
    requires: [structured_output]

  customer_draft:
    primary: provider_a/quality_model
    fallback: provider_b/quality_model
    requires: [tool_calling, policy_review]
```

The registry is reviewed independently from the agents that consume it. A model change runs the same evaluation fixtures before promotion.

## Routing Criteria

Route by task class, not agent personality:

| Criterion | Evidence |
|---|---|
| Quality | Domain eval pass rate and reviewer corrections |
| Tool reliability | Valid calls, schema adherence and retry behavior |
| Privacy | Contract terms and allowed data classes |
| Latency | p50/p95 under the real workload |
| Cost | Actual receipt cost, not list-price guesswork |
| Resilience | Different provider and account failure domain |
| Context | Effective retrieval and long-context eval, not advertised maximum alone |

## Failure Semantics

Provider failures must be explicit:

- `ok` - validated output exists;
- `blocked-provider` - outage, quota or unsupported model;
- `blocked-reauth` - token or OAuth state requires renewal;
- `failed-validation` - schema, citation or quality check failed;
- `escalated` - no approved fallback satisfies the contract.

Never silently downgrade to a model that lacks the required tool, privacy or output capabilities. Never switch to a broader identity to make a failing call pass.

## Fallback Rules

A fallback is production-ready only when:

1. it belongs to a different provider or meaningful failure domain;
2. it passes the same task-class fixtures;
3. it preserves source, authority and output contracts;
4. the cost ceiling remains acceptable;
5. a receipt records the route change;
6. repeated failure stops rather than loops forever.

## Subscription And OAuth Routes

Managed subscriptions or OAuth routes may reduce incremental API cost. Verify current provider terms and runtime support before using them for unattended workloads. Account entitlements, machine-use policies and quotas can change without your code changing.

Treat subscription reuse as an optimization layer, not an architectural dependency. Critical paths still need an approved API or second-provider fallback.

## Evaluation Before Promotion

For every task class:

- run representative positive fixtures;
- run stale-source, empty-source and wrong-account negatives;
- test tool-call schema failures;
- test provider timeout and reauthentication;
- compare reviewer corrections against the incumbent;
- record cost and latency distributions;
- require an independent judge to approve promotion.

## Porting Checklist

- [ ] Build one provider-neutral request and receipt schema.
- [ ] Keep model IDs in a dated runtime registry.
- [ ] Verify current IDs and terms from official provider sources during deployment.
- [ ] Route by task evidence, not one model for an entire agent.
- [ ] Test a second-provider fallback.
- [ ] Make reauth, outage and validation failures distinguishable.
- [ ] Record actual provider/model/version in receipts.
- [ ] Re-evaluate before any registry promotion.

---

*Next: [Chapter 19 — Factory Runtime →](19-factory-runtime.md)*
