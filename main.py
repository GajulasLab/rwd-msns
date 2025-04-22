# main.py

import pygame
from controller.controller import Controller
from ui.display import DisplayManager

def main():
    pygame.init()
    clock = pygame.time.Clock()
    controller = Controller()
    display_manager = DisplayManager()

    running = True
    last_trigger = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

            trigger = controller.process_event(event)
            if trigger and trigger != last_trigger:
                icon = trigger["icon"]
                message = trigger["message"]
                display_manager.render_instruction(icon, message)
                last_trigger = trigger

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
