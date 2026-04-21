import pygame
import random

# запуск pygame
pygame.init()

coin_img = pygame.image.load("coin.png")
coin_img = pygame.transform.scale(coin_img, (30, 30))

racer_img = pygame.image.load("space_racer.png")
racer_img = pygame.transform.scale(racer_img, (50, 70))

# размеры окна
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# цвета
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# игрок (машина)
player = pygame.Rect(180, 500, 50, 70)

# монеты
coins = []

# счет
score = 0
font = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((0, 0, 0))

    # выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # появление монет
    if random.randint(1, 40) == 1:
        x = random.randint(0, WIDTH - 20)
        coins.append(pygame.Rect(x, 0, 30, 30))

    # движение монет
    for coin in coins[:]:
        coin.y += 5

        # если поймал монету
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1
    
    #player
    screen.blit(racer_img, (player.x, player.y))

    # рисуем монеты
    for coin in coins:
        screen.blit(coin_img, (coin.x, coin.y))

    # счет (справа сверху)
    text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(text, (WIDTH - 120, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()