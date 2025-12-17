ROS Code Checker & Simulation Preview Tool
Overview

This project is a simple tool to check ROS / ROS2 code and run it in a robotic arm simulation.

It was built as part of a robotics internship task to demonstrate:

ROS code validation

Basic safety checks

Running code in a simulator

Showing results through a minimal web interface

What This Tool Does
1. Code Checker

Accepts a ZIP file containing a ROS/ROS2 package or node

Checks:

Python syntax using flake8

ROS package structure (package.xml, CMakeLists.txt / setup.py)

Detects publishers, subscribers, services, and init_node

Basic safety checks (joint limits, missing sleep in loops)

Generates:

A text report

A JSON report

2. Simulation Runner

Runs the validated code in Gazebo / CoppeliaSim

Uses a simple 6-DOF robotic arm

Scene includes:

Robotic arm

One cube

One target position

Records:

Joint movements

Success or failure

Few simulation screenshots

3. Web Interface

Simple web UI to:

Upload ROS code

View checker report

Trigger simulation

See logs and preview images
