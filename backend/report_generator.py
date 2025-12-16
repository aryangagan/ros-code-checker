import json
import os

def generate_reports(report_data, output_dir="reports"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Text report
    text_path = os.path.join(output_dir, "report.txt")
    with open(text_path, "w") as f:
        f.write(f"STATUS: {report_data['status']}\n\n")

        f.write("ERRORS:\n")
        if report_data["errors"]:
            for e in report_data["errors"]:
                f.write(f"- {e}\n")
        else:
            f.write("None\n")

        f.write("\nWARNINGS:\n")
        if report_data["warnings"]:
            for w in report_data["warnings"]:
                f.write(f"- {w}\n")
        else:
            f.write("None\n")

        f.write("\nROS SUMMARY:\n")
        for k, v in report_data["ros_summary"].items():
            f.write(f"{k}: {v}\n")

    # JSON report
    json_path = os.path.join(output_dir, "report.json")
    with open(json_path, "w") as jf:
        json.dump(report_data, jf, indent=2)
