import pygame 
from pygame.locals import *
from sys import exit

sprites_path = "JogoPlataforma/Jogo_Rua_Dispensario/Sprites/run/"

PLAYER_RUN = [
        pygame.image.load(f'{sprites_path}0001.png'),
        pygame.image.load(f'{sprites_path}0003.png'),
        pygame.image.load(f'{sprites_path}0005.png'),
        pygame.image.load(f'{sprites_path}0007.png'),
        pygame.image.load(f'{sprites_path}0009.png'),
        pygame.image.load(f'{sprites_path}0011.png'),
        pygame.image.load(f'{sprites_path}0013.png'),
        pygame.image.load(f'{sprites_path}0015.png'),
        pygame.image.load(f'{sprites_path}0017.png'),
        pygame.image.load(f'{sprites_path}0019.png'),
        pygame.image.load(f'{sprites_path}0021.png'),
        pygame.image.load(f'{sprites_path}0023.png'),
        pygame.image.load(f'{sprites_path}0025.png'),
        pygame.image.load(f'{sprites_path}0027.png'),
        pygame.image.load(f'{sprites_path}0029.png'),
]

# PLAYER_JUMP = []

class Player(pygame.sprite.Sprite):
    def __init__(self, screen): # Construtor
        pygame.sprite.Sprite.__init__(self)
        self.sprites:list = PLAYER_RUN
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect() # Coordenadas da imagem 
        self.rect.topleft = 100, 100 # Canto superior esquerdo
        self.animar = False
        self.screen = screen
        self.speed = 5

    def mover(self):
        self.animar = True

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.mover()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.mover()
        if keys[pygame.K_UP]  or keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.mover()
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
            self.mover()

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 1
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (120, 120))