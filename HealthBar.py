import pygame

pygame.init()

# Set up the display
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Health Bars")

# Define some colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Set up the fonts
font = pygame.font.Font(None, 30)

# Set up the initial health values
player_health = 100
enemy_health = 100

# Define the function to draw the health bars
def draw_health_bars():
    # Draw the player's health bar
    player_bar_width = 200
    player_bar_height = 20
    player_health_percent = max(player_health / 100, 0)
    player_bar_filled_width = player_bar_width * player_health_percent
    player_bar_rect = pygame.Rect(50, 50, player_bar_filled_width, player_bar_height)
    pygame.draw.rect(screen, green, player_bar_rect)
    player_bar_outline_rect = pygame.Rect(50, 50, player_bar_width, player_bar_height)
    pygame.draw.rect(screen, white, player_bar_outline_rect, 2)
    player_health_text = font.render(f"Player Health: {player_health}", True, white)
    screen.blit(player_health_text, (50, 25))
    
    # Draw the enemy's health bar
    enemy_bar_width = 200
    enemy_bar_height = 20
    enemy_health_percent = max(enemy_health / 100, 0)
    enemy_bar_filled_width = enemy_bar_width * enemy_health_percent
    enemy_bar_rect = pygame.Rect(screen_width - enemy_bar_filled_width - 50, 50, enemy_bar_filled_width, enemy_bar_height)
    pygame.draw.rect(screen, red, enemy_bar_rect)
    enemy_bar_outline_rect = pygame.Rect(screen_width - enemy_bar_width - 50, 50, enemy_bar_width, enemy_bar_height)
    pygame.draw.rect(screen, white, enemy_bar_outline_rect, 2)
    enemy_health_text = font.render(f"Enemy Health: {enemy_health}", True, white)
    screen.blit(enemy_health_text, (screen_width - enemy_health_text.get_width() - 50, 25))

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update the game state
    player_health -= 0.1
    enemy_health -= 0.05
    
    # Draw the game
    screen.fill(black)
    draw_health_bars()
    pygame.display.update()

pygame.quit()
