import pygame
import random
from Obstacle import Obstacle

class HorizontalObstacle(Obstacle):
    def __init__(self, screen_width, screen_height, obstacle_size, image_path):
        super().__init__(screen_width, screen_height, obstacle_size, image_path)
    
    def update(self):
        self.obstacle_speed = random.randint(20, 40)
        self.rect.x -= self.obstacle_speed
        if self.rect.x < 0:
            self.rect.x = self.screen_width