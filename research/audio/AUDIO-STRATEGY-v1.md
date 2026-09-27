# AUDIO-STRATEGY-v1

**Status:** Canonical strategy note  
**Date:** 2026-09-27  
**Scope:** Adult Audio only  
**Purpose:** Preserve the current product decomposition, brand architecture, and immediate research sequence.

---

## 1. Scope lock

For the current phase, the project stays **strictly inside Adult Audio**.

Do not expand into:
- adult games;
- comics;
- visual novels;
- AI companions;
- AI video;
- general furry media;
- broader creator platforms.

Those may become adjacent opportunities later, but they are explicitly out of scope until at least one adult-audio hypothesis shows credible demand and economics.

The current task is to identify the strongest adult-audio product before building broadly.

---

## 2. Core strategic principle

Do **not** treat Adult Audio as one product with many categories.

The current research suggests that different listener intents should be treated as separate consumer products.

### Rule

> **One primary consumer intent = one consumer brand.**

Products may share infrastructure, production tooling, actors, analytics, moderation and payment abstractions underneath, but they should not be forced into the same consumer-facing catalogue or brand when the listener intent is materially different.

The reason is not merely aesthetic. Different intents imply different:
- acquisition channels;
- homepage promises;
- discovery systems;
- catalogue structures;
- retention loops;
- monetization behavior;
- community identity;
- brand expectations.

A new niche product should feel immediately "for me", not like a large generic tube with unrelated categories.

---

## 3. Current product hypotheses

## A. MM Audio Drama

### Primary intent
**Story-first.**

The listener wants to follow a story about two male protagonists.

### Primary audience hypothesis
Readers/listeners of MM romance.

The current competing research suggests that the commercial core may include a large female MM-romance audience, with gay/bi male romance listeners as a secondary audience.

### Product unit
**Episode / series / season.**

### Product characteristics
- two or more voices;
- plot;
- recurring protagonists;
- romantic/sexual tension;
- serialized arcs;
- cliffhangers;
- adult scenes as narrative payoff rather than the only content.

### Retention mechanism
"What happens next to these characters?"

### Current status
Strong validation candidate, but willingness-to-pay and competition from existing MM audiobooks/full-cast content still need tighter validation.

---

## B. M4M Roleplay

### Primary intent
**Listener-first / desire-first.**

A gay or bi male listener wants a male performer/character speaking directly to him.

### Important distinction
**M4M as listener-direction is not the same market as MM as story genre.**

MM Audio Drama:
> "I want to hear their story."

M4M Roleplay:
> "I want him to talk to me."

### Product unit
**Standalone roleplay / recurring creator or character session.**

### Product characteristics
- direct-to-listener POV;
- creator/voice affinity;
- BFE / comfort / intimacy;
- explicit roleplay;
- precise speaker → listener taxonomy;
- dynamic and preference filters;
- potentially recurring characters.

### Retention mechanism
"I want more from this voice / creator / character."

### Current status
Clear supply and discovery gap. Existing willingness-to-pay among gay/bi male listeners is less well proven than the demand gap itself and must be tested.

---

## C. Furry Worlds

### Working definition

> **Serialized adult furry fiction — audio-first.**

### Primary intent
**Story / character / world-first.**

The user comes for a fictional universe, recurring characters, relationships and serialized story.

Sexual content is part of the adult fiction, but is not necessarily the majority of runtime.

A plausible initial hypothesis is approximately:
- 70–90% world / plot / character / relationship;
- 10–30% explicit payoff.

This ratio is a test hypothesis, not a fixed product rule.

### Product unit
**Episode / season / world.**

### Product characteristics
- anthropomorphic adult characters;
- recurring cast;
- worldbuilding;
- character arcs;
- relationships;
- serialized stories;
- optional multiple voice actors;
- adult scenes embedded in the fiction.

### Retention mechanism
"I want the next episode / season and I care what happens to these characters."

### Key thesis
The asset is not merely an MP3 library. It is accumulating fictional IP:
- worlds;
- characters;
- relationships;
- lore;
- voice identity;
- serialized narrative.

### Current status
Very interesting but under-researched. Story-first furry demand is visible in adjacent fiction formats, but the size and economics of an **audio-first destination product** are not yet established.

This requires a dedicated research pass before any build decision.

---

## D. Furry Explicit

### Primary intent
**Immediate desire / roleplay-first.**

The user wants a specific furry fantasy, character, voice or dynamic without needing a long narrative.

### Product unit
**Scene / roleplay / creator-character drop.**

### Product characteristics
- character/species;
- voice;
- speaker/listener direction;
- dynamic;
- explicitness;
- scenario;
- creator or recurring character;
- strong tagging and filtering.

### Retention mechanism
"I want this character / creator / fantasy again."

### Important distinction from Furry Worlds

Furry Worlds:
> "What happens next in this world?"

Furry Explicit:
> "Give me the scene/fantasy I want now."

These should not be treated as two tabs of the same consumer experience by default.

### Current status
Plausible creator-driven niche with strong fandom mechanics, but requires dedicated research into creator economics, discovery, willingness to pay and existing competition.

---

## 4. Brand architecture

Current working decision:

### Do not launch one generic Adult Audio consumer brand containing all four hypotheses.

If multiple hypotheses validate, use **separate market-facing brands**.

Potential structure:

- Brand A → MM Audio Drama
- Brand B → M4M Roleplay
- Brand C → Furry Worlds
- Brand D → Furry Explicit

These may share the same technical platform underneath.

### Shared backend may eventually include
- authentication;
- audio player;
- analytics;
- CMS;
- creator ingestion;
- catalogue storage;
- tagging engine;
- subscription/payment abstraction;
- moderation/compliance tooling;
- rights/provenance records;
- production tooling.

### Consumer-facing layers should remain independent where intent differs
- naming;
- visual identity;
- onboarding;
- homepage;
- recommendation logic;
- catalogue;
- CRM/email;
- acquisition;
- community tone.

This is the current preferred architecture: **multiple precise consumer brands over one reusable adult-audio stack**.

---

## 5. What is NOT a sufficient wedge

Do not mistake the following for standalone product strategies:

- "queer audio";
- "audio for everyone";
- "creator-first";
- "cinematic audio";
- "full-cast audio";
- "better search";
- "more inclusive tags";
- "furry audio";
- "adult audio with AI."

These can be features or format choices.

A valid wedge must specify:
1. who the user is;
2. what primary job they are hiring the product for;
3. why existing destinations serve that job poorly;
4. why the user would return;
5. why they might pay.

---

## 6. Current comparison

| Hypothesis | Primary intent | Core unit | Main retention loop | Main unknown |
|---|---|---|---|---|
| MM Audio Drama | Story | Episode / series | Plot + characters + cliffhangers | Does MM-romance demand convert into paid adult audio? |
| M4M Roleplay | Direct desire / intimacy | Roleplay / creator drop | Voice + creator + repeat fantasy | Will gay/bi male listeners pay enough vs free alternatives? |
| Furry Worlds | World / story / character | Episode / season / world | IP + character attachment + serialized story | Is there a meaningful audio-first market? |
| Furry Explicit | Immediate fantasy | Scene / roleplay | Character + creator + precise fantasy matching | Is a dedicated destination better than Patreon/community workflows? |

No winner is selected yet.

---

## 7. Testing philosophy

Do not build four products.

Make the hypotheses compete for the right to be built.

The intended sequence is:

1. research each market enough to define a falsifiable product hypothesis;
2. design the smallest realistic smoke test;
3. acquire relevant users;
4. measure listening depth, repeat intent and willingness to pay;
5. kill weak hypotheses quickly;
6. build only after a product demonstrates credible signal.

The purpose of proto-research is not to prove that an idea is exciting. It is to reduce the cost of being wrong.

---

## 8. Current research state

### Completed / substantially researched
- Adult Audio proto-research.
- AUDIO-R01 market/wedge research.
- MM Audio Drama vs M4M distinction has been identified.
- Independent competing research has strengthened MM Audio Drama as a serious validation candidate and challenged the assumption that M4M scarcity automatically implies strong monetization.

### Not yet adequately researched
- Furry Worlds.
- Furry Explicit.
- Comparative validation economics across all four hypotheses.

---

## 9. Immediate next task

### FURRY-R01 — Market & Wedge Research

Research Furry Worlds and Furry Explicit as **two separate hypotheses**.

The central question:

> **Is there a sufficiently large and monetizable market for an audio-first furry destination, and is the stronger job-to-be-done serialized story/world attachment or immediate explicit roleplay?**

Required areas:
- existing furry audio creators and platforms;
- Patreon/Fanbox/Gumroad and comparable creator economics;
- furry audiobooks and audio dramas;
- adult furry fiction and VN markets as demand proxies;
- relevant communities and discovery paths;
- creator/character loyalty;
- species / character / relationship / roleplay taxonomy;
- existing dedicated competitors;
- free-vs-paid behavior;
- willingness-to-pay evidence;
- whether users want a destination product or prefer creator-specific Patreon/community workflows;
- production economics;
- acquisition channels;
- realistic route to €10k/month;
- kill criteria.

### Required output
A canonical research memo:

`research/audio/FURRY-R01-market-and-wedge.md`

It must evaluate **Furry Worlds and Furry Explicit separately** and conclude whether either deserves an AUDIO-001-style smoke test.

---

## 10. Current strategic snapshot

The adult-audio track is no longer one vague product idea.

It is currently a portfolio of four falsifiable consumer hypotheses:

> **MM Drama — story about them**  
> **M4M Roleplay — directed at me**  
> **Furry Worlds — return to the world**  
> **Furry Explicit — return to the fantasy/character**

The current strategy is to preserve that distinction, research the furry branch next, and remain inside Adult Audio until one or more hypotheses earn further investment.
