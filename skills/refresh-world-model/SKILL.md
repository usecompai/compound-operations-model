---
name: refresh-world-model
description: Use to regenerate the company current-state from Brain tasks, outputs, health reports, capability gaps and DRI/world-model docs.
owner: the company Platform
risk: low
---

> Reusable method. Configure your own sources, scope and approval rules.


# Refresh World Model

Use this skill before strategic synthesis, weekly reviews, or after major Brain/task updates.

## Workflow

1. Call `brain_world_model_refresh(write_report=true)`.
2. Read `knowledge/the company/_world-model/current-state.md` if deeper context is needed.
3. If health issues appear, call `brain_health_check(write_report=true)`.
4. Convert repeated gaps into task cards or DRI-map updates.

## Rules

- Current-state is an operating snapshot, not a dashboard.
- It should cite tasks, outputs, health and gaps, not invent status.
- For business metrics, always query source-of-truth tools separately.
