import pygame
import sys

# Define constantes
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50
PLAYER_SPEED = 5
OBSTACLE_SPEED = 7
JUMP_HEIGHT = 10
GRAVITY = 0.5

# Classe para o jogador
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
        self.velocity_y = 0
        self.jumping = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jumping = True
            self.velocity_y = -JUMP_HEIGHT

    def update(self):
        if self.jumping:
            self.rect.y += self.velocity_y
            self.velocity_y += GRAVITY
            if self.rect.y >= HEIGHT - PLAYER_SIZE:
                self.rect.y = HEIGHT - PLAYER_SIZE
                self.jumping = False

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)

# Classe para o obstáculo
class Obstacle:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH, HEIGHT - OBSTACLE_SIZE, OBSTACLE_SIZE, OBSTACLE_SIZE)

    def update(self):
        self.rect.x -= OBSTACLE_SPEED
        if self.rect.x < 0:
            self.rect.x = WIDTH

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

# Classe para o jogo
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Jogo com Obstáculo')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 55)
        self.player = Player()
        self.obstacle = Obstacle()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(30)
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.handle_input()
        self.player.update()
        self.obstacle.update()
        if self.player.rect.colliderect(self.obstacle.rect):
            self.show_game_over()

    def draw(self):
        self.screen.fill(WHITE)
        self.player.draw(self.screen)
        self.obstacle.draw(self.screen)
        pygame.display.flip()

    def show_game_over(self):
        game_over_text = self.font.render('Game Over', True, RED)
        self.screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        self.running = False

if __name__ == "__main__":
    game = Game()
    game.run()
