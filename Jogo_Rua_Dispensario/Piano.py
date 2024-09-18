import pygame
import os
from Obstacle import Obstacle
import random

sprites_path = os.path.dirname(__file__)
sprites = os.path.join(sprites_path, 'Sprites')
image_path = sprites + '/piano/'
image_hydrant_path = f'{image_path}Piano.png'
obstacle_size = (32 * 3, 32 * 3)

class Piano(Obstacle):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, obstacle_size, image_hydrant_path)
        self.rect.y = 0
        self.rect.x = random.randint(0, 900)
        self.fall = True