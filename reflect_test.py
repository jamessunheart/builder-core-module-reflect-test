# reflect_test module
import requests

def run(_: str = None) -> dict:
    try:
        response = requests.post(
            "https://core-builder-v-2-jamesrickstinso.replit.app/api/modules/memory_core/run",
            json={"payload": {"action": "retrieve"}}
        )
        logs = response.json().get("results", [])
    except Exception as e:
        return {"error": str(e)}

    if not isinstance(logs, list):
        return {"error": "Unexpected memory format", "raw": logs}

    sample = logs[0] if logs else {}
    return {
        "entry_count": len(logs),
        "sample_entry": sample,
        "fields": list(sample.keys()) if isinstance(sample, dict) else []
    }