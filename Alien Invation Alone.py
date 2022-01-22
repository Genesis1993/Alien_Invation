import pygame
import sys

#Screen speed
FPS = 100
clock = pygame.time.Clock()


#Create Sreen/Main windoe of the game
pygame.init()
screencolor = (0,0,0)
screensize = (1200,600)
screen=pygame.display.set_mode(screensize)
screen_rect = screen.get_rect()

#PlayerImageUpload and Pixeling
shipsize =(80,80)
shipspeed = 2
ship = pygame.image.load('ship.png')
ship = pygame.transform.scale(ship, shipsize)
ship_rect = ship.get_rect() # Get ship rectangular char


#Player Initial position
ship_rect.bottom = screen_rect.bottom
ship_rect.centerx = screen_rect.centerx
centerfloat = float(ship_rect.centerx)  # for smooth movement of ship to store float

class Bullet(pygame.sprite.Sprite):
    """A class manage bullet from the ship"""
    def __init__(self):
        """create bullet object at the shipt current position """
        pygame.sprite.Sprite.__init__(self)
        # Bullet Characteristics
        self.size = [3, 15]
        self.color = (0, 230, 0)
        self.speedfactor = 4

       # self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        #self.rect.centerx = ship_rect.centerx
        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = ship_rect.centerx
        self.rect.bottom =ship_rect.top
        self.yfloat = float(self.rect.y)
    def update(self):
        self.yfloat -= self.speedfactor
        self.rect.y = self.yfloat




def draw_ship():
    """draw ship function"""
    screen.blit(ship, ship_rect)





#draw initial position of ship
draw_ship()

#setting Initial value of moving_right and moving_left
moving_right = False
moving_left = False

running = True #Set initial value of running equals to True
#Main Loop of the game
bulleta = Bullet()
bullets = pygame.sprite.Group()

while running:
    clock.tick(FPS)
    screen.fill(screencolor)
    if moving_right == True:
        centerfloat += shipspeed
    if moving_left == True:
        centerfloat -= shipspeed
    ship_rect.centerx = centerfloat

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and ship_rect.right < screen_rect.right:
                moving_right=True
            if event.key == pygame.K_LEFT and ship_rect.left > screen_rect.left:
                moving_left=True
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet()
                new_bullet.centerx = ship_rect.centerx
                new_bullet.y = ship_rect.y
                bullets.add(new_bullet)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left= False
        if event.type == pygame.K_SPACE:
            new_bullet = Bullet()
            bullets.append(new_bullet)

    bullets.update()
    for bullet in bullets.sprites():
        if bullet.rect.bottom <= 0:
            bullet.remove(bullets)
    print (bullets)
    draw_ship()
    bullets.draw(screen)
    pygame.display.flip()
