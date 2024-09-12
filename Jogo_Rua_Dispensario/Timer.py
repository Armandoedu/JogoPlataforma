import pygame
import time

pygame.init()
font = pygame.font.SysFont("Arial", 40)

class Timer:
    def __init__(self, screen):
        self.my_time = 60
        self.x = self.my_time
        self.last_time = time.time()
        self.screen = screen

    def updateTime(self):
        right_now = time.time()
        if right_now - self.last_time >= 1: # Atualiza a cada 1 segundo
            self.x -= 1
            self.last_time = right_now
        if self.x == -1:
            pygame.quit()

    def printTimeOnScreen(self):
        self.message = f"Time: {self.x}"
        self.formated_text = font.render(self.message, False, (255, 255, 255))
        self.text = self.formated_text.get_rect()

        # Preenche a tela com uma cor antes de desenhar o texto (limpa a tela)
        # self.screen.fill((0, 0, 0))

        # Centraliza o texto na self.screen
        self.text.center = (780, 35)
        self.screen.blit(self.formated_text, self.text)

        # Atualiza a tela
        pygame.display.flip()