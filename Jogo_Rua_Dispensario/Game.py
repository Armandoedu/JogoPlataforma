from Obstacle import Obstacle
from Player import Player
from Sound import Sound # Som agora é Sound (apagar esse comentário depois)
from Map import Map # Mapa agora é Map (apagar esse comentário depois)
import random
import pygame
import os

# Pegar o caminho da musica de fundo
abs_path = os.path.dirname(__file__)
background_music = os.path.join(abs_path, 'Music', 'background_music.mp3')

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

# Diminui o numero de "selfs" no construtor e coloquei o Sound antes loop while (apagar esse comentário depois)
class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.game_map = Map(screen, screen_width, screen_height)
        self.player = Player(screen, screen_width, screen_height)

    def printGameOver(self):
        '''Imprime "Game Over! na tela."'''
        font = pygame.font.SysFont("Arial", 60)
        text = font.render("Game Over!", True, RED)
        self.screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        pygame.display.flip()
        #pygame.time.wait(2000)
        #pygame.quit()
        #exit()

    def run(self):
        '''Roda o jogo.'''

        # Toca a música de fundo do jogo
        music = Sound(background_music)
        music.playMusic()
        music.setVolume(0.06) # 0.06 - para fones do ouvido (com fio)

        # Variável de controle do jogo
        # (antes era "self.running") (apagar esse comentário depois)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0,0,0))
            self.game_map.draw()
            self.player.draw()
            self.player.handleKeys()
            self.player.update()
            #Game.printGameOver(self)
            pygame.display.flip()
            self.clock.tick(15)