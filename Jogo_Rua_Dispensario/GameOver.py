import pygame
from pygame.locals import *
from sys import exit
import os

sprites_path = os.path.dirname(__file__)
sprites = os.path.join(sprites_path, 'Sprites')
image_path = sprites + '/game_over/'

class GameOver:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Rua do Dispensário")
        self.image_background = pygame.image.load(f'{image_path}GameOver(2).jpg')
        self.running = True

    def showGameOverScreen(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    self.running = False
                    pygame.quit()
                    exit()
            
            self.screen.blit(self.image_background, (0,0))
            pygame.display.flip()

