# Deploying the pay-app engine on Unraid

The engine is a tiny, dependency-free Docker container. Two ways to run it on Unraid — pick one.

---

## Prereq
- Unraid with the **Docker** service enabled (Settings → Docker → Enable = Yes).
- The repo available to your server (clone it, or build the image elsewhere and push to a registry).

---

## Option 1 — Docker Compose (easiest if you have the Compose Manager plugin)

1. Install **Docker Compose Manager** from Community Applications (one-time).
2. Clone the repo onto the array, e.g. `/mnt/user/appdata/payapp-engine/`:
   ```bash
   cd /mnt/user/appdata
   git clone https://github.com/mrmclaude1/Claude-CODE.git payapp-engine
   cd payapp-engine
   git checkout claude/wealth-portfolio-automation-58txm8
   ```
3. In Compose Manager, add a stack pointing at this folder's `docker-compose.yml`, then **Compose Up**.
   (Or from the Unraid terminal: `docker compose up -d --build`.)
4. Verify:
   ```bash
   curl http://localhost:8000/health
   # {"status": "ok", "service": "payapp-engine"}
   ```

---

## Option 2 — Build the image, run as a normal Unraid container

1. Build the image on the server (or build locally and `docker save`/`load`):
   ```bash
   cd /mnt/user/appdata/payapp-engine
   docker build -t payapp-engine:latest .
   ```
2. Unraid → **Docker** tab → **Add Container**:
   - **Name:** `payapp-engine`
   - **Repository:** `payapp-engine:latest`
   - **Network Type:** Bridge
   - **Port:** add a port mapping `Host 8000` → `Container 8000` (change the host port if 8000 is in use).
   - **Variable (optional):** `PORT=8000`
3. **Apply**, then verify with the same `curl` as above.

---

## Using it

Send a project JSON, get a draft package back:

```bash
curl -s -X POST http://<unraid-ip>:8000/draft \
  -H 'Content-Type: application/json' \
  --data @examples/sample_project.json | python3 -m json.tool
```

The response includes the computed G702 lines, the selected lien waiver, the compliance flags, a `blocking_errors` boolean, and a ready-to-read `markdown` package — all marked `requires_human_qa: true`.

---

## Wiring n8n (also on Unraid) to the engine

In `n8n/payapp-pipeline.workflow.json`, replace the `executeCommand` node with an **HTTP Request** node:
- **Method:** POST
- **URL:** `http://payapp-engine:8000/draft` (same Docker network) or `http://<unraid-ip>:8000/draft`
- **Body:** the extracted ProjectContext JSON from the LLM node
- Route on the response's `blocking_errors` field: `false` → Human QA queue, `true` → Return for Correction.

This keeps the LLM doing only extraction and the deterministic engine doing the money math — with the mandatory human-QA gate before anything ships.

---

## Notes
- **No secrets in this container.** The engine itself needs no API keys (the LLM extraction happens in n8n, which holds `ANTHROPIC_API_KEY`). Keep it that way.
- **Updates:** `git pull` in the appdata folder, then `docker compose up -d --build` (Option 1) or rebuild + recreate (Option 2).
- **Backups:** the container is stateless; just back up the repo folder. If you later mount a drafts volume, include it in your appdata backups.
