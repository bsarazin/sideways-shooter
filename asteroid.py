import pygame
from pygame.sprite import Sprite


class Asteroid(Sprite):
    """space rock!"""

    def __init__(self, ai_settings, screen):
        super(Asteroid, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.speed_factor = self.ai_settings.asteroid_speed_factor

        # Load the asteroid image and set its Rect attributes
        self.image = pygame.image.load('images/asteroid.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new asteroid near the middle of the screen
        self.rect.centerx = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery

        # Store the bullet's position as a decimal value
        self.x = float(self.rect.x)
        
    def blitme(self) -> None:
        """Draw the asteroid at it's current location"""
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        """Move the bullet up on the screen"""
        # Update the decimal position of the bullet
        self.x -= self.speed_factor
        # Update the rect position
        self.rect.x = self.x