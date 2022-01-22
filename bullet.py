import sys
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class manage bullet from the ship"""

    def __init__(self, screensettings, screen, ship):
        """create bullet object at the shipt current position """
        super(Bullet, self).__init__()
        self.screen = screen

        #create bullet at 0, 0 then set correct position
        self.rect = pygame.Rect(0,0, screensettings.bullet_width,
         screensettings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.bottom =ship.rect.top

        #store bullet value as float
        self.y = float(self.rect.y)

        self.color= screensettings.bullet_color
        self.speed_factor = screensettings.bullet_speed_factor

    def update(self):
        #move the bullet up of the scree
        self.y -= self.speed_factor
        #update the position of the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        #Draw bullets
        pygame.draw.rect(self.screen, self.color, self.rect)


