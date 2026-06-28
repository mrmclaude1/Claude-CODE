#!/usr/bin/env python3
"""
competitor_monitor.py — Weekly market & competitor monitor for the portfolio.

Fetches a list of tracked URLs (competitor pricing/feature pages, blogs), detects changes
since last run, and (optionally) asks Claude to summarize what changed and recommend one action.

Designed to run on your Unraid server via cron or n8n (BP-08). Zero paid dependencies beyond
the Claude API (optional). Stdlib + `requests` + `anthropic` (optional).

Usage:
    pip install requests anthropic
    export ANTHROPIC_API_KEY=sk-...        # optional; without it, runs change-detection only
    python competitor_monitor.py --config watchlist.json --state state.json

watchlist.json:
    {
      "targets": [
        {"name": "CompetitorA pricing", "url": "https://example.com/pricing"},
        {"name": "CompetitorB features", "url": "https://example.com/features"}
      ]
    }
"""
import argparse
import hashlib
import json
import os
import re
import sys
import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("Install requests: pip install requests", file=sys.stderr)
    sys.exit(1)

MODEL = "claude-opus-4-8"  # update to your preferred current model


def fetch_text(url: str, timeout: int = 30) -> str:
    """Fetch a URL and return a roughly text-only, whitespace-normalized version."""
    headers = {"User-Agent": "Mozilla/5.0 (portfolio-monitor)"}
    resp = requests.get(url, headers=headers, timeout=timeout)
    resp.raise_for_status()
    html = resp.text
    # crude tag strip — good enough for change detection
    text = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", "ignore")).hexdigest()


def load_json(path: Path, default):
    if path.exists():
        return json.loads(path.read_text())
    return default


def summarize_with_claude(changes: list) -> str:
    """Optional: summarize detected changes + one recommendation via Claude."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key or not changes:
        return ""
    try:
        import anthropic
    except ImportError:
        return "(anthropic SDK not installed; skipping AI summary)"

    client = anthropic.Anthropic(api_key=api_key)
    blob = "\n\n".join(
        f"### {c['name']} ({c['url']})\nSNIPPET:\n{c['snippet'][:2000]}" for c in changes
    )
    prompt = (
        "You monitor the construction-automation / vertical-SaaS market. The following pages "
        "CHANGED since last week. For each, infer what likely changed (pricing, features, "
        "positioning). Then give ONE actionable recommendation for our construction-automation "
        "business this week. Be concise. Cite the URL for each finding.\n\n" + blob
    )
    msg = client.messages.create(
        model=MODEL,
        max_tokens=1200,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="watchlist.json")
    ap.add_argument("--state", default="state.json")
    ap.add_argument("--report", default="market-report.md")
    args = ap.parse_args()

    cfg = load_json(Path(args.config), {"targets": []})
    state = load_json(Path(args.state), {})
    today = datetime.date.today().isoformat()

    changes = []
    for t in cfg.get("targets", []):
        name, url = t["name"], t["url"]
        try:
            text = fetch_text(url)
        except Exception as e:  # noqa: BLE001
            print(f"[warn] {name}: fetch failed: {e}", file=sys.stderr)
            continue
        h = content_hash(text)
        prev = state.get(url, {})
        if prev.get("hash") and prev["hash"] != h:
            changes.append({"name": name, "url": url, "snippet": text[:3000]})
            print(f"[CHANGED] {name}")
        elif not prev.get("hash"):
            print(f"[baseline] {name}")
        else:
            print(f"[same] {name}")
        state[url] = {"hash": h, "last_checked": today}

    Path(args.state).write_text(json.dumps(state, indent=2))

    # Build the report
    lines = [f"# Market Monitor — {today}", ""]
    if not changes:
        lines.append("No changes detected since last run.")
    else:
        lines.append(f"{len(changes)} page(s) changed:\n")
        for c in changes:
            lines.append(f"- **{c['name']}** — {c['url']}")
        ai = summarize_with_claude(changes)
        if ai:
            lines += ["", "## AI Analysis & Recommendation", "", ai]

    report = "\n".join(lines)
    Path(args.report).write_text(report)
    print("\n" + report)


if __name__ == "__main__":
    main()
