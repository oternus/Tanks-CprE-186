""" These are the conventions we are using for Tanks.
Please follow them.

Constants (something like SCREEN_WIDTH), are written in ALL CAPS with underscores "_" between words
The thing you draw on is called window, NOT background NOT screen.
Python does not conventionally use camel case. Use num_elements instead of numElements
 """

import pygame

RED = (255, 0, 0)
CYAN = (0,255,255)
BLUE = (0, 157, 196)
BLACK = (0,0,0)
ORANGE = (255,165,0)
WHITE = (255, 255, 255)
GREEN = (0, 102, 51)
YELLOW = (192, 192, 192)
BACKGROUND_WIDTH = 5

# sprite dimensions
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 650 # max height for background.png
GROUND_HEIGHT = 425 # y value of the flat line

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# tank dimensions
TANK_WIDTH = 100
TANK_HEIGHT = 100

# bullet dimensions
BULLET_WIDTH = 10
BULLET_HEIGHT = 10
BULLET_SPEED = 25
BULLET_DAMAGE = 10

# explosion dimensions, bullet hitboxes
EXPLOSION_WIDTH = 50
EXPLOSION_HEIGHT = 50

# timing
FPS = 60
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.Font(None, 30)

# Set up the health bar
HEALTH = 100
HEALTH_BAR_WIDTH = 200
HEALTH_BAR_HEIGHT = 20
HEALTH_BAR_BORDER_WIDTH = 2
HEALTH_BAR_COLOR = (255, 0, 0)
HEALTH_BAR_BACKGROUND_COLOUR = (255, 255, 255)
HEALTH_BAR_X = SCREEN_WIDTH - HEALTH_BAR_WIDTH - 10
HEALTH_BAR_Y = 10
