import pygame
import math
import Button
from endScreen import end_Screen
from Terrain import create_terrain, calculate_y, background_blit
from Collisions import *

pygame.init()
pygame.display.set_caption("Tanks")

def calculate_distance(x1, y1, x2, y2):
        """
        This function takes in the x and y coordinates of two points and calculates the distance between them.
        """
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        return int(distance)

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
TIME_DELAY = 400 # milliseconds paused when shot hits
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

# Sets up the weapons menu LEFT
L_WEAPON_ONE_X = 0.1 * SCREEN_WIDTH - 80
L_WEAPON_ONE_Y = 0.18 * SCREEN_HEIGHT
L_WEAPON_TWO_X = 0.15 * SCREEN_WIDTH - 95
L_WEAPON_TWO_Y = 0.18 * SCREEN_HEIGHT
BOX_HEIGHT = 50
BOX_WIDTH = 50

L_red_box_pressed = True
L_green_box_pressed = False

# Sets up the weapons menu RIGHT
R_WEAPON_ONE_X = 0.94 * SCREEN_WIDTH - 80
R_WEAPON_ONE_Y = 0.18 * SCREEN_HEIGHT
R_WEAPON_TWO_X = .99 * SCREEN_WIDTH - 95
R_WEAPON_TWO_Y = 0.18 * SCREEN_HEIGHT

R_red_box_pressed = True
R_green_box_pressed = False

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
L_tank_sprite_1 = pygame.image.load("tank_paint4.png")
L_tank_sprite_2 = pygame.image.load("tank_paint4.png")
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
GUN_ROTATION_SPEED = 5
DISTANCE_BETWEEN = calculate_distance(x_tank1, y_tank1, x_tank2, y_tank2)

# when the program is running
running = True
start_is_clicked = False

# create buttons
start_button = Button.Button(0.5 * SCREEN_WIDTH - 300, 0.33 * SCREEN_HEIGHT, "START", 25, CYAN, BLACK, 1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, border=2, border_color=(CYAN))
quit_button = Button.Button(0.5 * SCREEN_WIDTH - 300, 0.66 * SCREEN_HEIGHT, "QUIT", 25, RED, BLACK, 1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, border=2, border_color=(RED))
settings_button = Button.Button(0.5 * SCREEN_WIDTH - 300, 0.496 * SCREEN_HEIGHT, "SETTINGS", 25, ORANGE, BLACK, 1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, border=2, border_color=(ORANGE))
# main_menu_button 

while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # alt f4 or top left X  
            running = False

    #draw background color
    bg = window.fill(BLACK)

    # draw buttons
    start_action = start_button.draw(window)
    quit_action = quit_button.draw(window)
    setting_action = settings_button.draw(window)
    # check if buttons were clicked
    if start_action:
        start_button_clicked = True
        running = False
        turn_tank1 = True
        turn_tank2 = False
    elif setting_action:
        print("Settings button clicked")
    elif quit_action:
        running = False
        start_button_clicked = False
    
    myVar = True

    pygame.display.flip()

terrain = create_terrain(3)
pygame.draw.lines(window, (150, 75, 0), False, terrain, BACKGROUND_WIDTH)
pygame.display.flip()

# weapons menu buttons
red_bullet = pygame.image.load("bullet.png")
red_bullet = pygame.transform.scale(red_bullet, (BOX_WIDTH - 10, BOX_HEIGHT - 10))

green_bullet = pygame.image.load("greenBullet.png")
green_bullet = pygame.transform.scale(green_bullet, (BOX_HEIGHT - 10, BOX_HEIGHT - 10))

#LEFT
L_red_bullet_box = Button.Button(L_WEAPON_ONE_X, L_WEAPON_ONE_Y, "", 30, BLACK, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 2, border_color = (WHITE))
L_red_box_outline = Button.Button(L_WEAPON_ONE_X, L_WEAPON_ONE_Y, "", 30, BLACK, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 4, border_color = (RED))
L_white_outline_r = Button.Button(L_WEAPON_ONE_X, L_WEAPON_ONE_Y, "", 30, BLACK, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 2, border_color = (WHITE))

L_green_bullet_box = Button.Button(L_WEAPON_TWO_X, L_WEAPON_TWO_Y, "", 30, BLACK, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 2, border_color = (WHITE))
L_green_box_outline = Button.Button(L_WEAPON_TWO_X, L_WEAPON_TWO_Y, "", 30, BLACK, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 4, border_color = (RED))
L_white_outline_g = Button.Button(L_WEAPON_TWO_X, L_WEAPON_TWO_Y, "", 30, BLACK, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 2, border_color = (WHITE))

L_weapon_picked = red_bullet
L_tank_shell = L_weapon_picked

#RIGHT
R_red_bullet_box = Button.Button(R_WEAPON_ONE_X, R_WEAPON_ONE_Y, "", 30, BLACK, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 2, border_color = (WHITE))
R_red_box_outline = Button.Button(R_WEAPON_ONE_X, R_WEAPON_ONE_Y, "", 30, BLACK, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 4, border_color = (RED))
R_white_outline_r = Button.Button(R_WEAPON_ONE_X, R_WEAPON_ONE_Y, "", 30, BLACK, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 2, border_color = (WHITE))

R_green_bullet_box = Button.Button(R_WEAPON_TWO_X, R_WEAPON_TWO_Y, "", 30, BLACK, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 2, border_color = (WHITE))
R_green_box_outline = Button.Button(R_WEAPON_TWO_X, R_WEAPON_TWO_Y, "", 30, BLACK, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 4, border_color = (RED))
R_white_outline_g = Button.Button(R_WEAPON_TWO_X, R_WEAPON_TWO_Y, "", 30, BLACK, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 2, border_color = (WHITE))

R_weapon_picked = red_bullet
R_tank_shell = R_weapon_picked

# this loop runs as long as Tanks is running 
while start_button_clicked:

    main_menu_action = False
    if main_menu_action:
        start_button_clicked = False
        running = True

    # everything happens 1/60th of a second
    clock.tick(FPS)
    y_original_tank1 = y_tank1 + (TANK_HEIGHT/4) - 100
    y_original_tank2 = y_tank2 + (TANK_HEIGHT/4) - 100
    magic_number = -20

    # outputs background to screen
    # window.blit(background, (0, 0))
    background_blit(terrain)

    # checking if alt+f4 or top right X 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            start_button_clicked = False


    if (tank_2_left or tank_2_right or tank_1_left or tank_1_right):
        DISTANCE_BETWEEN = calculate_distance(x_tank1, y_tank1, x_tank2, y_tank2)

    # game has ended
    if (health_tank1 <= 0):
        if (end_Screen("TANK 1") == 1):
            health_tank1 = STARTING_HEALTH
            health_tank2 = STARTING_HEALTH
            x_tank1 = 0
            y_tank1 = calculate_y(x_tank1)
            x_tank2 = 600
            y_tank2 = calculate_y(x_tank2)
        else:
            start_button_clicked = 0    # ends the game
    if (health_tank2 <= 0):
        if (end_Screen("TANK 2") == 1):
            health_tank1 = STARTING_HEALTH
            health_tank2 = STARTING_HEALTH
            x_tank1 = 0
            y_tank1 = calculate_y(x_tank1)
            x_tank2 = 600
            y_tank2 = calculate_y(x_tank2)
        else:
            start_button_clicked = 0    # ends the game

    # Draw the HEALTH bar
    pygame.draw.rect(window, HEALTH_BAR_COLOR, (x_tank1, y_tank1 - 30, health_tank1/100 * HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
    pygame.draw.rect(window, HEALTH_BAR_COLOR, (x_tank2, y_tank2 - 30, health_tank2/100 * HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))

    keys = pygame.key.get_pressed()
    
    # Draws weapons menu LEFT
    L_red_bullet_box.draw(window)
    window.blit(red_bullet, (L_WEAPON_ONE_X + 5, L_WEAPON_ONE_Y + 5))

    L_green_bullet_box.draw(window)
    window.blit(green_bullet, (L_WEAPON_TWO_X + 5, L_WEAPON_TWO_Y + 5))
    
    if (keys[pygame.K_1]):
        L_red_box_pressed = True
        L_green_box_pressed = False
        L_weapon_picked = red_bullet
        
    elif (keys[pygame.K_2]):
        L_red_box_pressed = False
        L_green_box_pressed = True
        L_weapon_picked = green_bullet

    if L_red_box_pressed:
        L_red_outline = L_red_box_outline.draw(window)
        L_red_draw = window.blit(red_bullet, (L_WEAPON_ONE_X + 5, L_WEAPON_ONE_Y + 5))

        L_white_outline = L_white_outline_g.draw(window)
        L_green_draw = window.blit(green_bullet, (L_WEAPON_TWO_X + 5, L_WEAPON_TWO_Y + 5))

    if L_green_box_pressed:
        L_green_outline = L_green_box_outline.draw(window)
        L_green_draw = window.blit(green_bullet, (L_WEAPON_TWO_X + 5, L_WEAPON_TWO_Y + 5))

        L_white_outline = L_white_outline_r.draw(window)
        L_red_draw = window.blit(red_bullet, (L_WEAPON_ONE_X + 5, L_WEAPON_ONE_Y + 5))

    # Draws weapons menu RIGHT
    R_red_bullet_box.draw(window)
    window.blit(red_bullet, (R_WEAPON_ONE_X + 5, R_WEAPON_ONE_Y + 5))

    R_green_bullet_box.draw(window)
    window.blit(green_bullet, (R_WEAPON_TWO_X + 5, R_WEAPON_TWO_Y + 5))
    
    if (keys[pygame.K_9]):
        R_red_box_pressed = True
        R_green_box_pressed = False
        R_weapon_picked = red_bullet
        
    elif (keys[pygame.K_0]):
        R_red_box_pressed = False
        R_green_box_pressed = True
        R_weapon_picked = green_bullet

    if R_red_box_pressed:
        R_red_outline = R_red_box_outline.draw(window)
        R_red_draw = window.blit(red_bullet, (R_WEAPON_ONE_X + 5, R_WEAPON_ONE_Y + 5))

        R_white_outline = R_white_outline_g.draw(window)
        R_green_draw = window.blit(green_bullet, (R_WEAPON_TWO_X + 5, R_WEAPON_TWO_Y + 5))

    if R_green_box_pressed:
        R_green_outline = R_green_box_outline.draw(window)
        R_green_draw = window.blit(green_bullet, (R_WEAPON_TWO_X + 5, R_WEAPON_TWO_Y + 5))

        R_white_outline = R_white_outline_r.draw(window)
        R_red_draw = window.blit(red_bullet, (R_WEAPON_ONE_X + 5, R_WEAPON_ONE_Y + 5))
    R_tank_shell = pygame.transform.scale(R_weapon_picked, (BULLET_WIDTH, BULLET_HEIGHT))
    L_tank_shell = pygame.transform.scale(L_weapon_picked, (BULLET_WIDTH, BULLET_HEIGHT))
         
    # movement of tank1
    if (keys[pygame.K_a]) and (x_tank1 > 0) and (x_tank1 - TANK_WIDTH - speed_tank1 != x_tank2):
        x_tank1 -= speed_tank1
        y_tank1 = calculate_y(x_tank1)
        tank_1_left = True
        tank_1_right = False
    if (keys[pygame.K_d]) and (x_tank1 < (SCREEN_WIDTH - TANK_WIDTH)) and (x_tank1 + TANK_WIDTH + speed_tank1 != x_tank2) :
        x_tank1 += speed_tank1
        y_tank1 = calculate_y(x_tank1)
        tank_1_right = True
        tank_1_left = False

    if keys[pygame.K_w]:
        gun_angle += GUN_ROTATION_SPEED
    elif keys[pygame.K_s]:
        gun_angle -= GUN_ROTATION_SPEED

    # movement of tank2
    if (keys[pygame.K_LEFT]) and (x_tank2 > 0) and (x_tank2 - TANK_WIDTH - speed_tank1 != x_tank1):
        x_tank2 -= speed_tank2
        y_tank2 = calculate_y(x_tank2)
        tank_2_left = True
        tank_2_right = False
    if (keys[pygame.K_RIGHT]) and (x_tank2 < (SCREEN_WIDTH - TANK_WIDTH)) and (x_tank2 + TANK_WIDTH + speed_tank1 != x_tank1):
        x_tank2 += speed_tank2
        y_tank2 = calculate_y(x_tank2)
        tank_2_right = True
        tank_2_left = False

    # tank1
    if (tank_1_left):
        window.blit(L_tank_sprite_1, (x_tank1, y_tank1))
        pygame.draw.line(window, BLACK, (x_tank1 + (TANK_WIDTH/2), y_tank1),
                     (x_tank1 + (TANK_WIDTH/2) + math.cos(math.radians(gun_angle)) * 50,
                      y_tank1 - math.sin(math.radians(gun_angle)) * 50), 3)
    if (tank_1_right):
        window.blit(R_tank_sprite_1, (x_tank1, y_tank1))
        pygame.draw.line(window, BLACK, (x_tank1 + (TANK_WIDTH/2), y_tank1),
                     (x_tank1 + (TANK_WIDTH/2) + math.cos(math.radians(gun_angle)) * 50,
                      y_tank1 - math.sin(math.radians(gun_angle)) * 50), 3)

    # tank2
    if (tank_2_left):
        window.blit(L_tank_sprite_2, (x_tank2, y_tank2))
        pygame.draw.line(window, BLACK, (x_tank2 + (TANK_WIDTH/2), y_tank2),
                     (x_tank2 + (TANK_WIDTH/2) + math.cos(math.radians(gun_angle)) * 50,
                      y_tank2 - math.sin(math.radians(gun_angle)) * 50), 3)
    if (tank_2_right):
        window.blit(R_tank_sprite_2, (x_tank2, y_tank2))
        pygame.draw.line(window, BLACK, (x_tank2 + (TANK_WIDTH/2), y_tank2),
                     (x_tank2 + (TANK_WIDTH/2) + math.cos(math.radians(gun_angle)) * 50,
                      y_tank2 - math.sin(math.radians(gun_angle)) * 50), 3)


    # shooting
    angle_select = font.render(f"ANGLE: {round(shot_angle, 1)}", True, (0, 0, 0))
    window.blit(angle_select, (SCREEN_WIDTH/2 - 50, 20))

    power_select = font.render(f"POWER: {shot_power}", True, (0, 0, 0))
    window.blit(power_select, (SCREEN_WIDTH/2 - 50, 40))

    Distance_select = font.render(f"DISTANCE: {DISTANCE_BETWEEN}", True, (0, 0, 0))
    window.blit(Distance_select, (SCREEN_WIDTH/2 - 50, 60))
    


    if (keys[pygame.K_TAB]):
        jump = 100


    if (keys[pygame.K_w]) and (shot_angle < MAX_SHOT_ANGLE):
        pygame.time.delay(100)
        shot_angle += 0.1
        pygame.display.update()
    if (keys[pygame.K_s]) and (shot_angle > MIN_SHOT_ANGLE):
        pygame.time.delay(100)
        shot_angle -= 0.1
        pygame.display.update()

    if (keys[pygame.K_LSHIFT]) and (shot_power < MAX_SHOT_POWER):
        pygame.time.delay(100)
        shot_power += 1
    if (keys[pygame.K_LCTRL]) and (shot_power > MIN_SHOT_POWER):
        pygame.time.delay(100)
        shot_power -= 1

    # hitbox visualization
    pygame.display.flip()
    #pygame.draw.rect(window, HEALTH_BAR_COLOR, (HEALTH_BAR_X, HEALTH_BAR_Y, health_tank2 / 100 * HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))

    if (keys[pygame.K_SPACE]):
        
        bonus_bullet_damage = 0

        # tank 1 turn
        if (turn_tank1):

            x_tank_shell_old = x_tank_shell
            y_tank_shell_old = y_tank_shell
            y_tank_shell = y_tank1 + (TANK_HEIGHT/4) # starting position of shell
            x_tank_shell = x_tank1 + (TANK_WIDTH/2) # starting position of shell

            # while shell hasnt hit a tank and isnt out of bounds
            # this is the movement of the shell
            while ((x_tank_shell > 0) and (x_tank_shell < SCREEN_WIDTH) and (y_tank_shell < SCREEN_HEIGHT)):
                
                bonus_bullet_damage += BONUS_BULLET_DAMAGE_INCREMENT
                y_tank_shell_old = y_tank_shell
                magic_number += shot_angle

                pygame.time.delay(TIME_DELAY_BETWEEN_BULLETS)
                y_tank_shell = + y_original_tank1 + ((magic_number) * (magic_number) * (0.4)) - 40

                if (tank_1_right):
                    #pygame.draw.circle(window, (GREEN), (x_tank_shell, y_tank_shell), BULLET_WIDTH, 0)
                    window.blit(L_tank_shell, (x_tank_shell, y_tank_shell))
                    window.blit(background_clear, (x_tank_shell_old, y_tank_shell_old))
                    pygame.display.update()
                    x_tank_shell_old = x_tank_shell
                    x_tank_shell += shot_power

                if (tank_1_left):
                    window.blit(L_tank_shell, (x_tank_shell, y_tank_shell))
                    window.blit(background_clear, (x_tank_shell_old, y_tank_shell_old))
                    pygame.display.update()
                    x_tank_shell_old = x_tank_shell
                    x_tank_shell -= shot_power

                shell_to_tank_x = abs(x_tank_shell - x_tank2)
                shell_to_tank_y = abs(y_tank_shell - (y_tank2+50))

                hit_confirm = tank_hit_detection(shell_to_tank_x, shell_to_tank_y)
                hit_ground = y_tank_shell > (calculate_y(x_tank_shell) + 50)

                if (hit_confirm) or (hit_ground):
                    # window.blit(background_clear, (x_tank_shell, y_tank_shell))
                    window.blit(explosion, (x_tank_shell, y_tank_shell))
                    pygame.display.update()
                    pygame.time.delay(TIME_DELAY)
                    if (hit_confirm):
                        health_tank2 -= (BULLET_DAMAGE + bonus_bullet_damage)
                    x_tank_shell = 10000
                    y_tank_shell = 10000

                turn_tank1 = False
                turn_tank2 = True

        elif (turn_tank2):

            x_tank_shell_old = x_tank_shell
            y_tank_shell_old = y_tank_shell
            y_tank_shell = y_tank2 + (TANK_HEIGHT/4) # starting position of shell
            x_tank_shell = x_tank2 + (TANK_WIDTH/2) # starting position of shell

            # while shell hasnt hit a tank and isnt out of bounds
            # this is the movement of the shell
            while ((x_tank_shell > 0) and (x_tank_shell < SCREEN_WIDTH) and (y_tank_shell < SCREEN_HEIGHT)):
                
                bonus_bullet_damage += BONUS_BULLET_DAMAGE_INCREMENT
                y_tank_shell_old = y_tank_shell
                magic_number += shot_angle

                pygame.time.delay(TIME_DELAY_BETWEEN_BULLETS)
                y_tank_shell = + y_original_tank2 + ((magic_number) * (magic_number) * (0.4)) - 40

                if (tank_2_right):
                    window.blit(R_tank_shell, (x_tank_shell, y_tank_shell))
                    window.blit(background_clear, (x_tank_shell_old, y_tank_shell_old))
                    pygame.display.update()
                    x_tank_shell_old = x_tank_shell
                    x_tank_shell += shot_power

                if (tank_2_left):
                    window.blit(R_tank_shell, (x_tank_shell, y_tank_shell))
                    window.blit(background_clear, (x_tank_shell_old, y_tank_shell_old))
                    pygame.display.update()
                    x_tank_shell_old = x_tank_shell
                    x_tank_shell -= shot_power


                shell_to_tank_x = abs(x_tank_shell - x_tank1)
                shell_to_tank_y = abs(y_tank_shell - (y_tank1+50))

                hit_confirm = tank_hit_detection(shell_to_tank_x, shell_to_tank_y)
                hit_ground = y_tank_shell > (calculate_y(x_tank_shell) + 50)

                if (hit_confirm) or (hit_ground):
                    # window.blit(background_clear, (x_tank_shell, y_tank_shell))
                    window.blit(explosion, (x_tank_shell, y_tank_shell))
                    pygame.display.update()
                    pygame.time.delay(TIME_DELAY)
                    if (hit_confirm):
                        health_tank1 -= (BULLET_DAMAGE + bonus_bullet_damage)
                    x_tank_shell = 10000
                    y_tank_shell = 10000
 
                turn_tank2 = False
                turn_tank1 = True

    
    # refresh();
    pygame.display.update() 

# game over


pygame.quit()
