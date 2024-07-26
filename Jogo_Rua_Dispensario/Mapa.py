import pygame

image_path = "JogoPlataforma/Jogo_Rua_dispensario/Sprites/Rua.png"

class Mapa:
    def __init__(self, image_path, screen):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (800, 500))
        self.screen = screen
        self.rect = self.image.get_rect()

    def draw(self):
        self.screen.blit(self.image, self.rect)