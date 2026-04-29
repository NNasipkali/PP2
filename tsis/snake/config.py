# config.py — Game constants and configuration

# Window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650
TITLE = "Snake Game"

# Grid
CELL_SIZE = 20
GRID_COLS = WINDOW_WIDTH // CELL_SIZE   # 40
GRID_ROWS = (WINDOW_HEIGHT - 50) // CELL_SIZE  # 30 (50px reserved for HUD)
HUD_HEIGHT = 50

# Colors
BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
GRAY        = (40, 40, 40)
LIGHT_GRAY  = (180, 180, 180)
DARK_GRAY   = (25, 25, 25)

GREEN       = (0, 200, 80)
DARK_GREEN  = (0, 140, 50)
RED         = (220, 50, 50)
DARK_RED    = (140, 20, 20)
BLUE        = (50, 130, 220)
YELLOW      = (240, 200, 30)
ORANGE      = (240, 130, 30)
PURPLE      = (160, 60, 220)
CYAN        = (30, 210, 210)
PINK        = (230, 80, 160)

# Food colors by type
FOOD_NORMAL_COLOR   = (255, 80, 80)
FOOD_BONUS_COLOR    = (255, 215, 0)
FOOD_POISON_COLOR   = (120, 0, 20)

# Power-up colors
POWERUP_SPEED_COLOR = (255, 165, 0)
POWERUP_SLOW_COLOR  = (100, 180, 255)
POWERUP_SHIELD_COLOR = (180, 255, 100)

# Obstacle color
OBSTACLE_COLOR = (80, 80, 80)

# Snake defaults
DEFAULT_SNAKE_COLOR = (0, 200, 80)
DEFAULT_SNAKE_HEAD_COLOR = (0, 240, 100)

# Speed settings (FPS / ticks per move)
BASE_SPEED = 8          # moves per second at level 1
SPEED_INCREMENT = 1     # extra moves/sec per level
MAX_SPEED = 20

SPEED_BOOST_MULTIPLIER = 1.6
SLOW_MOTION_MULTIPLIER = 0.5

# Level progression
FOOD_PER_LEVEL = 5      # food items to advance one level
OBSTACLES_START_LEVEL = 3
OBSTACLES_PER_LEVEL = 3  # new obstacle blocks added each level

# Timers (milliseconds)
BONUS_FOOD_LIFETIME   = 7000
POISON_FOOD_LIFETIME  = 10000
POWERUP_FIELD_LIFETIME = 8000
POWERUP_EFFECT_DURATION = 5000

# Food point values
FOOD_NORMAL_POINTS = 10
FOOD_BONUS_POINTS  = 30

# DB connection (edit as needed)
DB_CONFIG = {
    "host":     "localhost",
    "port":     5432,
    "dbname":   "snakegame",
    "user":     "nursultannasipkali",
    "password": "",
}