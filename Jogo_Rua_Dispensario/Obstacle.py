import pygame
import random

YELLOW = (255, 255, 0)
screen_width = 800
screen_height = 600

# Obstacle ainda não está funcional
class Obstacle:
    def __init__(self, x, y, screen_width, screen_height):
        self.rect = pygame.Rect(x, y, screen_width, screen_height)
        self.speed = 7
        self.obstacle_size = 50
        self.obstacle_x = screen_width
        self.obstacle_y = screen_height - self.obstacle_size
        self.obstacle_speed = 7
        self.screen_width = screen_width
        self.screen_height = screen_height

    def moveObstacle(self):
        self.rect.y += self.speed
        if self.rect.y > self.screen_height:
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, self.screen_width - self.rect.width)

    def drawObstacle(self, screen):
        pygame.draw.rect(screen, YELLOW, self.rect)