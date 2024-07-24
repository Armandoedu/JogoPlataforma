import pygame 
from pygame.locals import *
from sys import exit
import os 

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Player')

class Player(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
            
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
            player.mover

    animacoes.draw(tela)
    animacoes.update()

    pygame.display.flip()
