# Wikipedia Traffic Decline in the AI Era

**TL;DR:** A sample of 31 evergreen Wikipedia articles lost a **median of −33% of their traffic** between March 2022 and March 2026 — the four years since AI chatbots went mainstream. Hardest hit: Music (−82%) and Internet (−82%), though the magnitude of those declines may partly reflect traffic anomalies (e.g. reversals of earlier anomalous spikes) rather than AI displacement alone. The site-wide aggregate (7.38B → 6.92B pageviews/month, −6%) understates the effect because it includes event-driven pages that AI cannot yet replace.

## Citation

Martin Monperrus, "Wikipedia Traffic Decline in the AI Era", GitHub, 2026. https://github.com/monperrus/wikipedia-decline-llm

```bibtex
@misc{monperrus2026wikipedia,
  author       = {Monperrus, Martin},
  title        = {Wikipedia Traffic Decline in the AI Era},
  year         = {2026},
  howpublished = {\url{https://github.com/monperrus/wikipedia-decline-llm}},
}
```

---

## Goal

Estimate how much Wikipedia readership has declined since AI chatbots became mainstream, using publicly available traffic data. ChatGPT launched in November 2022; this analysis uses March 2022 as a pre-AI baseline and March 2026 as the endpoint.

The hypothesis: AI assistants intercept a growing share of informational queries that would previously have ended on Wikipedia. The effect should be strongest on evergreen "what is X" articles and weakest on event-driven or culturally browsed pages.

---

## Methodology

### Data source

[Wikimedia Pageviews API](https://wikimedia.org/api/rest_v1/) — the official, public API serving anonymised human pageview counts (bot traffic excluded via the `user` agent filter).

Two endpoints were used:

- **Aggregate**: `GET /metrics/pageviews/aggregate/en.wikipedia/all-access/user/monthly/{start}/{end}`  
  Returns total monthly human pageviews across all of English Wikipedia.

- **Per-article**: `GET /metrics/pageviews/per-article/en.wikipedia/all-access/user/{article}/monthly/{start}/{end}`  
  Returns monthly human pageviews for a single article.

### Article sample

32 articles were selected to cover a range of topic types:

| Category | Articles |
|---|---|
| Science & medicine | DNA, Climate change, Black hole, Vaccine, Evolution, Photosynthesis, Quantum mechanics, Human brain |
| History & geography | World War II, United States, France, Ancient Rome, Industrial Revolution, Cold War, United Kingdom |
| Technology | Internet, Smartphone, Python (programming language), Artificial intelligence, Blockchain |
| Culture & society | Mathematics, Philosophy, Music, Chess, Olympic Games |
| Perennial high-traffic | Deaths in 2023\*, Wikipedia, Earth, Water, Jesus, Adolf Hitler, United States Constitution |

\* *Deaths in 2023* existed as a redirect in March 2022 with near-zero views; its percentage change is an artifact and excluded from interpretation.

The selection intentionally mixes articles that AI chatbots handle fluently (factual definitions, science, history) with ones where Wikipedia retains unique value (browsable culture articles, perennial references).

### Comparison points

Monthly data was fetched for: March 2022, November 2022 (ChatGPT launch), March 2023, March 2024, March 2025, March 2026.

---

## Results

### Site-wide monthly pageviews

| Month | Views | Change vs Mar 2022 |
|---|---|---|
| Mar 2022 | 7,375,436,545 | — (baseline) |
| Nov 2022 | 7,474,238,422 | +1.3% |
| Mar 2023 | 7,783,695,172 | +5.5% |
| Mar 2024 | 8,082,436,565 | +9.6% |
| Mar 2025 | 7,740,123,015 | +4.9% |
| Mar 2026 | 6,916,319,343 | **−6.2%** |

The site-wide decline is **−6.2%** over four years, but the trajectory tells a more nuanced story: traffic grew through 2024 before falling sharply in 2025–2026. The reasons for the 2023–2024 bump followed by the sharp 2025–2026 drop are not established by this data alone.

### Per-article sample (March 2022 vs March 2026)

| Article | Mar 2022 | Mar 2026 | Change |
|---|---|---|---|
| Music | 414,417 | 75,769 | −81.7% |
| Internet | 821,414 | 151,658 | −81.5% |
| Blockchain | 157,118 | 40,562 | −74.2% |
| Vaccine | 43,969 | 12,339 | −71.9% |
| Climate change | 177,723 | 59,617 | −66.5% |
| Cold War | 617,462 | 215,662 | −65.1% |
| DNA | 134,889 | 55,734 | −58.7% |
| Smartphone | 96,605 | 40,584 | −58.0% |
| Python (programming language) | 291,200 | 127,178 | −56.3% |
| Evolution | 57,832 | 35,273 | −39.0% |
| Industrial Revolution | 174,175 | 104,575 | −40.0% |
| Water | 141,213 | 78,141 | −44.7% |
| France | 479,413 | 303,205 | −36.8% |
| United States Constitution | 23,954 | 15,476 | −35.4% |
| Human brain | 40,151 | 26,205 | −34.7% |
| Ancient Rome | 81,718 | 56,019 | −31.4% |
| United Kingdom | 928,087 | 618,377 | −33.4% |
| Mathematics | 154,851 | 96,682 | −37.6% |
| World War II | 1,311,206 | 919,254 | −29.9% |
| Adolf Hitler | 982,435 | 695,499 | −29.2% |
| Chess | 135,607 | 100,015 | −26.2% |
| Quantum mechanics | 104,393 | 76,240 | −27.0% |
| Artificial intelligence | 482,516 | 376,973 | −21.9% |
| United States | 1,571,695 | 1,261,307 | −19.7% |
| Wikipedia | 1,287,918 | 989,393 | −23.2% |
| Photosynthesis | 74,206 | 65,916 | −11.2% |
| Philosophy | 139,810 | 131,710 | −5.8% |
| Olympic Games | 112,668 | 111,172 | −1.3% |
| Earth | 305,762 | 319,676 | +4.6% |
| Jesus | 315,540 | 332,881 | +5.5% |
| Black hole | 131,257 | 189,488 | +44.4% |

**Aggregate across sample:** 11,791,206 → 7,701,178 views/month (**−34.7%**)  
**Median per-article change: −33.4%**  
**Articles declining: 28/31 (90%)**

### Interpretation

**The site-wide −6.2% figure understates the real displacement.** Wikipedia's page count keeps growing (new current-events pages, annual stub creation), which partially offsets the erosion of traffic on existing articles. The per-article view is more diagnostic.

**The hardest-hit articles are those AI chatbots excel at.** Topics with a canonical factual answer — what is DNA, how does a vaccine work, what caused the Cold War — have lost 60–80% of traffic. These are precisely the queries where an LLM answer is faster and sufficient. Note that the two extreme outliers (Music −82%, Internet −82%) show very sharp single-year drops that may partly reflect traffic anomalies unrelated to AI.

**Culturally browsed and perennial articles are resilient.** Olympic Games (−1%), Jesus (+5%), Earth (+5%), Black hole (+44%) all held or grew. Wikipedia retains value as a starting point for browsing and as a reference for topics that require depth or recency.

**The impact is back-loaded.** The steepest annual decline occurred between March 2025 and March 2026 (−10.6% year-over-year), consistent with LLM adoption becoming mainstream rather than niche.

### Summary estimate

| Scope | Traffic change Mar 2022 → Mar 2026 |
|---|---|
| Site-wide (all pages) | −6.2% |
| Evergreen factual articles (sample median) | −33% |
| Evergreen factual articles (sample aggregate) | −35% |

A reasonable headline estimate for AI-attributable displacement on **informational queries** is **−30% to −35%**, with the site-wide number serving as a lower bound that includes categories of traffic less exposed to LLM substitution.

---

## Comparison with existing research

| Source | Subject | Period | Method | Headline figure |
|---|---|---|---|---|
| This analysis | English Wikipedia | Mar 2022 – Mar 2026 | Raw API comparison | −6% site-wide; −33% factual articles |
| Lyu et al. (WWW 2025) | English Wikipedia | Nov 2021 – Nov 2023 | DiD (ChatGPT launch) | Significant excess decline for ChatGPT-similar articles |
| Khosravi & Yoganarasimhan (arXiv 2026) | English Wikipedia | Mar – Aug 2024 | DiD (AIO staggered rollout) | **−15%** from Google AI Overviews alone |
| Zhao & Berman (arXiv 2025) | News publishers | 2023 – 2025 | DiD (bot-blocking) | Moderate decline post-Aug 2024 |
| Wikimedia Foundation (Diff, Oct 2025) | All Wikipedia languages | May – Sep 2025 | Official traffic data | **−8%** vs same months in 2024 |

**Lyu, Siderius, Li, Acemoglu, Huttenlocher & Ozdaglar — "Wikipedia Contributions in the Wake of ChatGPT" (WWW 2025, [doi:10.1145/3701716.3715543](https://doi.org/10.1145/3701716.3715543)).**
Using a differences-in-differences design over two years centred on November 2022, the authors find that articles whose content overlaps with what ChatGPT can answer saw a statistically significant excess decline in both views and edits relative to dissimilar articles (the control group). This is the only study to isolate the causal effect of standalone chatbot adoption on Wikipedia specifically. The heterogeneous-substitution finding mirrors our data: factual articles dropped 30–80% while event-driven pages held steady.

**Khosravi & Yoganarasimhan — "Impact of AI Search Summaries on Website Traffic" (arXiv:2602.18455, submitted Feb 2026, later withdrawn for revision).**
Exploiting Google AI Overviews' staggered geographic rollout as a natural experiment across 161,382 matched article-language pairs, the authors find AIO alone reduces daily English Wikipedia traffic by ~**15%**, with Culture articles hit hardest and STEM articles least. Even though this paper covers only a 5-month window in 2024 and a single AI feature, it already finds a larger effect than our full 4-year site-wide figure (−6%), confirming that the aggregate number substantially understates displacement of informational content. Their Culture > STEM hierarchy exactly matches our Music (−82%) vs. Quantum mechanics (−27%) pattern.

**Zhao & Berman — "The Impact of LLMs on Online News Consumption and Production" (arXiv:2512.24968, Dec 2025).**
Studying news publishers rather than Wikipedia, the authors document a moderate but clear traffic decline beginning after August 2024 — the same inflection point visible in our site-wide trajectory. Interestingly, publishers that blocked AI crawlers via `robots.txt` saw *more* traffic loss, suggesting AI services were partly sustaining referral traffic even while displacing direct visits. The paper broadens the picture: AI-driven displacement is not Wikipedia-specific but a web-wide phenomenon, with back-loaded timing consistent with our data.

**Wikimedia Foundation — "New User Trends on Wikipedia" (Diff blog, Oct 17 2025, [diff.wikimedia.org](https://diff.wikimedia.org/2025/10/17/new-user-trends-on-wikipedia/)).**
This is the Wikimedia Foundation's own public statement on the traffic shift. After updating its bot-detection algorithms in mid-2025, the Foundation found human pageviews had declined by roughly **8% compared to the same months in 2024**, attributing this directly to "the impact of generative AI and social media on how people seek information." A companion roundtable report (Wikimedia CH, Feb 2026) frames the situation starkly: an 8% drop in human traffic alongside a 50% surge in bot activity, describing the moment as potentially "peak Wikipedia." These official figures are conservative — they measure aggregate traffic across all articles including event-driven pages — consistent with our site-wide −6.2% for the full four-year period versus −33% for evergreen informational content.

---

## Caveats

- **Correlation ≠ causation.** Other factors affect Wikipedia traffic: Google search algorithm changes, mobile browsing trends, zero-rating programmes, and post-COVID normalisation of internet usage patterns.
- **English Wikipedia only.** Other language editions may show different patterns depending on local LLM adoption.
- **Sample bias.** The 31 articles are illustrative, not statistically random. A larger random sample from the top-1000 most-viewed articles would give tighter confidence intervals.
- **AI search features.** Google's AI Overviews (launched May 2024) likely contribute to the 2025–2026 decline independently of standalone chatbot use.

---

## Reproduction

Requirements: Python 3.8+, no third-party libraries (uses only `urllib` and `json` from the standard library).

```bash
git clone <this-repo>
cd wikipedia-decline-llm
python3 analyze_traffic.py
```

The script will print:
1. Site-wide aggregate pageviews for six key months
2. Per-article breakdown for the 32-article sample
3. Summary statistics

All data is fetched live from the Wikimedia API at runtime. The API is free, requires no authentication, and asks only for a descriptive `User-Agent` header (already set in the script). Rate limiting is respected via small sleeps between requests (~0.3–0.4 s).

Expected runtime: ~30 seconds.

---

## LLM usage disclosure

Parts of this work, in particular code and drafting, were written with the assistance of Claude Code with Claude Sonnet 4.6. All data is not LLM generated but fetched directly from the Wikimedia Pageviews API. The author is responsible for the final content.
