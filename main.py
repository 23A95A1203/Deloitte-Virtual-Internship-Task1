import json
import unittest
from datetime import datetime

# 🔁 Convert format from data-1.json
def convert_from_format_1(item):
    return {
        "device_id": item["device_id"],
        "timestamp": item["timestamp"],
        "value": item["value"]
    }

# 🔁 Convert format from data-2.json
def convert_from_format_2(item):
    dt = datetime.strptime(item["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
    return {
        "device_id": item["deviceId"],
        "timestamp": int(dt.timestamp() * 1000),
        "value": item["reading"]
    }

# 👇 Entry function to unify formats
def main(data1, data2):
    result = []

    for item in data1:
        result.append(convert_from_format_1(item))

    for item in data2:
        result.append(convert_from_format_2(item))

    return result

# ✅ Unit testing block
class TestTelemetryFormat(unittest.TestCase):

    def test_combined_output_matches_expected(self):
        with open("data-1.json") as f1, open("data-2.json") as f2, open("data-result.json") as fres:
            data1 = json.load(f1)
            data2 = json.load(f2)
            expected = json.load(fres)

        result = main(data1, data2)
        self.assertEqual(result, expected, "❌ Output does not match expected result")

# 🧪 Run test only if executed directly
if __name__ == "__main__":
    unittest.main()
