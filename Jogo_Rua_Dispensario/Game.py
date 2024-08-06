from Obstacle import Obstacle
from Player import Player
from Sound import Sound
from Map import Map
import random
import pygame
import os

# musica de fundo


# abs_path = os.path.dirname(__file__)
# background_music = os.path.join(abs_path, 'Music', 'background_music.mp3')
# barulho_colisao = os.path.join(abs_path, 'Music', 'smw_1-up.wav')

# Cores
RED = (255,0,0)

# Inicia o pygame
pygame.init()
pygame.display.set_caption("Rua Do Dispensário")

# Variáveis da tela
screen_width = 900
screen_height = 600

# Cria a tela do jogo
screen = pygame.display.set_mode((screen_width, screen_height))

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.game_map = Map(screen, screen_width, screen_height)
        self.player = Player(screen, screen_width, screen_height)
        self.obstacle = Obstacle(screen_width, screen_height)
        self.musica_fundo = Sound()
        # self.musica_colisao = Sound()
        self.running = True

    def printGameOver(self):
        '''Imprime "Game Over! na tela."'''
        font = pygame.font.SysFont("Arial", 60)
        text = font.render("Game Over!", True, RED)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        #exit()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self, screen):
        screen.fill((0,0,0))
        self.game_map.draw()
        self.player.draw()
        self.obstacle.draw(screen)
        pygame.display.flip()

    def update(self):
        self.player.handleKeys()
        self.player.update()
        self.obstacle.update()
        if self.player.isColision(self.obstacle):
            # self.barulho_colisao.playSaund()
            self.printGameOver()

    # def playBackgroundMusic(self):
    #     '''Toca a música de fundo do jogo.'''
    #     music = Sound()
    #     music.playMusic()
    #     music.setVolume(0.06) # 0.06 - para fones do ouvido (com fio)

    # def run(self):
    #     '''Roda o jogo.'''
    #     # self.playBackgroundMusic()
    #     self.barulho.playMusic()
    #     self.barulho.setVolume(3)

    #     while self.running:
    #         self.handleEvents()
    #         self.draw(screen)
    #         self.update()
    #         self.clock.tick(15)