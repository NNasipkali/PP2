# main.py — Entry point; manages all screens and the main game loop

import pygame
import sys
import time

import db
from game import (
    GameState, Direction, draw_game,
    load_settings, save_settings,
    FoodType, PowerUpType,
)
from config import *

#  Pygame initialisation 

pygame.init()
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock  = pygame.time.Clock()

# Fonts — using system mono for a retro terminal vibe
FONT_TITLE  = pygame.font.SysFont("Courier New", 52, bold=True)
FONT_BIG    = pygame.font.SysFont("Courier New", 32, bold=True)
FONT_MED    = pygame.font.SysFont("Courier New", 22, bold=True)
FONT_SM     = pygame.font.SysFont("Courier New", 16)

#  Color palette 

BG_MENU   = (10, 12, 20)
ACCENT    = (0, 230, 120)
DIM       = (80, 80, 100)
HIGHLIGHT = (255, 255, 255)

#  Utility helpers 

def draw_text_centered(surface, text, font, color, y):
    surf = font.render(text, True, color)
    surface.blit(surf, (WINDOW_WIDTH // 2 - surf.get_width() // 2, y))
    return surf.get_height()

def draw_button(surface, text, font, rect: pygame.Rect, hovered: bool):
    color  = ACCENT   if hovered else DIM
    border = HIGHLIGHT if hovered else (60, 60, 80)
    pygame.draw.rect(surface, (20, 25, 35), rect, border_radius=6)
    pygame.draw.rect(surface, border, rect, 2, border_radius=6)
    surf = font.render(text, True, color)
    surface.blit(surf, (rect.centerx - surf.get_width() // 2,
                        rect.centery - surf.get_height() // 2))

def make_button(label: str, cx: int, cy: int, w=260, h=48) -> pygame.Rect:
    return pygame.Rect(cx - w // 2, cy - h // 2, w, h)

def draw_scanlines(surface):
    """Subtle CRT scanline effect over the whole screen."""
    for y in range(0, WINDOW_HEIGHT, 4):
        pygame.draw.line(surface, (0, 0, 0, 30), (0, y), (WINDOW_WIDTH, y))

#  DB availability flag 

DB_AVAILABLE = db.init_db()

#  Screen: Main Menu 

def screen_main_menu() -> tuple[str, bool]:
    """
    Returns (username, quit_flag).
    username is '' if quit was chosen.
    """
    username   = ""
    typing     = True
    input_active = True

    BTN_PLAY   = make_button("PLAY",        WINDOW_WIDTH // 2, 370)
    BTN_LEADER = make_button("LEADERBOARD", WINDOW_WIDTH // 2, 430)
    BTN_SET    = make_button("SETTINGS",    WINDOW_WIDTH // 2, 490)
    BTN_QUIT   = make_button("QUIT",        WINDOW_WIDTH // 2, 550)
    buttons    = [BTN_PLAY, BTN_LEADER, BTN_SET, BTN_QUIT]

    tick = 0
    while True:
        tick += 1
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "", True

            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    elif event.key == pygame.K_RETURN:
                        if username.strip():
                            input_active = False
                    elif len(username) < 20 and event.unicode.isprintable():
                        username += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BTN_PLAY.collidepoint(mouse):
                    if username.strip():
                        return username.strip(), False
                elif BTN_LEADER.collidepoint(mouse):
                    screen_leaderboard()
                elif BTN_SET.collidepoint(mouse):
                    screen_settings()
                elif BTN_QUIT.collidepoint(mouse):
                    return "", True

        # Draw
        screen.fill(BG_MENU)

        # Animated grid background
        for gx in range(0, WINDOW_WIDTH, CELL_SIZE):
            pygame.draw.line(screen, (18, 22, 32), (gx, 0), (gx, WINDOW_HEIGHT))
        for gy in range(0, WINDOW_HEIGHT, CELL_SIZE):
            pygame.draw.line(screen, (18, 22, 32), (0, gy), (WINDOW_WIDTH, gy))

        # Title
        draw_text_centered(screen, "SNAKE", FONT_TITLE, ACCENT, 60)
        draw_text_centered(screen, "DATABASE EDITION", FONT_SM, DIM, 118)

        # Username input
        input_y = 200
        draw_text_centered(screen, "Enter your username:", FONT_MED, LIGHT_GRAY, input_y)
        input_rect = pygame.Rect(WINDOW_WIDTH // 2 - 150, input_y + 36, 300, 40)
        border_col = ACCENT if input_active else DIM
        pygame.draw.rect(screen, (15, 18, 28), input_rect, border_radius=4)
        pygame.draw.rect(screen, border_col, input_rect, 2, border_radius=4)

        display_name = username + ("|" if input_active and (tick // 30) % 2 == 0 else "")
        name_surf = FONT_MED.render(display_name, True, HIGHLIGHT)
        screen.blit(name_surf, (input_rect.x + 8, input_rect.y + 8))

        if not input_active:
            ready_surf = FONT_SM.render(f"Hello, {username}! Press PLAY.", True, ACCENT)
            screen.blit(ready_surf, (WINDOW_WIDTH // 2 - ready_surf.get_width() // 2, input_y + 82))

        # Buttons
        for btn in buttons:
            hovered = btn.collidepoint(mouse)
            labels  = ["PLAY", "LEADERBOARD", "SETTINGS", "QUIT"]
            draw_button(screen, labels[buttons.index(btn)], FONT_MED, btn, hovered)

        # DB status
        db_col  = ACCENT if DB_AVAILABLE else (200, 80, 80)
        db_text = "DB: connected" if DB_AVAILABLE else "DB: offline (scores not saved)"
        db_surf = FONT_SM.render(db_text, True, db_col)
        screen.blit(db_surf, (8, WINDOW_HEIGHT - 22))

        pygame.display.flip()
        clock.tick(60)

#  Screen: Leaderboard 

def screen_leaderboard():
    rows = db.get_leaderboard(10) if DB_AVAILABLE else []
    BTN_BACK = make_button("BACK", WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BTN_BACK.collidepoint(mouse):
                    return

        screen.fill(BG_MENU)

        draw_text_centered(screen, "LEADERBOARD", FONT_BIG, ACCENT, 20)

        if not DB_AVAILABLE:
            draw_text_centered(screen, "Database unavailable", FONT_MED, RED, 80)
        elif not rows:
            draw_text_centered(screen, "No scores yet!", FONT_MED, DIM, 80)
        else:
            # Header
            header_y = 75
            cols = [50, 130, 380, 510, 640]
            headers = ["#", "USERNAME", "SCORE", "LEVEL", "DATE"]
            for col_x, hdr in zip(cols, headers):
                surf = FONT_SM.render(hdr, True, DIM)
                screen.blit(surf, (col_x, header_y))
            pygame.draw.line(screen, DIM, (40, header_y + 22), (WINDOW_WIDTH - 40, header_y + 22))

            for i, row in enumerate(rows):
                y = header_y + 30 + i * 44
                bg_col = (18, 24, 36) if i % 2 == 0 else (14, 18, 28)
                pygame.draw.rect(screen, bg_col, (40, y - 4, WINDOW_WIDTH - 80, 38))

                rank_col = (255, 215, 0) if i == 0 else (192, 192, 192) if i == 1 else (205, 127, 50) if i == 2 else LIGHT_GRAY
                rank_surf  = FONT_MED.render(str(i + 1), True, rank_col)
                name_surf  = FONT_MED.render(str(row["username"])[:16], True, HIGHLIGHT)
                score_surf = FONT_MED.render(str(row["score"]), True, ACCENT)
                level_surf = FONT_MED.render(str(row["level_reached"]), True, YELLOW)
                date_str   = row["played_at"].strftime("%Y-%m-%d") if row.get("played_at") else "—"
                date_surf  = FONT_SM.render(date_str, True, DIM)

                screen.blit(rank_surf,  (cols[0], y))
                screen.blit(name_surf,  (cols[1], y))
                screen.blit(score_surf, (cols[2], y))
                screen.blit(level_surf, (cols[3], y))
                screen.blit(date_surf,  (cols[4], y + 4))

        draw_button(screen, "BACK", FONT_MED, BTN_BACK, BTN_BACK.collidepoint(mouse))
        pygame.display.flip()
        clock.tick(60)

#  Screen: Settings 

COLOR_PRESETS = [
    ("Green",  (0, 200, 80)),
    ("Cyan",   (0, 210, 210)),
    ("Yellow", (240, 200, 30)),
    ("Pink",   (230, 80, 160)),
    ("Orange", (240, 130, 30)),
    ("Purple", (160, 60, 220)),
    ("White",  (230, 230, 230)),
    ("Red",    (220, 60, 60)),
]

def screen_settings():
    settings = load_settings()
    BTN_SAVE = make_button("SAVE & BACK", WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)
    BTN_GRID = make_button("Grid: ON" if settings["grid_overlay"] else "Grid: OFF",
                           WINDOW_WIDTH // 2, 240, w=200)
    BTN_SOUND = make_button("Sound: ON" if settings["sound"] else "Sound: OFF",
                            WINDOW_WIDTH // 2, 300, w=200)

    while True:
        mouse = pygame.mouse.get_pos()
        # Rebuild toggle labels
        BTN_GRID  = make_button("Grid: ON"  if settings["grid_overlay"] else "Grid: OFF",  WINDOW_WIDTH // 2, 240, w=200)
        BTN_SOUND = make_button("Sound: ON" if settings["sound"]        else "Sound: OFF", WINDOW_WIDTH // 2, 300, w=200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                save_settings(settings)
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BTN_GRID.collidepoint(mouse):
                    settings["grid_overlay"] = not settings["grid_overlay"]
                elif BTN_SOUND.collidepoint(mouse):
                    settings["sound"] = not settings["sound"]
                elif BTN_SAVE.collidepoint(mouse):
                    save_settings(settings)
                    return
                # Color swatches
                for idx, (name, col) in enumerate(COLOR_PRESETS):
                    sw = _swatch_rect(idx)
                    if sw.collidepoint(mouse):
                        settings["snake_color"] = list(col)

        screen.fill(BG_MENU)
        draw_text_centered(screen, "SETTINGS", FONT_BIG, ACCENT, 20)

        draw_text_centered(screen, "Snake Color:", FONT_MED, LIGHT_GRAY, 370)
        # Color swatches
        for idx, (name, col) in enumerate(COLOR_PRESETS):
            sw = _swatch_rect(idx)
            pygame.draw.rect(screen, col, sw, border_radius=4)
            if list(col) == settings["snake_color"]:
                pygame.draw.rect(screen, WHITE, sw, 3, border_radius=4)

        draw_button(screen, "Grid: ON"  if settings["grid_overlay"] else "Grid: OFF",  FONT_MED, BTN_GRID,  BTN_GRID.collidepoint(mouse))
        draw_button(screen, "Sound: ON" if settings["sound"]        else "Sound: OFF", FONT_MED, BTN_SOUND, BTN_SOUND.collidepoint(mouse))
        draw_button(screen, "SAVE & BACK", FONT_MED, BTN_SAVE, BTN_SAVE.collidepoint(mouse))

        pygame.display.flip()
        clock.tick(60)

def _swatch_rect(idx: int) -> pygame.Rect:
    cols_per_row = 8
    sw_size = 40
    gap = 10
    total_w = cols_per_row * sw_size + (cols_per_row - 1) * gap
    start_x = (WINDOW_WIDTH - total_w) // 2
    x = start_x + idx * (sw_size + gap)
    y = 410
    return pygame.Rect(x, y, sw_size, sw_size)

#  Screen: Game Over 

def screen_game_over(score: int, level: int, personal_best: int) -> str:
    """Returns 'retry' or 'menu'."""
    BTN_RETRY = make_button("RETRY",     WINDOW_WIDTH // 2, 430)
    BTN_MENU  = make_button("MAIN MENU", WINDOW_WIDTH // 2, 490)
    BTN_LEAD  = make_button("LEADERBOARD", WINDOW_WIDTH // 2, 550)

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BTN_RETRY.collidepoint(mouse):
                    return "retry"
                elif BTN_MENU.collidepoint(mouse):
                    return "menu"
                elif BTN_LEAD.collidepoint(mouse):
                    screen_leaderboard()

        screen.fill(BG_MENU)

        draw_text_centered(screen, "GAME OVER", FONT_TITLE, RED, 60)

        draw_text_centered(screen, f"Score:        {score}",        FONT_MED, HIGHLIGHT,   200)
        draw_text_centered(screen, f"Level:        {level}",        FONT_MED, YELLOW,       240)
        draw_text_centered(screen, f"Personal Best: {personal_best}", FONT_MED, ACCENT,    280)

        if score >= personal_best and score > 0:
            draw_text_centered(screen, "NEW PERSONAL BEST!", FONT_MED, YELLOW, 330)

        draw_button(screen, "RETRY",       FONT_MED, BTN_RETRY, BTN_RETRY.collidepoint(mouse))
        draw_button(screen, "MAIN MENU",   FONT_MED, BTN_MENU,  BTN_MENU.collidepoint(mouse))
        draw_button(screen, "LEADERBOARD", FONT_MED, BTN_LEAD,  BTN_LEAD.collidepoint(mouse))

        pygame.display.flip()
        clock.tick(60)

#  Main game loop 

def run_game(username: str):
    settings      = load_settings()
    personal_best = db.get_personal_best(username) if DB_AVAILABLE else 0
    state         = GameState(username, personal_best, settings)

    # Timing: we run pygame at 60 fps but only advance snake every (60/fps) frames
    move_accumulator = 0.0

    while True:
        dt = clock.tick(60) / 1000.0  # seconds since last frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if DB_AVAILABLE:
                    db.save_game_session(username, state.score, state.level)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key_map = {
                    pygame.K_UP:    Direction.UP,
                    pygame.K_DOWN:  Direction.DOWN,
                    pygame.K_LEFT:  Direction.LEFT,
                    pygame.K_RIGHT: Direction.RIGHT,
                    pygame.K_w:     Direction.UP,
                    pygame.K_s:     Direction.DOWN,
                    pygame.K_a:     Direction.LEFT,
                    pygame.K_d:     Direction.RIGHT,
                }
                if event.key in key_map:
                    state.set_direction(key_map[event.key])

        # Advance snake
        fps = state.current_fps()
        move_accumulator += dt * fps
        while move_accumulator >= 1.0:
            move_accumulator -= 1.0
            alive = state.update()
            if not alive:
                break

        # Draw
        draw_game(screen, state, FONT_SM, FONT_MED)
        pygame.display.flip()

        if state.game_over:
            # Save to DB
            if DB_AVAILABLE:
                db.save_game_session(username, state.score, state.level)
            # Update personal best for display
            new_best = max(personal_best, state.score)
            result = screen_game_over(state.score, state.level, new_best)
            if result == "retry":
                run_game(username)   # recursive retry
                return
            else:
                return  # back to main menu

#  Entry point 

def main():
    while True:
        username, quit_flag = screen_main_menu()
        if quit_flag:
            break
        if username:
            run_game(username)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()