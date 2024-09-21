import pygame
import os
from VerticalObstacle import VerticalObstacle
import random

sprites_path = os.path.dirname(__file__)
sprites = os.path.join(sprites_path, 'Sprites')
image_path = sprites + '/piano/'
image_piano_path = f'{image_path}Piano.png'
obstacle_size = (32 * 3, 32 * 3)

class Piano(VerticalObstacle):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, obstacle_size, image_piano_path)
