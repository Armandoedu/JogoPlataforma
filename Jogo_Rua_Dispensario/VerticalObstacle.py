import pygame
import random
from Obstacle import Obstacle

class VerticalObstacle(Obstacle):
    def __init__(self, screen_width, screen_height, obstacle_size, image_path):
        super().__init__(screen_width, screen_height, obstacle_size, image_path)
        self.rect.y = 0
        self.rect.x = random.randint(0, 900)
        self.fall = True

    def update(self):
        self.obstacle_speed = random.randint(30, 60)
        self.rect.y += self.obstacle_speed
        if self.rect.y < 0:
            self.rect.y = self.screen_width