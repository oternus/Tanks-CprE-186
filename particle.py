import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 1080
screen_height = 720

# Create the Pygame screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the screen
pygame.display.set_caption("Weapon Particle Effect")

class WeaponParticles:
    def __init__(self, position):
        self.position = position
        self.particles = []
        self.max_particles = 50
        self.particle_size = 2
        self.particle_speed = 5
        self.particle_color = (255, 255, 255)

    def update_and_draw(self, screen):
        # Create new particles
        if len(self.particles) < self.max_particles:
            x = self.position[0]
            y = self.position[1]
            for i in range(5):
                offset_x = random.randint(-10, 10)
                offset_y = random.randint(-10, 10)
                particle = [x + offset_x, y + offset_y, random.randint(1, self.particle_size)]
                self.particles.append(particle)

        # Update and draw particles
        for particle in self.particles:
            particle[0] += random.randint(-self.particle_speed, self.particle_speed)
            particle[1] += random.randint(-self.particle_speed, self.particle_speed)
            particle[2] -= 0.1

            if particle[2] <= 0:
                self.particles.remove(particle)
            else:
                pygame.draw.circle(screen, self.particle_color, (int(particle[0]), int(particle[1])), int(particle[2]))

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
        self.particles = WeaponParticles(self.Position)



    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.Position[0]), int(self.Position[1])), self.width)
        self.particles.update_and_draw(screen)

# Create a list of tank weapons
weapons = []
weapons.append(tankWeapons(10, (100, 100), 'center', (255, 0, 0), 'circle', 20, None))
weapons.append(tankWeapons(10, (200, 200), 'center', (0, 255, 0), 'rectangle', None, 50))
weapons.append(tankWeapons(10, (300, 300), 'center', (0, 0, 255), 'line', None, 100))

# Run the Pygame loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with black
    screen.fill((0, 0, 0))
    
    # Draw the tank weapons and their particle effects
    for weapon in weapons:
        weapon.draw(screen)
    
    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
