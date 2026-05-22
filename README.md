# Simple Wheel Robot V1

A MicroPython-powered ESP32 wheeled robot project focused on learning embedded systems, motor control, networking, and remote robot operation.

This repository originally started as a basic motor movement test platform, but has now progressed into a WiFi-controlled robot with a Node.js control server and ESP32 command handling.

---

## Current Project Status

Current progress includes:

### Completed
- ESP32 configured with MicroPython
- Basic differential drive movement
- Forward, reverse, left, right, and stop controls
- Reusable motor helper functions
- GPIO motor driver integration
- WiFi connectivity on the ESP32
- HTTP command server running on the ESP32
- Node.js control server sending commands to the robot
- Basic command handling between PC and robot
- Initial power system planning and BOM

### In Progress
- Improving command reliability
- Cleaning up project structure
- Refining movement behaviour
- Preparing for onboard battery integration

### Planned
- Web dashboard / browser controls
- Speed control using PWM
- Acceleration smoothing
- Obstacle detection
- Camera support
- Autonomous behaviours
- Better chassis and cable management

---

## Features

### Robot Movement
- Forward movement
- Reverse movement
- Left turn
- Right turn
- Stop command

### Networking
- ESP32 WiFi connection
- HTTP command handling
- Remote control from external server

### Software Structure
- Modular movement helper functions
- Separate control/server logic
- Expandable project layout for future upgrades

---

## Tech Stack

### Hardware
- ESP32
- DC motors
- Motor driver module
- Wheeled chassis
- Planned battery power system

### Software
- MicroPython
- Python
- Node.js
- HTTP-based command communication

---

## Project Structure

```text
simple-wheel-robot-v1/
│
├── src/                 # ESP32 robot code
├── docs/                # Wiring notes and hardware docs
├── server/              # Node.js control server
├── power/               # Power system planning/BOM
└── README.md
```

---

## How It Works

### ESP32 Side
The ESP32:
- Connects to WiFi
- Runs the robot control code
- Receives HTTP commands
- Controls motor GPIO outputs

Movement commands are translated into motor driver signals for differential steering.

---

### Node.js Server
The Node.js server:
- Sends commands to the ESP32
- Acts as the bridge between the controller and robot
- Will eventually support a browser dashboard/UI

---

## Development Goals

This project is primarily being used to develop practical skills in:

- Embedded programming
- Robotics fundamentals
- Motor control
- Networking and communication
- Remote systems
- Project structure and documentation
- Hardware/software integration

---

## Next Major Milestone

The next major upgrade is planned to be:

1. Stable onboard battery power
2. Browser-based remote controls
3. PWM speed control
4. Smoother driving behaviour
5. Safer shutdown and stop handling

---

## Notes

This project intentionally started simple and is being expanded iteratively.

The goal is to build a strong foundation before introducing more advanced robotics concepts like:
- autonomy
- sensor fusion
- SLAM
- computer vision
- advanced navigation
