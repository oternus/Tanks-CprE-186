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
                particle_size = random.randint(1, self.particle_size)
                particle_speed = random.randint(1, self.particle_speed)
                particle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                particle = [x + offset_x, y + offset_y, particle_size, particle_speed, particle_color]
                self.particles.append(particle)

        # Update and draw particles
        for particle in self.particles:
            particle[0] += random.randint(-particle[3], particle[3])
            particle[1] += random.randint(-particle[3], particle[3])
            particle[2] -= 0.1

            if particle[2] <= 0:
                self.particles.remove(particle)
            else:
                particle_size = int(min(particle[2], 3))
                pygame.draw.circle(screen, particle[4], (int(particle[0]), int(particle[1])), particle_size)




