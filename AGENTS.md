# Agent Entry Point

Before substantive work, read `README.md`, `DECISIONS.md`, and the relevant research artifact.

Execution discipline:
- pinned standard: `docs/standards/AGENT_EXECUTION_DISCIPLINE_v1.1.md`;
- local adoption: `docs/operations/agent_execution_discipline_adoption.md`.

Do not treat adoption of the standard as reactivation of a HOLD workstream.

For authorized tasks, run `python3 scripts/task_sync.py start` before edits.
After the relevant checks and an explicit scoped commit, run
`python3 scripts/task_sync.py finish`; publication is complete only when the
configured same-name upstream branch is verified at the same SHA.

Explicit user no-commit/no-push instructions take precedence; report
LOCAL_ONLY / HANDOFF_INCOMPLETE instead. Use one writing agent per worktree.
Details and recovery: `docs/operations/git-handoff.md`.
