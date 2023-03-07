import pygame
import math

pygame.init()

# set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tank Gun Movement")

# set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# set up tank variables
tank_width = 40
tank_height = 20
tank_x = screen_width // 2 - tank_width // 2
tank_y = screen_height // 2 - tank_height // 2
tank_speed = .2

# set up gun variables
gun_width = 5
gun_height = 20
gun_x = tank_x + tank_width // 2 - gun_width // 2
gun_y = tank_y + tank_height // 2 - gun_height // 2
gun_angle = 0
gun_rotation_speed = .1

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # rotate gun with 'a' and 'd' keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        gun_angle -= gun_rotation_speed
    elif keys[pygame.K_d]:
        gun_angle += gun_rotation_speed

    # move the tank
    if keys[pygame.K_LEFT]:
        tank_x -= tank_speed
    elif keys[pygame.K_RIGHT]:
        tank_x += tank_speed
    elif keys[pygame.K_UP]:
        tank_y -= tank_speed
    elif keys[pygame.K_DOWN]:
        tank_y += tank_speed

    # update gun position
    gun_x = tank_x + tank_width // 2 - gun_width // 2
    gun_y = tank_y + tank_height // 2 - gun_height // 2

    # draw everything
    screen.fill(white)
    tank_rect = pygame.draw.rect(screen, black, (tank_x, tank_y, tank_width, tank_height))
    gun_rect = pygame.draw.rect(screen, black, (gun_x, gun_y, gun_width, gun_height))
    pygame.draw.line(screen, black, (gun_x + gun_width // 2, gun_y + gun_height // 2),
                     (gun_x + gun_width // 2 + math.cos(math.radians(gun_angle)) * 20,
                      gun_y + gun_height // 2 - math.sin(math.radians(gun_angle)) * 20), 3)

    # update the display
    pygame.display.update()

pygame.quit()
