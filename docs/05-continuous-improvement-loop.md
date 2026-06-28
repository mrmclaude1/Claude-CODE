# 05 — Continuous Improvement Loop

> The self-improving machine. Recurring research, monitoring, and optimization that make the whole system more valuable every month with almost none of your time.

---

## 1. The principle

A static business decays — competitors copy it, prices compress, tools get better, regulations shift. The fix is to make *improvement itself* a scheduled, automated process rather than something you do when you remember to. Each loop runs on a cadence, is mostly executed by an AI agent, and ends with a short decision queue for you.

```
        ┌──────────► SENSE ──────────┐
        │   (agents gather signal)   │
        │                            ▼
   ACT (you approve)            ANALYZE (agent ranks
        ▲                        what changed & why it matters)
        │                            │
        └──────────◄ DECIDE ◄────────┘
              (weekly digest → your queue)
```

You touch only the **DECIDE/ACT** corner — ~30 min/week reviewing a ranked digest and approving actions. Everything else is automated.

---

## 2. The loops (cadence, owner, output)

| Loop | Cadence | Run by | Output → where |
|---|---|---|---|
| **Competitor & pricing watch** | Weekly | Research agent | Price/feature changes of incumbents → digest |
| **Regulation watch** | Weekly | Research agent | Lien-law / AIA / state statutory-form changes → compliance update |
| **New-AI-tool scan** | Bi-weekly | Research agent | Tools that could cut cost or add capability → eval queue |
| **Customer-feedback mining** | Weekly | Support agent | Themes from client messages → product backlog |
| **Bottleneck review** | Monthly | You + Reporting agent | Highest hrs/client step → automation target |
| **Margin & cost audit** | Monthly | Reporting agent | Cost creep, underused subscriptions → cut list |
| **Prompt/automation tuning** | Monthly | You | Underperforming agent prompts → rewritten |
| **SOP refresh** | Monthly | You | Any SOP that drifted from reality → updated |
| **New-product / acquisition radar** | Quarterly | Research agent | Adjacent products, SMB deals at good multiples → opportunity log |
| **Experiment review** | Quarterly | You | Archive failures, double down on winners |

---

## 3. The monthly improvement ritual (45 min, Friday block)

1. **Read the digest** the agents compiled (5 min).
2. **Find the #1 bottleneck** — the single step costing the most hours or causing the most rework (`Hours_Per_Client`, `QA_Error_Rate` in the dashboard). (10 min)
3. **Kill one cost** — cancel/renegotiate one subscription or vendor. (5 min)
4. **Improve one automation** — rewrite the weakest agent prompt or n8n flow. (15 min)
5. **Update one SOP/doc** to match how things actually work now. (5 min)
6. **Log one experiment outcome** — archive or double down. (5 min)

One improvement per category per month compounds into a dramatically better machine over a year — without a single "improvement project."

---

## 4. The experiment ledger (how you avoid sunk-cost traps)

Every new bet is logged with a kill criterion *before* it starts:

```
Experiment: <name>
Hypothesis: <what we believe>
Bet: <time/$ committed>
Kill criterion: <if X by date Y, stop>
Result: <archived | doubled-down>
```

- **Archive failures fast and without ego** — a documented "no" is a real asset (it stops you re-running the same mistake).
- **Double down on winners deliberately** — when something clears its success bar, the next month's reinvestment budget (from the waterfall) flows to it first.

Keep this ledger in a simple Airtable/Sheet; the quarterly Experiment Review reads it.

---

## 5. Decision metadata

- **Evidence:** the loop encodes the research finding that distribution and adaptation — not the initial product — determine survival; static products lose to faster-iterating ones.
- **Key assumptions:** you actually run the 45-min monthly ritual; agents have access to the sources they monitor.
- **Biggest risks:** (1) the loop becomes busywork that doesn't change decisions — mitigated by the "one action per category" rule (bias to action, not analysis). (2) alert fatigue — mitigated by ranking the digest and surfacing only what crosses a threshold.
- **Confidence: 7/10.**
- **Next action:** stand up the **Research/Monitor agent** (`automation/ai-agents/research-monitor-agent.md`) and schedule its weekly digest.
- **Autonomous vs. you:** agents and prompts are built. **You** schedule them, grant source access, and spend the 45 min/month deciding.
