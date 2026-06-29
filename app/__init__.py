"""
Deterministic core engine for the construction pay-application + lien-waiver service.

This package handles the parts that MUST NOT be left to an LLM:
- AIA G702/G703 arithmetic (money math)
- Lien-waiver type selection + state statutory-form / notarization rules
- Compliance checks

The LLM (extraction, drafting) and n8n (orchestration) wrap AROUND this core.
Every output is a DRAFT and requires human QA before it ships. See app/README.md.
"""

__all__ = [
    "models",
    "payapp",
    "lien_waiver",
    "compliance",
    "pipeline",
]
