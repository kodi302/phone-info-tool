import json
from datetime import datetime


def export_json(data, filename="report.json"):
    try:
        report = {
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "data": data,
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)

        print(f"\n✅ Report exported successfully: {filename}")

    except Exception as e:
        print("❌ Export Error:", e)

