# Build 1 — Construction & Trades AI Automation Service

**Working name:** *BuiltFlow* (placeholder — see naming options below)
**One-liner:** "I automate the back-office paperwork that's drowning contractors — bids, RFIs,
submittals, change orders, invoicing follow-up — so owners get nights and weekends back."

This is the **engine** of the portfolio: fastest cash flow, funds everything else, and surfaces the
exact problems Build 2 (SaaS) will productize.

---

## 1. The opportunity (evidence-based)

- Construction/trades is one of the **least-digitized** sectors; owners run complex workflows on
  paper, email, and spreadsheets (source: aimagicx, superframeworks 2026).
- Contractors will pay **$500–$2,000/mo** for tools/services that recover estimator and admin time;
  estimator time alone can be $2,000+ per bid (superframeworks).
- AI-automation retainers for SMBs run **$1,000–$3,500/mo**, with project setup fees of
  **$9,000–$14,000** and **~5-month client payback** (arsum, taskip, digitalagencynetwork).
- **61% of automation-vendor dissatisfaction is scope/change-management failure, not tech** (PwC
  2025, via arsum). This is the gap your PM background closes — and almost no competitor has it.

**Why you win:** You speak the customer's language (you *were* the customer). You can read a set of
plans, understand a submittal log, talk schedule and budget fluently, and you negotiate. AI-agency
operators who can build n8n flows usually can't do that; contractors who understand the pain can't
build automation. You sit in the rare overlap.

## 2. Customer (ICP — Ideal Customer Profile)

- **Who:** Specialty trade contractors and small GCs, **$1M–$15M revenue, 5–40 employees.**
- **Decision maker:** Owner / operations manager / office manager (often the owner's spouse runs
  the office — a key, underrated buyer).
- **Trades to start (highest paperwork pain):** electrical, mechanical/HVAC, plumbing, concrete,
  commercial roofing, glazing, fire protection.
- **Trigger events:** growing fast and drowning in admin; lost a bid due to slow turnaround; an
  office person quit; getting audited/behind on collections.
- **Where they are:** local/regional — your geography is an advantage, not a limit. Also: trade
  association directories, supply-house counters, BlueBeam/Procore user groups, local FB groups.

## 3. Offer architecture (productized, not custom consulting)

Productize ruthlessly — fixed scopes, fixed prices, repeatable delivery. Three tiers:

| Tier | Setup (one-time) | Retainer (monthly) | What it includes |
|---|---:|---:|---|
| **Starter — "One Workflow"** | $1,500 | $300 | Automate ONE painful workflow (e.g., bid follow-up sequence, or RFI/submittal logging). 1 revision. |
| **Operator — "Back-Office"** | $4,500 | $750 | 3 workflows + a simple ops dashboard + monthly tune-up + Slack/email support. |
| **Partner — "Run My Ops"** | $9,000 | $1,500 | 5+ workflows, AI inbox/quote follow-up agent, KPI dashboard, quarterly roadmap, priority support. |

**Productized "starter workflows" menu (pick from these — don't invent custom each time):**
1. **Bid/quote follow-up engine** — auto-sequence emails/texts after a quote goes out; logs
   responses; flags hot leads. (Directly recovers lost revenue → easiest sale.)
2. **RFI / submittal / change-order tracker** — intake form → auto-logged → reminders → status
   dashboard. (Their #1 paperwork headache.)
3. **AR / collections chaser** — overdue invoice detection → polite escalating reminder sequence →
   owner gets a "needs a call" shortlist. (Pays for itself in recovered cash.)
4. **Job intake → estimate prep** — standardize incoming requests; AI drafts a first-pass scope and
   line-item checklist from a description/photos for the estimator to finish.
5. **Subcontractor/vendor onboarding & COI tracking** — collect W-9s, insurance certs, track
   expirations, auto-remind. (Compliance pain = high willingness to pay.)
6. **Daily report / photo log automation** — field texts photos → auto-compiled daily report → PDF
   to owner/GC.

Each of these is a **template you build once and re-deploy**, which is what makes delivery scalable
and is the seed list for Build 2 (whichever one sells the most becomes the SaaS).

## 4. Revenue model

- **Mix:** one-time setup fee (cash to fund operations) + monthly retainer (the compounding MRR).
- **Target by month 12:** ~8 active retainers averaging ~$750 + occasional setups ≈ **~$9k/mo
  recurring** plus lumpy setup revenue. This is the scorecard figure and it's deliberately
  conservative (8 clients is very achievable in a regional vertical with referrals).
- **Value-based upsell:** when a workflow demonstrably recovers $X/mo, price the next one against
  that value, not against your time (taskip value-based model).

## 5. Technology stack (mostly things you own / near-free)

| Function | Tool | Cost | Notes |
|---|---|---|---|
| Automation orchestration | **n8n** (self-host on your Unraid server) | $0 | Your unfair infra advantage — no per-task SaaS fees. |
| AI reasoning | Claude API + your existing subs | usage | Drafting, classification, extraction, summarization. |
| CRM / pipeline | n8n + Airtable or Baserow (self-host) | $0–$20 | Track leads, clients, workflows. |
| Email/SMS sending | Resend/SES + Twilio | usage | Pennies per message. |
| Client dashboards | Metabase or Appsmith (self-host) or simple n8n→Sheets | $0 | Runs on Unraid. |
| Contracts/e-sign | Documenso (self-host) or PandaDoc free tier | $0 | |
| Payments | Stripe | 2.9%+30¢ | Invoices + subscriptions. |
| Website/landing | Astro/Next static page on Cloudflare Pages | $0 | One page is enough to start. |

**Your Unraid server hosting n8n is a genuine margin advantage** — competitors pay Zapier/Make
per-task fees that destroy margin at scale; you don't.

> Detailed automation architecture and agent prompts live in `03-automation/`.

## 6. Customer acquisition (the part that actually decides success)

Ranked by expected ROI for a solo, time-constrained operator with domain credibility:

1. **Warm network + direct outreach (PRIMARY).** You know contractors, GCs, suppliers, vendors from
   your career. Make a list of 50. Personal outreach beats everything. Script + sequence in
   `sales-and-outreach.md`.
2. **Referral engine.** Every happy client → ask for 2 intros. Offer one free workflow tune-up for
   a referral that closes. Construction runs on word of mouth.
3. **"Teardown" content.** Short LinkedIn/email posts: "Here's the bid-follow-up system I built for
   a $4M electrical contractor — recovered ~$6k/mo in dead quotes." Specific, credible, vertical.
4. **Local trade associations / supply houses.** Lunch-and-learns, association newsletters. Cheap,
   high-trust.
5. **Niche cold email** (later, automated) — only after you have 2–3 case studies to point to.

We do **not** rely on paid ads early — your advantage is trust and specificity, which ads dilute.

## 7. KPIs (see `04-operations/kpi-dashboard.md` for the full board)

- Outreach: contacts/week, discovery calls booked, call→proposal rate, proposal→close rate.
- Revenue: MRR, setup revenue, ARPU, MRR churn, LTV.
- Delivery: time-to-launch per workflow, hours/client/month (must trend DOWN — that's the moat).
- Health: NPS / "would you refer", referrals generated.

## 8. Growth strategy

- **Phase 1 (0→3 clients):** do it semi-manually, document everything, find the repeatable winner.
- **Phase 2 (3→8 clients):** templatize delivery, raise prices, build the referral loop, hire a VA
  (~$6–$10/hr) for admin once retainers cover it.
- **Phase 3 (8+):** productize the top workflow into Build 2 (SaaS); the service becomes both a
  cash cow and a SaaS sales channel ("done-for-you" upsell on top of the software).

## 9. Risk analysis

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| You don't do the outreach (the real killer) | Med | High | Weekly cadence (04-operations) makes it a habit, not a decision. Time-box 2 hrs/wk to outreach, non-negotiable. |
| Slow construction sales cycles | Med | Med | Lead with revenue-recovering workflows (bid follow-up, AR) that show ROI fast. |
| Client churns after setup | Med | Med | Retainer = ongoing tuning + dashboard they check daily → sticky. Tie retainer to a live, changing workflow. |
| You become the bottleneck (time) | Med | High | Templatize + VA + self-hosted automation. Track hours/client; it must fall every month. |
| Scope creep / "make it do X too" | High | Med | Fixed scopes, change-order pricing (you're a PM — enforce it). This is literally your edge. |
| Liability if an automation errors (e.g., misses a COI expiry) | Low | Med | Clear SLA + "human-in-the-loop for compliance-critical steps" + liability cap in contract (see template). |

## 10. Naming options (pick one, check domain)

BuiltFlow · TradeFlow Ops · SiteDesk · PunchList AI · Foreman (ops) · BackOffice for Builders ·
Hardhat Automation · Plumb Ops · Bid Bridge · CrewDesk.
*(Avoid anything that implies you're a licensed GC or engineer-of-record — see legal note in
the service agreement template.)*

---

### Confidence: 8/10
The market is real and your moat is real. The only thing standing between this plan and
$5k–$9k/mo is consistent weekly outreach for the first 90 days. Everything else is built for you in
this repo.
