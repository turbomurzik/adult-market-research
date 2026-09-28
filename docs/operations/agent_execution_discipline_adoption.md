# Adult Market Research adoption of Agent Execution Discipline v1.1

**Status:** ADOPTED GOVERNANCE BASELINE — NO ACTIVE LEVEL 2 WORKFLOW

## Authority

The pinned shared standard is:

- path: `docs/standards/AGENT_EXECUTION_DISCIPLINE_v1.1.md`;
- version: `1.1`;
- SHA-256: `e79cad59a54f45d4dddc4335db543634563c9388b1310bc225b1e451eb6d2940`;
- upstream status: `Canonical internal standard`, dated 2026-09-26.

The adjacent `.sha256` file records the same byte identity. The pinned standard
is a vendor copy and must not be edited locally. Repository-specific
applicability is defined only by this adoption record.

`README.md`, the append-only `DECISIONS.md`, and the relevant research
artifact remain the authority for portfolio status and research conclusions.
This adoption does not supersede or reinterpret them.

## Current boundary

The repository currently records the entire Adult Audio portfolio as HOLD and
states that there is no active validation workstream.

Therefore this adoption does not authorize or reactivate:

- creator or licensing outreach;
- processor/payment outreach;
- commissioning or content production;
- AUDIO-V01 or another smoke test;
- MM production;
- product development.

The presence of the execution standard is not a reactivation decision.

## Execution-level classification

Use the shared levels proportionally:

- **Level 0** — one-off maintenance, formatting, a small code/doc correction, or
  another bounded task with little recovery need.
- **Level 1** — multi-step research synthesis, reconciliation, source review,
  unit-economics revision, or another bounded research task spanning related
  steps/sessions.
- **Level 2** — an explicitly authorized repeated validation/evidence workflow,
  such as structured creator/outreach batches, systematic market sweeps, smoke
  tests, repeated candidate evaluation, or multi-agent evidence production
  whose output may support a portfolio decision.

A Level 2 workflow is allowed only after the relevant commercial/research branch
has been explicitly reactivated by a new decision.

## Existing substrate reused

The discipline builds on existing project artifacts rather than replacing them:

- append-only `DECISIONS.md`;
- the canonical research files under `research/`;
- `research/SOURCES.md` for source registration;
- runnable unit-economics models for explicit assumptions;
- reconciliations that distinguish evidence from interpretation;
- `scripts/task_sync.py` for task-start/task-finish Git synchronization and
  verified publication.

No second decision log, research-status system, or orchestration layer is
introduced by this adoption.

## Implemented now

This repository now has:

1. a byte-identical pinned copy of Agent Execution Discipline v1.1;
2. its recorded SHA-256;
3. this repository-specific applicability record;
4. short pointers from `AGENTS.md` and `CLAUDE.md`.

No market conclusion, unit-economics assumption, source record, validation
result, or portfolio status is changed.

## Deferred Level 2 activation

If a future decision reactivates a repeated validation workflow, that workflow
must prospectively define the minimum applicable Level 2 controls before
execution, including as relevant:

- batch/run identity and explicit source snapshot identity;
- durable state for completed/pending/failed items;
- attempt/retry history rather than overwriting failed attempts;
- fixed promotion/kill criteria before the batch;
- cost/budget/stop rules;
- evidence manifests and claim-to-source bindings;
- isolated parallel workers where multiple agents are used;
- checkpoint/resume and stale-identity behavior;
- deterministic aggregation of mechanical results;
- explicit semantic-review authority for judgement calls;
- recovery/idempotency testing appropriate to the workflow.

Promotion means qualification under the registered criteria, not proof of
conversion, revenue, or product-market fit.

## Validation boundary

This adoption is documentation/governance only. It performs no outreach,
validation, content production, paid inference, payment processing, or product
build.

Normal repository checks still apply. Passing them establishes repository
consistency only; it does not reactivate Adult Audio or establish a market
claim.
