from pygame.locals import *
from Player import Player
from Timer import Timer
from Sound import Sound
from Menu import Menu
from Map import Map
from GameOver import GameOver
from ObstacleFactory import ObstacleFactory
import pygame
import os

abs_path = os.path.dirname(__file__)
musica_fundo = os.path.join(abs_path, 'Music', 'background_music.mp3')
musica_colisao = os.path.join(abs_path, 'Music', 'smw_1-up.wav')

screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.game_map = Map(screen, screen_width, screen_height)
        self.player = Player(screen)
        self.menu = Menu()
        self.music = Sound(musica_fundo, musica_colisao)
        self.game_over = GameOver()
        self.obstacle = ObstacleFactory.makeObstacle(screen_width, screen_height)

        self.running = True
        self.state = "Menu"
        self.timer = Timer(screen)

    # def makeObstacle(self,screen):
    #     obstacles = [self.car, self.motorcycle]
    #     choose = random.choice(obstacles)
    #     return choose.draw(screen)

    def draw(self, screen):
        self.game_map.draw()
        self.player.draw()
        self.obstacle.draw(screen)
        if self.obstacle.rect.x >= screen_width: #verificando se o obstaculo passou da tela 
            self.obstacle = ObstacleFactory.makeObstacle(screen_width, screen_height)
            #se passou, cria-se outro obstaculo aleatorio
        self.timer.printTimeOnScreen()
        pygame.display.flip()

    def update(self):
        self.player.handleKeys()
        self.player.update()
        self.obstacle.update()
        self.timer.updateTime()
        if self.player.isCollision(self.obstacle):
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