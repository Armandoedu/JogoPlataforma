import pygame
import os

# Pegar o caminho da imagem de fundo
sprites_path = os.path.dirname(__file__)
sprites = os.path.join(sprites_path, 'Sprites')
image_path = sprites + '/map/'

# adicionados "screen_width, screen_height" ao construtor (apagar esse comentário depois)
# Mapa agora é Map (apagar esse comentário depois)
class Map:
    def __init__(self, screen, screen_width, screen_height):
        self.image = pygame.image.load(f'{image_path}Road2.jpeg')
        self.image = pygame.transform.scale(self.image, (screen_width+250, screen_height))
        self.screen = screen
        self.rect = self.image.get_rect()

    def draw(self):
        '''Desenha o mapa do jogo na tela.'''
        self.screen.blit(self.image, self.rect)