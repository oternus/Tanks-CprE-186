import pygame
import math
import Button

# initialize font
pygame.font.init()

from Conventions import *
background = pygame.image.load("Game Assets/background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

def background_blit(terrain):
    window.blit(background, (0, 0))
    pygame.draw.lines(window, (BLACK), False, terrain, BACKGROUND_WIDTH)

def calculate_y(x):
    x += 50
    y = 500 + (10*3) * math.sin(0.005*3*x)
    return (y - 70)

def create_terrain(difficulty):
    terrain_length = SCREEN_WIDTH
    terrain_x_offset = 0
    terrain_y_offset = 500
    terrain_amplitude = 10 * difficulty
    terrain_frequency = 0.005 * difficulty
    terrain_points = []
    for i in range(terrain_length):
        x = i + terrain_x_offset
        y = terrain_y_offset + terrain_amplitude * math.sin(terrain_frequency * x)
        # y = 500 + (10*difficulty) * sin(0.005*difficulty)x
        terrain_points.append((x, y))

    return terrain_points

def terrain_generator():
  # initialize pygame
  pygame.init()

  # set up the window
  window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Difficulty Selection")

  # set up the font
  font_size = 40
  font = pygame.font.SysFont(None, font_size)

  EASY_BUTTON = Button.Button(0.5 * SCREEN_WIDTH - 75, 0.33 * SCREEN_HEIGHT, "EASY", 25, GREEN, BLACK, 1, width=150, height=50, border=2, border_color=(GREEN))
  MEDIUM_BUTTON = Button.Button(0.5 * SCREEN_WIDTH - 75, 0.496 * SCREEN_HEIGHT, "MEDIUM", 25, YELLOW, BLACK, 1, width=150, height=50, border=2, border_color=(YELLOW))
  HARD_BUTTON = Button.Button(0.5 * SCREEN_WIDTH - 75, 0.66 * SCREEN_HEIGHT, "HARD", 25, RED, BLACK, 1, width=150, height=50, border=2, border_color=(RED))



  # set up the clock
  clock = pygame.time.Clock()

  # define the terrain function

  # set up game loop
  difficulty_selected = False
  terrain = None

  while not difficulty_selected:
      
      pygame.display.update()

      # handle events
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              quit()

      EASY_ACTION =  EASY_BUTTON.draw(window)
      MEDIUM_ACTION = MEDIUM_BUTTON.draw(window)
      HARD_ACTION = HARD_BUTTON.draw(window)
      pygame.display.update()

      # check if buttons were clicked
      if EASY_ACTION:
          terrain = create_terrain(1)
          difficulty_selected = True
          print("e")
      elif MEDIUM_ACTION:
          terrain = create_terrain(2)
          difficulty_selected = True
          print("m")
      elif HARD_ACTION:
          terrain = create_terrain(3)
          print("h")
          difficulty_selected = True

  # main loop
  while True:
      # handle events
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              quit()

      # draw the terrain
      if difficulty_selected:
          bg = window.fill(WHITE)
          pygame.draw.lines(window, (150, 75, 0), False, terrain, BACKGROUND_WIDTH)

      # update the display
      pygame.display.update()

      # set the frame rate
      clock.tick(FPS)
