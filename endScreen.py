import pygame
import Button

pygame.init()

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 650 
BUTTON_WIDTH = 600
BUTTON_HEIGHT = 75
myfont = pygame.font.SysFont("Arial", 30)
#winner should be TANK1 or TANK2 as a string

def end_Screen(winner):
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    red = (255, 0, 0)
    cyan = (0,255,255)
    black = (0,0,0)
    orange = (255,165,0)
    white = (255,255, 255)

    winnerBox = Button.Button(0.5 * SCREEN_WIDTH - 300, 0.00 * SCREEN_HEIGHT + 50, f"{winner} WON", 100, white, black, 1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT+100, border=2, border_color=(black))

    # create buttons
    start_button = Button.Button(0.5 * SCREEN_WIDTH - 300, 0.25 * SCREEN_HEIGHT + 100, "PLAY AGAIN", 25, cyan, black, 1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, border=2, border_color=(cyan))
    quit_button = Button.Button(0.5 * SCREEN_WIDTH - 300, 0.55 * SCREEN_HEIGHT + 100, "QUIT", 25, red, black, 1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, border=2, border_color=(red))
    settings_button = Button.Button(0.5 * SCREEN_WIDTH - 300, 0.40 * SCREEN_HEIGHT + 100, "SETTINGS", 25, orange, black, 1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, border=2, border_color=(orange))

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
        winnerBox.draw(window)

        # check if buttons were clicked
        if start_action:
            print("Play again button clicked")
            running = False
            return 1
        elif setting_action:
            print("Settings button clicked")
        elif quit_action:
            running = False
            return 0

        pygame.display.flip()
