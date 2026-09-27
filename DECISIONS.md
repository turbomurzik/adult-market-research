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

**Decision:** Treat furry adult audio as two separate hypotheses:

- **Furry Worlds:** serialized adult furry fiction; world/character/story-first; episode/season/world as the unit of value.
- **Furry Explicit:** immediate fantasy/roleplay; character/species/dynamic-first; scene/roleplay as the unit of value.

**Reason:** Some users want long-form story, character attachment and worldbuilding with adult payoff; others want immediate explicit fantasy and do not want narrative overhead. Combining both intents in one catalogue risks weakening product clarity for both.

## D-007 — 2026-09-27 — One primary consumer intent equals one consumer brand

**Decision:** If several Adult Audio hypotheses validate, prefer separate market-facing brands rather than one generic adult-audio site with unrelated categories.

Shared infrastructure is allowed and encouraged:
- auth;
- player;
- analytics;
- CMS;
- creator ingestion;
- tagging;
- payment abstraction;
- moderation/compliance;
- production tooling.

Consumer-facing layers should remain separate where the intent differs:
- naming;
- visual identity;
- onboarding;
- homepage;
- catalogue;
- recommendation logic;
- acquisition;
- CRM/community tone.

**Reason:** A focused new product should immediately feel "for me." Category adjacency does not imply consumer-brand compatibility.

## D-008 — 2026-09-27 — Research Furry Worlds and Furry Explicit next

**Decision:** The next dedicated Adult Audio research task is `FURRY-R01 — Market & Wedge Research`.

**Required question:** Is there a sufficiently large and monetizable market for an audio-first furry destination, and is the stronger job-to-be-done serialized story/world attachment or immediate explicit roleplay?

**Required output:** `research/audio/FURRY-R01-market-and-wedge.md`.

**Reason:** MM/M4M have already received substantial research. The furry branch is strategically interesting but remains the least evidenced part of the current Adult Audio portfolio.

## D-009 — 2026-09-27 — Advance both furry hypotheses to smoke-test design, with Furry Explicit as primary

**Decision:** FURRY-R01 does not justify building either product yet. It does justify designing two separate smoke tests:

- **Primary:** Furry Explicit — direct willingness-to-pay is already evidenced by multiple furry audio/ASMR creators with recurring paid memberships.
- **Exploratory:** Furry Worlds — story/character/world retention is strongly evidenced in adjacent furry fiction/VN markets and exists in serialized furry audiobooks, but a dedicated audio-first business remains unproven.

Do not combine these tests into one consumer-facing brand.

**Reason:** Furry Explicit has stronger direct monetization evidence and a cheaper/faster MVP. Furry Worlds has higher potential IP/retention defensibility if narrative continuation demand proves real, but its production cost and format risk are materially higher.

## D-010 — 2026-09-27 — The next furry task is comparative validation design, not platform development

**Decision:** After reconciling FURRY-R01 with the independent research pass, the next furry work product should be `FURRY-V01 — Comparative Smoke-Test Design`.

It must test:
- whether Furry Explicit users explore across creators/characters rather than staying loyal to one creator;
- whether Furry Worlds listeners continue to episode 2 and show season-unlock/payment intent.

**Reason:** These are the two unresolved questions that determine whether either concept is a platform/product opportunity rather than merely an existing creator or adjacent-media behavior.
