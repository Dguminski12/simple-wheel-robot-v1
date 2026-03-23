# Robot Lab 0 — Simple Wheeled Robot (MicroPython)

## Overview
This phase focuses on getting a basic two-wheeled robot moving using MicroPython on the ESP32.  
The goal is to validate motor wiring, direction control, and core movement functions before adding complexity.

---

## Objectives
- Verify motor wiring is correct
- Implement basic movement controls
- Ensure consistent and predictable motor behaviour

---

## Features
- Forward movement
- Reverse movement
- Turning left
- Turning right
- Stop function

No advanced features are included at this stage:
- ❌ No WiFi connectivity  
- ❌ No web interface  
- ❌ No state machine  
- ❌ No acceleration or speed control  

---

## Project Structure
```
robot-lab-0/
│
├── src/
│   ├── motor.py     # Motor control helpers
│   └── main.py      # Simple movement test script
│
├── docs/
│   └── wiring.md    # Pin mapping and wiring notes
│
└── README.md
```

---

## How It Works

### `motor.py`
Contains reusable helper functions for controlling the motors:
- `forward()`
- `reverse()`
- `left()`
- `right()`
- `stop()`

These functions directly control GPIO pins connected to the motor driver.

---

### `main.py`
A simple test routine that:
1. Moves forward  
2. Stops  
3. Moves backward  
4. Turns left/right  
5. Stops again  

Used to confirm:
- Wiring is correct  
- Motor directions are correct  

---

## Success Criteria (Phase 0)
- ✅ Motors spin in the correct direction  
- ✅ Robot moves forward, reverse, left, and right  
- ✅ Robot stops reliably  
- ✅ Code runs consistently without errors  

---

## Next Steps (Phase 1 Preview)
Once this phase is complete, the next upgrades will include:
- Onboard battery power system (NiMH + buck converter)
- ESP32 WiFi connectivity
- Remote control via web dashboard
- Basic command protocol between controller and robot

---

## Notes
- If movement directions are incorrect, swap motor polarity or adjust logic in `motor.py`
- Keep this phase as simple as possible — avoid adding extra features too early
