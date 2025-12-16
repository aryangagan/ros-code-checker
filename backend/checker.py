import zipfile
import os
import shutil
import json
import subprocess
import uuid

from simulation.simulator import run_simulation
from backend.ros_parser import parse_ros_code
from backend.safety_checks import run_safety_checks
from backend.report_generator import generate_reports


def extract_zip(zip_path):
    extract_dir = f"temp_{uuid.uuid4().hex}"
    os.makedirs(extract_dir)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    return extract_dir


def syntax_check_python(base_dir, errors):
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                result = subprocess.run(
                    ["python", "-m", "py_compile", file_path],
                    capture_output=True,
                    text=True
                )
                if result.returncode != 0:
                    errors.append(f"Syntax error in {file}")


def check_ros_structure(base_dir, errors):
    has_package_xml = False
    has_setup_or_cmake = False

    for root, _, files in os.walk(base_dir):
        if "package.xml" in files:
            has_package_xml = True
        if "setup.py" in files or "CMakeLists.txt" in files:
            has_setup_or_cmake = True

    if not has_package_xml:
        errors.append("Missing package.xml")
    if not has_setup_or_cmake:
        errors.append("Missing setup.py or CMakeLists.txt")


def run_checker(zip_path):
    errors = []
    warnings = []

    extracted_dir = extract_zip(zip_path)

    syntax_check_python(extracted_dir, errors)
    check_ros_structure(extracted_dir, errors)

    ros_summary = parse_ros_code(extracted_dir)
    safety_warnings = run_safety_checks(extracted_dir)
    warnings.extend(safety_warnings)

    simulation_result = None
    if not errors:
        simulation_result = run_simulation(extracted_dir)

    report = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "warnings": warnings,
        "ros_summary": ros_summary,
        "simulation": simulation_result
    }

    generate_reports(report)

    if os.path.exists(extracted_dir):
        shutil.rmtree(extracted_dir)

    return report


if __name__ == "__main__":
    zip_file = "good_package.zip"
    result = run_checker(zip_file)
    print(json.dumps(result, indent=2))
