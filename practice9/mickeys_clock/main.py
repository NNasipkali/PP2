import pygame
from clock import draw_clock

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey Clock")

font = pygame.font.SysFont("Arial", 40)

hand_img = pygame.image.load("images/mickey_hand.png").convert_alpha()
hand_img.set_colorkey((255, 255, 255))  # убираем фон

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((255, 255, 255))

    title = font.render("MICKEY CLOCK", True, (0, 0, 0))
    screen.blit(title, (260, 30))

    draw_clock(screen, hand_img)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(1)

pygame.quit()