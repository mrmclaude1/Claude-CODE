# CRM Schema — Pipeline & Client Tracking

Use **Airtable** (fastest to start) or **Baserow** (self-host free on your Unraid server, no per-seat
fees — preferred long-term). Import `contacts-template.csv` to bootstrap. Two linked tables.

---

## Table 1: `Contacts` (your 50-name list + everyone after)

| Field | Type | Notes / options |
|---|---|---|
| Name | Single line text | Primary field |
| Company | Single line text | |
| Trade | Single select | Electrical, Mechanical/HVAC, Plumbing, Concrete, Roofing, Glazing, Fire Protection, GC, Supplier, Other |
| Role | Single select | Owner, Ops Manager, Office Manager, Estimator, PM, Other |
| Revenue Band | Single select | <$1M, $1–5M, $5–15M, $15M+, Unknown |
| Relationship | Single select | Close, Worked together, Acquaintance, Cold-referred, Cold |
| Known Pain | Long text | The specific complaint you've heard (bids/AR/submittals/COI/admin) |
| Email | Email | |
| Phone | Phone | |
| LinkedIn | URL | |
| Source | Single select | Career network, Referral, Supplier intro, Association, Inbound, Cold |
| Stage | Single select | New, Contacted, Replied, Call Booked, Proposal Sent, Won, Lost, Nurture |
| Owner Action | Single select | None, Send outreach, Follow up, Send SOW, Schedule call |
| Next Action Date | Date | Drives your weekly outreach queue |
| Last Contact | Date | |
| Referred By | Link → Contacts | For the referral flywheel |
| Notes | Long text | Call notes, context |
| Workflow Interest | Multi-select | Bid follow-up, Collections, RFI/Submittal, COI/Sub, Daily reports, Job intake |
| Est. Deal Value | Currency | Setup + (retainer × 12) estimate |

### Recommended views
- **This Week's Queue** — filter `Next Action Date` ≤ today AND `Stage` ≠ Won/Lost. Sort by date.
- **Awaiting Reply** — `Stage` = Contacted, `Last Contact` > 3 days ago → auto follow-up.
- **Hot** — `Stage` = Call Booked / Proposal Sent.
- **Pipeline (Kanban)** — group by `Stage`.
- **Referral Sources** — group by `Referred By`.

## Table 2: `Clients` (becomes active when a Contact = Won)

| Field | Type | Notes |
|---|---|---|
| Client | Link → Contacts | |
| Tier | Single select | Starter, Operator, Partner |
| Setup Fee | Currency | |
| Monthly Retainer | Currency | |
| MRR | Rollup/Currency | Feeds the KPI dashboard |
| Status | Single select | Onboarding, Active, At-Risk, Churned |
| Workflows Live | Multi-select | Which BP-0x are deployed |
| Launch Date | Date | |
| Hours This Month | Number | Must trend DOWN — the core metric |
| Last Tune-Up | Date | |
| Value Delivered ($/time) | Long text | For monthly reports + case studies |
| Referrals Generated | Number | Flywheel KPI |
| Churn Reason | Long text | If churned — feeds continuous improvement |

### Automations to wire (via n8n, BP-06/BP-07)
- When `Stage` → Call Booked: create a calendar hold + send confirmation.
- When `Last Contact` > 3 days and `Stage` = Contacted: queue a follow-up draft.
- When a Contact flips to Won: auto-create the matching `Clients` row, status = Onboarding.
- Weekly: roll up MRR, pipeline counts, and `Hours This Month` into the KPI dashboard.
