import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# размер клетки
BLOCK = 20

# начальная позиция змейки
snake = [(100, 100), (80, 100), (60, 100)]

# направление
dx = BLOCK
dy = 0

# еда
food = (200, 200)

score = 0

running = True
while running:
    screen.fill((0, 0, 0))

    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # управление
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dx, dy = 0, -BLOCK
            if event.key == pygame.K_DOWN:
                dx, dy = 0, BLOCK
            if event.key == pygame.K_LEFT:
                dx, dy = -BLOCK, 0
            if event.key == pygame.K_RIGHT:
                dx, dy = BLOCK, 0

    # новая голова
    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)

    # если съел еду
    if head == food:
        score += 1

        # новая еда (не на змее)
        while True:
            food = (
                random.randint(0, (WIDTH//BLOCK)-1) * BLOCK,
                random.randint(0, (HEIGHT//BLOCK)-1) * BLOCK
            )
            if food not in snake:
                break
    else:
        snake.pop()

    # проверка выхода за границы
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False

    # рисуем змейку
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, BLOCK, BLOCK))

    # рисуем еду
    pygame.draw.rect(screen, (255, 0, 0), (*food, BLOCK, BLOCK))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()