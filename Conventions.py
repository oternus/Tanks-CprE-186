""" These are the conventions we are using for Tanks.
Please follow them.

Constants (something like SCREEN_WIDTH), are written in ALL CAPS with underscores "_" between words
The thing you draw on is called window, NOT background NOT screen.
Python does not conventionally use camel case. Use num_elements instead of numElements
 """

import pygame
import Button
from Terrain import create_terrain, calculate_y, background_blit

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
TANK_WIDTH = 100
TANK_HEIGHT = 100
TANK_HITBOX_WIDTH = TANK_WIDTH
TANK_HITBOX_HEIGHT = TANK_HEIGHT/5

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
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.Font(None, 30)

# Set up the health bar
STARTING_HEALTH = 100
HEALTH_BAR_WIDTH = 200
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
WHITE = (0, 0, 0)

# loads the background image
BACKGROUND_WIDTH = 5
terrain = None
background = pygame.image.load("background.png")
background_clear = pygame.image.load("sky.png")
background_clear = pygame.transform.scale(background_clear, (BULLET_WIDTH, BULLET_HEIGHT))

# loads and scales the tank image
L_tank_sprite_1 = pygame.image.load("tankSprite.png")
L_tank_sprite_2 = pygame.image.load("tankSprite.png")
L_tank_sprite_1 = pygame.transform.scale(L_tank_sprite_1, (TANK_WIDTH, TANK_HEIGHT))
L_tank_sprite_2 = pygame.transform.scale(L_tank_sprite_2, (TANK_WIDTH, TANK_HEIGHT))

# loads and scales the bullet image
tank_shell = pygame.image.load("bullet.png")
tank_shell = pygame.transform.scale(tank_shell, (BULLET_WIDTH, BULLET_HEIGHT))
explosion = pygame.image.load("black_explosion.png")
explosion = pygame.transform.scale(explosion, (EXPLOSION_WIDTH, EXPLOSION_HEIGHT))

# direction changes
R_tank_sprite_1 = pygame.transform.flip(L_tank_sprite_1, True, False)
R_tank_sprite_2 = pygame.transform.flip(L_tank_sprite_2, True, False)

# position of tank 
x_tank1 = 0
y_tank1 = calculate_y(x_tank1)
x_tank2 = 600
y_tank2 = calculate_y(x_tank2)
tank_1_left = True
tank_1_right = False
tank_2_left = True
tank_2_right = False
  
# sensitivity to key input
speed_tank1 = 2.5
speed_tank2 = 2.5

# default starting points of tank shell
x_tank_shell = x_tank1 + (TANK_WIDTH/2)
y_tank_shell = y_tank1 + (TANK_HEIGHT/4)

shot_power = BULLET_SPEED
shot_angle = 2
gun_angle = 0
hit_confirm = False
bonus_bullet_damage = 0

# when the program is running
running = True
start_is_clicked = False

# create buttons
start_button = Button.Button(0.5 * SCREEN_WIDTH - 300, 0.33 * SCREEN_HEIGHT, "START", 25, CYAN, BLACK, 1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, border=2, border_color=(CYAN))
quit_button = Button.Button(0.5 * SCREEN_WIDTH - 300, 0.66 * SCREEN_HEIGHT, "QUIT", 25, RED, BLACK, 1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, border=2, border_color=(RED))
settings_button = Button.Button(0.5 * SCREEN_WIDTH - 300, 0.496 * SCREEN_HEIGHT, "SETTINGS", 25, ORANGE, BLACK, 1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, border=2, border_color=(ORANGE))
