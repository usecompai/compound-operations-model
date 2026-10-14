---
name: handoff-task
description: Use when a Brain task card should be delegated to Claude, Codex, or a swarm agent with all context included.
owner: the company Platform
risk: medium
---

> Reusable method. Configure your own sources, scope and approval rules.


# Handoff Task

Use this skill to move a Brain task from `todo` to `handoff` and produce a self-contained execution prompt.

## Workflow

1. Read the task card.
2. Read linked sources and entity pages.
3. Decide executor:
   - Codex for code/scripts/debug/bulk processing.
   - Swarm domain agent for CS/finance/retail/marketing/merch/HR.
   - Claude for short synthesis/docs/strategy.
4. Improve the `Handoff Prompt` if needed.
5. Call `brain_task_move(task_path, status="handoff", review_notes="...")`.
6. Deliver the exact prompt to use.

## Rules

- Never hand off a task that lacks source context.
- Include success criteria and expected output format.
- Include risk class and any tools that should or should not be used.
