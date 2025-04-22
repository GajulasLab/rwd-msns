# 🚘 MSNS - Rear Windshield Display Messaging and Sign Navigation System

A smart modular system designed to display real-time driver intentions and navigation cues on a vehicle’s **rear windshield**, helping reduce accidents, honking, and road rage by improving communication with following drivers.

---

## 🎯 Purpose

MSNS (Modular Sign Navigation System) enhances road safety by communicating:
- U-turns
- Sharp turns after intersections
- Parking intentions
- Emergency stops
- Caution alerts (e.g. fog, traffic jam, school zones)

---

## 🧠 Features Implemented in MVP

- 🔑 18 unique trigger modes (mapped to keyboard for simulation)
- 🧠 Modular logic system (separated into core, UI, controller)
- 💻 Pygame-based visual output (message + icon)
- 🛠️ Ready for hardware integration (e.g. Raspberry Pi, OLED HUD)
- 📦 Built with clean project structure (scalable, real-product ready)

---

## 🗂️ Folder Structure

RearDisplayPro/ ├── main.py ├── core/ │ └── trigger_engine.py ├── controller/ │ └── controller.py ├── ui/ │ └── display.py ├── data/ ├── hardware/ ├── assets/ │ └── arrows/ ├── utils/ └── requirements.txt

---

## 🧪 How to Run

### 🔧 Install dependencies:
```bash
pip install -r requirements.txt
▶️ Start app:
bash
Copy
python main.py
🕹️ Trigger a mode (keyboard keys):

Key	Action
1	U-turn ahead
7	Parking right in 100m
a	Left turn
q	Damaged road ahead
...	All 18 modes mapped (see code)
🔧 Built With
Python 3.x

Pygame

Modular OOP design

Ready for integration with car OS / sensor data

📘 License
MIT License ❤️

🚀 Future Enhancements
Real hardware trigger integration (CAN bus / GPIO)

Transparent OLED or LED Matrix display hookup

Mini-map visuals for directional context

Mobile app portal for driver presets

Made with vision by Saikiran Gajula 🚗✨
“Let cars speak to each other — not just blink.”

### ✅ Step 5: Save and Commit to Git

```bash
git add README.md
git commit -m "Added README.md with project summary and instructions"
git push