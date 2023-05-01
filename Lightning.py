import pygame
import random
from particle import WeaponParticles

from Collisions import *


# set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# create terrain surface
terrain_surface = pygame.Surface((width, height // 2))
terrain_surface.fill((0, 100, 0))  # green color

# create target object to mark the point where the lightning strikes
target_rect = pygame.Rect(width // 2 - 25, height // 2 - 25, 50, 50)
pygame.draw.rect(terrain_surface, (255, 0, 0), target_rect)

# define lightning function
def draw_lightning(start_x, start_y, end_x, end_y, num_strikes, delay, shell_x, shell_y, health_tank):
    # create a new surface for the lightning and particles
    lightning_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    particles_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    for strike in range(num_strikes):
        # create a list of points for the lightning
        points = [(start_x, start_y)]

        # add random displacement to each point
        offset = random.randint(-10, 10)
        for i in range(5):
            x = start_x + (i * (end_x - start_x) // 7) + random.randint(-7, 17)
            y = start_y + (i * (end_y - start_y) // 7) + random.randint(-7, 17)
            points.append((x, y))
        

        # add final point at target location
        points.append((end_x + offset, end_y))

        # create a random color for the lightning
        color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # draw the lightning on the surface
        pygame.draw.aalines(lightning_surface, color, False, points, blend=1)

        # create a second line of lightning
        points2 = [(x, y) for x, y in points]
        for i in range(len(points2)):
            if i % 2 == 0:
                points2[i] = (points2[i][0] + random.randint(-5, 5), points2[i][1] + random.randint(5, 10))

        points3 = [(x, y) for x, y in points]
        for i in range(len(points3)):
            if i % 2 == 0:
                points3[i] = (points3[i][0] + random.randint(-5, 5), points3[i][1] + random.randint(5, 10))

        # draw the second line of lightning on the surface
        pygame.draw.aalines(lightning_surface, color, False, points2, blend=1)
        pygame.draw.aalines(lightning_surface, color, False, points3, blend=1)

        # check if lightning hit the tank
        if tank_hit_detection(shell_x, shell_y):
            Lightning_DAMAGE = 3
            health_tank -= Lightning_DAMAGE

        # create WeaponParticles effect at target location
        particles = WeaponParticles((end_x, end_y))
        particles.update_and_draw(particles_surface)

        # blit the surfaces to the screen
        screen.blit(lightning_surface, (0, 0))
        screen.blit(particles_surface, (0, 0))
        pygame.display.update()

        # delay between strikes
        pygame.time.delay(delay)

    return lightning_surface, health_tank


       