import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to manage start"""

    def __init__(self, ai_settings, screen):
        """Create a star"""
        super(Star, self).__init__()
        self.screen = screen

        # Create a star at 0,0 and then set the correct position
        self.rect = pygame.Rect(
            0, 0, ai_settings.star_width, ai_settings.star_height)

        self.color = ai_settings.star_color
        

    def draw_star(self) -> None:
        """Draw stars on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)