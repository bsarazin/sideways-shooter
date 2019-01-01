import pygame
from pygame.sprite import Group
from ship import Ship
from settings import Settings
import game_functions

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Pew Pew Pew")
    
    ship = Ship(ai_settings,screen)
    bullets = Group()
    stars = Group()
    asteroids = Group()

    game_functions.create_stars(ai_settings, screen, stars)

    while True:
        game_functions.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        game_functions.update_bullets(ai_settings,screen,ship,asteroids,bullets)
        game_functions.update_asteroids(ai_settings,screen,ship,asteroids,bullets)
        game_functions.update_screen(ai_settings,screen,ship,bullets,stars,asteroids)

run_game()