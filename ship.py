import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('images/mf.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the left center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.left = self.screen_rect.left

        # Store a decimal value for the ship's center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self) -> None:
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
