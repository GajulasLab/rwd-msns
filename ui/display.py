# Pygame-based display manager for rendering icons + text
# ui/display.py

import pygame
import os

class DisplayManager:
    def __init__(self, screen_width=800, screen_height=480):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("MSNS - Rear Display")
        self.font = pygame.font.SysFont("Arial", 36)
        self.bg_color = (0, 0, 0)  # black background

    def render_instruction(self, icon_path, message):
        self.screen.fill(self.bg_color)

        # Load and draw icon
        if icon_path and os.path.exists(icon_path):
            try:
                icon = pygame.image.load(icon_path)
                icon = pygame.transform.scale(icon, (150, 150))
                self.screen.blit(icon, (50, 150))
            except pygame.error:
                print(f"Error loading image: {icon_path}")

        # Draw text
        if message:
            text_surface = self.font.render(message, True, (255, 255, 255))
            self.screen.blit(text_surface, (250, 200))

        pygame.display.flip()

    def clear(self):
        self.screen.fill(self.bg_color)
        pygame.display.flip()
