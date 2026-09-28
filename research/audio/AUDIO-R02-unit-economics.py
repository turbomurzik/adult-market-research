#!/usr/bin/env python3
"""
AUDIO-R02 — MM Audio Drama vs M4M Roleplay: reproducible unit economics.

All inputs are ASSUMPTIONS [E] unless marked otherwise. Replace them with
observed values as smoke-test data arrives. Currency: EUR. Monthly figures.

Run:  python3 AUDIO-R02-unit-economics.py
"""
from dataclasses import dataclass
import math

MM_LINES = {
    "script_per_ep":        (150,   450,  1200),
    "principal_voice_per_ep_per_actor": (100, 300, 900),
    "minor_voices_per_ep":  (0,     100,   300),
    "direction_per_ep":     (0,     150,   500),
    "post_per_finished_min":(10,     30,    80),
    "music_sfx_fixed":      (0,     200,  1000),
    "key_art_fixed":        (100,   400,  1500),
}
EP_MIN = 20

def mm_cost(episodes: int, tier: int) -> float:
    L = {k: v[tier] for k, v in MM_LINES.items()}
    per_ep = (L["script_per_ep"] + 2 * L["principal_voice_per_ep_per_actor"]
              + L["minor_voices_per_ep"] + L["direction_per_ep"]
              + L["post_per_finished_min"] * EP_MIN)
    fixed = L["music_sfx_fixed"] + L["key_art_fixed"]
    return episodes * per_ep + fixed

def mm_per_episode(tier: int) -> float:
    return mm_cost(2, tier) - mm_cost(1, tier)

M4M_LINES = {
    "script":          (25,  120,  350),
    "voice":           (100, 240,  450),
    "edit_master":     (20,   60,  150),
    "thumbnail":       (0,    20,   80),
}

def m4m_cost(audios: int, tier: int) -> float:
    return audios * sum(v[tier] for v in M4M_LINES.values())

@dataclass
class Assumptions:
    tax_share_of_gross: float = 0.12
    processor_pct: float = 0.12
    processor_fixed: float = 0.25
    refunds_cb_pct: float = 0.03
    fixed_opex: float = 1500.0
    age_check_cost: float = 0.30
    checks_per_new_payer: float = 8.0

A = Assumptions()

def net_per_sub(price: float, a: Assumptions = A) -> float:
    return price * (1 - a.tax_share_of_gross - a.processor_pct - a.refunds_cb_pct) - a.processor_fixed

def content_budget(product: str, tier: int) -> float:
    if product == "MM":
        return 4 * mm_per_episode(tier)
    if product == "M4M":
        return 8 * m4m_cost(1, tier)
    raise ValueError(product)

def monthly_profit(n: int, price: float, churn: float, cac: float,
                   content: float, revshare: float = 0.0, a: Assumptions = A) -> dict:
    gross = n * price
    net = n * net_per_sub(price, a)
    new_payers = churn * n
    acq = new_payers * cac
    age = new_payers * a.checks_per_new_payer * a.age_check_cost
    creator = revshare * net
    contribution = net - content - creator - acq - age
    profit = contribution - a.fixed_opex
    return dict(gross=gross, net=net, content=content + creator, acq=acq,
                age=age, contribution=contribution, profit=profit,
                replacement=new_payers)

def subs_needed(price, churn, cac, content, revshare=0.0, target=10_000.0, a=A):
    per_sub = net_per_sub(price, a) * (1 - revshare) - churn * (cac + a.checks_per_new_payer * a.age_check_cost)
    if per_sub <= 0:
        return math.inf
    return math.ceil((target + content + a.fixed_opex) / per_sub)

def max_cac(n, price, churn, content, revshare=0.0, target=10_000.0, a=A):
    surplus = n * net_per_sub(price, a) * (1 - revshare) - content - a.fixed_opex - target \
        - churn * n * a.checks_per_new_payer * a.age_check_cost
    return surplus / (churn * n)

def fmt(x):
    return "inf" if x == math.inf else f"{x:,.0f}"

def main():
    tiers = ("low", "mid", "high")
    print("== Production cost (EUR) ==")
    for t, name in enumerate(tiers):
        print(f"MM {name:4}: pilot 3 eps {fmt(mm_cost(3, t)):>7} | season 6 eps {fmt(mm_cost(6, t)):>7}"
              f" | marginal ep {fmt(mm_per_episode(t)):>6} | cost per finished min {mm_cost(6, t)/(6*EP_MIN):,.0f}")
    for t, name in enumerate(tiers):
        print(f"M4M {name:4}: 10 {fmt(m4m_cost(10, t)):>7} | 25 {fmt(m4m_cost(25, t)):>7} | 50 {fmt(m4m_cost(50, t)):>7}"
              f" | cost per finished min {m4m_cost(1, t)/12:,.0f}")

    print("\n== Net revenue per subscriber per month ==")
    for p in (7.99, 9.99):
        print(f"price {p}: net {net_per_sub(p):.2f}")

    print("\n== Monthly content budgets (EUR) ==")
    for prod in ("MM", "M4M"):
        print(prod, {tiers[t]: fmt(content_budget(prod, t)) for t in range(3)})

    cacs = (0, 10, 20, 40)
    churns = (0.10, 0.15, 0.20)
    print("\n== Subscribers needed for EUR 10k/month operating profit (mid content tier) ==")
    for prod, rs in (("MM", 0.0), ("M4M", 0.0), ("M4M-revshare40", 0.40)):
        base = "M4M" if prod.startswith("M4M") else "MM"
        content = content_budget(base, 1) if rs == 0 else 1000.0
        for p in (7.99, 9.99):
            row = []
            for ch in churns:
                row.append(" / ".join(fmt(subs_needed(p, ch, c, content, rs)) for c in cacs))
            print(f"{prod:15} @ {p}: " + " | ".join(f"churn {int(ch*100)}%: {r}" for ch, r in zip(churns, row)))
    print("(each cell: CAC 0 / 10 / 20 / 40)")

    print("\n== P&L grid, price 7.99, churn 15%, CAC 20, mid content ==")
    for prod in ("MM", "M4M"):
        for n in (500, 1250, 2500, 5000, 10000):
            r = monthly_profit(n, 7.99, 0.15, 20, content_budget(prod, 1))
            print(f"{prod:3} n={n:>6}: gross {fmt(r['gross']):>7} net {fmt(r['net']):>7} content {fmt(r['content']):>6}"
                  f" acq {fmt(r['acq']):>7} age {fmt(r['age']):>5} contribution {fmt(r['contribution']):>7}"
                  f" profit {fmt(r['profit']):>7} replace/mo {fmt(r['replacement']):>5}")

    print("\n== Break-even payers (profit = 0), price 7.99, CAC 20 ==")
    for prod in ("MM", "M4M"):
        for ch in churns:
            be = subs_needed(7.99, ch, 20, content_budget(prod, 1), target=0)
            print(f"{prod:3} churn {int(ch*100)}%: {fmt(be)}")

    print("\n== Max sustainable CAC at given payers (price 7.99, mid content, EUR 10k profit) ==")
    for prod in ("MM", "M4M"):
        for n in (1250, 2500, 5000, 10000):
            vals = [max_cac(n, 7.99, ch, content_budget(prod, 1)) for ch in churns]
            print(f"{prod:3} n={n:>6}: " + " | ".join(f"churn {int(ch*100)}%: {v:,.1f}" for ch, v in zip(churns, vals)))

    print("\n== LTV (net, no discount) ==")
    for p in (7.99, 9.99):
        print(f"price {p}: " + ", ".join(f"churn {int(ch*100)}% -> {net_per_sub(p)/ch:,.1f}" for ch in churns))

    print("\n== Alternative monetisation ==")
    sp_net = net_per_sub(12.99)
    for t, name in enumerate(tiers):
        print(f"MM season pass 12.99, {name} season cost {fmt(mm_cost(6, t))}: break-even buyers {math.ceil(mm_cost(6, t)/sp_net):,}"
              f" (net/buyer {sp_net:.2f}, before CAC)")
    pa_net = net_per_sub(2.99)
    for t, name in enumerate(tiers):
        print(f"M4M per-audio 2.99, {name} cost/audio {fmt(m4m_cost(1, t))}: break-even sales per audio {math.ceil(m4m_cost(1, t)/pa_net):,}"
              f" (net/sale {pa_net:.2f})")

    print("\n== First-renewal cohort decay (RevenueCat 2026 Media&Ent median first renewal 58%) ==")
    for later in (0.10, 0.15, 0.20):
        surv = [1.0, 0.58]
        for _ in range(10):
            surv.append(surv[-1] * (1 - later))
        paid_months = sum(surv)
        print(f"after-first-renewal churn {int(later*100)}%: expected paid months in first 12 = {paid_months:.2f};"
              f" net LTV12 @7.99 = {paid_months*net_per_sub(7.99):.1f}")

if __name__ == "__main__":
    main()
