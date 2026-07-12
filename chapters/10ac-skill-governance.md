# Chapter 10ac: Skill Governance — From Prompt Collection to Tested Operating Memory

## A skill library can grow faster than its reliability

Adding a skill is easy. Knowing that a zero-context agent can trigger it, follow it and verify its output six months later is the hard part.

The reference deployment now separates three numbers that used to be collapsed into one:

- **373 available skills** across company-authored, installed, vendor and community layers;
- **47 canonical company-authored skills** owned in the brain;
- **31 public skills** shipped in the Compai v5.0 repo after anonymization.

The counts answer different questions. "Available" describes reach. "Canonical" describes ownership. "Public" describes what can be safely copied. None of them alone proves quality.

## The skill contract

A canonical skill must make these decisions explicit:

1. **Trigger.** Literal words and situations that should route to it.
2. **When not to use it.** The nearest sibling workflow or manual gate.
3. **Inputs.** Sources, permissions and context required before execution.
4. **Procedure.** Finite steps with observable completion criteria.
5. **Output contract.** The artifact or state change the caller receives.
6. **Verification.** Evidence that proves the work, independent of confidence.
7. **Failure states.** Blocked, approval-required, exhausted and clean no-op.
8. **Provenance.** Owner, sources, dates and re-verification method.

This turns a skill from "advice that often works" into procedural memory the company can depend on.

## Builder and judge are different jobs

The person or model that wrote the skill should not be its only evaluator. The evaluation pattern is:

1. give a blind runner the skill and a realistic task;
2. capture the artifact and execution trace;
3. let a separate judge score it against a quality bar;
4. diagnose the failed contract rows;
5. repair the smallest material weakness;
6. re-run before promotion.

The bar is not "did the output look plausible?" It is "could a zero-context operator follow this without inventing tools, losing data or claiming success without evidence?"

## Failure archaeology before debugging

Procedural memory includes failures. Before investigating a familiar symptom, search for the literal error string and inspect the gotcha chronicle.

Each durable failure record needs:

```yaml
symptom: "exact error or observable behavior"
root_cause: "what was actually wrong"
evidence: "commands, logs or source-system result"
failed_attempts: "what not to repeat"
fix: "the smallest verified repair"
status: "fixed | mitigated | open"
```

This is how the skill layer compounds. The company does not merely add procedures; it stops paying twice for the same diagnosis.

## Progressive disclosure

Keep the main `SKILL.md` short enough to route and execute. Put long API references, examples, scripts and rubrics in `references/` or `scripts/`. An agent should load the expensive context only after the skill has actually matched.

The pattern reduces token cost, improves routing and makes maintenance safer: changing a vendor reference does not rewrite the core operating contract.

## Promotion ladder

| Stage | Requirement |
|---|---|
| Draft | owner, trigger, output and basic verification |
| Candidate | blind run completed; failures recorded |
| Canonical | separate judge passes the required bar |
| Fleet | propagated only where the runtime needs a local copy |
| Public | anonymized, license-safe, portable and re-tested |

Brain-served skills should remain canonical in one place. Copying every skill to every node creates silent drift; local copies are an exception for runtime requirements, not the default.

## Porting checklist

- [ ] Separate available, canonical, evaluated and public skill counts.
- [ ] Require triggers, when-not guidance, output and verification.
- [ ] Use a blind runner and a separate judge.
- [ ] Search literal prior failures before debugging.
- [ ] Split long references from the main skill.
- [ ] Keep one canonical source and document any runtime copies.
- [ ] Re-test after tool, model, API or policy changes.
- [ ] Publish only after anonymization and license review.

## For Compai readers

A large skill library is impressive for a week. A tested skill library becomes company memory. The moat is not the number of prompts; it is the number of procedures that still work when the original author is not in the room.

