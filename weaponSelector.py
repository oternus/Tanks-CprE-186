import pygame
import Button

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
RED_BOX_X = 0.5 * SCREEN_WIDTH - 80
RED_BOX_Y = 0.85 * SCREEN_HEIGHT
GREEN_BOX_X = 0.55 * SCREEN_WIDTH - 80
GREEN_BOX_Y = 0.85 * SCREEN_HEIGHT
BOX_HEIGHT = 50
BOX_WIDTH = 50

def weapon_Selection():
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    black = (0,0,0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    red_bullet = pygame.image.load("bullet.png")
    red_bullet = pygame.transform.scale(red_bullet, (BOX_WIDTH - 10, BOX_HEIGHT - 10))
    red_bullet_box = Button.Button(RED_BOX_X, RED_BOX_Y, "", 30, black, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 2, border_color = (white))
    red_box_outline = Button.Button(RED_BOX_X, RED_BOX_Y, "", 30, black, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 4, border_color = (red))
    
    green_bullet = pygame.image.load("greenBullet.png")
    green_bullet = pygame.transform.scale(green_bullet, (BOX_HEIGHT - 10, BOX_HEIGHT - 10))
    green_bullet_box = Button.Button(GREEN_BOX_X, GREEN_BOX_Y, "", 30, black, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 2, border_color = (white))
    green_box_outline = Button.Button(GREEN_BOX_X, GREEN_BOX_Y, "", 30, black, 1, width = BOX_WIDTH, height = BOX_HEIGHT, border = 4, border_color = (red))

    running = True
    red_box_pressed = True
    green_box_pressed = False
    
    while running:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # alt f4 or top left X  
                running = False

        keys = pygame.key.get_pressed()
        bg = window.fill(black)

        # draw buttons
        red_box = red_bullet_box.draw(window)
        red_draw = window.blit(red_bullet, (RED_BOX_X + 5, RED_BOX_Y + 5))

        green_box = green_bullet_box.draw(window)
        green_draw = window.blit(green_bullet, (GREEN_BOX_X + 5, GREEN_BOX_Y + 5))
        
        # weapon selection
        if (keys[pygame.K_1]):
            red_box_pressed = True
            green_box_pressed = False
            
        elif (keys[pygame.K_2]):
            red_box_pressed = False
            green_box_pressed = True

        if red_box_pressed:
            red_outline = red_box_outline.draw(window)
            red_draw = window.blit(red_bullet, (RED_BOX_X + 5, RED_BOX_Y + 5))

        if green_box_pressed:
            green_outline = green_box_outline.draw(window)
            green_draw = window.blit(green_bullet, (GREEN_BOX_X + 5, GREEN_BOX_Y + 5))

        pygame.display.flip()
