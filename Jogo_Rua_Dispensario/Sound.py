import pygame
import os

class Sound:
    def __init__(self, musica_fundo, musica_colisao):
        pygame.mixer.init()
        self.musica_fundo = musica_fundo
        pygame.mixer.music.load(self.musica_fundo)
        self.musica_colisao = pygame.mixer.Sound(musica_colisao)


    def playMusic(self, loops=-1):
        pygame.mixer.music.play(loops)

    def stopMusic(self):
        pygame.mixer.music.stop()

    def pauseMusic(self):
        pygame.mixer.music.pause()

    def unpauseMusic(self):
        pygame.mixer.music.unpause()

    def setVolume(self, new_volume):
        pygame.mixer.music.set_volume(new_volume)

    def playSaund(self):
        self.musica_colisao.play()
        

    