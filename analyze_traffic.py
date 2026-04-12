"""
Estimate decrease in Wikipedia traffic between March 2022 and March 2026,
attributable to the rise of AI chatbots (ChatGPT launched Nov 2022).

Uses:
- Wikimedia Pageviews aggregate API for overall traffic
- Per-article API for a representative sample of pages

Saves all fetched numbers and derived statistics to data.json.
"""

import json
import time
import urllib.request
from datetime import datetime, timezone

API_BASE = "https://wikimedia.org/api/rest_v1/metrics/pageviews"
HEADERS = {"User-Agent": "wikipedia-traffic-research/1.0 (research project)"}

# ── Representative sample: spread across topic categories ──────────────────
SAMPLE_PAGES = [
    # Science & medicine
    "DNA", "Climate_change", "Black_hole", "Vaccine", "Evolution",
    "Photosynthesis", "Quantum_mechanics", "Human_brain",
    # History & geography
    "World_War_II", "United_States", "France", "Ancient_Rome",
    "Industrial_Revolution", "Cold_War", "United_Kingdom",
    # Technology (deliberately avoiding pure-AI topics)
    "Internet", "Smartphone", "Python_(programming_language)",
    "Artificial_intelligence", "Blockchain",
    # Culture & society
    "Mathematics", "Philosophy", "Music", "Chess", "Olympic_Games",
    # Perennial high-traffic articles
    "Deaths_in_2023", "Wikipedia", "Earth", "Water", "Jesus",
    "Adolf_Hitler",   # historically one of the most-viewed articles
    "United_States_Constitution",
]


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())


def monthly_aggregate(year: int, month: int) -> int:
    """Return total human pageviews for English Wikipedia for one month."""
    start = f"{year}{month:02d}0100"
    # end = last day of month; using 01 of next month works for the API range
    if month == 12:
        end = f"{year+1}010100"
    else:
        end = f"{year}{month+1:02d}0100"
    # granularity=monthly → single item covering the whole month
    url = (f"{API_BASE}/aggregate/en.wikipedia/all-access/user"
           f"/monthly/{start}/{end}")
    data = fetch(url)
    return data["items"][0]["views"]


def monthly_article(article: str, year: int, month: int) -> int:
    """Return total human pageviews for one article for one month."""
    start = f"{year}{month:02d}0100"
    if month == 12:
        end = f"{year+1}010100"
    else:
        end = f"{year}{month+1:02d}0100"
    url = (f"{API_BASE}/per-article/en.wikipedia/all-access/user"
           f"/{article}/monthly/{start}/{end}")
    try:
        data = fetch(url)
        return data["items"][0]["views"]
    except Exception as e:
        print(f"  [warn] {article}: {e}")
        return None


# ── 1. Site-wide aggregate ──────────────────────────────────────────────────
print("=" * 60)
print("WIKIPEDIA ENGLISH – SITE-WIDE MONTHLY PAGEVIEWS")
print("=" * 60)

months_to_fetch = [
    (2022, 3),   # baseline (pre-ChatGPT)
    (2022, 11),  # ChatGPT launch month
    (2023, 3),
    (2024, 3),
    (2025, 3),
    (2026, 3),   # latest
]

aggregate = {}
for y, m in months_to_fetch:
    views = monthly_aggregate(y, m)
    aggregate[(y, m)] = views
    print(f"  {y}-{m:02d}: {views:>13,}")
    time.sleep(0.4)

baseline = aggregate[(2022, 3)]
latest   = aggregate[(2026, 3)]
pct_change_site = (latest - baseline) / baseline * 100

print(f"\n  March 2022 → March 2026: {pct_change_site:+.1f}%")
print(f"  Absolute change: {latest - baseline:+,} views/month")


# ── 2. Per-article sample ───────────────────────────────────────────────────
print("\n" + "=" * 60)
print("PER-ARTICLE SAMPLE (March 2022 vs March 2026)")
print("=" * 60)
print(f"{'Article':<40} {'Mar-2022':>12} {'Mar-2026':>12} {'Change':>8}")
print("-" * 76)

results = []
for article in SAMPLE_PAGES:
    v22 = monthly_article(article, 2022, 3)
    time.sleep(0.3)
    v26 = monthly_article(article, 2026, 3)
    time.sleep(0.3)
    if v22 and v26:
        pct = (v26 - v22) / v22 * 100
        results.append((article, v22, v26, pct))
        print(f"  {article:<38} {v22:>12,} {v26:>12,} {pct:>+7.1f}%")
    else:
        print(f"  {article:<38} {'N/A':>12} {'N/A':>12} {'N/A':>8}")


# ── 3. Summary statistics ───────────────────────────────────────────────────
if results:
    total_22 = sum(r[1] for r in results)
    total_26 = sum(r[2] for r in results)
    pct_sample = (total_26 - total_22) / total_22 * 100
    sorted_pcts = sorted(r[3] for r in results)
    median_pct = sorted_pcts[len(sorted_pcts) // 2]
    declines  = [r for r in results if r[3] < 0]
    increases = [r for r in results if r[3] >= 0]
    top_declines = sorted(results, key=lambda x: x[3])[:5]
    top_gains    = sorted(results, key=lambda x: x[3], reverse=True)[:5]

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Sample size                : {len(results)} articles")
    print(f"  Articles with lower traffic: {len(declines)}/{len(results)}")
    print(f"  Articles with higher traffic:{len(increases)}/{len(results)}")
    print(f"  Sum of sample views Mar-2022: {total_22:,}")
    print(f"  Sum of sample views Mar-2026: {total_26:,}")
    print(f"  Sample aggregate change     : {pct_sample:+.1f}%")
    print(f"  Median per-article change   : {median_pct:+.1f}%")
    print(f"  Site-wide aggregate change  : {pct_change_site:+.1f}%")

    print("\n  Top 5 declines:")
    for a, v22, v26, p in top_declines:
        print(f"    {a:<38} {p:+.1f}%")

    print("\n  Top 5 gains:")
    for a, v22, v26, p in top_gains:
        print(f"    {a:<38} {p:+.1f}%")

    print()
    print("NOTE: ChatGPT launched November 2022. The site-wide trajectory")
    print("and per-article median give a rough bound on AI-chatbot displacement.")


# ── 4. Save to data.json ────────────────────────────────────────────────────
output = {
    "fetched_at": datetime.now(timezone.utc).isoformat(),
    "source": "Wikimedia Pageviews API (en.wikipedia, all-access, user agent)",
    "site_wide": {
        f"{y}-{m:02d}": views
        for (y, m), views in aggregate.items()
    },
    "site_wide_summary": {
        "baseline_month": "2022-03",
        "latest_month": "2026-03",
        "baseline_views": baseline,
        "latest_views": latest,
        "absolute_change": latest - baseline,
        "pct_change": round(pct_change_site, 2),
        "yoy_2025_to_2026": round((aggregate[(2026, 3)] - aggregate[(2025, 3)]) / aggregate[(2025, 3)] * 100, 2),
    },
    "articles": [
        {
            "article": a,
            "views_2022_03": v22,
            "views_2026_03": v26,
            "absolute_change": v26 - v22,
            "pct_change": round(pct, 2),
        }
        for a, v22, v26, pct in results
    ],
    "sample_summary": {
        "n_articles": len(results),
        "n_declining": len(declines),
        "n_increasing": len(increases),
        "total_views_2022_03": total_22,
        "total_views_2026_03": total_26,
        "aggregate_pct_change": round(pct_sample, 2),
        "median_pct_change": round(median_pct, 2),
        "top_5_declines": [{"article": a, "pct_change": round(p, 2)} for a, _, _, p in top_declines],
        "top_5_gains":    [{"article": a, "pct_change": round(p, 2)} for a, _, _, p in top_gains],
    },
}

with open("data.json", "w") as f:
    json.dump(output, f, indent=2)

print("Data saved to data.json")
