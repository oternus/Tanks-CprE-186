import math
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Projectile Arc")

# Set up the font
font = pygame.font.SysFont("Arial", 20)

# Set up the variables for the projectile
x = 0
y = screen_height // 2
velocity = 50
angle = 45
time = 0
gravity = 9.8
arc_color = pygame.Color("white")

# Set up the variables for the tank and gun
tank_image = pygame.image.load("tank.png").convert_alpha()
gun_image = pygame.image.load("gun.png").convert_alpha()
gun_offset = 25
gun_angle = 0

# Combine the tank and gun images into one surface
tank_gun_surface = pygame.Surface((max(tank_image.get_width(), gun_image.get_width()),
                                   tank_image.get_height() + gun_offset + gun_image.get_height()),
                                  flags=pygame.SRCALPHA)
tank_gun_surface.blit(tank_image, (0, 0))
tank_gun_surface.blit(gun_image, (0, tank_image.get_height() + gun_offset))

# Start the game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the variables
    radians = math.radians(angle)
    x = int(velocity * time * math.cos(radians))
    y = int(screen_height // 2 - (velocity * time * math.sin(radians) - 0.5 * gravity * time ** 2))
    time += 0.1

    # Update the gun angle
    dx = x - gun_image.get_width() // 2
    dy = y - gun_offset - gun_image.get_height()
    gun_angle = -math.degrees(math.atan2(dy, dx))

    # Draw the arc
    pygame.draw.circle(screen, arc_color, (x, y), 5)

    # Draw the tank and gun
    tank_gun_surface_rotated = pygame.transform.rotate(tank_gun_surface, gun_angle)
    tank_gun_rect = tank_gun_surface_rotated.get_rect(center=(x, y - gun_offset))
    screen.blit(tank_gun_surface_rotated, tank_gun_rect)

    # Display the angle on the screen
    angle_text = font.render(f"Angle: {angle} degrees", True, arc_color)
    screen.blit(angle_text, (10, 10))

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()