# FURRY-R01 unit economics — all inputs are [E] assumptions, see memo
payers = [500, 1250, 2500, 5000, 10000]
prices = [7.99, 9.99]
TAX = 0.12      # blended VAT/sales tax share of gross (EU VAT-inclusive + US mix)
PROC = 0.13     # adult processor fee (CCBill adult 10.8-14.5%)
REFCB = 0.02    # refunds + chargebacks
NET_SHARE = 1 - TAX - PROC - REFCB
INFRA = 700     # hosting, CDN, age-assurance SaaS base, tools / month
AV_PER_NEW = 0.40  # per-verification cost for new payer

# Content cost per month (mid, low, high)
worlds = {"low": 4*1000, "mid": 4*1800, "high": 4*3000}      # 4 episodes/mo, 1 flagship series
explicit_commission = {"low": 10*350, "mid": 12*550, "high": 16*800}  # new audios/mo
REVSHARE = 0.45  # share of NET to creators in rev-share variant (Quinn-like pool)
churns = [0.10, 0.15, 0.20]

def row(n, p, content, revshare=False, churn=0.15):
    gross = n*p
    net = gross*NET_SHARE
    new = n*churn
    av = new*AV_PER_NEW
    payout = net*REVSHARE if revshare else 0
    cost = (0 if revshare else content) + payout + INFRA + av
    profit = net - cost
    return gross, net, payout, cost, profit, new

print(f"NET_SHARE of gross = {NET_SHARE:.2f}")
for p in prices:
    print(f"\n=== price €{p} ===")
    print("payers | gross | net | WORLDS mid profit | EXPL commission mid profit | EXPL revshare profit | new payers/mo @10/15/20%")
    for n in payers:
        g,net,_,_,pw,_ = row(n,p,worlds["mid"])
        _,_,_,_,pe,_ = row(n,p,explicit_commission["mid"])
        _,_,po,_,pr,_ = row(n,p,0,revshare=True)
        news = "/".join(f"{int(n*c)}" for c in churns)
        print(f"{n:>6} | {g:>8,.0f} | {net:>8,.0f} | {pw:>9,.0f} | {pe:>9,.0f} | {pr:>9,.0f} | {news}")

# break-even payers & payers for €10k owner profit
print("\n=== payers needed ===")
for p in prices:
    unit = p*NET_SHARE - 0.15*AV_PER_NEW
    for name, c in [("Worlds low",worlds["low"]),("Worlds mid",worlds["mid"]),("Worlds high",worlds["high"]),
                    ("Expl comm low",explicit_commission["low"]),("Expl comm mid",explicit_commission["mid"]),("Expl comm high",explicit_commission["high"])]:
        be = (c+INFRA)/unit
        tenk = (c+INFRA+10000)/unit
        print(f"€{p} {name:15s}: break-even {be:,.0f}  | €10k profit {tenk:,.0f}")
    unit_rs = p*NET_SHARE*(1-REVSHARE) - 0.15*AV_PER_NEW
    print(f"€{p} Expl revshare   : break-even {INFRA/unit_rs:,.0f}  | €10k profit {(INFRA+10000)/unit_rs:,.0f}")

# Season pass / per-item
print("\n=== season pass & individual purchase ===")
season_cost = {"low":6*1000,"mid":6*1800,"high":6*3000}
for sp in [14.99, 19.99, 24.99]:
    for k,v in season_cost.items():
        print(f"Season pass €{sp}: {k} season cost €{v:,} -> buyers to recoup {v/(sp*NET_SHARE):,.0f}")
for ip in [3.99, 5.99, 7.99]:
    for k,v in {"low":350,"mid":550,"high":800}.items():
        print(f"Single audio €{ip}: {k} cost €{v} -> sales to recoup {v/(ip*NET_SHARE):,.0f}")

# LTV
print("\n=== LTV (net, before content) ===")
for p in prices:
    for c in churns:
        print(f"€{p} churn {c:.0%}: lifetime {1/c:.1f} mo, net LTV €{p*NET_SHARE/c:,.0f}")

# pilot/season/production pack costs
print("\n=== production packs ===")
print("Worlds pilot 3 eps:", [3*x for x in (1000,1800,3000)])
print("Worlds season 6 eps:", [6*x for x in (1000,1800,3000)])
for k in (10,50,100):
    print(f"Explicit {k} audios:", [k*x for x in (350,550,800)])
