# Automation Architecture

> How the flagship runs on autopilot. Built on tools you already own (Unraid server) plus near-free SaaS, all under the $500 cap.

---

## Stack

| Layer | Tool | Why | Cost |
|---|---|---|---|
| **Orchestration** | **n8n, self-hosted on your Unraid server** | You own the hardware; per-execution model is ~10× cheaper than Zapier; full control of data | $0 |
| **Intelligence** | Claude API | Document extraction, drafting, compliance reasoning | usage-based |
| **Data** | Airtable (free) or Supabase (free tier) | CRM, client profiles, experiment ledger | $0–25/mo |
| **Billing** | Stripe | Subscriptions + invoicing | 2.9% + $0.30 |
| **Intake** | Tally form + shared Drive | Client document upload | $0 |
| **Email** | Google Workspace | Outreach + delivery | ~$7/user/mo |
| **Domain** | Namecheap | — | ~$12/yr |

Fixed monthly burn at start: **~$30–80**. Comfortably inside $500.

---

## The core pipeline (pay-app + lien-waiver, sub-first)

```
 ┌──────────┐   ┌─────────────┐   ┌──────────────────────┐   ┌───────────┐   ┌──────────┐
 │  INTAKE  │──▶│   EXTRACT   │──▶│      GENERATE        │──▶│ HUMAN QA  │──▶│ DELIVER  │
 │ docs in  │   │ LLM parses  │   │ G702/G703 + SOV +    │   │ YOU sign  │   │ package  │
 │ via form │   │ SOV, retain │   │ correct lien waiver  │   │ off (gate)│   │ + Stripe │
 └──────────┘   │ -age, dates │   │ by state/type        │   └───────────┘   └──────────┘
                └─────────────┘   │ + compliance checks  │         │
                                  └──────────────────────┘         ▼
                                                            CRM update + KPI log
```

**Design rules:**
1. **Deterministic checks on money/dates** — never let the LLM be the final authority on a dollar figure or a statutory deadline. Validate with code.
2. **Human QA gate is mandatory** — every document a human (you) approves before it leaves. This is the liability firewall (risk F2) and the quality moat.
3. **State-aware waiver logic** — the generator selects the correct waiver type and statutory form per state (the insider moat). Encode the rules; flag anything unusual for manual review.
4. **Everything logs to the dashboard** — the Reporting agent reads pipeline events to keep `models/kpi-dashboard.csv` live.

---

## Agent crew

Each agent in `ai-agents/` is a ready-to-paste system prompt. Drop into Claude (API or app) and wire its inputs/outputs through n8n.

| File | Agent | Cadence |
|---|---|---|
| `ai-agents/research-monitor-agent.md` | Competitor/regulation/AI-tool watch | Weekly |
| `ai-agents/outreach-agent.md` | Drafts personalized discovery + follow-ups | On demand |
| `ai-agents/onboarding-agent.md` | New client docs → structured profile + checklist | Per client |
| `ai-agents/payapp-waiver-agent.md` | The core delivery agent | Per pay cycle |
| `ai-agents/support-agent.md` | Drafts client support replies | On demand |
| `ai-agents/reporting-agent.md` | Updates KPI dashboard + weekly summary | Weekly |

**Universal guardrails (apply to all agents):**
- Human approval before anything external is sent or any real document ships.
- Cite sources for any external fact; never fabricate a citation, price, or legal rule.
- On uncertainty, flag for human review rather than guessing — especially on money, dates, and legal forms.
