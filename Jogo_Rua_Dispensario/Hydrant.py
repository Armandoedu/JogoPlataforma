import pygame
import os
from Obstacle import Obstacle

sprites_path = os.path.dirname(__file__)
sprites = os.path.join(sprites_path, 'Sprites')
image_path = sprites + '/hydrant/'

class Hydrant (Obstacle):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.image = pygame.image.load(f'{image_path}Hydrant.png')

