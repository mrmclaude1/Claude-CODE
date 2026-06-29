# Models — importable spreadsheets

Import any file into Google Sheets or Excel (File → Import → upload CSV).

| File | What it is | How to use |
|---|---|---|
| `opportunity-scorecard.csv` | All 16 opportunities scored on 10 weighted criteria, ranked. | Sort by `WeightedOverall_10`. Re-score as your situation changes; the ranking updates. |
| `financial-model-flagship.csv` | Month-by-month base-case P&L for the flagship (24 months) + conservative/base/upside scenarios. | Replace `Notes`/figures with actuals as you go. The base case is more optimistic than the scorecard's deliberately conservative income column — track reality between the two. |
| `capital-allocation-waterfall.csv` | Stage-gated rules for where each profit dollar goes. | Find your current monthly-profit stage; apply those percentages. |
| `kpi-dashboard.csv` | The metrics you watch. | Fill `Current` weekly/monthly; set `Status` 🟢/🟡/🔴. Wire the Reporting agent to auto-update it. |

**Reconciliation note:** the scorecard's `Yr1/Yr3 income` columns are intentionally conservative, risk-adjusted planning numbers. The financial model shows the fuller base/upside range. Treat the scorecard as the floor you plan around and the model's base case as the target you steer toward — actuals should land between them if execution is on track.

All figures are modeled scenarios with stated assumptions, **not guarantees.** See each doc's "Decision metadata" for confidence and downside.
