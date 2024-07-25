import pygame

class Som:
    def __init__(self, som1):
        pygame.mixer.init()
        self.som1 = som1
        pygame.mixer.music.load(self.som1)

    def play(self, loops=-1):
        pygame.mixer.music.play(loops)
    
    def parar(self):
        pygame.mixer.music.stop()

    def pausar(self):
        pygame.mixer.music.pausar()

    def despausar(self):
        pygame.mixer.music.unpause()

    def volume(self):
        pygame.mixer.music.set_volume(3)

    