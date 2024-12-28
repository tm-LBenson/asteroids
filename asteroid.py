import pygame, random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x,y,radius):
    super().__init__(x,y,radius)
  def draw(self, screen):
     pygame.draw.circle(screen, "white",self.position,self.radius, 2)
  def update(self, dt):
    self.position += self.velocity * dt
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    rand = random.uniform(20,50)
    x = self.position[0]
    y = self.position[1]
    v1 = self.velocity.rotate(rand)
    v2 = self.velocity.rotate(-rand)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    new_asteroid = Asteroid(x,y,new_radius)
    new_asteroid.velocity = v1 * 1.2
    new_asteroid2 = Asteroid(x,y,new_radius)
    new_asteroid2.velocity = v2 * 1.2
    
