# n8n Workflow Blueprints (self-hosted on Unraid)

These are the reusable automations that power both the service (Build 1) and the SaaS (Build 2).
Build each once as a template, then clone per client. **Your Unraid-hosted n8n is the margin
advantage** — no per-task Zapier/Make fees.

## Setup (one-time)
1. Install n8n on Unraid (Community Apps → n8n). Put it behind a reverse proxy + HTTPS.
2. Add credentials vault entries: Claude API, Stripe, Resend/SES, Twilio, Airtable/Baserow,
   Supabase (for SaaS).
3. Create a global **Error Workflow** → on any failure, send yourself an alert with context.
4. Create a `clients` table (CRM) and a `runs` log table (for metrics + AI cost tracking).

---

## BP-01 — Bid/Quote Follow-Up Engine  ⭐ (lead workflow; likely SaaS seed)
```
Trigger: New quote (form submit / email-forward / QuickBooks webhook)
  → Store quote in CRM (client, amount, contact, date)
  → Schedule sequence: Day 1 email, Day 3 SMS, Day 7 email, Day 14 "last check" email
  → Each step: Claude drafts personalized message (Agent #2 style) → [human approve OR auto-send]
  → Inbound reply detected (email/SMS webhook) → Claude classifies hot/cold/objection
  → Hot → notify owner immediately + stop sequence
  → Update dashboard: quotes out / followed / replied / won / $ recovered
```

## BP-02 — RFI / Submittal / Change-Order Tracker
```
Trigger: Intake form or email
  → Claude extracts: type, project, description, due date, responsible party
  → Log to tracker table; assign status = Open
  → Scheduled reminders before due date (escalating)
  → Status dashboard (Open / In Review / Closed) + overdue alerts to owner
```

## BP-03 — AR / Collections Chaser
```
Trigger: Daily cron → pull open invoices (QuickBooks/Stripe)
  → Identify overdue by aging bucket (1-15, 16-30, 31+)
  → Claude drafts polite escalating reminder per bucket → [approve/auto-send]
  → 31+ days → build a "needs a personal call" shortlist for the owner
  → Log recovered $ when invoices clear → dashboard
```

## BP-04 — Subcontractor / Vendor COI & Onboarding
```
Trigger: New sub added
  → Send W-9 + COI request (e-sign via Documenso)
  → Claude reads uploaded COI → extracts coverage + expiration dates
  → Store; schedule expiry reminders (60/30/7 days before)
  → HUMAN CHECKPOINT: compliance-critical — owner confirms coverage adequacy
  → Dashboard: who's compliant / expiring / missing
```

## BP-05 — Daily Field Report Compiler
```
Trigger: Field crew texts/emails photos + notes (Twilio inbound)
  → Claude assembles into a structured daily report (date, crew, work done, issues, photos)
  → Generate PDF → send to owner/GC → archive to project folder
```

## BP-06 — Lead-Gen / Outreach Pipeline (for YOUR sales)
```
Trigger: Weekly cron
  → Pull next batch from prospect list (CRM, status = New)
  → Agent #1 researches each → builds dossier
  → Agent #2 drafts cold email + LinkedIn DM + follow-up
  → Queue to a review folder → [you approve] → send + log
  → Track opens/replies → book calls → update pipeline
```

## BP-07 — Monthly Client Value Report
```
Trigger: Monthly cron per active client
  → Pull client's run metrics from runs log
  → Agent #5 writes the value report (leads with best number)
  → Every 3rd month: append referral ask
  → Send to client; log sent → feeds retention/NPS tracking
```

## BP-08 — Market & Competitor Monitor
```
Trigger: Weekly cron
  → Fetch tracked competitor pages, pricing pages, relevant subreddits/forums, AI-tool releases
  → Agent #6 summarizes signal + one weekly recommendation, with URLs
  → Post to your "ops" channel + append to continuous-improvement log
  (Companion Python script: ../03-automation/competitor_monitor.py)
```

## BP-09 — Weekly KPI Roll-Up
```
Trigger: Weekly cron (Sunday)
  → Aggregate: pipeline metrics, MRR, churn, hours/client, errors, AI spend
  → Agent #7 (CFO) writes the dashboard summary vs. targets
  → Agent #9 (improvement) appends the ranked action list
  → Deliver to your inbox Monday AM → drives the weekly operating cadence
```

---

### Build order (matches the plan)
1. BP-01 (first client, first revenue) → 2. BP-06 (your own lead-gen) → 3. BP-03 / BP-02 / BP-04
(expand service menu) → 4. BP-07, BP-08, BP-09 (run the business on autopilot) → 5. harden BP-01
into the SaaS (Build 2).
