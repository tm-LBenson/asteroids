import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():


  pygame.init()
  updatables = pygame.sprite.Group()
  drawables = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  Asteroid.containers = (asteroids, updatables, drawables)
  AsteroidField.containers = (updatables)
  clock = pygame.time.Clock()
  dt = 0
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  Player.containers = (updatables, drawables)
  AsteroidField()
  player = Player(x,y)
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  while True:
    screen.fill("black")
    for updatable in updatables:
      updatable.update(dt)
    for drawable in drawables:
      drawable.draw(screen)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return

    dt = clock.tick(MAX_FRAME_RATE)
    dt /= 1000 # convert to millisecond
    for asteroid in asteroids:
      if asteroid.collision(player):
        print("Game Over...")
        return
    pygame.display.flip()# last


if __name__ == "__main__":
  main()
