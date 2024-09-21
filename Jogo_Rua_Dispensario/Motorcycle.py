import pygame
import os
from HorizontalObstacle import HorizontalObstacle

sprites_path = os.path.dirname(__file__)
sprites = os.path.join(sprites_path, 'Sprites')
image_path = sprites + '/motorcycle/'
image_motorcycle_path = f'{image_path}motorcycle.png'
obstacle_size = (32 * 3, 32 * 3)

class Motorcycle(HorizontalObstacle):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, obstacle_size, image_motorcycle_path)