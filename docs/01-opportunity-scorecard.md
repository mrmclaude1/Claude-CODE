# 01 — Opportunity Scorecard

> Every candidate opportunity, scored on weighted criteria, ranked, with the math fully exposed.
> Spreadsheet: `models/opportunity-scorecard.csv` (import to Sheets/Excel).

---

## 1. Scoring methodology

Each opportunity is scored **1–10** on ten criteria. Criteria are weighted by how much they matter *at your specific scale and constraints* (solo, <$500, ≤10 hrs/wk, moat-driven). The weighted overall is:

```
Overall = 0.18·Moat + 0.15·ProbSuccess + 0.13·Automation + 0.12·IncomePotential
        + 0.10·Scalability + 0.10·ExitValue + 0.08·TimeLight + 0.06·CostLight
        + 0.05·Durability + 0.03·LegalSafety
```

| Criterion | Weight | What a 10 means |
|---|---|---|
| **Moat / Defensibility** | 18% | Hard to copy; your domain authority is decisive. |
| **Probability of Success** | 15% | High base rate of reaching cash flow. |
| **Automation Potential** | 13% | Can run with minimal human touch. |
| **Income Potential** | 12% | Large absolute monthly cash flow at maturity. |
| **Scalability** | 10% | Revenue grows without proportional cost/time. |
| **Exit / Asset Value** | 10% | Sellable; a multiple-bearing asset. |
| **Time-Light** | 8% | Low ongoing labor (10 = passive). |
| **Cost-Light** | 6% | Low capital to start (10 = ~$0). |
| **Durability** | 5% | Survives trends/competition for years. |
| **Legal Safety** | 3% | Low regulatory/liability risk. |

**Why these weights:** at your scale, *distribution and defensibility* — not market size — decide outcomes. CB Insights' startup post-mortems put "no market need" (42%) and "ran out of cash" (29%) as the top two killers; both are distribution/validation failures. So Moat (can you reach and convince buyers) and Probability (validated demand) carry the most weight, with Automation third because it is the explicit mandate.

---

## 2. The ranking

| # | Opportunity | Layer | Startup | Hrs/wk | Yr1 MRR | Yr3 MRR | P(success) | **Score** |
|---|---|---|---|---|---|---|---|---|
| **1** | **AEC automation service → micro-SaaS (FLAGSHIP)** | L1→L2 | $300 | 5 | $2.5k | $12k | 65% | **8.18** |
| **2** | Contractor prequal/compliance-doc automation (wedge) | L1→L2 | $150 | 4 | $1.5k | $7k | 70% | **7.41** |
| 3 | Vertical construction newsletter + intel product | L2 | $200 | 5 | $0.8k | $6k | 55% | 7.21 |
| 4 | Construction bid/opportunity intelligence data product | L2 | $250 | 5 | $0.7k | $6.5k | 55% | 7.21 |
| 5 | Templates + licensing (estimating/Airtable/Notion) | L2 | $100 | 3 | $0.4k | $3k | 65% | 7.04 |
| 6 | Passive investing engine (index+dividend+crypto) | L3 | $0 | 1 | — | — | 90% | 6.99 |
| 7 | Project-controls / delay-claim consulting (high-ticket) | L1 | $150 | 4 | $3k | $8k | 70% | 6.75 |
| 8 | Contractor pay-per-lead generation | L2 | $300 | 5 | $0.6k | $5k | 55% | 6.75 |
| 9 | Info product / cohort course (PM + AI estimating) | L2 | $150 | 5 | $0.5k | $4k | 55% | 6.65 |
| 10 | Rental real estate (continue / BRRRR) | L4 | capital | 6 | $0.4k | $2.5k | 75% | 6.34 |
| 11 | Affiliate / SEO content site | L2 | $150 | 5 | $0.2k | $3.5k | 45% | 6.30 |
| 12 | Crypto core allocation (BTC/ETH) | L3 | $0 | 1 | — | — | 60% | 6.27 |
| 13 | Local service automation (CRM/booking for trades) | L1→L2 | $250 | 5 | $0.8k | $4k | 55% | 6.20 |
| 14 | SMB acquisition (boring cash-flow business) | L4 | capital | n/a | $2k | $15k | 55% | 6.02 |
| 15 | Dividend / covered-call income overlay | L3 | $0 | 1 | — | — | 60% | 5.63 |
| 16 | General AI automation agency (non-construction) | L1 | $300 | 8 | $2k | $8k | 45% | 5.58 |

*MRR = modeled monthly recurring revenue scenarios, not guarantees. See assumptions in §4 and `docs/06-risk-register.md`.*

---

## 3. What the ranking is telling you

**The top of the board is almost entirely construction-domain plays.** That is not a coincidence — it is the scorecard correctly rewarding your moat. The generic AI automation agency, the single most-hyped "make money with AI" play of 2025–26, ranks **dead last (5.58)** precisely because it has no moat: anyone with an n8n account competes with you, and the research shows that category already facing 20–30% price deflation and heavy saturation.

Three structural conclusions:

1. **Start with the narrowest, highest-moat wedge, not the biggest market.** The #2 play — *document-compliance automation* (prequal/pay-apps/waivers) — scores nearly as high as the flagship and is really its *entry wedge*: a single, painful, recurring, unglamorous workflow that incumbents ignore for small/mid contractors. `docs/02` runs a sub-scorecard across five candidate workflows and selects **pay-application + lien-waiver compliance** as the sharpest wedge. You land customers there, then expand into the broader flagship surface (submittals, RFIs, change orders, schedule analysis). **Strategy: lead with the wedge (#2), grow into the flagship (#1).**

2. **The passive engine (#6) is the highest-probability line on the board (90%)** and the lowest labor. It will never make you rich on its own, but it is the *destination* for the operating profits and the thing that ultimately makes employment optional. It runs in parallel from day one with ~1 hr/month.

3. **SMB acquisition (#14) is a trap relative to your mandate — for now.** It has the highest absolute income potential, but the research is blunt: ETA is "every bit as risky and time-consuming as building from scratch," ~32% of searches never close, and years 1–3 are full-time. It directly violates your low-labor constraint. **It is a Layer-4 move for *later*, funded by the waterfall, ideally as a semi-absentee owner — not a starting point.**

---

## 4. The winner, with full decision metadata

**Recommendation: Build the flagship (#1), entering through the document-compliance wedge (#2) — specifically pay-app + lien-waiver compliance, per the wedge selection in `docs/02`. Run the passive engine (#6) in parallel automatically.**

- **Evidence:** Construction is a ~$2T+ US industry that is famously under-digitized; small/mid GCs and subs are underserved by enterprise tools (Procore et al.) that are priced and built for large firms. Repetitive document-heavy workflows (prequal packets, COIs, RFIs, submittals, change orders, pay apps) are universal, painful, and deadline-driven — ideal automation targets. AI has collapsed the build cost of document-processing tools to near zero. Your domain authority solves the one thing AI can't: getting the meeting and being believed. *(Construction-market specifics are being finalized by a research pass and folded into `docs/02`.)*
- **Key assumptions:** (a) you can reach 30–50 target contractors via your existing network/associations in 60 days; (b) at least a few have a workflow painful enough to pay $300–$1,500/mo to make disappear; (c) you can deliver v1 as a *productized service* (you + AI behind the curtain) before writing any SaaS code.
- **Biggest risks:** (1) you fall in love with building and skip validation (the #1 startup killer); (2) sales cycle in construction is slow and relationship-driven; (3) liability if an automated document contains an error on a real project. Mitigations in `docs/06`.
- **Confidence: 7/10.** High confidence the *category* is right for you; medium confidence on which specific wedge wins — that's what the first 30 days of customer conversations resolve.
- **Downside case:** you spend ~$300 and ~8 weekends, validate that no one will pay, and walk away with a sharpened ICP, a reusable automation stack, and zero meaningful capital lost. Asymmetric: small, capped downside; large, compounding upside.
- **Next action:** execute Week 1 of `docs/07-90-day-execution-plan.md` — build the target list of 40 contractors and send the first 10 "problem-discovery" messages (template in `templates/cold-outreach.md`).
- **Autonomous vs. you:** *I have already built* the business design, automation architecture, agent prompts, outreach scripts, proposal, and financial model. *You must* send the outreach from your own identity, take the discovery calls, and make the go/no-go call — trust cannot be outsourced, and that's exactly the point.

---

## 5. Confidence & missing information

- **Highest confidence:** the *relative ranking* — domain plays beat generic plays for you. (9/10)
- **Medium confidence:** the absolute MRR figures. These are scenarios anchored to indie-SaaS benchmarks (first $1k MRR in 3–6 months, $5–10k MRR within ~12 months for solo founders who reach product–market fit), not your specific market. (5/10)
- **Missing information that the first 30 days will supply:** which exact workflow is most painful for *your* reachable contractors, what they currently pay for alternatives, and how fast their buying cycle moves. The 90-day plan is designed to buy this information cheaply before any real money or build time is committed.
