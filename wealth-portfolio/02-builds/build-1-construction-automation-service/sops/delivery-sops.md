# Standard Operating Procedures — Service Delivery

Productized delivery = the same repeatable steps every time. This is how a PM turns a service into a
near-asset. Each SOP is a checklist; follow it, don't improvise.

---

## SOP-01: Client Onboarding (target: < 90 min of your time)

1. [ ] Countersigned SOW received + first invoice paid (Stripe). **Never start before payment.**
2. [ ] Send the onboarding form (auto via n8n) — collects: tools in use, the one workflow to start,
       access needs, key contacts, sample documents.
3. [ ] Create client record in CRM (Airtable/Baserow) with status = Onboarding.
4. [ ] Create a shared folder + a private Slack channel or email alias.
5. [ ] Book the 30-min kickoff call. Confirm the exact workflow scope in writing (PM move).
6. [ ] Set the launch-by date in the CRM. Add to the delivery board.

## SOP-02: Workflow Build (per workflow)

1. [ ] Pull the matching **template** from your library (don't build from scratch).
2. [ ] Map the client's specific inputs/outputs onto the template (document the diffs).
3. [ ] Build in n8n on your Unraid instance. Use a per-client sub-workflow + credentials vault.
4. [ ] Add the human-in-the-loop checkpoint for any compliance-critical step.
5. [ ] Test with 3 real examples from the client's data.
6. [ ] Record a 3-min Loom walkthrough for the client.
7. [ ] Go live. Set monitoring/alerting (n8n error workflow → your inbox).
8. [ ] Log build hours in the CRM (this number must trend down across clients).

## SOP-03: Go-Live & Handoff

1. [ ] 15-min live walkthrough with the client.
2. [ ] Confirm they can see the dashboard / receive the outputs.
3. [ ] Set expectations: "Here's what's automated, here's where you still approve."
4. [ ] Schedule the first monthly tune-up.
5. [ ] Update CRM status = Active. Start the retainer billing in Stripe.

## SOP-04: Monthly Retainer Tune-Up (target: < 45 min/client)

1. [ ] Pull the client's KPIs (auto-compiled report — see automation).
2. [ ] Check error logs / missed runs for the month.
3. [ ] One improvement: make the workflow a little better OR add a small new automation.
4. [ ] Send a 1-paragraph "here's what your system did this month" update with numbers.
5. [ ] Every 3rd month: ask the referral question (SOP-06).

## SOP-05: Capture a Case Study (do this after every quantifiable win)

1. [ ] Identify the metric (time saved, $ recovered, faster turnaround).
2. [ ] Get one sentence of permission to share (anonymized if needed).
3. [ ] Write: Situation → What we automated → Result (the number) → Quote.
4. [ ] Add to the case-study library; schedule a content post (template C).

## SOP-06: Referral Request

1. [ ] Trigger: a quantified win or a positive tune-up.
2. [ ] Use outreach template B.
3. [ ] Log the referral in CRM; set the reward to pay on close.

## SOP-07: Scope Change / Change Order (enforce this — it's your margin)

1. [ ] Request comes in that's outside the SOW.
2. [ ] "Happy to — that's a change order. Here's the price/timeline." (Same as a real project.)
3. [ ] One-line written approval before building.
4. [ ] Invoice or add to next retainer cycle.

## SOP-08: Offboarding (if a client leaves)

1. [ ] Exit survey (why — feeds continuous improvement).
2. [ ] Export their data, hand over or shut down workflows per contract.
3. [ ] Revoke credentials. Mark CRM = Churned with reason.
4. [ ] 60-day later: a friendly "how's it going?" win-back touch.

---

### Time-to-launch targets (your efficiency must improve)

| Client # | Acceptable build time/workflow |
|---|---|
| 1–2 | 8–12 hrs (you're learning) |
| 3–5 | 4–6 hrs (templates forming) |
| 6+ | 1–3 hrs (mature templates) |

If build time isn't falling, your templates aren't tight enough — fix the template, not the symptom.
