import pygame
import os

# abs_path = os.path.dirname(__file__)
# background_music = os.path.join(abs_path, 'Music', 'background_music.mp3')
# barulho_colisao = os.path.join(abs_path, 'Music', 'smw_1-up.wav')

class Sound:
    def __init__(self, musica_fundo):
        pygame.mixer.init()
        self.musica_fundo = musica_fundo
        # self.musica_colisao = musica_colisao
        self.musica_fundo = pygame.mixer.load('JogoPlataforma/Jogo_Rua_Dispensario/Music/BoxCat Games - Trace Route.mp3')
        # self.musica_colisao = pygame.mixer.Sound('JogoPlataforma/Jogo_Rua_Dispensario/Music/smw_1-up.wav')
        # pygame.mixer.musica_fundo.load(self.music)
        # pygame.mixer.musica_colisao.load(self.Sound)
        # self.barulho_colisao = os.path.join(abs_path, 'Music', 'smw_1-up.wav')
        # self.barulho_colisao = pygame.mixer.Sound(barulho_colisao)


    def playMusic(self, loops=-1):
        pygame.mixer.musica_fundo.play(loops)

    def stopMusic(self):
        pygame.mixer.musica_fundo.stop()

    def pauseMusic(self):
        pygame.mixer.musica_fundo.pause()

    def unpauseMusic(self):
        pygame.mixer.musica_fundo.unpause()

    def setVolume(self, new_volume):
        pygame.mixer.musica_fundo.set_volume(new_volume)

    # def playSaund(self):
        # self.musica_colisao.play()
        

    