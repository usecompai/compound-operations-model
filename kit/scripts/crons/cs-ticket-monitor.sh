#!/usr/bin/env bash
# Poll an approved helpdesk endpoint and create a private, propose-only draft queue.
set -euo pipefail
umask 077

: "${HELPDESK_API_URL:?Set HELPDESK_API_URL to the approved tickets endpoint}"
: "${HELPDESK_API_KEY:?Set HELPDESK_API_KEY in a secret store or mode-600 env file}"

QUEUE_FILE="${CS_TICKET_QUEUE_FILE:-/tmp/compai-cs-ticket-queue.json}"
PROCESSED_FILE="${CS_PROCESSED_FILE:-/tmp/compai-cs-processed-ticket-ids.json}"
LOG_EVENT_SCRIPT="${COMPAI_LOG_EVENT_SCRIPT:-/opt/compai/scripts/log-event.sh}"

python3 - "$HELPDESK_API_URL" "$HELPDESK_API_KEY" "$QUEUE_FILE" "$PROCESSED_FILE" <<'PY'
import json
import os
import sys
import urllib.request

url, api_key, queue_file, processed_file = sys.argv[1:]
request = urllib.request.Request(
    url,
    headers={"Authorization": f"Bearer {api_key}", "Accept": "application/json"},
)

with urllib.request.urlopen(request, timeout=30) as response:
    payload = json.loads(response.read())

tickets = payload.get("data", payload.get("tickets", []))
if isinstance(tickets, dict):
    tickets = tickets.get("data", [])

processed = set()
if os.path.exists(processed_file):
    try:
        with open(processed_file, encoding="utf-8") as source:
            processed = set(json.load(source))
    except (OSError, json.JSONDecodeError):
        processed = set()

queue = []
for ticket in tickets[:30]:
    ticket_id = str(ticket.get("id", ticket.get("_id", "")))
    if not ticket_id or ticket_id in processed:
        continue
    processed.add(ticket_id)
    queue.append(
        {
            "ticket_id": ticket_id,
            "subject": str(ticket.get("subject", "No subject"))[:200],
            "message": str(ticket.get("message", ticket.get("body", "")))[:1000],
            "authority": "PROPOSE",
            "customer_send_allowed": False,
        }
    )
    if len(queue) >= 5:
        break

with open(queue_file, "w", encoding="utf-8") as output:
    json.dump(queue, output)
os.chmod(queue_file, 0o600)

with open(processed_file, "w", encoding="utf-8") as output:
    json.dump(list(processed)[-500:], output)
os.chmod(processed_file, 0o600)

print(len(queue))
PY

queued_count="$(python3 - "$QUEUE_FILE" <<'PY'
import json
import sys

with open(sys.argv[1], encoding="utf-8") as source:
    print(len(json.load(source)))
PY
)"

if [[ -x "$LOG_EVENT_SCRIPT" ]]; then
  "$LOG_EVENT_SCRIPT" "CS Agent" "${queued_count} new tickets triaged into a propose-only draft queue"
fi
