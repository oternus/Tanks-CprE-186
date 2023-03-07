import pygame
import Button

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650 
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

red = (255, 0, 0)
cyan = (0,255,255)
black = (0,0,0)
orange = (255,165,0)

myfont = pygame.font.SysFont("Arial", 30)


# create buttons
start_button = Button.Button(0.5 * SCREEN_WIDTH - 75, 0.33 * SCREEN_HEIGHT, "START", 25, cyan, black, 1, width=150, height=50, border=2, border_color=(cyan))
quit_button = Button.Button(0.5 * SCREEN_WIDTH - 75, 0.66 * SCREEN_HEIGHT, "QUIT", 25, red, black, 1, width=150, height=50, border=2, border_color=(red))
settings_button = Button.Button(0.5 * SCREEN_WIDTH - 75, 0.496 * SCREEN_HEIGHT, "SETTINGS", 25, orange, black, 1, width=150, height=50, border=2, border_color=(orange))

running = True

while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # alt f4 or top left X  
            running = False

    #draw background color
    bg = window.fill(black)


    # draw buttons
    start_action = start_button.draw(window)
    quit_action = quit_button.draw(window)
    setting_action = settings_button.draw(window)
    # check if buttons were clicked
    if start_action:
        print("Start button clicked")
    elif setting_action:
        print("Settings button clicked")
    elif quit_action:
        running = False

    pygame.display.flip()
