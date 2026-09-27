# DECISIONS

Append-only decision log.

## D-001 — 2026-09-26 — Create a separate adult digital markets research workspace

**Decision:** Treat Adult Audio, Adult Games and AI Video as three parallel product hypotheses inside one research repository.

**Reason:** The hypotheses share an adult-market context but differ materially in acquisition, content supply, infrastructure, retention, monetization and compliance. Keeping them together enables direct comparison without prematurely committing to one.

## D-002 — 2026-09-26 — Do not select a winner during proto-research

**Decision:** Research the three tracks against a common evaluation framework before choosing a build candidate.

**Reason:** Initial enthusiasm is high across all three and could otherwise cause premature build commitment.

## D-003 — 2026-09-26 — Prefer discovery/network value over commodity hosting

**Decision:** Evaluate product concepts primarily on their ability to own discovery, identity/follows, structured metadata and repeat usage rather than generic content hosting.

**Reason:** Commodity adult content is easy to replicate; audience relationships and structured graphs are more defensible.

## D-004 — 2026-09-27 — Lock the active workstream to Adult Audio

**Decision:** Keep the current active research and validation work strictly inside Adult Audio. Do not expand the active workstream into games, comics, visual novels, AI companions, AI video or other adjacent formats until an adult-audio hypothesis demonstrates credible demand and economics.

**Reason:** Adjacent opportunities are attractive but would dilute the current validation effort. Adult Audio is cheap enough to test directly and already contains several distinct promising wedges.

## D-005 — 2026-09-27 — Treat MM Audio Drama and M4M Roleplay as different consumer products

**Decision:** Do not treat MM and M4M as interchangeable categories.

- **MM Audio Drama:** story-first; the user wants to hear a story about two male protagonists.
- **M4M Roleplay:** listener-first; the gay/bi male user wants a male voice or character addressing him directly.

**Reason:** The two products differ in audience, consumption psychology, catalogue structure, retention loop, acquisition and likely monetization. "MM as genre" and "M4M as listener direction" are different markets.

## D-006 — 2026-09-27 — Split the furry hypothesis into Furry Worlds and Furry Explicit

**Decision:** Treat furry adult audio as two separate primary-intent hypotheses:

- **Furry Worlds:** serialized adult furry fiction; world/character/story-first.
- **Furry Explicit:** immediate fantasy/roleplay; character/species/dynamic-first.

**Reason:** Long-form story intent and immediate explicit intent should not be assumed to belong in one consumer experience.

## D-007 — 2026-09-27 — One primary consumer intent equals one consumer brand

**Decision:** If several Adult Audio hypotheses validate, prefer separate market-facing brands rather than one generic adult-audio site with unrelated intents.

Shared infrastructure is allowed and encouraged.

**Reason:** A focused new product should immediately feel "for me." Category adjacency does not imply consumer-brand compatibility.

## D-008 — 2026-09-27 — Research Furry Worlds and Furry Explicit next

**Decision:** Run `FURRY-R01 — Market & Wedge Research`.

**Reason:** The furry branch was strategically interesting but materially less researched than MM/M4M.

## D-009 — 2026-09-27 — Advance furry hypotheses to validation, not development

**Decision:** FURRY-R01 does not justify building a platform. It justifies designing falsifiable validation tests.

**Reason:** Direct market evidence remains limited and adjacent-market evidence must not be mistaken for audio product-market fit.

## D-010 — 2026-09-27 — Use reproducible unit economics

**Decision:** Keep furry economics in a runnable model at `research/audio/FURRY-R01-unit-economics.py`.

**Reason:** Key economics are assumptions and should be replaced incrementally with observed values rather than frozen into prose.

## D-011 — 2026-09-27 — Split Furry Explicit into character-anchored and category-anchored models

**Decision:** Refine Furry Explicit into:

- **Explicit-C:** recurring-character / OC anchored;
- **Explicit-K:** category/kink/species anchored.

**Current priority:** Explicit-C.

**Reason:** Independent FURRY-R01 evidence shows recurring OCs, sequels and character-linked audio already exist, while pure category catalogues are easier to commoditize. The working thesis is that category may be the acquisition mechanism while character attachment may be the retention mechanism.

Explicit-C and Explicit-K are not automatically separate brands; this relationship must be tested.

## D-012 — 2026-09-27 — Treat furry-audio market size conservatively

**Decision:** Do not infer furry-audio TAM from total furry traffic or pornography consumption.

Use a working posture of a small, fragmented niche until first-party validation proves otherwise.

**Economic guardrail:** current assumptions imply roughly 2,000–4,000 payers may be required for ~€10k/month operating profit before CAC.

**Reason:** Existing furry-audio supply is small, strongest willingness-to-pay evidence comes from adjacent VN/game projects, and visible leading furry projects themselves generally operate at low-thousands paid-user scale.

## D-013 — 2026-09-27 — Add a creator and processor gate before content production

**Decision:** The next furry step is `FURRY-G00 — Creator & Processor Gate`.

Before meaningful content spend:

1. conduct structured outreach to approximately 15 relevant creators / VAs / furry projects;
2. determine licensing, rev-share and aggregation feasibility;
3. obtain written policy/pre-approval guidance from at least two adult-friendly processors for the intended anthro-audio content boundaries.

If no workable processor path exists, stop the furry commercial branch before production spend.

**Reason:** Payments/compliance can invalidate the business regardless of user demand, and creator willingness determines whether a multi-creator catalogue is feasible.

## D-014 — 2026-09-27 — Keep Furry Worlds consumer-positioning separate during validation

**Decision:** Furry Worlds may share backend, analytics and production infrastructure with Furry Explicit, but its smoke test should use a separate story-first consumer façade.

Do not place Worlds inside an Explicit catalogue by default.

**Reason:** Combining story-first and immediate-explicit positioning would confound the central validation question and could reproduce the exact intent-mixing problem the brand architecture is designed to avoid.

## D-015 — 2026-09-27 — Define post-gate furry validation priorities

**Decision:** If FURRY-G00 passes:

1. **Priority 1:** Explicit-C — test recurring-character return and payment intent.
2. **Priority 2:** Furry Worlds — test episode completion and next-episode/season intent.
3. **Control/secondary:** Explicit-K — compare category-led discovery against character-led retention.

**Reason:** Explicit-C currently combines the strongest direct furry-audio evidence with a plausible retention/IP mechanism. Worlds retains higher speculative IP upside but weaker direct audio monetization evidence.

## D-016 — 2026-09-27 — Put the furry branch on HOLD

**Decision:** Move all furry-audio hypotheses to:

> **HOLD — interesting but not compelling.**

This applies to:
- Furry Explicit-C;
- Furry Explicit-K;
- Furry Worlds.

Do not currently run:
- FURRY-G00 creator outreach;
- processor outreach;
- furry content commissioning;
- FURRY-V01;
- furry product development.

Preserve all research, reconciliation notes and unit economics for possible reactivation.

**Reason:** After two independent research passes and explicit unit-economics modelling, the niche appears real but relatively small, fragmented and operationally inconvenient. Direct audio willingness-to-pay evidence is weaker than initially hoped; the strongest WTP evidence often comes from adjacent VN/game markets; a ~€10k/month operating-profit target appears to require material penetration of the plausible specialist paying market; and payment/compliance overhead is high relative to the opportunity.

**Reactivation condition:** Return to furry only if the stronger Adult Audio candidates disappoint, or if materially better first-party evidence appears.

**Next active workstream:** MM Audio Drama vs M4M Roleplay.
