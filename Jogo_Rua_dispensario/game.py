import pygame
from mapa import Mapa
from som import Som


class Game:
    def __init__(self):
        pygame.init()
        self.screen_whidth = 1920
        self.screen_height = 1080
        self.screen = pygame.display.set_mode((self.screen_whidth, self.screen_height))
        pygame.display.set_caption("Rua Do Dispensário")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_mapa = Mapa('Jogo_Rua_dispensario\Rua.png', self.screen)

        self.musica = Som('Jogo_Rua_dispensario\musica_de_fundo.mp3')
        self.musica.play()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()   

            self.screen.fill((0,0,0))
            self.game_mapa.draw()
            pygame.display.flip()
            self.clock.tick(60)