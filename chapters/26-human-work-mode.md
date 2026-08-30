# Chapter 26: Humans And Autonomous Runtimes Need Different Rules

The safest system is not the one that puts the same friction in front of everyone. An authenticated employee doing normal work and an unattended machine making external changes are different actors.

## Human work mode

An authenticated employee should be able to use stable, role-permitted capabilities without asking an administrator for a temporary token on every run. Identity, role, audience and capability scope are evaluated server-side. Consequential financial, legal, HR, destructive or customer-facing effects can still require a named approval step.

## Autonomous work mode

An unattended runtime receives narrower authority:

- exact capability and account scope;
- bounded parameters and expiry;
- idempotency and duplicate protection;
- explicit stop conditions;
- source-system verification;
- a complete receipt;
- promotion only from reviewed evidence.

Confidence is evidence quality, not permission. A model that is 99% confident still cannot perform an action outside its contract.

## Ship it

- [ ] Every person and machine has its own identity.
- [ ] Normal human work uses durable role permissions, not shared secrets or one-use grants.
- [ ] Autonomous external mutations require an approved capability contract.
- [ ] Sensitive domains have named approval boundaries.
- [ ] All enforcement lives on the server, not only in prompts or UI copy.
