# SOP — Customer Onboarding

> From signed client to first delivered package. Target: first value within 7 days.

---

## Trigger
A subcontractor signs the DFY agreement (`templates/service-agreement-template.md`) and the first invoice is paid via Stripe.

## Steps

| # | Step | Who | Tool |
|---|---|---|---|
| 1 | Send welcome email + intake form link | Auto | n8n + Tally |
| 2 | Client uploads: subcontracts, current SOVs, prior pay-apps, COI, W-9, GC billing requirements | Client | Tally + Drive |
| 3 | Onboarding agent builds structured profile + missing-items list | Auto | Onboarding agent |
| 4 | **You review the profile**, confirm projects/retainage/states, fill gaps | You | CRM |
| 5 | Confirm each project's billing cutoff dates and required forms | You | Client call (15 min) |
| 6 | Set up the client in the pipeline; schedule their billing cycle | Auto | n8n |
| 7 | Run the first pay-app/waiver package through the core agent | Auto | Pay-app agent |
| 8 | **QA every field**; deliver the first submit-ready package | You | QA queue |
| 9 | Confirm receipt + ask: "Did this save you time? Mind if I quote the result?" | You | Email |

## Definition of done
- Profile complete and confirmed.
- Billing cycle scheduled.
- First package delivered and acknowledged.
- Baseline metrics captured (their prior hours/cycle, days-to-pay) for the case study.

## Quality bar
- Zero math errors in the first package (it sets the trust anchor).
- Correct waiver type and statutory form for each project's state.
- Delivered before their actual billing deadline with buffer.

## Common pitfalls
- Missing GC-specific form requirements → ask in step 5, not after.
- Retainage % assumed instead of confirmed → always read it from the contract.
- State waiver rules overlooked → the agent flags; you verify.
