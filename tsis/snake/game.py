# game.py — Core Snake gameplay logic

import pygame
import random
import json
import os
from enum import Enum, auto
from config import *

#  Enums

class Direction(Enum):
    UP    = (0, -1)
    DOWN  = (0,  1)
    LEFT  = (-1, 0)
    RIGHT = (1,  0)

class FoodType(Enum):
    NORMAL = auto()
    BONUS  = auto()
    POISON = auto()

class PowerUpType(Enum):
    SPEED_BOOST = auto()
    SLOW_MOTION = auto()
    SHIELD      = auto()

#  Settings 

SETTINGS_PATH = os.path.join(os.path.dirname(__file__), "settings.json")

def load_settings() -> dict:
    defaults = {"snake_color": list(DEFAULT_SNAKE_COLOR), "grid_overlay": True, "sound": True}
    try:
        with open(SETTINGS_PATH, "r") as f:
            data = json.load(f)
        for k, v in defaults.items():
            data.setdefault(k, v)
        return data
    except Exception:
        return defaults

def save_settings(settings: dict):
    try:
        with open(SETTINGS_PATH, "w") as f:
            json.dump(settings, f, indent=4)
    except Exception as e:
        print(f"[Settings] Save error: {e}")

#  Food

class Food:
    def __init__(self, pos: tuple, food_type: FoodType, spawn_time: int):
        self.pos        = pos
        self.food_type  = food_type
        self.spawn_time = spawn_time
        self.lifetime   = {
            FoodType.NORMAL: None,           # never disappears
            FoodType.BONUS:  BONUS_FOOD_LIFETIME,
            FoodType.POISON: POISON_FOOD_LIFETIME,
        }[food_type]

    def is_expired(self, now: int) -> bool:
        if self.lifetime is None:
            return False
        return (now - self.spawn_time) >= self.lifetime

    def color(self) -> tuple:
        return {
            FoodType.NORMAL: FOOD_NORMAL_COLOR,
            FoodType.BONUS:  FOOD_BONUS_COLOR,
            FoodType.POISON: FOOD_POISON_COLOR,
        }[self.food_type]

    def points(self) -> int:
        return {
            FoodType.NORMAL: FOOD_NORMAL_POINTS,
            FoodType.BONUS:  FOOD_BONUS_POINTS,
            FoodType.POISON: 0,
        }[self.food_type]

#  Power-up 

class PowerUp:
    def __init__(self, pos: tuple, ptype: PowerUpType, spawn_time: int):
        self.pos        = pos
        self.ptype      = ptype
        self.spawn_time = spawn_time

    def is_expired(self, now: int) -> bool:
        return (now - self.spawn_time) >= POWERUP_FIELD_LIFETIME

    def color(self) -> tuple:
        return {
            PowerUpType.SPEED_BOOST: POWERUP_SPEED_COLOR,
            PowerUpType.SLOW_MOTION: POWERUP_SLOW_COLOR,
            PowerUpType.SHIELD:      POWERUP_SHIELD_COLOR,
        }[self.ptype]

    def symbol(self) -> str:
        return {
            PowerUpType.SPEED_BOOST: "",
            PowerUpType.SLOW_MOTION: "",
            PowerUpType.SHIELD:      "",
        }[self.ptype]

#  Game state 

class GameState:
    """All mutable runtime state for one play session."""

    def __init__(self, username: str, personal_best: int, settings: dict):
        self.username      = username
        self.personal_best = personal_best
        self.settings      = settings

        # Snake
        mid_x = GRID_COLS // 2
        mid_y = GRID_ROWS // 2
        self.snake: list[tuple] = [
            (mid_x, mid_y),
            (mid_x - 1, mid_y),
            (mid_x - 2, mid_y),
        ]
        self.direction       = Direction.RIGHT
        self.next_direction  = Direction.RIGHT

        # Score / level
        self.score          = 0
        self.level          = 1
        self.food_eaten     = 0   # counter toward next level

        # Obstacles (added from level 3)
        self.obstacles: set[tuple] = set()

        # Food list (multiple foods can coexist)
        self.foods: list[Food] = []

        # Power-up (at most one on field)
        self.active_powerup: PowerUp | None = None
        self._next_powerup_time = pygame.time.get_ticks() + random.randint(5000, 12000)

        self._spawn_normal_food()

        # Active effect
        self.effect_type:  PowerUpType | None = None
        self.effect_until: int = 0
        self.shield_ready: bool = False

        # Speed
        self.base_fps = BASE_SPEED

        # Game over flag
        self.game_over = False

    #  helpers 

    def _occupied(self) -> set[tuple]:
        """All cells that food/powerup must not appear on."""
        occupied = set(self.snake) | self.obstacles
        for f in self.foods:
            occupied.add(f.pos)
        if self.active_powerup:
            occupied.add(self.active_powerup.pos)
        return occupied

    def _random_free_cell(self) -> tuple | None:
        occupied = self._occupied()
        free = [
            (x, y)
            for x in range(GRID_COLS)
            for y in range(GRID_ROWS)
            if (x, y) not in occupied
        ]
        return random.choice(free) if free else None

    def _spawn_normal_food(self):
        pos = self._random_free_cell()
        if pos:
            self.foods.append(Food(pos, FoodType.NORMAL, pygame.time.get_ticks()))

    def _spawn_bonus_food(self):
        pos = self._random_free_cell()
        if pos:
            self.foods.append(Food(pos, FoodType.BONUS, pygame.time.get_ticks()))

    def _spawn_poison_food(self):
        pos = self._random_free_cell()
        if pos:
            self.foods.append(Food(pos, FoodType.POISON, pygame.time.get_ticks()))

    def _spawn_powerup(self):
        pos = self._random_free_cell()
        if pos:
            ptype = random.choice(list(PowerUpType))
            self.active_powerup = PowerUp(pos, ptype, pygame.time.get_ticks())

    def _add_obstacles(self):
        """Add obstacle blocks for the current level (avoid trapping snake)."""
        head = self.snake[0]
        count = 0
        attempts = 0
        while count < OBSTACLES_PER_LEVEL and attempts < 200:
            attempts += 1
            x = random.randint(0, GRID_COLS - 1)
            y = random.randint(0, GRID_ROWS - 1)
            pos = (x, y)
            # Do not place on snake, food, other obstacles, or adjacent to head
            if pos in self.obstacles:
                continue
            if pos in set(self.snake):
                continue
            if any(f.pos == pos for f in self.foods):
                continue
            # Keep a 3-cell buffer around the snake head
            if abs(x - head[0]) <= 2 and abs(y - head[1]) <= 2:
                continue
            self.obstacles.add(pos)
            count += 1

    #  per-frame update 

    def current_fps(self) -> float:
        fps = self.base_fps + (self.level - 1) * SPEED_INCREMENT
        fps = min(fps, MAX_SPEED)
        now = pygame.time.get_ticks()
        if self.effect_type == PowerUpType.SPEED_BOOST and now < self.effect_until:
            fps = min(fps * SPEED_BOOST_MULTIPLIER, MAX_SPEED)
        elif self.effect_type == PowerUpType.SLOW_MOTION and now < self.effect_until:
            fps = max(fps * SLOW_MOTION_MULTIPLIER, 2)
        return fps

    def set_direction(self, new_dir: Direction):
        opposites = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT,
        }
        if new_dir != opposites[self.direction]:
            self.next_direction = new_dir

    def update(self):
        """Advance the snake by one step. Returns True if still alive."""
        now = pygame.time.get_ticks()
        self.direction = self.next_direction

        # Expire effects
        if self.effect_type and now >= self.effect_until:
            self.effect_type = None

        # Expire field items
        self.foods = [f for f in self.foods if not f.is_expired(now)]
        if self.active_powerup and self.active_powerup.is_expired(now):
            self.active_powerup = None

        # Always keep at least one normal food
        if not any(f.food_type == FoodType.NORMAL for f in self.foods):
            self._spawn_normal_food()

        # Randomly spawn bonus / poison food
        if random.random() < 0.005 and not any(f.food_type == FoodType.BONUS for f in self.foods):
            self._spawn_bonus_food()
        if random.random() < 0.004 and not any(f.food_type == FoodType.POISON for f in self.foods):
            self._spawn_poison_food()

        # Spawn power-up on schedule
        if self.active_powerup is None and now >= self._next_powerup_time:
            self._spawn_powerup()
            self._next_powerup_time = now + random.randint(8000, 20000)

        # Move snake
        dx, dy = self.direction.value
        head_x, head_y = self.snake[0]
        new_head = (head_x + dx, head_y + dy)

        # Collision: border
        if not (0 <= new_head[0] < GRID_COLS and 0 <= new_head[1] < GRID_ROWS):
            if self.shield_ready:
                self.shield_ready = False
                new_head = self._bounce(new_head)
            else:
                self.game_over = True
                return False

        # Collision: obstacle
        if new_head in self.obstacles:
            if self.shield_ready:
                self.shield_ready = False
                new_head = self.snake[0]  # stay in place this tick
            else:
                self.game_over = True
                return False

        # Collision: self
        if new_head in self.snake:
            if self.shield_ready:
                self.shield_ready = False
                new_head = self.snake[0]
            else:
                self.game_over = True
                return False

        self.snake.insert(0, new_head)

        # Check food
        ate_food = False
        for food in list(self.foods):
            if new_head == food.pos:
                self.foods.remove(food)
                if food.food_type == FoodType.POISON:
                    # Shorten by 2
                    for _ in range(2):
                        if len(self.snake) > 1:
                            self.snake.pop()
                    if len(self.snake) <= 1:
                        self.game_over = True
                        return False
                else:
                    self.score += food.points() * self.level
                    self.food_eaten += 1
                    # Level up check
                    if self.food_eaten >= FOOD_PER_LEVEL:
                        self.food_eaten = 0
                        self.level += 1
                        if self.level >= OBSTACLES_START_LEVEL:
                            self._add_obstacles()
                    ate_food = True
                break  # only eat one food per tick

        if not ate_food:
            self.snake.pop()  # no growth

        # Check power-up pickup
        if self.active_powerup and new_head == self.active_powerup.pos:
            self._apply_powerup(self.active_powerup, now)
            self.active_powerup = None

        return True

    def _apply_powerup(self, pu: PowerUp, now: int):
        if pu.ptype == PowerUpType.SHIELD:
            self.shield_ready = True
            self.effect_type  = PowerUpType.SHIELD
            self.effect_until = now + POWERUP_EFFECT_DURATION
        else:
            self.effect_type  = pu.ptype
            self.effect_until = now + POWERUP_EFFECT_DURATION

    def _bounce(self, pos: tuple) -> tuple:
        """Clamp position to grid bounds (used when shield absorbs wall hit)."""
        x = max(0, min(GRID_COLS - 1, pos[0]))
        y = max(0, min(GRID_ROWS - 1, pos[1]))
        return (x, y)


#  Renderer 

def _cell_rect(x: int, y: int) -> pygame.Rect:
    return pygame.Rect(
        x * CELL_SIZE,
        HUD_HEIGHT + y * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE
    )

def draw_game(surface: pygame.Surface, state: GameState, font_sm, font_md):
    now = pygame.time.get_ticks()
    settings = state.settings
    snake_color = tuple(settings.get("snake_color", list(DEFAULT_SNAKE_COLOR)))

    # Background
    surface.fill(DARK_GRAY)

    # Grid overlay
    if settings.get("grid_overlay", True):
        for gx in range(GRID_COLS):
            for gy in range(GRID_ROWS):
                r = _cell_rect(gx, gy)
                pygame.draw.rect(surface, GRAY, r, 1)

    # Obstacles
    for (ox, oy) in state.obstacles:
        r = _cell_rect(ox, oy)
        pygame.draw.rect(surface, OBSTACLE_COLOR, r)
        pygame.draw.rect(surface, (100, 100, 100), r, 1)

    # Food
    for food in state.foods:
        r = _cell_rect(*food.pos)
        pygame.draw.ellipse(surface, food.color(), r.inflate(-4, -4))
        # Flash when about to expire
        if food.lifetime:
            remaining = food.lifetime - (now - food.spawn_time)
            if remaining < 2000 and (now // 200) % 2 == 0:
                pygame.draw.ellipse(surface, WHITE, r.inflate(-4, -4), 2)

    # Power-up on field
    if state.active_powerup:
        pu = state.active_powerup
        r = _cell_rect(*pu.pos)
        pygame.draw.rect(surface, pu.color(), r.inflate(-2, -2))
        pygame.draw.rect(surface, WHITE, r.inflate(-2, -2), 2)

    # Snake body
    for i, (sx, sy) in enumerate(state.snake):
        r = _cell_rect(sx, sy)
        if i == 0:
            # Head — slightly lighter
            head_col = tuple(min(255, c + 50) for c in snake_color)
            pygame.draw.rect(surface, head_col, r.inflate(-2, -2))
            pygame.draw.rect(surface, WHITE, r.inflate(-2, -2), 1)
        else:
            alpha_color = snake_color
            pygame.draw.rect(surface, alpha_color, r.inflate(-3, -3))

    # Shield indicator
    if state.shield_ready:
        hx, hy = state.snake[0]
        r = _cell_rect(hx, hy)
        pygame.draw.rect(surface, POWERUP_SHIELD_COLOR, r, 2)

    #  HUD 
    pygame.draw.rect(surface, (20, 20, 30), (0, 0, WINDOW_WIDTH, HUD_HEIGHT))

    score_surf = font_md.render(f"Score: {state.score}", True, WHITE)
    level_surf = font_md.render(f"Level: {state.level}", True, YELLOW)
    best_surf  = font_sm.render(f"Best: {state.personal_best}", True, LIGHT_GRAY)
    user_surf  = font_sm.render(state.username, True, CYAN)

    surface.blit(score_surf, (10, 8))
    surface.blit(level_surf, (200, 8))
    surface.blit(best_surf,  (380, 14))
    surface.blit(user_surf,  (WINDOW_WIDTH - user_surf.get_width() - 10, 14))

    # Active effect indicator
    if state.effect_type and now < state.effect_until:
        remaining_s = (state.effect_until - now) / 1000
        labels = {
            PowerUpType.SPEED_BOOST: ("SPEED BOOST", POWERUP_SPEED_COLOR),
            PowerUpType.SLOW_MOTION: ("SLOW MOTION", POWERUP_SLOW_COLOR),
            PowerUpType.SHIELD:      ("SHIELD READY", POWERUP_SHIELD_COLOR),
        }
        label, col = labels[state.effect_type]
        effect_surf = font_sm.render(f"{label} {remaining_s:.1f}s", True, col)
        surface.blit(effect_surf, (WINDOW_WIDTH // 2 - effect_surf.get_width() // 2, 14))