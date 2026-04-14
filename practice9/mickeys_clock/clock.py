import pygame
import math
import datetime

def draw_clock(screen, hand_img):
    center = (400, 300)

    now = datetime.datetime.now()
    sec = now.second
    minute = now.minute

    sec_angle = sec * 6
    min_angle = minute * 6

    # --- считаем координаты (как у тебя уже работает)
    sec_x = center[0] + 200 * math.sin(math.radians(sec_angle))
    sec_y = center[1] - 200 * math.cos(math.radians(sec_angle))

    min_x = center[0] + 150 * math.sin(math.radians(min_angle))
    min_y = center[1] - 150 * math.cos(math.radians(min_angle))

    # --- рисуем линии (основа)
    pygame.draw.line(screen, (200, 200, 200), center, (sec_x, sec_y), 2)
    pygame.draw.line(screen, (100, 100, 255), center, (min_x, min_y), 5)

    # --- вращаем руку (теперь просто как декор)
    hand = pygame.transform.scale(hand_img, (120, 120))

    sec_hand = pygame.transform.rotate(hand, -sec_angle)
    min_hand = pygame.transform.rotate(hand, -min_angle)

    sec_rect = sec_hand.get_rect(center=(sec_x, sec_y))
    min_rect = min_hand.get_rect(center=(min_x, min_y))

    screen.blit(sec_hand, sec_rect)
    screen.blit(min_hand, min_rect)

    # центр
    pygame.draw.circle(screen, (0, 0, 0), center, 6)