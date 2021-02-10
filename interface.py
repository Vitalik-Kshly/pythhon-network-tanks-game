import pygame, sys
from pygame.locals import *

pygame.init()
SCREEN = (800, 800)
WHITE  = (255, 255, 255, 255)
BLACK  = (0, 0, 0, 255)
GREEN  = (0, 255, 0, 255)
BLUE   = (0, 0, 255, 0)
DISPSURF = pygame.display.set_mode(SCREEN)
FONT = pygame.font.Font('freesansbold.ttf', 32)
DISPSURF.fill(WHITE)

texture = pygame.image.load("img/Tank.png")



clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    DISPSURF.blit(texture, (0, 0))
    time = clock.get_time()
    
    clock.tick()
    pygame.display.update()
