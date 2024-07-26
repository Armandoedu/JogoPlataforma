import pygame
import os

image_path = "/home/joao/Jogo_Rua_dispensario/JogoPlataforma/Jogo_Rua_dispensario/Sprites/Rua.png"
#image_path = os.path.join("Sprites", "Rua.png")


class Mapa:
    def __init__(self, image_path, screen):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (800, 500))
        self.screen = screen
        self.rect = self.image.get_rect()

    def draw(self):
        self.screen.blit(self.image, self.rect)

class Game:
    def __init__(self):
        pygame.init()
        self.screen_whidth = 1920
        self.screen_height = 1080
        self.screen = pygame.display.set_mode((self.screen_whidth, self.screen_height))
        pygame.display.set_caption("Rua Do Dispensário")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_mapa = Mapa(image_path, self.screen)

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