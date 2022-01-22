import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,screensettings,screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        new_bullet = Bullet(screensettings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(screensettings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            check_keydown_events(event,screensettings, screen,ship, bullets)

        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        if event.type == pygame.K_SPACE:
                new_bullet = Bullet(screensettings, screen, ship)
                bullets.append(new_bullet)


def update_screen( ship, bullets):


    #Redraw all bullets behind ship and alliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()