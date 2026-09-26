# Proto-Research: Adult Audio vs Adult Games vs AI Video

**Date:** 2026-09-26  
**Status:** Proto-research. Not an investment memo and not a final product decision.

## 1. Why this research exists

The initial question was whether a very niche adult "tube" can still make sense in 2026.

The working answer is: **yes, but probably not as a classic generic video tube.**

A defensible product is more likely to win by owning a specific discovery problem, audience habit, creator/developer graph, or content format. Three hypotheses currently stand out:

1. Adult Audio
2. Adult Games
3. AI Video

These are deliberately being kept as separate tracks because their economics and product dynamics are very different.

---

## 2. Initial market signals

### Adult Games

F95Zone is the strongest early signal that adult gaming is not a tiny fringe niche.

Semrush estimated **116.86 million visits in August 2026**, an average session duration of **10:05**, **9.42 pages per visit**, and roughly **79.6% direct traffic**.

That matters more than the headline traffic alone. High direct traffic suggests a destination/habit product rather than a site living only on opportunistic search traffic.

Semrush also lists substantial adjacent competitors in August 2026, including:

- porngameshub.com — ~31.92M visits
- lewdzone.com — ~11.47M
- lewd.ninja — ~9.61M
- lewdgames.to — ~5.12M

**Proto-thesis:** the market is already large, but much of the experience is forum/thread/download oriented. There may be room for a cleaner discovery and metadata layer: something closer to IMDb/Steam/Reddit for adult games.

Potential product primitives:

- canonical game page
- developer page
- platform / engine / genre / art style
- latest version
- last update
- development status
- screenshots / trailers where rights permit
- reviews
- similar games
- follow game
- update notifications
- creator/developer claim page
- outbound support / purchase links

The key potential moat is the **structured game/developer/update graph**, not hosting binaries.

### Adult Audio

Adult audio appears much smaller than mainstream visual pornography, but the economics are attractive.

Quinn describes itself as a creator-driven audio erotica platform. Its current public pricing is **$7.99/month**, or **$4.99/month billed annually**, with creator tipping through virtual "Roses." It also explicitly recruits voice creators, writers, scriptwriters and sound engineers.

Sacra estimates Quinn reached approximately **$34M ARR in August 2026**, up from an estimated $25M at the end of 2025. Treat this as a third-party estimate, not audited financial data.

Dipsea currently offers an annual plan at **$69.99/year** and positions itself around professionally produced spicy audiobooks / romance audio.

**Proto-thesis:** audio is attractive because it combines subscription-friendly consumption with dramatically lighter infrastructure and production costs than video. It also creates a distinct behavioral use case: screenless consumption.

Potential product directions:

- creator-first adult audio network
- feed / discovery rather than a static story library
- creators + follows + series
- playlists / tags / mood / scenario discovery
- free discovery layer + premium subscription
- tips
- premium episodes
- optional AI-assisted production, without making "AI" the consumer-facing proposition

The core question is whether the market has room for a more open creator/discovery layer rather than another vertically produced story app.

### AI Video

The market is already crowded enough that "AI porn" by itself is not a differentiation.

A 2026 New Media & Society study examined governance materials from **98 AI pornography platforms**. In the sampled platform set, governance practices varied widely. The authors also report that by September 18, 2025 only **66.3%** of the sampled websites were still active, while 27.6% no longer existed.

A 2025 Archives of Sexual Behavior study of 36 AI-porn websites found:

- 80.6% offered image generation
- 41.7% offered video generation
- 44.4% offered interactions with artificial agents

This demonstrates both meaningful supply and rapid product expansion.

**Proto-thesis:** a generic AI generation site or anonymous video dump is weak. A more interesting concept is a **synthetic-only creator network** structured around:

Creator → Fictional Character → Series/Universe → Video → Followers

Possible differentiation:

- synthetic-only content
- no real-person impersonation
- no non-consensual deepfakes
- provenance / model metadata where useful
- persistent fictional characters
- creator pages
- follows
- series
- short-form discovery feed
- longer-form video pages
- eventually audio / companion extensions

The actual asset would be the **creator-character-follower graph**, not the generated files themselves.

---

## 3. First comparison

| Dimension | Adult Audio | Adult Games | AI Video |
|---|---|---|---|
| Evidence of demand | Strong but smaller | Very strong | Strong / fast-moving |
| Content hosting cost | Low | Low if metadata-first | High |
| Content supply | Creators / studios / AI-assisted | Existing developers | Potentially enormous |
| SEO potential | Medium-good | Very good | Potentially strong but uncertain |
| Repeat usage | High | Very high | Unknown / potentially high |
| Subscription fit | Very good | Moderate-good | Good |
| Affiliate fit | Moderate | Good | Good |
| Creator network effect | Strong | Strong | Potentially very strong |
| Compliance burden | Moderate | Moderate / IP-heavy | High |
| Platform/payment risk | Moderate | Moderate | High |
| MVP difficulty | Low-medium | Medium | Medium-high |
| Defensibility path | Creator graph + taste data | Structured catalogue + update graph | Character/creator/follower graph |
| Main risk | Incumbents may own the premium audience | Rights/data ingestion + incumbent communities | Commoditization + deepfake/compliance/payment risk |

This table is provisional and should not yet be used to select a winner.

---

## 4. What NOT to build

Current negative hypotheses:

- generic Pornhub clone
- generic fetish/category tube with commodity embeds
- scrape-and-republish tube
- stolen creator content aggregator
- celebrity / real-person deepfake platform
- AI video dump with no identity, graph or repeat-use mechanism
- adult games download mirror as the primary value proposition

The common failure mode is **commodity content without an owned audience relationship**.

---

## 5. Shared strategic thesis

The potentially valuable layer is:

**content/discovery → intent → identity/follow → repeat usage → monetization**

rather than:

**pageview → banner CPM**

The project should therefore evaluate every concept by its ability to produce:

1. repeat visits;
2. first-party preference data;
3. creator/developer relationships;
4. high-value outbound actions or subscriptions;
5. compounding catalogue/network value.

---

## 6. Immediate research questions

### Audio

- How large are Quinn, Dipsea, Bloom, Ferly and smaller creator-first competitors?
- Where does discovery fail?
- How much content is exclusive?
- What economics are offered to creators?
- Can web distribution compete with app-first incumbents?
- What content formats drive repeat listening?
- Are there underserved male, couple, queer, multilingual or scenario-specific markets without making the product a narrow fetish site?
- What are payment processor and app-store constraints?

### Games

- What exact jobs does F95Zone solve?
- Which jobs does it solve badly?
- What metadata can be collected legally and sustainably?
- How do developers announce updates now?
- Can developers be induced to claim/maintain their pages?
- What outbound monetization exists: Patreon, SubscribeStar, itch.io, Steam, direct?
- What are the dominant search patterns?
- What content can be embedded or indexed without becoming a piracy mirror?
- Can update-following create a durable notification habit?

### AI Video

- What are the current major AI adult video destinations vs generators?
- Is there a meaningful distinction between creation platforms and discovery platforms?
- What content provenance can practically be verified?
- Can a fictional-character identity remain consistent across models/releases?
- What upload policy materially reduces deepfake/non-consensual risk?
- What payment and hosting providers tolerate the model?
- Can creators bring their own audience?
- Is short-form vertical feed behavior actually desirable in this category?
- What are the economics of video storage, transcoding and delivery at 10k / 100k / 1M monthly users?

---

## 7. Decision rule for the next phase

Do not pick a winner from enthusiasm.

For each track, build an evidence pack sufficient to answer:

- Is there a visible product gap?
- Can we acquire the first 10k monthly visitors without buying expensive traffic?
- Can a meaningful percentage become repeat users?
- Is there a plausible path to €10k/month revenue without requiring massive scale?
- Does the product gain value as the catalogue / creator base grows?
- Can it operate with manageable legal, moderation, hosting and payment risk?

Only after all three have the same research depth should we select a primary build candidate.

---

## 8. Early interpretation

**Adult Games** currently has the strongest evidence of a large habitual audience and a potentially improvable product layer.

**Adult Audio** currently appears to have the cleanest small-business economics: cheap delivery, natural subscriptions, creator supply and strong repeat-use potential.

**AI Video** currently has the largest speculative upside if the product becomes a network of persistent synthetic creators/characters rather than a commodity generation site, but it also carries the largest compliance, payment and infrastructure burden.

These are hypotheses, not rankings.

---

## Sources

- Semrush, F95Zone traffic, Aug 2026: https://www.semrush.com/website/f95zone.to/overview/
- Semrush, F95Zone competitors, Aug 2026: https://www.semrush.com/website/f95zone.to/competitors/
- Quinn official About / pricing / creator information: https://www.tryquinn.com/about
- Sacra, Quinn revenue estimate: https://sacra.com/c/quinn/
- Dipsea subscription: https://www.dipseastories.com/subscribe/
- Lapointe et al. (2026), *The governance of AI-generated pornography platforms: A content analysis*, New Media & Society: https://journals.sagepub.com/doi/10.1177/14614448261421873
- Lapointe et al. (2025), *The Present and Future of Adult Entertainment: A Content Analysis of AI-Generated Pornography Websites*, Archives of Sexual Behavior: https://doi.org/10.1007/s10508-025-03099-1

## Source caution

Traffic figures from Semrush are modeled estimates, not first-party analytics. Sacra revenue figures are third-party estimates. They are useful for market sizing signals, not as audited facts.
