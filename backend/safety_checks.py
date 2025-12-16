import os
import re

def run_safety_checks(base_dir):
    warnings = []

    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        lines = f.readlines()
                        content = "".join(lines)

                        # Infinite loop without sleep
                        if "while True" in content and "sleep" not in content:
                            warnings.append(
                                f"Possible infinite loop without sleep in {file}"
                            )

                        # Unsafe joint values (very basic heuristic)
                        joint_values = re.findall(r"[-+]?\d*\.\d+|\d+", content)
                        for val in joint_values:
                            try:
                                if abs(float(val)) > 3.14:
                                    warnings.append(
                                        f"Possible unsafe joint value {val} in {file}"
                                    )
                                    break
                            except:
                                pass
                except:
                    pass

    return warnings
