import pygame
import os

sprites_path = os.path.dirname(__file__)
sprites = os.path.join(sprites_path, 'Sprites')
image_path = sprites + '/mapa/'

class Mapa:
    def __init__(self, screen):
        self.image = pygame.image.load(f'{image_path}Rua.png')
        self.image = pygame.transform.scale(self.image, (800, 500))
        self.screen = screen
        self.rect = self.image.get_rect()

    def draw(self):
        self.screen.blit(self.image, self.rect)