import pygame
from constants import *
from player import Player
def main():
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  player = Player(x,y)
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  while True:
    screen.fill("black")
    player.draw(screen)


    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return

    dt = clock.tick(MAX_FRAME_RATE)
    dt /= 1000 # convert to millisecond

    pygame.display.flip()# last


if __name__ == "__main__":
  main()
