import pygame 
import os

sprites_path = os.path.dirname(__file__)
sprites = os.path.join(sprites_path, 'Sprites')
player_sprites_run = sprites + '/spritesBoy/' + 'Boyrun.png'
player_sprites_idle = sprites + '/spritesBoy/' + 'BoyIdle.png'
player_sprites_jump = sprites + '/spritesBoy/' + 'Boyjump.png'

sprite_sheet_run = pygame.image.load(player_sprites_run)
sprite_sheet_idle = pygame.image.load(player_sprites_idle)
sprite_sheet_jump = pygame.image.load(player_sprites_jump)

PLAYER_DIMENSION = (32*3, 32*3)
sprite_width, sprite_heigth = 32, 32

PLAYER_RUN = []
PLAYER_IDLE = []
PLAYER_JUMP = []

for i in range(4):
    x = i * sprite_width
    y = 0
    IMG_RUN = sprite_sheet_run.subsurface((x, y, sprite_width, sprite_heigth ))
    IMG_IDLE = sprite_sheet_idle.subsurface((x, y, sprite_width, sprite_heigth ))
    IMG_JUMP = sprite_sheet_jump.subsurface((x, y, sprite_width, sprite_heigth ))
    PLAYER_RUN.append(IMG_RUN)
    PLAYER_IDLE.append(IMG_IDLE)
    PLAYER_JUMP.append(IMG_JUMP)

class Player(pygame.sprite.Sprite):
    def __init__(self, screen): # Construtor
        pygame.sprite.Sprite.__init__(self)
        self.sprites:list = PLAYER_RUN
        self.sprites_idle: list = PLAYER_IDLE
        self.sprites_jump: list = PLAYER_JUMP
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (PLAYER_DIMENSION))
        self.rect = self.image.get_rect() # Coordenadas da imagem 
        self.rect.topleft = 100, 100 # Canto superior esquerdo
        self.animar = False
        self.isJumping = False
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
        if self.animar == True: #correndo
            self.atual = self.atual + 1
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (120, 120))
        else: ## parado
            self.atual = self.atual + 1
            if self.atual >= len(self.sprites_idle):
                self.atual = 0
                # self.animar = False
            self.image = self.sprites_idle[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (PLAYER_DIMENSION))

