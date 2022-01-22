import pygame

class Ship():
    def __init__(self,screensettings,screen):
        """INITIALIZE CLASS SHIP"""
        self.screen = screen
        self.screensettings = screensettings

        #load image and set its rect.
        self.image = pygame.image.load('ship.png')
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        #start ship at the buttom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #make ships center value a float
        self.center = float(self.rect.centerx)
        #movement flag or notifier
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
             self.center += self.screensettings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
             self.center -= self.screensettings.ship_speed_factor
        #update self.rect.centerx as self.center
        self.rect.centerx = self.center

    def blitme(self):
        """draw ship at its current position"""
        self.screen.blit(self.image, self.rect)
