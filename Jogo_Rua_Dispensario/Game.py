import pygame
import os
from Player import Player
from Mapa import Mapa
from Som import Som

abs_path = os.path.dirname(__file__)
music = os.path.join(abs_path, 'Music', 'musica_de_fundo.mp3')

class Game:
    def __init__(self):
        pygame.init()
        self.screen_whidth = 800
        self.screen_height = 500
        self.screen = pygame.display.set_mode((self.screen_whidth, self.screen_height))
        pygame.display.set_caption("Rua Do Dispensário")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_mapa = Mapa(self.screen)
        self.musica = Som(music)
        self.musica.play()
        self.player = Player(self.screen)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

            self.screen.fill((0,0,0))
            self.game_mapa.draw()
            self.player.draw()
            self.player.handle_keys()
            self.player.update()
            pygame.display.flip()
            self.clock.tick(15)