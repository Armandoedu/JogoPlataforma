import pygame

class Sound:
    def __init__(self, background_music, collision_music):
        pygame.mixer.init()
        self.background_music = background_music
        pygame.mixer.music.load(self.background_music)
        self.collision_music = pygame.mixer.Sound(collision_music)

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

    def playSound(self):
        self.collision_music.play()