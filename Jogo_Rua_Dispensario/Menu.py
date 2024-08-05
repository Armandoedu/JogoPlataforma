# from Game import Game
import pygame
import os
from sys import exit
from pygame.locals import *

sprites_path = os.path.dirname(__file__)
sprites = os.path.join(sprites_path, 'Sprites')
image_path =  sprites + '/menu/'


class Menu:
    def __init__(self, screen, screen_width, screen_height):
        pygame.init()
        # self.width = 1472
        # self.height = 704
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Rua do Dispensário")
        self.image_background = pygame.image.load(f'{image_path}image_menu.png')
        self.background = (0,0,0)
        self.running = True
        self.title = pygame.font.Font(None, 72) 
        self.title_surface = self.title.render("Rua Do Dispensário", False, (28,28,28))
        self.title_rect = self.title_surface.get_rect(center=(screen_width/2, screen_height/2-200))
        self.instruction = pygame.font.Font(None, 50) 
        self.instruction_surface = self.instruction.render("Press ENTER", False, (28,28,28))
        self.instruction_rect = self.instruction_surface.get_rect(center=(screen_width/2, screen_height/2-50))
        

    def ruunning(self):    
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.quit()
                    exit()
            
                if event.type == KEYDOWN:
                    if event.key == K_KP_ENTER or event.key == K_RETURN:
                        print("Tecla enter pressionada")
                        self.running = False
                        # pygame.quit()
                        # exit()
            
            self.screen.blit(self.image_background, (0,0))
            self.screen.blit(self.title_surface, self.title_rect)
            self.screen.blit(self.instruction_surface, self.instruction_rect)
            pygame.display.flip()

        # pygame.quit()

# teste = Menu()
# teste.ruunning()