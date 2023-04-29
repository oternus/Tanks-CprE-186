""" 
These are the conventions we are using for Tanks.
Please follow them.

Constants (something like SCREEN_WIDTH), are written in ALL CAPS with underscores "_" between words
The thing you draw on is called window, NOT background NOT screen.
Python does not conventionally use camel case. Use num_elements instead of numElements
"""

import pygame
import Button

RED = (255, 0, 0)
CYAN = (0,255,255)
BLUE = (0, 157, 210)
BLACK = (0,0,0)
ORANGE = (255,165,0)
WHITE = (255, 255, 255)
GREEN = (0, 102, 51)
YELLOW = (192, 192, 192)
BACKGROUND_WIDTH = 5

# sprite dimensions
SCREEN_WIDTH = 1300 # change to 1000 if problems
SCREEN_HEIGHT = 650 # max height for background.png
GROUND_HEIGHT = 425 # y value of the flat line

BUTTON_WIDTH = 600
BUTTON_HEIGHT = 100

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# tank dimensions
TANK_WIDTH = 80
TANK_HEIGHT = 80
TANK_HITBOX_WIDTH = TANK_WIDTH
TANK_HITBOX_HEIGHT = TANK_HEIGHT

# bullet dimensions
BULLET_WIDTH = 10
BULLET_HEIGHT = 10
BULLET_SPEED = 25
BULLET_DAMAGE = 10
BONUS_BULLET_DAMAGE_INCREMENT = 1

# shot parameters
MAX_SHOT_ANGLE = 4.0
MIN_SHOT_ANGLE = 1.5
MAX_SHOT_POWER = 45
MIN_SHOT_POWER = 0

# explosion dimensions, bullet hitboxes
EXPLOSION_WIDTH = 50
EXPLOSION_HEIGHT = 50

# timing
FPS = 60
TIME_DELAY = 200 # milliseconds paused when shot hits
TIME_DELAY_BETWEEN_BULLETS = 30 # milliseconds between bullet position update
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.Font(None, 30)

# Set up the health bar
STARTING_HEALTH = 100
HEALTH_BAR_WIDTH = 150
HEALTH_BAR_HEIGHT = 20
HEALTH_BAR_BORDER_WIDTH = 2
HEALTH_BAR_COLOR = (255, 0, 0)
HEALTH_BAR_BACKGROUND_COLOUR = (255, 255, 255)
HEALTH_BAR_X = SCREEN_WIDTH - HEALTH_BAR_WIDTH - 10
HEALTH_BAR_Y = 10
health_tank1 = STARTING_HEALTH
health_tank2 = STARTING_HEALTH

RED = (255, 0, 0)
CYAN = (0,255,255)
BLACK = (0,0,0)
ORANGE = (255,165,0)
WHITE = (255, 255, 255)

# loads the background image
BACKGROUND_WIDTH = 5
terrain = None

# create buttons
start_button = Button.Button(0.5 * SCREEN_WIDTH - 300, 0.33 * SCREEN_HEIGHT, "START", 25, CYAN, BLACK, 1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, border=2, border_color=(CYAN))
quit_button = Button.Button(0.5 * SCREEN_WIDTH - 300, 0.66 * SCREEN_HEIGHT, "QUIT", 25, RED, BLACK, 1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, border=2, border_color=(RED))
settings_button = Button.Button(0.5 * SCREEN_WIDTH - 300, 0.496 * SCREEN_HEIGHT, "SETTINGS", 25, ORANGE, BLACK, 1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, border=2, border_color=(ORANGE))


def calculate_distance(x1, y1, x2, y2):
    """
    This function takes in the x and y coordinates of two points and calculates the distance between them.
    """
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return int(distance)
