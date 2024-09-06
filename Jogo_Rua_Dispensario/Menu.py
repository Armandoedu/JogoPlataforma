from pygame.locals import *
import pygame
import os
from Screen import Screen 

sprites_path = os.path.dirname(__file__)
sprites = os.path.join(sprites_path, 'Sprites')
image_path = sprites + '/menu/'

class Menu (Screen):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.image_background = pygame.image.load(f'{image_path}dispeImagem.png')
        self.running = True


    def showMenuScreen(self):
        self.Tela()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_KP_ENTER or event.key == K_RETURN:
                        self.running = False
            self.screen.blit(self.image_background, (0,0))
            pygame.display.flip()
