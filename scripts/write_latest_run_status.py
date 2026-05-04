"""Generate a machine-readable JSON status file for the latest Daily Horizon run."""

import json
from pathlib import Path
from datetime import datetime
import subprocess

STATUS_DIR = Path("docs/status")
STATUS_DIR.mkdir(parents=True, exist_ok=True)
STATUS_FILE = STATUS_DIR / "latest-run.json"

# Minimal placeholder, can be integrated with orchestrator/daily summary pipeline
# Fetch latest commit SHA for traceability
try:
    commit_sha = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
except Exception:
    commit_sha = "unknown"

# Example structure, real numbers can be updated dynamically from orchestrator summary
status = {
    "date": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "commit": commit_sha,
    "fetched_items": 0,
    "selected_items": 0,
    "sources": {},
    "status": "success",
    "config_version": "1.0",
}

STATUS_FILE.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote latest run status to {STATUS_FILE}")
