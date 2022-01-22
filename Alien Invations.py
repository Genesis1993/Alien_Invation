import pygame
from pygame.sprite import Group
from screen_settings import Settings
from ship_settings import Ship
import game_functions as gf


##Trial changes for git demo

FPS = 100
pygame.init()
screensettings = Settings()
#intialize game and create screen object
screen = pygame.display.set_mode((screensettings.screen_with, screensettings.screen_height))
pygame.display.set_caption("Alien Invations")
#make a ship
ship = Ship(screensettings,screen)
# Make a group to store bullets
bullets = Group()
clock = pygame.time.Clock()

Running = True
#Start the main loop of the game
while Running:
    clock.tick(FPS)
    #fill the screen with background
    screen.fill(screensettings.backgroundcolor)
    #See the keyboard events
    gf.check_events(screensettings, screen, ship, bullets)
    ship.update()
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= ship.screen_rect.top:
            bullet.remove(bullets)

    print(bullets)
    gf.update_screen(ship,bullets)
    pygame.display.flip()







