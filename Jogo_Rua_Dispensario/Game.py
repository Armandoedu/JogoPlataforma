from Obstacle import Obstacle
from pygame.locals import *
from Player import Player
from Timer import Timer
from Sound import Sound
from Menu import Menu
from Map import Map
from GameOver import GameOver
#from Hydrant import Hydrant
from Motorcycle import Motorcycle
from Car import Car
import pygame
import os
#from sys import exit // Roda sem

abs_path = os.path.dirname(__file__)
musica_fundo = os.path.join(abs_path, 'Music', 'background_music.mp3')
musica_colisao = os.path.join(abs_path, 'Music', 'smw_1-up.wav')

#pygame.init() // Roda sem
#pygame.display.set_caption("Rua Do Dispensário") // Roda sem

# Tamanho da tela
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.game_map = Map(screen, screen_width, screen_height)
        self.player = Player(screen)
        #self.obstacle = Obstacle(screen_width, screen_height)
        self.menu = Menu()
        self.music = Sound(musica_fundo, musica_colisao)
        self.game_over = GameOver()
        #self.hydrant = Hydrant(screen_width, screen_height)
        self.car = Car(screen_width, screen_height)
        self.motorcycle = Motorcycle(screen_width, screen_height)

        self.running = True
        self.state = "Menu"
        self.timer = Timer(screen)


    def draw(self, screen):
        self.game_map.draw()
        self.player.draw()
        #self.obstacle.draw(screen)
        #self.hydrant.draw(screen)
        self.motorcycle.draw(screen)
        self.car.draw(screen)
        self.timer.printTimeOnScreen()
        pygame.display.flip()


    def update(self):
        self.player.handleKeys()
        self.player.update()
        self.car.update()
        self.motorcycle.update()
        self.timer.updateTime()
        obstacles = [self.car, self.motorcycle]
        for o in obstacles:
            if self.player.isCollision(o):
                self.music.playSound()
                self.game_over.showGameOverScreen()

    def playBackgroundMusic(self):
        '''Toca a música de fundo do jogo.'''
        self.music.playMusic()
        self.music.setVolume(3)

    def run(self):
        '''Roda o jogo.'''
        if self.state == "Menu":
            self.menu.showMenuScreen()
            self.state = "Playing"

        if self.state == "Playing":
            self.playBackgroundMusic()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()

                self.draw(screen)
                self.update()
                self.clock.tick(15)