import pygame
import time
# from Game import Game

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
# tela = pygame.display.set_mode((400, 400))

# Define a fonte
font = pygame.font.SysFont("Arial", 40)

class Crono:
    def __init__(self, screen):
        self.meu_tempo = 10
        self.x = self.meu_tempo
        self.ultimo_tempo = time.time()
        self.screen = screen
        # self.game = Game()

    def atualizar_tempo(self):
        agora = time.time()
        if agora - self.ultimo_tempo >= 1:  # Atualiza a cada 1 segundo
            self.x -= 1
            self.ultimo_tempo = agora
        if self.x == -1:
            # self.game.printGameOver()
            pygame.quit()

    def renderizar(self):
        self.mensagem = f"Tempo: {self.x}"
        self.textoformatado = font.render(self.mensagem, False, (255, 255, 255))
        self.retTexto = self.textoformatado.get_rect()
        
        # Preenche a tela com uma cor antes de desenhar o texto (limpa a tela)
        # self.screen.fill((0, 0, 0))

        # Centraliza o texto na self.screen
        self.retTexto.center = (780, 35)
        self.screen.blit(self.textoformatado, self.retTexto)

        # Atualiza a tela
        pygame.display.flip()

# # Instancia o cronômetro
# crono = Crono()






# Loop principal
# executando = True
# while executando:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             executando = False

#     if crono.x > 0:
#         crono.atualizar_tempo()
#         crono.renderizar()
#     else:
#         executando = False  # Encerra o loop quando o cronômetro chegar a 0

# # Encerra o Pygame
# pygame.quit()


