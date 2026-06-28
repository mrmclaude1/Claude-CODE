# KPI Dashboard Specification

What to measure, the target, and the red-flag threshold. Build this as a single sheet/Metabase
dashboard fed by the n8n `runs` and `clients` tables. The CFO Agent (#7) reads it weekly.

## North-Star Metrics (the only 3 that matter most)
| Metric | Why it's a north star | Target trajectory |
|---|---|---|
| **MRR (recurring revenue)** | The compounding asset; employment-optional depends on it | +10–20% / mo early |
| **Hours per client per month** | Proves automation > labor (the whole thesis) | DOWN every month |
| **Portfolio net worth** | The actual end goal | Up and to the right |

## Sales / Pipeline
| Metric | Target | Red flag |
|---|---|---|
| Outreach contacts / week | ≥ 10 (first 90 days) | < 5 |
| Discovery calls booked / week | ≥ 3 | < 1 |
| Call → proposal rate | ≥ 50% | < 30% |
| Proposal → close rate | ≥ 30% | < 15% |
| Sales cycle length | < 30 days | > 60 days |

## Revenue
| Metric | Target | Red flag |
|---|---|---|
| MRR | per financial model | flat 2 mo in a row |
| Setup revenue / month | ≥ $1,500 | $0 two months |
| ARPU (avg revenue/client) | rising | falling |
| MRR churn | < 5% / mo | > 10% |
| LTV : CAC | > 4:1 | < 3:1 |

## Delivery / Operations
| Metric | Target | Red flag |
|---|---|---|
| Time-to-launch / workflow | falling (see SOP targets) | rising |
| Hours / client / month | < 1 hr by client #6 | > 3 hrs |
| Workflow error rate | < 2% of runs | > 5% |
| Support response time | < 1 business day | > 2 days |

## Automation Health
| Metric | Target | Red flag |
|---|---|---|
| % of recurring tasks automated | rising toward 80%+ | stalled |
| AI/API spend as % of revenue | < 5% | > 10% |
| Agent-run success rate | > 95% | < 90% |

## Financial / Wealth
| Metric | Target | Red flag |
|---|---|---|
| Net profit margin | > 60% | < 40% |
| Monthly cash flow | rising | negative 2 mo |
| Cash runway | > 6 months | < 3 months |
| Portfolio contribution (actual vs. waterfall) | 100% of plan | < 50% |
| Net worth growth (QoQ) | positive | flat/negative 2 quarters |

## Customer Health
| Metric | Target | Red flag |
|---|---|---|
| "Would you refer?" (NPS proxy) | ≥ 8/10 | < 6 |
| Referrals generated / client | ≥ 1 | 0 across all clients |
| At-risk clients flagged | acted on within 1 wk | ignored |

---

### Dashboard build note
Minimum viable version = one Google Sheet with tabs (Pipeline, Revenue, Delivery, Finance) fed by
n8n. Upgrade to Metabase (self-host on Unraid) once you want charts. Don't over-build the dashboard
before you have data — a sheet is fine for the first 5 clients.
