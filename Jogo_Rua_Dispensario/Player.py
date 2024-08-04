import pygame
import os

# Pegar o caminho das sprites
sprites_path = os.path.dirname(__file__)
sprites = os.path.join(sprites_path, 'Sprites')
player_sprites_run = sprites + '/spritesBoy/' + 'Boyrun.png'
player_sprites_idle = sprites + '/spritesBoy/' + 'BoyIdle.png'
player_sprites_jump = sprites + '/spritesBoy/' + 'Boyjump.png'

# Carregar sprites
sprite_sheet_run = pygame.image.load(player_sprites_run)
sprite_sheet_idle = pygame.image.load(player_sprites_idle)
sprite_sheet_jump = pygame.image.load(player_sprites_jump)
PLAYER_RUN = []
PLAYER_IDLE = []
PLAYER_JUMP = []

# Dimensões do player
PLAYER_DIMENSION = (32*3, 32*3)
sprite_width, sprite_heigth = 32, 32

# Adicionar sprites em uma lista
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
    def __init__(self, screen, screen_width, screen_height): # Construtor
        pygame.sprite.Sprite.__init__(self)
        self.sprites:list = PLAYER_RUN
        self.sprites_idle: list = PLAYER_IDLE
        self.sprites_jump: list = PLAYER_JUMP
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (PLAYER_DIMENSION))
        self.rect = self.image.get_rect() # Coordenadas da imagem 
        self.rect.topleft = 0, 455 # Canto superior esquerdo
        self.animate = False
        self.screen = screen
        self.speed = 5
        self.isJumping = False

        ''' adicições (ainda não estão sendo usadas)
        self.player_size = 32
        self.player_x = screen_width // 2
        self.player_y = screen_height - self.player_size
        self.jump_height = 10
        self.gravity = 0.5
        self.player_velocity_y = 0'''

    def move(self):
        self.animate = True

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def handleKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.move()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.move()
        if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
            self.rect.y -= self.speed
            self.move()
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
            self.move()

    def update(self):
        if self.animate == True: # Correndo
            self.current_sprite = self.current_sprite + 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.animate = False
            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, (120, 120))
        else: # Parado
            self.current_sprite = self.current_sprite + 1
            if self.current_sprite >= len(self.sprites_idle):
                self.current_sprite = 0
                # self.animar = False
            self.image = self.sprites_idle[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, (PLAYER_DIMENSION))