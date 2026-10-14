# Architecture Contract

Owner: `[owner]`  
Last verified: `[YYYY-MM-DD]`  
Change gate: `[approval rule]`

## Load-Bearing Decisions

1. `[decision and why it exists]`
2. `[decision and why it exists]`

## Invariants

| Invariant | Verify | Failure state | Rollback |
|---|---|---|---|
| Every material write is attributable | `[ledger query]` | `blocked_missing_attribution` | `[restore path]` |
| Search is an index, not source truth | `[disk/read check]` | `blocked_index_stale` | `[re-index path]` |
| Runtime credentials are not shared files | `[ownership check]` | `blocked_identity_collision` | `[reauth path]` |

## Change Control

| Change | Required gate |
|---|---|
| Knowledge document | source + owner + receipt |
| Canonical skill | authoring standard + separate evaluation |
| Runtime/auth/MCP | backup + human approval + smoke test |
| Public release | anonymity + parity + package verification |

## Known Weaknesses

- `[weakness, evidence, accepted mitigation and review date]`
