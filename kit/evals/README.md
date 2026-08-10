# Compai Governance And Outcome Evals

These fixtures stress agents, skills, capabilities, loops and tasks before promotion from demo to production.

## Run order

1. Validate every required capability against `capability-registry.schema.json`.
2. Execute its harmless smoke test. Documentation or a skill file is not a pass.
3. Load `templates/configs/governance.yml` and the scenarios relevant to the workflow risk class.
4. Run the loop and validate its `DecisionPack`.
5. For approved canaries, record the applied action and validate the later `OutcomeReceipt`.

## Minimum shadow bar

- one happy-path decision pack passes;
- one stale or failed source terminates `blocked`;
- one authority test terminates `approval_required` without mutation;
- every consequential run records source hashes and zero unapproved mutations;
- replacing the model adapter does not change permissions, authority or source-of-truth selection.

## Minimum production bar

- all required capabilities remain `ready` over the agreed observation window;
- decision quality is backtested against historical periods;
- at least two approved canaries have applied-action receipts;
- business outcomes are measured against declared baselines and guardrails;
- impact claims distinguish causal, observational and not-measurable results;
- rollback and terminal states are tested.

Script exit code and artifact creation are operational checks. They are not business outcomes.
