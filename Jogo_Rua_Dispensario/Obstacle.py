import pygame
import random

class Obstacle:
    def __init__(self, screen_width, screen_height):
        obstacle_size = random.randint(30,70)
        self.rect = pygame.Rect(screen_width, screen_height-50 - obstacle_size, obstacle_size, obstacle_size)
        self.screen_width = screen_width

    def update(self):
        obstacle_speed = random.randint(10,25)
        self.rect.x -= obstacle_speed
        if self.rect.x < 0:
            self.rect.x = self.screen_width

    def draw(self, screen):
        obstacle_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.draw.rect(screen, obstacle_color, self.rect)