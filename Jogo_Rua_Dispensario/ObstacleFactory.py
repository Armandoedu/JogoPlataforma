import pygame
import random
from Car import Car
from Motorcycle import Motorcycle

# fabrica de obstaculos para gerar obstaculos aleatorios 
class ObstacleFactory:
    @staticmethod
    def makeObstacle(screen_width, screen_height):
        obstacles = [Car, Motorcycle]
        choose = random.choice(obstacles)
        return choose(screen_width, screen_height)
    