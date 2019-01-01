import sys
import pygame
from ship import Ship
from bullet import Bullet
from star import Star
from pygame.sprite import Sprite
from random import randint
from asteroid import Asteroid

def check_events(ai_settings,screen,ship,bullets) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def check_keydown_events(event,ai_settings,screen,ship,bullets) -> None:
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event,ship) -> None:
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def update_screen(ai_settings,screen,ship,bullets,stars,asteroids) -> None:
    screen.fill(ai_settings.bg_color)

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    for star in stars.sprites():
        star.draw_star()
    
    for asteroid in asteroids.sprites():
        asteroid.blitme()

    ship.blitme()
    pygame.display.flip()

def update_bullets(ai_settings, screen,ship,asteroids,bullets) -> None:
    """Update the positions of bullets and remove old bullets"""
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.left > ai_settings.screen_width:
            bullets.remove(bullet)

    check_bullet_asteroid_collisions(ai_settings, screen, ship, asteroids, bullets)

def check_bullet_asteroid_collisions(ai_settings, screen,  ship, asteroids, bullets) -> None:
    """Respond to any bullet collisions"""
    # Check for any bullets that have hit asteroids
    # If so, get rid of the bullet and the asteroid
    # stored in a Dictionary
    collisions = pygame.sprite.groupcollide(bullets, asteroids, True, True)

def fire_bullet(ai_settings, screen, ship, bullets) -> None:
    """Fires bullet if limit not reached"""
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)

def remove_bullets(bullets) -> None:
    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_stars(ai_settings, screen, stars) -> None:
    """Create stars"""
    # Create stars
    for i in range(ai_settings.star_density):
        star = Star(ai_settings, screen)
        star.x = randint(0,ai_settings.screen_width)
        star.y = randint(0,ai_settings.screen_height)
        star.rect.x = star.x
        star.rect.y = star.y
        stars.add(star)

def update_asteroids(ai_settings, screen, ship, asteroids, bullets) -> None:
    """Check if the fleet is at an edge, and then update the position of all aliens"""
    asteroids.update()

    random = randint(0,100)
    if random <= ai_settings.asteroid_density:
        create_asteroid(ai_settings,screen,asteroids)

    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, asteroids):
        pass

def create_asteroid(ai_settings, screen, asteroids) -> None:
    """Create a fleet of aliens"""
    # Create an alien and place it in the row
    asteroid = Asteroid(ai_settings, screen)
    asteroid.x = ai_settings.screen_width
    asteroid.y = randint(0,ai_settings.screen_height)
    asteroid.rect.x = asteroid.x
    asteroid.rect.y = asteroid.y
    asteroids.add(asteroid)