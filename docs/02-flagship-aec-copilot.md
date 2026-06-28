# 02 — Flagship: Construction Document-Compliance Automation

> The #1 asset (scorecard 8.18). A productized service that becomes a micro-SaaS, built on the one moat AI can't copy: your construction-domain authority.

---

## 1. Why construction, why now

The market data makes the case better than any pitch:

- **Construction is the second-least-digitized of 22 industries**, spends **<1% of revenue on IT**, and **~65% of firms still estimate in spreadsheets**. ([McKinsey](https://www.mckinsey.com/capabilities/operations/our-insights/imagining-constructions-digital-future))
- **99.94% of US construction firms have <500 employees** — an enormously fragmented, underserved long tail that enterprise tools (Procore, Autodesk) price *out*, not *for*. ([Construction Dive](https://www.constructiondive.com/news/despite-50b-of-investment-contech-is-being-held-back-by-its-fragmented-cu/652240/))
- The industry burns **>$177B/yr** on non-productive work — pros lose **~14 hrs/week (~35% of time)** to finding data, resolving conflicts, and rework. ([PlanGrid/FMI](https://www.prnewswire.com/news-releases/new-research-from-plangrid-and-fmi-identifies-factors-costing-the-construction-industry-more-than-177-billion-annually-300689826.html))
- AI has collapsed the cost of building document-processing tools to near zero — yet the research found **AI is barely used in submittal review, lien-waiver compliance, pay-app reconciliation, or change orders.** Most "automation" here is still dumb forms, not LLMs.

The gap is screaming: a huge population of small contractors, doing painful document work by hand, ignored by enterprise vendors, with almost no AI applied to their most regulation-heavy workflows. **That gap is exactly the shape of your moat.**

---

## 2. The wedge decision (don't boil the ocean — pick one workflow)

The research surfaced five viable entry workflows. Land on **one**, dominate it, then expand. Mini-scorecard (1–5, higher better):

| Wedge workflow | Pain/$ | Recurring-native | AI gap | Insider moat | Fast ROI proof | **Total** |
|---|---|---|---|---|---|---|
| **Pay-app + lien-waiver compliance (sub-first)** | 5 | **5** | 5 | **5** | **5** | **25** |
| Submittal / spec review | 5 | 4 | 5 | 4 | 4 | 22 |
| Bid leveling | 4 | 4 | 4 | 4 | 4 | 20 |
| AI takeoff / estimating | 5 | 3 | 3 | 3 | 4 | 18 |
| Subcontractor prequalification | 4 | 4 | 4 | 5 | 3 | 20 |

### Winner: **Pay-Application + Lien-Waiver Compliance Automation, sub-first.**

Why it wins on every axis that matters:

- **Recurring by nature.** Pay applications happen *every billing cycle, every project, forever.* The workflow itself is a subscription — no convincing the customer to "keep using it."
- **Brutal, quantified pain.** Slow payments cost the industry **~$280B (2024)**; subs wait an average of **56 days**, **86% of subs float payroll personally**, and sector DSO is **~83 days**. The bottleneck is manual generation/matching of AIA **G702/G703** forms, schedules of values, retainage math, and **lien waivers** — not disputes. ([Rabbet](https://rabbet.com/reports/construction-payments-2024))
- **Fast, provable ROI** — the #1 thing contractors demand before buying (62% said they would *not* add software in 2024; long payback is the top blocker). "Get paid 2 weeks faster" is a one-meeting sell. ([CFMA](https://cfma.org/articles/construction-market-outlook-for-2-24-gc-feedback-on-technology-adoption-labor-shortages-and-more))
- **Deepest insider moat.** This workflow is a minefield of domain rules a generalist gets *wrong*: AIA G702/G703 mechanics, Schedule of Values and **retainage**, and **lien-waiver law** — 4 waiver types, ~12 states mandating statutory forms, TX/WY/MS notarization quirks, GA's 90-day auto-conversion. ([AIA forms](https://www.autodesk.com/blogs/construction/g702-g703-forms-aia-billing/), [lien waivers](https://terrapincg.com/news/construction-lien-waiver-types-guide)) You know this cold; a prompt engineer does not.
- **Incumbents are weak here for small subs.** The sub-first tool (Siteline) is quote-gated; GCPay charges $15/txn; Textura is per-project and GC-centric. Transparent, flat, sub-first pricing is an open lane. ([pricing survey](https://www.levelset.com/pricing/))

**Documented alternative:** if early discovery calls reveal pay-app pain is "owned" by an existing tool in your network, pivot to **submittal review** (35% of submittals rejected on first pass, ~$805 each, AI barely applied — [BuildSync](https://buildsync.ai/resources/complete-guide-to-construction-submittal-reviews)). Same playbook, different document.

---

## 3. Business & revenue model — the productization ladder

You climb three rungs. Each de-risks the next. **Never skip a rung.**

```
 RUNG 1: PRODUCTIZED SERVICE  (Months 0–4)   "Done-for-you" — you + AI behind a curtain
   → Validate demand with real dollars BEFORE building software.
   → You manually run pay-apps/waivers for 3–5 subs using AI tools you control.
   → Revenue: $750–$2,000/mo per client retainer. Margin secondary; LEARNING is the product.

 RUNG 2: PRODUCTIZED SERVICE + INTERNAL TOOL  (Months 4–10)
   → Codify the repeated steps into your own software you operate.
   → Same price, but your hours/client drop sharply → margin expands, capacity grows.

 RUNG 3: MICRO-SAAS / SELF-SERVE  (Months 10+)
   → Expose the tool to customers directly. $200–$600/mo flat, unlimited users.
   → Service tier remains for premium clients who want it done for them.
```

This ladder is the whole strategy in miniature: **sell before you build** (Rung 1 proves people pay), **automate to expand margin** (Rung 2 buys back your hours), **productize to scale** (Rung 3 decouples revenue from your time). The research is explicit that "no market need" kills 42% of startups and validation-first founders reach revenue ~40% faster — Rung 1 is the antidote.

---

## 4. Ideal customer profile (ICP)

| Attribute | Target |
|---|---|
| **Who** | Specialty **subcontractors** ($2M–$30M revenue) — electrical, mechanical, concrete, drywall, sitework. Sub-first because they feel payment pain hardest and decide faster (owner-led, not committee). |
| **Decision-maker** | Owner, controller, or office/billing manager — *not* a 10-person buying committee. |
| **Why they buy** | "I spend X hours every month assembling pay-app packages and chasing waivers, and I still get paid late." |
| **Where they are** | Your existing network first; then AGC (26k firms) / ABC (21k firms, 70 chapters) chapters and **CFMA** (the CFO/controller channel — and CFMA *admits software vendors as Associate Members*). ([CFMA/AGC](https://www.agc.org/)) |
| **Anti-ICP (avoid early)** | Large GCs with Procore/Textura already embedded (long committee sales, integration burden, 6–24 mo cycles). |

---

## 5. Pricing

Anchored to research (SMB construction SaaS clusters **$200–$1,000/mo flat**; productized DFY retainers **$2k–$10k/mo + setup**; realistic *net* margins 20–35% with human QA — not the mythical 80%).

| Tier | Rung | Price | What they get |
|---|---|---|---|
| **Done-for-you** | 1–2 | **$1,500/mo** + $750 setup | You/AI assemble every pay-app package and waiver, ready to submit. |
| **Co-pilot** | 3 | **$499/mo** flat, unlimited users | Self-serve tool; AI drafts the package, they review/submit. |
| **Starter** | 3 | **$199/mo** | Single-entity, capped projects; on-ramp for the smallest subs. |

Land DFY first (high touch, high learning, fast cash), migrate clients down-price to software as Rung 3 matures — counterintuitively *raising* your margin and capacity while *lowering* their bill. ROI framing always leads: *"Pay $499 to get paid two weeks sooner on $400k of monthly billing."*

---

## 6. Customer acquisition (referrals and trust, not ads)

Construction is a **relationship and committee sale; cycles run 6–24 months and referrals cut CAC most.** ([Digital Clarity](https://digital-clarity.com/blog/how-construction-tech-companies-can-shorten-sales-cycles-in-a-relationship-driven-market/)) The plan respects that:

1. **Warm network first (Month 1).** Your existing GC/sub/vendor relationships are the unfair advantage. 20–40 problem-discovery conversations → first 3–5 DFY clients. Scripts in `templates/cold-outreach.md`.
2. **Referrals engineered in.** Every happy client is asked for one intro; offer a referral month-free. Referral is the cheapest CAC channel in the data.
3. **Association/chapter presence (Months 2–6).** Join a CFMA/AGC/ABC local chapter as a member; speak/write on "getting paid faster." This is a credibility channel a generalist can't access.
4. **Directory visibility (Months 3+).** A Capterra/GetApp/Software Advice listing — that's where contractors actually discover software. ([Capterra](https://www.capterra.com/resources/construction-software-buyer-insight/))
5. **Content as proof, not volume.** One sharp case study ("Sub X cut pay-app prep from 9 hrs to 1 and got paid 11 days faster") outperforms a content mill. Multi-channel LinkedIn + personalized email doubles response. ([Building Radar](https://www.buildingradar.com/construction-blog/linkedin-outreach-strategies-that-actually-work-for-construction-reps))

**No paid ads early.** CAC is too high and trust too low for a cold-traffic motion in this vertical.

---

## 7. Technology & automation architecture

Built on the cheap, solo-founder stack the research validated (full diagram in `automation/README.md`):

```
  Intake (client docs: SOV, contracts, prior pay-apps)
        │   email / shared Drive / simple upload form
        ▼
  ┌─────────────────────────────────────────────────────────┐
  │  ORCHESTRATION:  n8n (self-hosted on your Unraid server) │  ← $0; you already own it
  │  • Document parse → LLM extract (line items, retainage)  │
  │  • Generate G702/G703 + Schedule of Values              │
  │  • Match & generate correct lien waiver by state/type   │
  │  • Compliance check (dates, signatures, statutory form) │
  │  • Human-QA gate (you approve) → output package          │
  └─────────────────────────────────────────────────────────┘
        │
        ▼
  Delivery (submit-ready PDF package) + Stripe billing + CRM update
```

| Layer | Tool | Cost |
|---|---|---|
| Orchestration | **n8n self-hosted on your Unraid server** | $0 (you own it) |
| LLM | Claude API (document extraction, drafting, compliance) | usage-based, low |
| Storage/DB | Airtable or Supabase (free tier) | $0–25/mo |
| Billing | Stripe | 2.9% + $0.30 |
| Forms/intake | Tally / simple form | $0 |
| Domain + email | Namecheap + Google Workspace | ~$20/mo |

**Total fixed burn well under the $500 cap.** Your Unraid server hosting n8n is itself an unfair advantage — zero marginal orchestration cost.

> ⚠️ **Data-handling note:** if you ever integrate with Procore, its marketplace terms **ban using Procore data to train AI/ML** and gate apps through review. Design to stay independent of those terms early. ([Procore reqs](https://developers.procore.com/documentation/partner-content-reqs))

---

## 8. The AI agent crew (see `automation/ai-agents/`)

| Agent | Job | Human gate |
|---|---|---|
| **Research/Monitor agent** | Watches lien-law changes, competitor pricing, new AEC AI tools | Weekly digest to you |
| **Outreach agent** | Drafts personalized discovery + follow-up messages from your ICP list | You approve before send |
| **Onboarding agent** | Turns a new client's docs into a structured profile + checklist | You confirm |
| **Pay-app/waiver agent** | The core: extracts, generates G702/G703 + correct waiver, flags compliance issues | **You QA every package** (liability) |
| **Support agent** | Drafts answers to client questions from your knowledge base | You approve novel answers |
| **Reporting agent** | Updates `models/kpi-dashboard.csv` and the weekly summary | Auto |

**Non-negotiable control:** a human (you) approves every document that touches a real project. The agent drafts; you sign off. This is both a liability firewall and your quality moat.

---

## 9. Operations, KPIs, financials

- **SOPs:** `sops/sop-customer-onboarding.md`, `sops/sop-weekly-operating-rhythm.md`, `sops/sop-sales-pipeline.md`.
- **KPIs:** tracked in `models/kpi-dashboard.csv` — MRR, active clients, hrs/client (must fall), gross margin, pipeline, churn.
- **Financial model:** `models/financial-model-flagship.csv` — month-by-month revenue, cost, and hours through 24 months, with conservative/base/upside columns.

---

## 10. Defensibility — why this lasts

1. **Domain-trust moat.** The sale requires speaking construction fluently and being believed. Highest barrier; you already cleared it.
2. **Regulatory-knowledge moat.** Correct lien waivers by state/type and AIA-compliant billing are *expensive to get wrong* — a generalist's tool produces legally defective documents. Your correctness *is* the product.
3. **Stickiness.** Vertical construction software is "extremely sticky" — it embeds in monthly cash-flow operations and rarely gets ripped out. ([Construction Dive](https://www.constructiondive.com/news/despite-50b-of-investment-contech-is-being-held-back-by-its-fragmented-cu/652240/))
4. **Data moat (later).** Aggregated, anonymized pay-cycle/benchmark data becomes a second product (see opportunity #4).

---

## 11. Decision metadata

- **Evidence:** all cited above — market under-digitization, quantified payment pain, weak sub-first incumbents, AI gap in compliance workflows, your insider knowledge of AIA/lien law.
- **Key assumptions:** (a) you can reach 20–40 subs via network/associations in 60 days; (b) ≥3 will pay $750–$1,500/mo to make pay-app/waiver prep disappear; (c) you can deliver Rung 1 manually-with-AI before writing real software.
- **Biggest risks:** (1) **liability** — a defective waiver/pay-app on a live project. Mitigation: human QA gate + clear service terms + E&O insurance before scaling + lawyer-reviewed disclaimers. (2) **slow sales cycle** — mitigated by sub-first (faster deciders) and warm network. (3) **build-before-validate temptation** — mitigated by the Rung-1 service-first mandate. (4) **saturation/"no new software"** — mitigated by leading with provable fast-payment ROI. Full register in `docs/06`.
- **Confidence: 7/10.** Category and moat: high. Exact wedge: medium until discovery calls confirm pay-app is the sharpest pain for *your* reachable subs.
- **Downside case:** ~$300 + ~8 weekends spent; if no one pays, you exit with a validated "no," a reusable n8n/AI stack, and a sharpened ICP. Capped, reversible downside.
- **Next action:** Week 1 of `docs/07` — build the 40-sub target list and send the first 10 discovery messages (`templates/cold-outreach.md`).
- **Autonomous vs. you:** *Built for you* — the entire design, automation blueprint, agent prompts, SOPs, templates, financial model. *Needs you* — sending outreach from your identity, running discovery calls, QA-ing real documents, buying E&O insurance, the go/no-go call, and a lawyer's review of the service terms before any real document ships.
