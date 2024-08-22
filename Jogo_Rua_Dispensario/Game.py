from Obstacle import Obstacle
from pygame.locals import *
from Player import Player
from Timer import Timer
from Sound import Sound
from Menu import Menu
from Map import Map
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
        self.obstacle = Obstacle(screen_width, screen_height)
        self.menu = Menu(screen_width, screen_height)
        self.music = Sound(musica_fundo, musica_colisao)
        self.running = True
        self.state = "Menu"
        self.timer = Timer(screen)

    def printGameOver(self):
        '''Imprime "Game Over!" na tela."'''
        font = pygame.font.SysFont("Arial", 60)
        text = font.render("Game Over!", True, True, (255,0,0))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        exit()

    def draw(self, screen):
        self.game_map.draw()
        self.player.draw()
        self.obstacle.draw(screen)
        self.timer.printTimeOnScreen()
        pygame.display.flip()

    def update(self):
        self.player.handleKeys()
        self.player.update()
        self.obstacle.update()
        self.timer.updateTime()
        if self.player.isCollision(self.obstacle):
            self.music.playSound()
            self.printGameOver()

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