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

            # новые фигуры
            if event.key == pygame.K_4:
                mode = "square"          # NEW
            if event.key == pygame.K_5:
                mode = "right_triangle"  # NEW
            if event.key == pygame.K_6:
                mode = "equilateral"     # NEW
            if event.key == pygame.K_7:
                mode = "rhombus"         # NEW

            # цвета
            if event.key == pygame.K_1:
                color = (255, 0, 0)
            if event.key == pygame.K_2:
                color = (0, 255, 0)
            if event.key == pygame.K_3:
                color = (0, 0, 255)

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

            # квадрат
            if mode == "square":   # NEW
                size = min(abs(end_pos[0]-start_pos[0]), abs(end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], size, size))

            # прямоугольный треугольник
            if mode == "right_triangle":   # NEW
                pygame.draw.polygon(screen, color, [
                    start_pos,
                    (end_pos[0], start_pos[1]),
                    end_pos
                ])

            # равносторонний треугольник
            if mode == "equilateral":   # NEW
                x, y = start_pos
                size = 60
                pygame.draw.polygon(screen, color, [
                    (x, y),
                    (x + size, y),
                    (x + size // 2, y - size)
                ])

            # ромб
            if mode == "rhombus":   # NEW
                x, y = start_pos
                size = 40
                pygame.draw.polygon(screen, color, [
                    (x, y - size),
                    (x + size, y),
                    (x, y + size),
                    (x - size, y)
                ])

    # рисование кистью
    if drawing:
        mouse = pygame.mouse.get_pos()

        if mode == "brush":
            pygame.draw.circle(screen, color, mouse, 5)

        if mode == "eraser":
            pygame.draw.circle(screen, (0, 0, 0), mouse, 50)

    pygame.display.flip()
    clock.tick(60)

pygame.quit() 