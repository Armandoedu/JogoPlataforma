import pygame

class Sound:
    def __init__(self, music):
        pygame.mixer.init()
        self.music = music
        pygame.mixer.music.load(self.music)

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