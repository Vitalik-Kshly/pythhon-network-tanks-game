import pygame, sys
from pygame.locals import *
from client import Player, PlayerObj, GameData




class GUI:
    SCREEN = (800, 800)
    WHITE  = (255, 255, 255, 255)
    BLACK  = (0, 0, 0, 255)
    GREEN  = (0, 255, 0, 255)
    BLUE   = (0, 0, 255, 0)
    players = []
    TANK_SOURCE = pygame.image.load('img/tank.png')

    def __init__(self) -> None:
        
        self.DISPSURF = pygame.display.set_mode(self.SCREEN)
        self.DISPSURF.fill(self.WHITE)
        self.player = Player(ADDR)
        self.angle = 0
        self.image = self.TANK_SOURCE
        self.update()
        

    def update(self):
        pygame.init()

        while True:
            self.get_input()
            self.DISPSURF.fill(self.WHITE)
            self.display()
            pygame.display.update()

    def add_player():
        pass

    def display(self):
        # self.image = pygame.transform.rotate(self.image, self.angle)
        for data in self.player.player_pos:
            self.DISPSURF.blit(self.image, (data.data.pos_x, data.data.pos_y))
        self.angle += 1


    def get_input(self):
        for event in pygame.event.get():
                if event.type == QUIT:
                    self.player.alive = False
                    self.player.close_connection()
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player.game_data.keys['W'] = 1
                    if event.key == pygame.K_a:
                        self.player.game_data.keys['A'] = 1
                    if event.key == pygame.K_s:
                        self.player.game_data.keys['S'] = 1
                    if event.key == pygame.K_d:
                        self.player.game_data.keys['D'] = 1
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.player.game_data.keys['W'] = 0
                    if event.key == pygame.K_a:
                        self.player.game_data.keys['A'] = 0
                    if event.key == pygame.K_s:
                        self.player.game_data.keys['S'] = 0
                    if event.key == pygame.K_d:
                        self.player.game_data.keys['D'] = 0



ADDR = input('Enter address: ')
gui = GUI()