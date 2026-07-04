#!/bin/bash
# Usage: log-audit-event.sh /path/to/event.json
# Appends a validated JSON object to the Compai audit JSONL ledger.

set -euo pipefail

EVENT_FILE="${1:-}"
LOG_FILE="${COMPAI_AUDIT_LOG:-/opt/compai/logs/audit-events.jsonl}"

if [ -z "$EVENT_FILE" ]; then
  echo "usage: log-audit-event.sh /path/to/event.json" >&2
  exit 64
fi

python3 - "$EVENT_FILE" "$LOG_FILE" <<'AUDITPY'
import json
import os
import sys

event_path, log_path = sys.argv[1], sys.argv[2]

with open(event_path, "r", encoding="utf-8") as f:
    event = json.load(f)

required = ["kind", "api_version", "id", "run_id", "agent", "risk_class", "action_type", "source_refs", "outputs", "approval", "verification", "terminal_state", "created_at"]
missing = [key for key in required if key not in event]
if missing:
    raise SystemExit(f"missing required audit fields: {', '.join(missing)}")

if event["kind"] != "AuditEvent":
    raise SystemExit("kind must be AuditEvent")
if event["api_version"] != "compai/v0.1":
    raise SystemExit("api_version must be compai/v0.1")

os.makedirs(os.path.dirname(log_path), exist_ok=True)
with open(log_path, "a", encoding="utf-8") as f:
    f.write(json.dumps(event, ensure_ascii=True, sort_keys=True))
    f.write("\n")
AUDITPY
