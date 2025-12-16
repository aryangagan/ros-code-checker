import os
import re

def parse_ros_code(base_dir):
    init_node = False
    publishers = 0
    subscribers = 0
    services = 0

    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                        if "rospy.init_node" in content:
                            init_node = True

                        publishers += len(re.findall(r"Publisher\s*\(", content))
                        subscribers += len(re.findall(r"Subscriber\s*\(", content))
                        services += len(re.findall(r"Service\s*\(", content))
                except:
                    pass

    return {
        "init_node_found": init_node,
        "publishers": publishers,
        "subscribers": subscribers,
        "services": services
    }
