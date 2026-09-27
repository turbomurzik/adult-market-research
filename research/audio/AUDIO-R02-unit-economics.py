# AUDIO-R02 unit economics — all business-model inputs are [E] assumptions.
# Evidence and rationale: research/audio/AUDIO-R02-MM-vs-M4M-decision.md

PAYERS = [500, 1250, 2500, 5000, 10000]
PRICES = [7.99, 9.99]
CHURNS = [0.10, 0.15, 0.20]
CACS = [0, 10, 20]

# Common standalone adult-audio assumptions [E]
TAX = 0.12       # blended VAT / sales-tax share of gross
PROC = 0.13      # adult payment processor
REFCB = 0.02     # refunds + chargebacks
NET_SHARE = 1 - TAX - PROC - REFCB
INFRA = 700      # hosting/CDN/tools/base compliance per month
AV_PER_NEW = 0.40  # age verification per new payer

# Mid production scenarios [E]
MM_EPISODES_PER_MONTH = 4
MM_COST_PER_EPISODE = 1800
MM_CONTENT = MM_EPISODES_PER_MONTH * MM_COST_PER_EPISODE

M4M_AUDIOS_PER_MONTH = 10
M4M_COST_PER_AUDIO = 400
M4M_COMMISSION_CONTENT = M4M_AUDIOS_PER_MONTH * M4M_COST_PER_AUDIO

M4M_REVSHARE = 0.45  # share of NET revenue paid to creators

def economics(n, price, content=0, revshare=0, churn=0.15, cac=0):
    gross = n * price
    net = gross * NET_SHARE
    new = n * churn
    acquisition = new * cac
    age_verification = new * AV_PER_NEW
    creator_payout = net * revshare
    cost = content + creator_payout + INFRA + age_verification + acquisition
    profit = net - cost
    return {
        "gross": gross,
        "net": net,
        "new": new,
        "creator_payout": creator_payout,
        "acquisition": acquisition,
        "cost": cost,
        "profit": profit,
    }

def payers_for_profit(price, target_profit, content=0, revshare=0, churn=0.15, cac=0):
    unit = price * NET_SHARE * (1 - revshare) - churn * (AV_PER_NEW + cac)
    if unit <= 0:
        return float("inf")
    return (target_profit + content + INFRA) / unit

def max_cac_for_target(n, price, target_profit, content=0, revshare=0, churn=0.15):
    contribution_before_acq = (
        n * price * NET_SHARE * (1 - revshare)
        - content
        - INFRA
        - n * churn * AV_PER_NEW
        - target_profit
    )
    return contribution_before_acq / (n * churn)

print(f"NET_SHARE = {NET_SHARE:.2f}")
print(f"MM monthly content = €{MM_CONTENT:,.0f}")
print(f"M4M commissioned monthly content = €{M4M_COMMISSION_CONTENT:,.0f}")
print(f"M4M rev-share = {M4M_REVSHARE:.0%} of net")

for price in PRICES:
    print(f"\n=== €{price}/month, churn 15%, CAC €0 ===")
    print("payers | MM profit | M4M commissioned | M4M rev-share | replacement payers")
    for n in PAYERS:
        mm = economics(n, price, content=MM_CONTENT)
        m4m = economics(n, price, content=M4M_COMMISSION_CONTENT)
        rs = economics(n, price, revshare=M4M_REVSHARE)
        print(
            f"{n:>6} | {mm['profit']:>10,.0f} | {m4m['profit']:>16,.0f} | "
            f"{rs['profit']:>13,.0f} | {mm['new']:>7,.0f}"
        )

print("\n=== Payers needed for €10k/month operating profit ===")
for price in PRICES:
    for cac in CACS:
        mm = payers_for_profit(price, 10000, content=MM_CONTENT, cac=cac)
        m4m = payers_for_profit(price, 10000, content=M4M_COMMISSION_CONTENT, cac=cac)
        rs = payers_for_profit(price, 10000, revshare=M4M_REVSHARE, cac=cac)
        print(
            f"€{price}, CAC €{cac:>2}: "
            f"MM {mm:,.0f} | M4M commission {m4m:,.0f} | M4M rev-share {rs:,.0f}"
        )

print("\n=== Max sustainable CAC at 5,000 payers while retaining €10k/month profit ===")
for price in PRICES:
    mm = max_cac_for_target(5000, price, 10000, content=MM_CONTENT)
    m4m = max_cac_for_target(5000, price, 10000, content=M4M_COMMISSION_CONTENT)
    rs = max_cac_for_target(5000, price, 10000, revshare=M4M_REVSHARE)
    print(
        f"€{price}: MM €{mm:.2f} | M4M commission €{m4m:.2f} | M4M rev-share €{rs:.2f}"
    )

print("\n=== Net LTV before content/fixed costs ===")
for price in PRICES:
    for churn in CHURNS:
        ltv = price * NET_SHARE / churn
        rs_ltv = price * NET_SHARE * (1 - M4M_REVSHARE) / churn
        print(
            f"€{price}, churn {churn:.0%}: gross-net LTV €{ltv:.2f}; "
            f"M4M rev-share contribution LTV €{rs_ltv:.2f}"
        )

print("\n=== Production packs [E] ===")
for low, mid, high, label in [
    (1200, 2400, 4000, "M4M smoke: 3 voices x 2 audios"),
    (1500, 2500, 4000, "MM smoke: one 20-25 min premium pilot + trailer/assets"),
    (3000, 4500, 6500, "MM smoke: two real episodes + trailer/assets"),
]:
    print(f"{label}: low €{low:,} | mid €{mid:,} | high €{high:,}")
