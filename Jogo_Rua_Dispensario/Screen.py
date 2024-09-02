import pygame
from pygame.locals import *
from sys import exit

class Screen:
    def __init__(self):
        pygame.init()
        self.screen_width = 900 
        self.screen_height = 600
        self.nome = "Rua do Dispensário"
        self.screen = ""
        
    def Tela(self):
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.nome)
        