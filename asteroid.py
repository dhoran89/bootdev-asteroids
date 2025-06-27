import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.position.x, self.position.y), self.radius, width = 2)
    
    def update(self, dt):
        delta_pos = self.velocity * dt
        self.position += delta_pos

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            a = self.velocity.rotate(random_angle)
            b = self.velocity.rotate(-random_angle)

            asteroid = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid.velocity = a * 1.20

            asteroid = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid.velocity = b * 1.20