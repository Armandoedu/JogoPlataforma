import pygame 
from pygame.locals import *
from sys import exit

pygame.init()

largura = 800
altura = 400

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Player')

PLAYER_RUN = [
        pygame.image.load('Jogo_Rua_dispensario/JogoPlataforma/Jogo_Rua_dispensario/Sprites/run/0001.png'), 
        pygame.image.load('sprites/run/0003.png'),
        pygame.image.load('sprites/run/0005.png'),
        pygame.image.load('sprites/run/0007.png'),
        pygame.image.load('sprites/run/0009.png'),
        pygame.image.load('sprites/run/0011.png'),
        pygame.image.load('sprites/run/0013.png'),
        pygame.image.load('sprites/run/0015.png'),
        pygame.image.load('sprites/run/0017.png'),
        pygame.image.load('sprites/run/0019.png'),
        pygame.image.load('sprites/run/0021.png'),
        pygame.image.load('sprites/run/0023.png'),
        pygame.image.load('sprites/run/0025.png'),
        pygame.image.load('sprites/run/0027.png'),
        pygame.image.load('sprites/run/0029.png'),
]

PLAYER_JUMP = []

class Player(pygame.sprite.Sprite):
    def __init__(self): #construtor
        pygame.sprite.Sprite.__init__(self)
        self.sprites:list = PLAYER_RUN
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect() #coordenadas da imagem 
        self.rect.topleft = 100, 100 #canto superior esquerdo
        self.animar = False

    def mover(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 1
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (120, 120))


if __name__ == "__main__":
    animacoes = pygame.sprite.Group()
    player = Player()
    animacoes.add(player)

    relogio = pygame.time.Clock()

    while True:
        relogio.tick(30)
        tela.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_a:
                    x = x - 20
                if event.key == K_d:
                    x = x + 20
                if event.key == K_w:
                    y = y - 20
                if event.key == K_s:
                    y = y + 20
                player.mover()
        
        animacoes.draw(tela)
        animacoes.update()
        player.update()

        pygame.display.flip()