import pygame, sys
from pygame.locals import *






class GUI:
    SCREEN = (800, 800)
    WHITE  = (255, 255, 255, 255)
    BLACK  = (0, 0, 0, 255)
    GREEN  = (0, 255, 0, 255)
    BLUE   = (0, 0, 255, 0)
    def __init__(self) -> None:
        pygame.init()
        DISPSURF = pygame.display.set_mode(SCREEN)
        DISPSURF.fill(WHITE)