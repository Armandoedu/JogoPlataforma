import pygame
import os
import random
from Obstacle import Obstacle

sprites_path = os.path.dirname(__file__)
sprites = os.path.join(sprites_path, 'Sprites')
image_path = sprites + '/Spikes/'
image_motorcycle_path = f'{image_path}Spikes.png'
obstacle_size = (32 * 3, 32 * 3)

class Spikes(Obstacle):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, obstacle_size, image_motorcycle_path, x=random.randint(0, screen_width), y=920)
        self.fall = True