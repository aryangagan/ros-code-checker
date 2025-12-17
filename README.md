# ROS Code Checker and Simulation Preview Tool

## Overview
This project is a simple ROS/ROS2 code checker and simulation preview tool built as part of a robotics internship assignment.

The tool validates ROS code, performs basic safety checks, runs the code in a robotic arm simulator, and shows the results through a minimal web interface.

---

## Features

### Code Checker
- Accepts a ZIP file containing a ROS/ROS2 package or node
- Checks Python syntax using flake8
- Verifies ROS package structure (package.xml, CMakeLists.txt / setup.py)
- Detects publishers, subscribers, services, and init_node
- Performs basic motion safety checks
- Generates text and JSON reports

### Simulation Runner
- Runs validated code in Gazebo or CoppeliaSim
- Uses a simple 6-DOF robotic arm
- Scene includes one cube and one target position
- Records joint movements and execution result
- Captures simulation screenshots

### Web Interface
- Upload ROS code
- View checker reports
- Trigger simulation
- View logs and preview images

---

## Project Structure

