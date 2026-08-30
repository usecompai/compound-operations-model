# Chapter 28: Decision Packs And Outcome Receipts

Most AI systems stop at a recommendation. A useful operating system follows the decision until a person accepts or rejects it, the action is applied and the result can be measured.

## Decision Pack

A Decision Pack contains the trigger, fresh source references, observations, proposed action, assumptions, uncertainty, owner, authority boundary and outcome contract. It is designed for a decision, not for showcasing a long answer.

## Outcome Receipt

An Outcome Receipt connects the decision to what happened later. It records the approved action, application evidence, observation window, business metric, baseline, result, verification and any correction needed for the next run.

This prevents two common errors:

1. counting generated recommendations as completed work;
2. promoting autonomy because a model sounded convincing rather than because prior outcomes were measured.

## Governed loops

A business loop follows:

```text
observe -> propose -> review -> apply -> verify -> record -> stop or repeat
```

Start in shadow mode. Promote only after reviewed receipts show useful, repeatable outcomes and no authority violations. If new evidence cannot change the next action, it is a one-shot workflow, not a loop.

## Ship it

- [ ] The recommendation names a measurable outcome and observation window.
- [ ] A person or policy contract owns approval.
- [ ] Application is verified in the source system.
- [ ] The Outcome Receipt compares result with baseline.
- [ ] The next run can consume the correction without rewriting history.
