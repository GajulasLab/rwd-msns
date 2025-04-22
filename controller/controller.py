# controller/controller.py

import pygame
from core.trigger_engine import TriggerEngine

class Controller:
    def __init__(self):
        self.engine = TriggerEngine()
        self.current_trigger = None

        # Key mapping
        self.key_map = {
            pygame.K_1: "N1",
            pygame.K_2: "N2",
            pygame.K_3: "N3",
            pygame.K_4: "N4",
            pygame.K_5: "N5",
            pygame.K_6: "P1",
            pygame.K_7: "P2",
            pygame.K_8: "P3",
            pygame.K_9: "P4",
            pygame.K_0: "P5",
            pygame.K_q: "H1",
            pygame.K_w: "H2",
            pygame.K_e: "H3",
            pygame.K_r: "H4",
            pygame.K_a: "C1",
            pygame.K_s: "C2",
            pygame.K_d: "C3",
            pygame.K_f: "C4"
        }

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            print(f"🔑 Key Pressed: {event.key} ({pygame.key.name(event.key)})")
            trigger_code = self.key_map.get(event.key)
            if trigger_code:
                print(f"✅ Trigger Matched: {trigger_code}")
                self.current_trigger = self.engine.get_trigger(trigger_code)
                return self.current_trigger
            else:
                print("⚠️ No mapped trigger for this key.")
        return None
