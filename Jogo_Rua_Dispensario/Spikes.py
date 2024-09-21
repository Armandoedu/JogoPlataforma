import pygame
import os
import random
from VerticalObstacle import VerticalObstacle

sprites_path = os.path.dirname(__file__)
sprites = os.path.join(sprites_path, 'Sprites')
image_path = sprites + '/Spikes/'
image_spikes_path = f'{image_path}Spikes.png'
obstacle_size = (32 * 3, 32 * 3)

class Spikes(VerticalObstacle):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, obstacle_size, image_spikes_path)