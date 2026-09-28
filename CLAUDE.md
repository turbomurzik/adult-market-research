# Claude Entry Point

Before substantive work, read `README.md`, `DECISIONS.md`, and the relevant research artifact.

Follow the pinned execution standard at
`docs/standards/AGENT_EXECUTION_DISCIPLINE_v1.1.md` through the local adoption
record at `docs/operations/agent_execution_discipline_adoption.md`.

Do not treat adoption of the standard as reactivation of a HOLD workstream.

For authorized tasks, run `python3 scripts/task_sync.py start` before edits.
After the relevant checks and an explicit scoped commit, run
`python3 scripts/task_sync.py finish`; explicit user no-commit/no-push
instructions take precedence.

Use one writing agent per worktree. Details: `docs/operations/git-handoff.md`.
