import pygame
import random
import os 

sprites_path = os.path.dirname(__file__)
sprites = os.path.join(sprites_path, 'Sprites')
image_path = sprites + '/car/'

obstacle_size = (32 * 3, 32 * 3)

class Obstacle:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load(f'{image_path}Car.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, obstacle_size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (screen_width - obstacle_size[0], screen_height - obstacle_size[1] - 45)
        self.screen_width = screen_width
        self.obstacle_speed = 5
        self.rect.inflate_ip((- 45, - 45))
        
    def update(self):
        self.obstacle_speed = random.randint(10,25)
        self.rect.x -= self.obstacle_speed 
        if self.rect.x < 0:
            self.rect.x = self.screen_width

    def draw(self, screen):
        screen.blit(self.image, self.rect)
