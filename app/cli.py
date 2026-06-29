"""Run the engine on a project JSON and print the draft package.

Usage:
    python -m app.cli examples/sample_project.json
    python -m app.cli examples/sample_project.json --out examples/output_sample.md
"""

from __future__ import annotations

import argparse
import json
import sys

from .models import ProjectContext
from .pipeline import build_draft_package, render_markdown, has_blocking_errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a DRAFT pay-app + lien-waiver package.")
    parser.add_argument("input", help="Path to a project JSON file.")
    parser.add_argument("--out", help="Optional path to write the markdown package.")
    args = parser.parse_args(argv)

    with open(args.input, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    ctx = ProjectContext.from_dict(data)
    pkg = build_draft_package(ctx)
    md = render_markdown(pkg)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(md + "\n")
        print(f"Wrote draft package to {args.out}")
    else:
        print(md)

    # Non-zero exit if blocking errors — useful for n8n/CI gating.
    return 1 if has_blocking_errors(pkg.flags) else 0


if __name__ == "__main__":
    sys.exit(main())
