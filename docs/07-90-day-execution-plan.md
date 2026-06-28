# 07 — 90-Day Execution Plan

> Week-by-week from zero to validated flagship + a running passive engine. Designed for ≤5 hrs/week. Every item is tagged **[YOU]** (only you can do it) or **[DONE/AUTO]** (built or automatable).

**Guiding rule for the quarter: spend under $500, write zero production software until 3 people pay, and get the passive engine running on autopilot in week 1.**

---

## Phase 1 — Validate (Weeks 1–4): *Does anyone pay?*

The goal is not revenue yet — it's **evidence**. By day 30 you want a clear yes/no on whether subs will pay to make pay-app/waiver prep disappear.

| Week | Actions | Tag |
|---|---|---|
| **1** | Build a list of **40 target subcontractors** from your network + local AGC/ABC/CFMA rosters. Send the first **10 problem-discovery messages** (`templates/cold-outreach.md`). Open a **separate tax-reserve + business-reserve account**. Set up **one automatic monthly index-fund contribution** (passive engine live — even $50). | [YOU] |
| **2** | Send next **15 discovery messages**; book **4+ discovery calls**. Stand up **n8n on your Unraid server** + Claude API key. Stand up the **Research/Monitor agent**. | [YOU] + [AUTO] |
| **3** | Hold discovery calls; use the **discovery script** to quantify their pain (hours/month, days-to-pay, current tools). Send remaining outreach. Draft your **one-line value prop** from what you hear. | [YOU] |
| **4** | Synthesize: is pay-app/waiver the sharpest pain, or pivot to submittals? Pick the wedge. Build a **simple landing page** describing the DFY offer + price. Make **3 soft offers** ("I'll do this for you for $X/mo — want in?"). | [YOU] |

**Phase-1 gate:** ≥2 verbal yeses or 1 signed DFY client → proceed. Zero interest after 25+ quality conversations → pivot wedge or vertical (you've lost ~$150 and learned a lot). 

---

## Phase 2 — Deliver manually (Weeks 5–8): *Can you deliver value by hand?*

Now you fulfill **manually, with AI tools you control** (Rung 1). No customer-facing software. You are the product; the AI is your leverage.

| Week | Actions | Tag |
|---|---|---|
| **5** | Sign your **first DFY client** ($1,500/mo + setup, lawyer-reviewed terms). Onboard via `sops/sop-customer-onboarding.md`. Stand up the **Onboarding + Pay-app/waiver agents** in n8n. | [YOU] + [AUTO] |
| **6** | Deliver the first pay-app package end to end. **QA every field yourself.** Time the workflow; log `Hours_Per_Client`. Buy **E&O insurance** before the second client. | [YOU] |
| **7** | Sign **client #2**. Note every repeated manual step — these become automation targets. Ask client #1 for a **referral** + a metric for a case study. | [YOU] |
| **8** | Sign **client #3** → **Phase-1 risk F1 fully retired** (validated). Write the **first case study**. Start the **internal tool** that automates your most-repeated step (Rung 2 begins). | [YOU] |

**Phase-2 gate:** 3 paying clients, documented workflow, hours/client trending down → proceed to scale. 

---

## Phase 3 — Systematize & seed scale (Weeks 9–12): *Make it run without you*

Convert the manual service into a semi-automated machine and lay the rails for self-serve.

| Week | Actions | Tag |
|---|---|---|
| **9** | Finish the internal tool for the top-2 repeated steps. Hours/client should drop noticeably. Stand up the **Reporting agent** → auto-fill `models/kpi-dashboard.csv`. | [YOU] + [AUTO] |
| **10** | Join a **CFMA or AGC local chapter**; offer to speak/write on "getting paid faster." Set up the **referral ask** as a standard step. Run the **first monthly improvement ritual** (`docs/05`). | [YOU] |
| **11** | Build the **self-serve pilot** (Rung 3) for one friendly client at $499/mo. Create a **Capterra/GetApp listing**. Apply the **waterfall** to your first months of profit. | [YOU] |
| **12** | Review the quarter against KPIs. Decide: **double down** (it's working — pour reinvestment into automation + acquisition) or **adjust** (tweak wedge/ICP/pricing). Set Q2 targets. | [YOU] |

**Phase-3 gate:** semi-automated delivery, falling hours/client, ≥1 self-serve client, profit flowing onto the waterfall → you have a real L1 asset. 

---

## Parallel track (runs the whole 90 days, ~1 hr/month) — Passive Engine

| When | Action | Tag |
|---|---|---|
| Week 1 | Open/confirm brokerage; set **automatic monthly contribution** into a low-cost total-market index fund. | [YOU] |
| Week 1 | Confirm account-funding order (401k match → HSA → Roth → etc.) with your situation. | [YOU] |
| Monthly | Confirm the auto-buy fired (Friday block). Measure total crypto exposure before adding any. | [YOU] |
| Quarterly | Rebalance if any sleeve drifts >5 points. | [YOU] |

This runs from day one regardless of the business, because compounding rewards *time in market* — there is no reason to wait for the flagship.

---

## The first five things to do this week

1. **[YOU]** Open a separate tax-reserve account and set one automatic index-fund contribution (passive engine live).
2. **[YOU]** Build the 40-sub target list.
3. **[YOU]** Send the first 10 discovery messages (`templates/cold-outreach.md`).
4. **[AUTO]** Stand up n8n on Unraid + the Research/Monitor agent.
5. **[YOU]** Book your first 4 discovery calls.

---

## What I can do autonomously vs. what needs you

**Already done (in this repo):** strategy, scorecard, flagship design, financial model, automation architecture, all AI agent prompts, SOPs, outreach/proposal/contract templates, KPI dashboard, risk register, this plan.

**Needs you (cannot be delegated):**
- Sending real outreach from your identity and holding discovery calls (trust is the moat — that's the point).
- Opening/funding bank, brokerage, and Stripe accounts.
- Signing clients and QA-ing real project documents.
- Buying E&O insurance and getting service terms lawyer-reviewed before any document ships.
- The go/no-go decision at each phase gate.

**Can be automated next, on your say-so:** wiring the n8n flows to live data, scheduling the agent digests, and building the internal tool — I can write that code when you're ready to move from plan to build.
