# 00 — Strategy & Operating System

> The thesis, the portfolio architecture, and the rules the machine runs on.

---

## 1. The strategic insight

Most "build wealth with AI" plans fail because they put a generalist into a red ocean (generic AI agency, generic SaaS, generic newsletter) where the only differentiation is hustle. You have something almost no one in that crowd has:

**An expensive-to-replicate moat: 10+ years of credible authority in construction and capital projects.**

That moat matters because the hardest part of any B2B business is not building the product — AI has collapsed that cost — it is **distribution and trust**. You can get a contractor on the phone, speak their language (RFIs, submittals, schedule float, retainage, change orders, pay apps), and be believed. A 25-year-old prompt engineer cannot. That asymmetry is the whole game.

So the portfolio is deliberately **barbell-shaped**:

```
        CONCENTRATED RISK                         ZERO-LABOR COMPOUNDING
   ┌──────────────────────────┐            ┌──────────────────────────────┐
   │  FLAGSHIP OPERATING BIZ  │            │   PASSIVE INVESTING ENGINE   │
   │  Construction automation │  profits   │  Index + Dividend + Crypto   │
   │  (productized → SaaS)    │ ─────────▶ │  + Real Estate + (later) SMB │
   │  High effort, high moat  │            │  Near-zero labor, durable    │
   └──────────────────────────┘            └──────────────────────────────┘
        Your time goes here                     Your money goes here
```

The operating business is where your *time* compounds into equity and cash flow. The passive engine is where that cash flow compounds into freedom with no further labor. The waterfall between them (`docs/04`) is the engine of independence.

---

## 2. Portfolio architecture — the four layers

| Layer | Purpose | Labor | Examples | Time horizon |
|---|---|---|---|---|
| **L1 — Cash Engine** | Generate surplus cash from your edge | High → declining (you automate it) | Flagship AEC service/SaaS; high-ticket project-controls consulting | 0–18 mo to cash flow |
| **L2 — Recurring Assets** | Convert cash into self-running recurring revenue | Low | Micro-SaaS, data/intel products, templates & licensing | 6–36 mo |
| **L3 — Passive Markets** | Compound surplus with ~zero labor | ~Zero | Index funds, dividend growth, crypto core, REITs | Forever |
| **L4 — Ownership** | Buy durable cash-flowing assets | Medium, episodic | Rental real estate, SMB acquisition | 2–7 yr |

You build **outward and downward**: L1 funds L2, L1+L2 cash flow funds L3, and L3 surplus eventually funds L4. You never skip a layer with money you don't have.

---

## 3. Operating principles (the rules)

1. **Moat before scale.** Pursue the opportunity where your unfair advantage is largest *first*, even if a "bigger" market exists elsewhere. Defensibility beats TAM at your scale.
2. **Automation is a precondition, not a feature.** Any task that recurs weekly gets a documented SOP; any SOP that runs >2×/month gets automated or delegated to an AI agent. Manual-forever work is a design failure.
3. **Sell before you build.** No code or product is built before a paying customer (or a signed letter of intent) validates demand. AI makes building cheap; *demand* is the scarce resource.
4. **Recurring over one-time.** Always prefer revenue that renews. A $300/mo retainer is worth more than a $2,000 one-off because it compounds and is financeable/sellable.
5. **Own the asset, not the job.** Optimize for things that keep their value when you stop touching them (subscriptions, equity, IP, portfolios) over things that pay only while you work (consulting hours).
6. **Reversible bets are cheap; make them fast.** Under the $500 ceiling, most experiments are reversible. Decide quickly, run the experiment, kill or double-down on evidence.
7. **One active business at a time.** Splitting 5–10 hrs/week across three startups guarantees all three fail. Concentrate L1 effort until it is automated, then start the next.
8. **Profit is sacred; recycle it on the waterfall.** Business profit is not spending money — it is fuel for L3/L4. The waterfall (`docs/04`) governs it.

---

## 4. The decision framework (how every choice gets made)

For any fork, score each option with the **weighted scorecard** in `docs/01` and apply:

```
Decision = argmax( Weighted Score )  subject to:
  - Startup cost ≤ $500 (or justified exception)
  - Net new weekly time ≤ remaining time budget
  - Legal/regulatory risk = LOW
  - Reversibility = HIGH (prefer)  unless conviction ≥ 8/10
```

Every recommendation in this repo ships with the required decision metadata:
**evidence · key assumptions · biggest risks · confidence (1–10) · next action · autonomous-vs-needs-you.**

---

## 5. Success metrics (the dashboard you actually watch)

Tracked monthly in `models/kpi-dashboard.csv`:

| Metric | Why it matters | Target trajectory |
|---|---|---|
| **MRR (recurring)** | The core compounding number | ↑ every month |
| **Net cash flow** | Surplus available for the waterfall | ↑ |
| **Automation %** | (Automated tasks ÷ total recurring tasks) | → 80%+ |
| **Hours worked / week** | Time freedom — should *fall* as MRR rises | ↓ toward ≤5 |
| **Revenue per hour** | Leverage indicator | ↑ |
| **Passive income (L3+L4)** | Distance to independence | ↑ |
| **FI coverage ratio** | Passive income ÷ living expenses | → 1.0 = optional employment |
| **Net worth** | The scoreboard | ↑ |

**The north-star equation:** *Financial independence is reached when L3+L4 passive income ≥ monthly expenses.* Everything else is in service of driving that ratio to 1.0 as fast as risk-adjusted prudence allows.

---

## 6. The weekly operating rhythm (your ≤5 hrs)

A fixed cadence keeps the whole system advancing on minimal time. Full version in `sops/sop-weekly-operating-rhythm.md`.

| Block | Time | Focus |
|---|---|---|
| **Monday — Pipeline** | 60 min | Review AI-generated leads; approve/send outreach; advance deals. |
| **Wednesday — Delivery** | 90 min | Service delivery / product work for paying customers (shrinks as you automate). |
| **Friday — Improve & Invest** | 60 min | Review KPI dashboard; run the improvement loop's outputs; execute the monthly investment buy. |
| **Async — Approvals** | ~30 min | Approve AI agent drafts (emails, proposals, content) throughout the week. |

Total ≈ 4 hrs/week steady-state. The Wednesday block is the one automation is designed to shrink toward zero.

---

## 7. How the pieces connect

```
        ┌─────────────────────────────────────────────────────────┐
        │  CONTINUOUS IMPROVEMENT LOOP (docs/05)                   │
        │  research · monitor · optimize · rewrite SOPs · suggest  │
        └───────────────┬─────────────────────────────────────────┘
                        │ feeds insights into everything
   ┌────────────────────▼───────────────────┐
   │  L1 FLAGSHIP (docs/02)                  │   AI AGENTS (automation/)
   │  AEC automation service → micro-SaaS    │◀──research·sales·support·
   │  KPIs ▶ models/kpi-dashboard.csv        │   content·reporting
   └────────────────────┬───────────────────┘
                        │ net profit
   ┌────────────────────▼───────────────────┐
   │  CAPITAL ALLOCATION WATERFALL (docs/04) │
   └────────────────────┬───────────────────┘
                        │ allocates to
   ┌────────────────────▼───────────────────┐
   │  L3 PASSIVE ENGINE (docs/03)            │
   │  index · dividend · crypto · RE         │
   └─────────────────────────────────────────┘
```

Next: open `docs/01-opportunity-scorecard.md` to see why the flagship wins on the numbers.
