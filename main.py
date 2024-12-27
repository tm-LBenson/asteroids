import pygame
from constants import *
def main():
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  while True:
    screen.fill("black")
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return

    dt = clock.tick(MAX_FRAME_RATE)
    dt /= 1000 # convert to millisecond

    pygame.display.flip()# last
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
  main()
