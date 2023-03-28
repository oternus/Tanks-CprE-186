import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 1080
screen_height = 720

# Create the Pygame screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the screen
pygame.display.set_caption("Default Pygame Screen")

class tankWeapons:

    def __init__(self, Speed, Position, shotOrigin, color, Shape, radius, width):
        self.Speed = Speed
        self.Position = Position
        self.shotOrigin = shotOrigin
        self.color = color
        if Shape == 'circle':
            self.width = radius
        else:
            self.width = width

def drawWeapon(screen, position, speed, color, Wantedshape, radius=None, width=None, height=None):
        if Wantedshape == 'rectangle':
            shape = pygame.draw.rect(screen, color, (int(position[0]), int(position[1]), width, height))

        elif Wantedshape == 'circle':
            shape = pygame.draw.circle(screen, color, (int(position[0]), int(position[1])), radius)

        elif Wantedshape == 'line':
            shape = pygame.draw.line(screen, color, (int(position[0]), int(position[1])), (int(position[0])+width, int(position[1])), None)

        return shape

# Run the Pygame loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with white
    screen.fill((255, 255, 255))
    drawWeapon(screen, (123, 123), None, (123,53,34), 'circle', radius=23)
    
    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
