# app/ — Deterministic core engine

The liability-critical core of the flagship (`docs/02`). It does the parts that **must not** be left to an LLM: AIA **G702/G703** money math, **lien-waiver** type selection + state statutory-form/notarization rules, and **compliance checks**. The LLM (extraction, drafting) and n8n (orchestration) wrap *around* this — see `automation/README.md` and `n8n/`.

**Pure Python 3 standard library — no dependencies, no install.**

---

## Run it

```bash
# Generate a draft package from a project JSON
python3 -m app.cli examples/sample_project.json

# Write it to a file
python3 -m app.cli examples/sample_project.json --out examples/output_sample.md

# Run the test suite
python3 -m unittest discover -s tests -v
```

The CLI exits non-zero if any **blocking ERROR** is present — so n8n (or CI) can gate on it before a package reaches the human QA queue.

---

## What it computes

**G703 continuation** per line item: `G = D + E + F` (completed + stored), `% = G/C`, `balance = C - G`.

**G702 application** lines 1–9, including split retainage (work vs. stored material), total earned less retainage, less previous certificates, and current payment due.

**Lien waiver**: selects one of the four standard types (conditional/unconditional × progress/final), applies the correct state statutory form + notarization requirement from `app/data/state_lien_rules.json`, and **flags for human review** on any risky combination (e.g. an unconditional waiver demanded before payment clears, or a state with a timing/auto-conversion trap).

**Compliance**: SOV-vs-contract reconciliation, over-billing, negative payment due, retainage math, missing period, and waiver/pay-app amount mismatch.

---

## Design guarantees

- **Decimal money, never float** (`app/money.py`) — no binary rounding drift on dollar figures.
- **Every output is a DRAFT** marked `NOT FINAL — PENDING HUMAN QA`. Nothing here finalizes or sends.
- **Uncertainty flags, never guesses** — missing state rules or risky waivers raise `human_review_required` rather than asserting a legal conclusion.

---

## ⚠️ Scope and disclaimers

- `app/data/state_lien_rules.json` is a **non-exhaustive starting point** with statutory citations that **must be verified by a licensed attorney** before any waiver ships. Lien law changes; states are missing. The engine deliberately flags unknown states for human review.
- This code produces **administrative drafts, not legal documents or legal advice.** The human QA gate + attorney-reviewed templates (`templates/service-agreement-template.md`) + E&O insurance are the controls that make it safe to operate (risk F2 in `docs/06`).

---

## File map

| File | Role |
|---|---|
| `money.py` | Decimal money/percent helpers |
| `models.py` | Typed inputs (`ProjectContext`, `LineItem`, …) and results |
| `payapp.py` | G702/G703 computation |
| `lien_waiver.py` | Waiver selection + state rules |
| `compliance.py` | Deterministic checks |
| `pipeline.py` | Orchestrates core → `DraftPackage`, renders markdown |
| `cli.py` | Command-line entry point |
| `data/state_lien_rules.json` | State waiver rules (verify before use) |
