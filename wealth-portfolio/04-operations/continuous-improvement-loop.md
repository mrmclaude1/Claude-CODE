# Continuous Improvement Loop

"Every system must continually improve itself." This is the meta-system that makes the portfolio
worth more every month. It runs weekly (light) and quarterly (deep), mostly driven by AI agents
with you as the decision-maker.

## The loop (weekly, ~30 min, mostly automated)

```
   COLLECT ───► ANALYZE ───► PRIORITIZE ───► ACT ───► MEASURE ───► (repeat)
     │             │              │            │          │
   agents       Agent #9      impact/effort   you      KPIs feed
   (auto)       ranks         scoring        execute   back in
```

1. **COLLECT (automated):** BP-08 (market monitor), BP-09 (KPI roll-up), error logs, client
   feedback, time tracking — all pushed to your ops inbox.
2. **ANALYZE (Agent #9):** identifies the single biggest bottleneck + opportunities.
3. **PRIORITIZE:** rank by leverage = impact ÷ effort. Pick the top 1–2.
4. **ACT (you, Friday block):** implement one improvement.
5. **MEASURE:** confirm the KPI moved next week. Keep or revert.

## Standing improvement questions (the agent checks these every week)
- What was the biggest time-sink this week? → automate or eliminate it.
- Which manual step can a workflow now handle? → graduate it to auto.
- Which SOP did reality diverge from? → rewrite the SOP.
- Where did a client get confused/frustrated? → fix onboarding or comms.
- What's the most expensive AI call, and can a cheaper model do it? → optimize cost.
- Which prompt produced a bad output? → improve the prompt (version it).

## Quarterly deep review (~2 hrs)

### Market & competition
- [ ] Review the quarter's market-monitor reports. Any competitor pricing/feature shifts to react to?
- [ ] New AI tools/models that cut delivery cost or add a feature? Test the top one.
- [ ] Regulatory changes affecting clients (e.g., new compliance/insurance rules = new product).

### Pricing & margin
- [ ] Are you underpriced? (If close rate > 50%, you're too cheap — raise rates.)
- [ ] Where did margin erode? Scope creep? Tooling cost? AI spend? Fix the leak.

### Product & portfolio
- [ ] SaaS decision-gate status (Agent #8). Build / wait / pivot?
- [ ] Re-score the opportunity scorecard. Promote a rising bet; archive a dead one.
- [ ] Any acquisition targets appearing (a struggling competitor, a complementary tool)?

### The archive (this matters)
- [ ] **Failed-experiment log:** write down what you tried, why it failed, what you learned.
      Killing things fast is a feature. Keep this log in `04-operations/experiments-log.md`.
- [ ] **Winners:** what's working beyond expectation? Allocate more time/capital to it.

## Improvement backlog format (keep a simple table)

| Date | Idea/Bottleneck | Impact (1-5) | Effort (1-5) | Leverage | Status | Result |
|---|---|---|---|---|---|---|
| | | | | impact/effort | backlog/doing/done/archived | |

## The compounding principle
Each loop should make the next loop cheaper: better templates → faster builds → more capacity →
more clients → more data → better automation → less of your time. **If your hours/client aren't
falling quarter over quarter, the loop isn't working — that's the alarm.**
