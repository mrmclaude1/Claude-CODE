# Build 2 — Construction-Niche Micro-SaaS (The Long-Term Asset)

**Status: DO NOT BUILD YET.** This is the asset you create *after* Build 1 tells you exactly which
product to build. Building software before you have paying proof is the #1 way solo founders waste
months. This spec is the blueprint you execute in **months 4–6**, funded by service profit.

---

## The decision gate (build only when ALL are true)

- [ ] ≥3 service clients paid you to solve the **same** workflow.
- [ ] You can articulate the product in one sentence a contractor instantly gets.
- [ ] You have ≥2 clients who say "I'd pay monthly for a self-serve version of this."
- [ ] Service cash flow covers your time to build it (no dipping into savings).

## Why micro-SaaS is the asset (evidence)

- Sells at **3.9–5× SDE** (Acquire.com 2024–2025 median 3.9×, 71% avg margins).
- Recurring revenue that compounds; **9/10 automation** ceiling (self-serve, AI onboarding).
- A $4k/mo product at 4× SDE ≈ a meaningful exit — and you'll have built it on *validated* demand.

## Most likely product (front-runner based on the service menu)

**"Bid Follow-Up Autopilot for Contractors"** is the top candidate because the bid-follow-up
workflow has the clearest, fastest ROI (recovers lost revenue) and is the easiest to sell — but
**let the service data decide.** Runner-ups: COI/insurance-expiry tracker; RFI/submittal tracker;
AR collections chaser.

### Product thesis (example: Bid Follow-Up Autopilot)
> Contractors send quotes and then forget to follow up. Most lost jobs aren't lost on price —
> they're lost on silence. This product auto-sequences follow-ups (email + SMS) after a quote goes
> out, detects replies, and surfaces hot leads — so contractors close more of the bids they already
> made.

## MVP scope (4–6 weeks of build, ruthlessly minimal)

- [ ] Quote intake: simple form OR email-forward OR QuickBooks/Jobber connection.
- [ ] Auto follow-up sequence (configurable cadence, AI-drafted but editable messages).
- [ ] Reply detection → mark lead hot/cold; notify owner.
- [ ] One dashboard: quotes out, follow-ups sent, replies, jobs won, $ recovered.
- [ ] Stripe self-serve subscription + simple auth.
- **Explicitly NOT in MVP:** mobile app, deep integrations beyond one, team permissions, white-label.

## Tech stack (boring, cheap, fast)

| Layer | Choice | Why |
|---|---|---|
| Frontend | Next.js / Astro on Cloudflare/Vercel | Fast, cheap, you can ship it. |
| Backend/logic | n8n (self-host, Unraid) + a thin API | Reuse everything from the service. |
| DB / auth | Supabase (free tier → cheap) | Auth, Postgres, row-level security out of the box. |
| AI | Claude API | Message drafting, reply classification. |
| Email/SMS | Resend / SES + Twilio | Cheap per-message. |
| Billing | Stripe | Subscriptions + usage. |
| Analytics | PostHog (free tier) | Activation/retention funnels. |

**Reuse advantage:** the service already built and battle-tested these workflows on real clients.
The SaaS is largely *packaging* proven n8n logic behind self-serve auth + billing — far lower risk
than a cold-start product.

## Pricing (land where the service validated)

| Plan | Price/mo | Target |
|---|---:|---|
| Solo | $49 | 1-person shops / owner-operators |
| Crew | $99 | 5–15 employees (the sweet spot) |
| Pro | $199 | 15–40 employees, multi-user |

Anchor: even Solo pays for itself if it recovers **one** extra job per quarter.

## Go-to-market (you start with an unfair distribution edge)

1. **Your service clients are beta users + first paying customers.** Built-in launch.
2. **The service becomes a sales channel:** offer "done-for-you setup" on top of the SaaS for a fee.
3. **Case studies from the service** become the SaaS's social proof.
4. Vertical content, trade groups, supply-house partnerships (same channels as Build 1).
5. A simple affiliate cut for suppliers/consultants who refer.

## Key SaaS metrics to instrument from day 1

- Activation rate (signup → first quote tracked), Week-1 retention.
- MRR, net revenue retention, logo + revenue churn (churn < 5%/mo is the goal).
- CAC vs. LTV; payback < 6 months.
- "$ recovered" per customer — your headline ROI metric (drives retention + referrals).

## Risk analysis

| Risk | Mitigation |
|---|---|
| Building before validation | The decision gate above. Non-negotiable. |
| Construction's slow software adoption | You're selling to *existing* service clients first — already trusting you. |
| Churn (SaaS killer) | Tie the product to a visible $ result; show "$ recovered" monthly. |
| You get pulled back into service work | Hire VA + a part-time dev with service profit before building. |
| Bigger player adds the feature | Stay vertical and specific; your moat is contractor-language + service+software bundle. |

### Confidence: 7/10 — *conditional on the decision gate.* If you build it on validated demand with
service cash flow, the risk profile is dramatically better than a typical cold SaaS start.
