# Compai Governance Evals

These fixtures are default stress scenarios for agents, skills, loops and tasks before a workflow is promoted from demo to production.

Use them as behavioral tests:

1. Load `templates/configs/governance.yml`.
2. Select the fixtures relevant to the workflow risk class.
3. Run the workflow against each scenario.
4. Pass only when the expected terminal state, blocked action and audit receipt match the fixture.

Minimum launch bar:

- one happy path passes;
- one source failure passes;
- one authority failure passes when the workflow can mutate state;
- an audit event is written for each consequential run.
