# Logic to handle all trigger-based messaging
# core/trigger_engine.py

class TriggerEngine:
    def __init__(self):
        # Centralized trigger definitions (message + icon file)
        self.triggers = {
            "N1": {"message": "U-turn Ahead", "icon": "assets/arrows/uturn.png"},
            "N2": {"message": "Sharp Left After Intersection", "icon": "assets/arrows/left_arrow.png"},
            "N3": {"message": "Highway Ramp Approaching", "icon": "assets/arrows/ramp.png"},
            "N4": {"message": "Roundabout Approaching", "icon": "assets/arrows/roundabout.png"},
            "N5": {"message": "Lane Switching", "icon": "assets/arrows/switch_lane.png"},

            "P1": {"message": "Looking for Parking", "icon": "assets/arrows/search.png"},
            "P2": {"message": "Parking Right in 100m", "icon": "assets/arrows/parking_right.png"},
            "P3": {"message": "Parallel Parking", "icon": "assets/arrows/parking_parallel.png"},
            "P4": {"message": "Stopped. Waiting for Assistance", "icon": "assets/arrows/emergency.png"},
            "P5": {"message": "Custom Parking Message", "icon": "assets/arrows/custom.png"},

            "H1": {"message": "Damaged Road Ahead", "icon": "assets/arrows/road_damage.png"},
            "H2": {"message": "Emergency Braking!", "icon": "assets/arrows/brake.png"},
            "H3": {"message": "Weather Caution: Fog", "icon": "assets/arrows/fog.png"},
            "H4": {"message": "Emergency Override Triggered", "icon": "assets/arrows/alert.png"},

            "C1": {"message": "Left Turn", "icon": "assets/arrows/left_arrow.png"},
            "C2": {"message": "Stopping Ahead", "icon": "assets/arrows/brake.png"},
            "C3": {"message": "Drop-off Zone", "icon": "assets/arrows/bus.png"},
            "C4": {"message": "Traffic Jam Ahead", "icon": "assets/arrows/slow.png"},
        }

    def get_trigger(self, trigger_code):
        return self.triggers.get(trigger_code, {"message": "No Action", "icon": None})
