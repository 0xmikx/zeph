import pygame
import random

# Inisialisasi
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Coin")

# Warna
WHITE = (255, 255, 255)
BLUE = (122, 162, 255)
YELLOW = (255, 209, 102)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont("Arial", 24)

# Player
player = pygame.Rect(WIDTH//2 - 25, HEIGHT - 40, 50, 20)
player_speed = 6

# Coin
coin_radius = 10
coin_x = random.randint(coin_radius, WIDTH - coin_radius)
coin_y = 0
coin_speed = 4

# Skor dan nyawa
score = 0
lives = 3

# Clock
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)

    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Gerak koin
    coin_y += coin_speed

    # Tangkap koin
    if player.collidepoint(coin_x, coin_y):
        score += 1
        coin_speed += 0.2
        coin_x = random.randint(coin_radius, WIDTH - coin_radius)
        coin_y = 0

    # Miss
    if coin_y > HEIGHT:
        lives -= 1
        coin_x = random.randint(coin_radius, WIDTH - coin_radius)
        coin_y = 0
        if lives <= 0:
            running = False

    # Gambar player
    pygame.draw.rect(screen, BLUE, player)

    # Gambar koin
    pygame.draw.circle(screen, YELLOW, (coin_x, int(coin_y)), coin_radius)

    # Gambar skor dan nyawa
    score_text = font.render(f"Skor: {score} | Nyawa: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
