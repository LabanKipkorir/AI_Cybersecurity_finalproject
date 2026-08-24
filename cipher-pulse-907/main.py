"""Cipher Pulse - defensive authentication log triage."""
import json
from collections import Counter


def analyze(events):
    failures = Counter(e.get("user") for e in events if e.get("outcome") == "failure")
    flagged = []
    for event in events:
        if failures[event.get("user")] >= 5:
            flagged.append({"event": event, "reason": "Repeated failed sign-ins"})
    return flagged


if __name__ == "__main__":
    sample = [{"user": "demo", "outcome": "failure"}] * 5
    print(json.dumps(analyze(sample), indent=2))
