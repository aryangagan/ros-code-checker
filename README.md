# ROS Code Checker Tool

## Overview
This project is developed as part of an internship assignment to build a simple tool that can
check ROS/ROS2 code before running it in a simulator.

The main focus of this phase is to validate the structure and safety of ROS Python code and
generate clear reports that highlight errors and warnings.

---

## What is Implemented

### ROS Code Checker
The tool accepts a ZIP file containing a ROS Python package or node and performs the following checks:

- Python syntax validation
- ROS package structure verification
  - Checks for presence of `package.xml`
  - Checks for `setup.py` or `CMakeLists.txt`
- Detection of basic ROS components:
  - `rospy.init_node`
  - Publishers
  - Subscribers
  - Services
- Basic safety checks such as:
  - Infinite loops without sleep
  - Potentially unsafe numeric values used in code

After validation, the tool generates:
- A readable text report
- A JSON report for structured output

---

## Test Packages

Two sample test packages are included to verify the checker:

### good_package
- Contains a valid ROS Python node
- Includes `package.xml` and `setup.py`
- Passes syntax and structural checks

### bad_package
- Missing `package.xml`
- Contains an infinite loop without delay
- Fails validation as expected

These packages help demonstrate both pass and fail cases of the checker.

---

## How to Run the Project

### Requirements
- Python 3.x
- No ROS installation required for this phase

### Steps
1. Open a terminal in the project root directory:
   ```bash
   cd ros-code-checker
