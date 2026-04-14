import pygame
import sys
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# цвета (как Spotify)
BG = (18, 18, 18)
CARD = (30, 30, 30)
TEXT = (255, 255, 255)
SUBTEXT = (180, 180, 180)
GREEN = (30, 215, 96)

font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 22)
big_font = pygame.font.SysFont("Arial", 50)

player = MusicPlayer(["music/track1.mp3", "music/track2.mp3"])
player.play()

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BG)

    # 🎵 Заголовок
    title = big_font.render("NOW PLAYING", True, TEXT)
    screen.blit(title, (300, 40))

    # 🎧 Карточка трека
    pygame.draw.rect(screen, CARD, (150, 130, 600, 200), border_radius=20)

    track_name = player.get_current_track().split("/")[-1]
    track_text = font.render(track_name, True, TEXT)
    screen.blit(track_text, (180, 180))

    subtitle = small_font.render("Your Playlist", True, SUBTEXT)
    screen.blit(subtitle, (180, 220))

    # ▶️ Прогресс бар (визуальный)
    pygame.draw.rect(screen, (80, 80, 80), (180, 260, 540, 6), border_radius=3)
    pygame.draw.rect(screen, GREEN, (180, 260, 200, 6), border_radius=3)

    # 🎮 Кнопки (как Spotify)
    controls = ["B", "P", "S", "N"]
    labels = ["Back", "Play", "Stop", "Next"]

    for i, (c, label) in enumerate(zip(controls, labels)):
        x = 300 + i * 80
        pygame.draw.circle(screen, CARD, (x, 350), 30)
        text = small_font.render(c, True, TEXT)
        screen.blit(text, (x - 8, 340))

        label_text = small_font.render(label, True, SUBTEXT)
        screen.blit(label_text, (x - 20, 390))

    # Подсказка
    hint = small_font.render("Press keys on keyboard (ENG)", True, SUBTEXT)
    screen.blit(hint, (300, 450))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next()
            elif event.key == pygame.K_b:
                player.prev()
            elif event.key == pygame.K_q:
                running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()