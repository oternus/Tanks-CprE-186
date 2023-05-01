import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the caption for the window
pygame.display.set_caption("Marker Object")

# Define the marker object
class Marker:
    def __init__(self, color, width, height, pos):
        self.color = color
        self.width = width
        self.height = height
        self.pos = pos if pos is not None else (0, 0)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.pos[0], self.pos[1], self.width, self.height])

    def draw_smoke(self, surface):
        for i in range(10):
            x = self.pos[0] + random.randint(0, self.width)
            y = self.pos[1] + random.randint(0, self.height)
            radius = random.randint(5, 20)
            alpha = random.randint(150, 255) # increase alpha value range
            color = (200, 200, 200, alpha)
            pygame.draw.circle(surface, color, (x, y), radius)