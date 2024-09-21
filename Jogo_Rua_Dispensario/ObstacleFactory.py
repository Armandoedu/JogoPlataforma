import pygame
import random
from Motorcycle import Motorcycle
from Spikes import Spikes
from Piano import Piano
from Car import Car

class ObstacleFactory:
    @staticmethod
    def makeObstacle(screen_width, screen_height):
        obstacles = [Motorcycle, Car, Piano, Spikes]
        choose = random.choice(obstacles)
        return choose(screen_width, screen_height)