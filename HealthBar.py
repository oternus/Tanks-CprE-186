import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the font
font = pygame.font.Font(None, 30)

# Set up the health bar
health = 100
health_bar_width = 200
health_bar_height = 20
health_bar_border_width = 2
health_bar_color = (255, 0, 0)
health_bar_background_color = (255, 255, 255)
health_bar_x = screen_width - health_bar_width - 10
health_bar_y = 10

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the health bar background
    pygame.draw.rect(screen, health_bar_background_color, (health_bar_x, health_bar_y, health_bar_width, health_bar_height))

    # Draw the health bar
    pygame.draw.rect(screen, health_bar_color, (health_bar_x, health_bar_y, health / 100 * health_bar_width, health_bar_height))

    # Draw the health text
    health_text = font.render(f"Health: {health}", True, (0, 0, 0))
    screen.blit(health_text, (10, 10))

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
