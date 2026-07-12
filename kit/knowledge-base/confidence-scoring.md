# Confidence And Authority Framework

> Confidence is evidence about an output. It is never permission to act.

## Four Independent Gates

Every consequential capability must pass four gates:

| Gate | Question |
|---|---|
| Identity | Which human or machine is calling? |
| Scope | Which sources and tools may that identity reach? |
| Authority | May it read, propose, execute or administer this capability? |
| Risk | Is the action reversible, internal, customer-facing, financial, legal, HR or destructive? |

## Default Authority

| Capability | Default | Required evidence |
|---|---|---|
| Read and retrieve | Execute | Authenticated source access, citations, freshness |
| Analyse and recommend | Execute with receipt | Reproducible inputs and validation |
| Draft external work | Propose | Human review until a named promotion gate passes |
| Change operational systems | Human-gated | Explicit scope, limits, rollback, idempotency and receipt |
| Money, legal, HR, destructive | Human approval | Named approver; no confidence bypass |

## Confidence Reporting

Confidence can help reviewers prioritize sampling:

```text
[Confidence: 0.94] Tracking source is current; preparing a response draft.
[Authority: PROPOSE] Customer-facing send requires approval.
[Evidence: order/1234, policy/shipping-v4]
```

Do not ask a model to assign a number and then use that same number as the execution gate. Calibrate confidence against reviewed outcomes and deterministic checks where possible.

## Promotion

Start in shadow or propose-only mode. A capability can earn bounded execution after:

1. ten or more reviewed runs;
2. at least 80% verified closure;
3. no authority violations;
4. acceptable sampled quality for the domain;
5. tested rollback and stop conditions;
6. an explicit approval that names the capability and limits.

Promotion applies to one capability, not the whole agent. A CS runtime may execute a read-only tracking lookup while still requiring approval for the customer send, refund or exception.

## Metrics

- verified closure rate;
- reviewer correction rate;
- authority violations;
- source/freshness failures;
- rollback success;
- false confidence calibration by score band;
- escalation quality and time to resolution.

Never report one company-wide autonomy percentage. Publish capability-specific authority and evidence instead.
