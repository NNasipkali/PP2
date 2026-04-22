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

# игрок
player = pygame.Rect(180, 500, 50, 70)

# ВРАГ 
enemy = pygame.Rect(random.randint(0, WIDTH-50), 0, 50, 70)  # NEW
enemy_speed = 5  # NEW

# монеты теперь (rect, value)
coins = []
coin_values = [1, 2, 3]  # NEW

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

    # появление монет с value
    if random.randint(1, 40) == 1:
        x = random.randint(0, WIDTH - 30)  # CHANGED (было 20)
        rect = pygame.Rect(x, 0, 30, 30)   # NEW
        value = random.choice(coin_values) # NEW
        coins.append((rect, value))        # CHANGED

    # движение монет
    for coin, value in coins[:]:  # CHANGED
        coin.y += 5

        # если поймал монету
        if player.colliderect(coin):
            coins.remove((coin, value))  # CHANGED
            score += value               # CHANGED (было +1)

    # движение врага
    enemy.y += enemy_speed  # NEW

    if enemy.y > HEIGHT:
        enemy.y = 0
        enemy.x = random.randint(0, WIDTH - 50)

    # ⚡ ускорение врага
    if score >= 10:
        enemy_speed = 8  # NEW

    # столкновение
    if player.colliderect(enemy):  # NEW
        print("GAME OVER")
        running = False

    # player
    screen.blit(racer_img, (player.x, player.y))

    # рисуем врага
    pygame.draw.rect(screen, (255, 0, 0), enemy)  # NEW

    # рисуем монеты
    for coin, value in coins:  # CHANGED
        screen.blit(coin_img, (coin.x, coin.y))

    # счет
    text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(text, (WIDTH - 120, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()