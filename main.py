import json
from datetime import datetime

def iso_to_millis(iso_str):
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%SZ")
    return int(dt.timestamp() * 1000)

def unify_telemetry_data(data1, data2):
    unified = []

    # data‑1.json already in target format
    for item in data1:
        unified.append({
            "device_id": item["device_id"],
            "timestamp": item["timestamp"],
            "value": item["value"]
        })

    # convert data‑2.json and append **after** data‑1.json items
    for item in data2:
        unified.append({
            "device_id": item["deviceId"],
            "timestamp": iso_to_millis(item["timestamp"]),
            "value": item["reading"]
        })

    # 👉 NO sorting – keep original‑file order
    return unified

if __name__ == "__main__":
    with open("data-1.json") as f1, open("data-2.json") as f2, open("data-result.json") as fres:
        data1 = json.load(f1)
        data2 = json.load(f2)
        expected = json.load(fres)

        result = unify_telemetry_data(data1, data2)

        assert result == expected, "❌ Test Failed: Output doesn't match expected result."
        print("✅ All tests passed! Output matches expected result.")
