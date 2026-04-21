import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

# текущий цвет
color = (255, 255, 255)

# режим
mode = "brush"

drawing = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # смена инструмента
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                mode = "brush"
            if event.key == pygame.K_r:
                mode = "rect"
            if event.key == pygame.K_c:
                mode = "circle"
            if event.key == pygame.K_e:
                mode = "eraser"
            if event.key == pygame.K_1:
                color = (255, 0, 0)  # красный
            if event.key == pygame.K_2:
                color = (0, 255, 0)  # зеленый
            if event.key == pygame.K_3:
                color = (0, 0, 255)  # синий

        # нажатие мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # отпускание мыши
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if mode == "rect":
                pygame.draw.rect(screen, color, (*start_pos, 50, 50))

            if mode == "circle":
                pygame.draw.circle(screen, color, start_pos, 25)

    # рисование кистью
    if drawing:
        mouse = pygame.mouse.get_pos()

        if mode == "brush":
            pygame.draw.circle(screen, color, mouse, 5)

        if mode == "eraser":
            pygame.draw.circle(screen, (0, 0, 0), mouse, 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()