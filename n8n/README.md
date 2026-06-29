# n8n/ — Orchestration workflows

Importable **skeletons** that wire the deterministic core (`app/`) into a running pipeline on your self-hosted n8n (Unraid). These are scaffolds to adapt, not finished production flows.

## `payapp-pipeline.workflow.json`

The flagship delivery pipeline:

```
Intake Webhook → LLM Extract (Claude) → Deterministic Core (app.cli) → Blocking Errors? ──true──→ Human QA Queue → Respond
                                                                              └────false────→ Return for Correction
```

**Import:** n8n → Workflows → Import from File → select the JSON.

**Before it runs, you must:**
1. Set `ANTHROPIC_API_KEY` in n8n's environment (the extract node reads `$env.ANTHROPIC_API_KEY`).
2. Make `app/` importable from the `executeCommand` node (run n8n with the repo on its path, or call `python3 -m app.cli /path/to/input.json`).
3. Replace **Human QA Queue** (a NoOp placeholder) with a real approval step — email/Slack approve, an n8n **Wait** node, or a review UI. **This gate is mandatory** (risk F2): no document leaves before you approve it.
4. Decide where drafts are written (`/data/drafts/...` in the skeleton).

**Design intent:** the LLM only *extracts* structured data — it never computes money. The deterministic core does the math and gates on blocking errors (non-zero exit), so a bad pay-app can't silently reach a client.
