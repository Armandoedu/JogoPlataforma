from Obstacle import Obstacle
from Player import Player
from Sound import Sound
from Map import Map
from Menu import Menu
from pygame.locals import *
from sys import exit
import pygame
import os
from Crono import Crono




abs_path = os.path.dirname(__file__)
musica_fundo = os.path.join(abs_path, 'Music', 'background_music.mp3')
musica_colisao = os.path.join(abs_path, 'Music', 'smw_1-up.wav')




pygame.init()
pygame.display.set_caption("Rua Do Dispensário")
# font = pygame.font.SysFont("Arial", 30)

screen_width = 900 
screen_height = 600


screen = pygame.display.set_mode((screen_width, screen_height))

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.game_map = Map(screen, screen_width, screen_height)
        self.player = Player(screen)
        self.obstacle = Obstacle(screen_width, screen_height)
        self.menu = Menu(screen_width, screen_height)
        self.musica = Sound(musica_fundo, musica_colisao)
        self.running = True
        self.state = "Menu"
        self.crono = Crono(screen)

    def printGameOver(self):
        '''Imprime "Game Over! na tela."'''
        font = pygame.font.SysFont("Arial", 60)
        text = font.render("Game Over!", True, True, (255,0,0))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        exit()



    def draw(self, screen):
        self.game_map.draw()
        self.player.draw()
        self.obstacle.draw(screen)
        self.crono.renderizar()
        pygame.display.flip()

    def update(self):
        self.player.handleKeys()
        self.player.update()
        self.obstacle.update()
        self.crono.atualizar_tempo()
        if self.player.isCollision(self.obstacle):
            self.musica.playSound()
            self.printGameOver()

    def playBackgroundMusic(self):
        '''Toca a música de fundo do jogo.'''
        self.musica.playMusic()
        self.musica.setVolume(3)

    # def renderizar(self):
    #     self.mensagem = f"tempo: {self.x}"
    #     self.textoformatado = font.render(self.mensagem, False, (255, 255, 255))
    #     self.retTexto = self.textoformatado.get_rect()
        
    #     # Preenche a tela com uma cor antes de desenhar o texto (limpa a tela)
    #     screen.fill((0, 0, 0))

    #     # Centraliza o texto na screen
    #     self.retTexto.center = (screen_width// 2, screen_height // 2)
    #     screen.blit(self.textoformatado, self.retTexto)

    #     # Atualiza a tela
    #     pygame.display.flip()

# Instancia o cronômetro
# crono = Crono()

    def run(self):
        '''Roda o jogo.'''
        if self.state == "Menu":
            self.menu.ruunning()
            self.state = "Playing"
        
        if self.state == "Playing":
            self.playBackgroundMusic()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                
                self.draw(screen)
                # self.renderizar()
                self.update()
                self.clock.tick(15)
        pygame.quit()
        exit()
