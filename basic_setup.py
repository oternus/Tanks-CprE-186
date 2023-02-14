import pygame    

# initializing the window
pygame.init() # initscr();
Width = 800
Height = 800
screen = pygame.display.set_mode((Width,Height))
logo = pygame.image.load("logo.png") # image.png is the logo
pygame.display.set_icon(logo) # refresh();
pygame.display.set_caption("My Game") # name of program

image = pygame.image.load("logo.png") # loads the image

running = True
x = 0
y = 0

if running:
    print("User started the game")

while running:    
    for event in pygame.event.get():
        screen.blit(image, (x,y))
        if pygame.key.get_pressed()[pygame.K_s]: # if user presses s
            y -= 10 # moves down
            print(y)
        if event.type == pygame.QUIT: # alt f4 or top left X  
            running = False
            print("User quit the game")
    pygame.display.flip() # refresh();
