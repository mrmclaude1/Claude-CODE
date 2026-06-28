# Wealth Portfolio System

A complete, implementation-ready system for building a diversified portfolio of automated,
income-producing assets — designed as a family office for someone with a construction /
capital-projects / PM / automation background, $500 startup budget, and 1–10 hrs/week.

**Goal:** make active employment optional by building assets (not just income) that compound and
require progressively less of your time.

> ⚠️ Research-grounded estimates, not guarantees. Not financial or legal advice. Legal/tax items are
> flagged for professional review throughout.

---

## ▶ START HERE — Week 1 (the only thing that matters right now)

Do these five things this week. Everything else in this repo supports them.

1. **List 50 contacts** — contractors, GCs, estimators, suppliers, office managers from your career.
   Drop into a CRM (Airtable/Baserow). → `02-builds/build-1.../sales-and-outreach.md`
2. **Claim identity** — pick a name (`business-plan.md` has options), register the domain, start the
   LLC + EIN. → `02-builds/build-1.../templates/service-agreement-SOW.md` (checklist at bottom).
3. **Stand up n8n** on your Unraid server + build the **Bid Follow-Up Engine (BP-01)**.
   → `03-automation/n8n-workflow-blueprints.md`
4. **Send 10 outreaches** using the warm-intro template. Book 3 discovery calls.
   → `02-builds/build-1.../sales-and-outreach.md`
5. **Seed the portfolio** — open a brokerage account, set up an auto-buy, put in $100 to start the
   habit. → `02-builds/build-3.../investment-policy-statement.md`

Then follow `04-operations/weekly-operating-cadence.md` every week.

---

## Repository map

```
wealth-portfolio/
├── 00-EXECUTIVE-SUMMARY.md         ← read first: the decision, the math, the autonomy split
├── 01-portfolio/                   ← the analysis behind the strategy
│   ├── opportunity-scorecard.csv      22 opportunities scored on all your criteria
│   ├── scoring-methodology.md         how scores are weighted + source citations
│   └── ranking-rationale.md           why the top 3 win; what we rejected and why
├── 02-builds/
│   ├── build-1-construction-automation-service/   ← THE ENGINE (build first)
│   │   ├── business-plan.md            full plan: offer, ICP, stack, GTM, risks
│   │   ├── financial-model.csv         12-month P&L projection
│   │   ├── sales-and-outreach.md       90-day plan, templates, scripts, objections
│   │   ├── sops/delivery-sops.md       repeatable delivery checklists
│   │   └── templates/service-agreement-SOW.md   contract + legal setup checklist
│   ├── build-2-micro-saas/            ← THE ASSET (build after validation)
│   │   ├── product-spec.md             decision gate, MVP scope, stack, GTM
│   │   └── financial-model.csv         SaaS growth + exit-value projection
│   └── build-3-capital-portfolio/     ← THE WEALTH STORE (start now, passive)
│       ├── investment-policy-statement.md   allocation, rules, behavior guardrails
│       └── allocation-model.csv        10-year contribution/growth projection
├── 03-automation/                  ← the AI workforce + infrastructure
│   ├── agent-prompt-library.md        9 production-ready agent prompts
│   ├── n8n-workflow-blueprints.md     9 reusable workflow blueprints
│   └── competitor_monitor.py          working market-monitor script (Claude-powered)
├── 04-operations/                  ← how you run it in <10 hrs/week
│   ├── weekly-operating-cadence.md    your weekly/monthly/quarterly rhythm
│   ├── kpi-dashboard.md               what to measure + targets + red flags
│   └── continuous-improvement-loop.md the self-improving meta-system
└── 05-finance/                     ← where the money goes
    ├── capital-allocation-waterfall.md   profit-routing policy by stage
    └── consolidated-projection.csv       10-year net-worth model (up/base/down)
```

## The strategy in one diagram

```
  Construction AI Service (cash)  ──profit──►  Capital Portfolio (compounds)  ──►  Financial
        │                                          ▲              ▲                Independence
        └─validated patterns─►  Micro-SaaS  ──profit┘              │
                                (sellable asset)                Real Estate + Acquisitions
```

## Operating principles
1. **Vertical, not generic** — the construction niche is the moat.
2. **Service before software** — sell it manually, then automate what sells.
3. **Automate or delegate every repeatable task** — your time only goes to sales + decisions.
4. **Reinvest by the waterfall** — income → automation → assets → freedom.
5. **The portfolio survives partial failure** — diversified by design.
6. **Improve every month** — hours/client must fall; that's the alarm if it doesn't.

## How to use this with me (your AI operator)
Tell me to proceed and I can autonomously draft the landing-page copy, the 50-contact CRM schema,
the first outreach batch, and the BP-01 workflow config next. I'll bring anything outbound,
financial, or legal to you for approval. See the autonomy split in `00-EXECUTIVE-SUMMARY.md`.
