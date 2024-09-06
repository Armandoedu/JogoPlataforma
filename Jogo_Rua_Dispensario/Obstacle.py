import pygame
import random
import os

class Obstacle:
    def __init__(self, screen_width, screen_height, obstacle_size, image_path):
        self.obstacle_size : tuple= obstacle_size
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.obstacle_size)
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.rect.topleft = (screen_width - obstacle_size[0], screen_height - obstacle_size[1] - 45)
        self.obstacle_speed: int = 5
        self.rect.inflate_ip((- 45, - 45))
        
    def update(self):
        self.obstacle_speed = random.randint(10,40)
        self.rect.x -= self.obstacle_speed 
        if self.rect.x < 0:
            self.rect.x = self.screen_width
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)