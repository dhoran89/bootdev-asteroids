import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red",(self.position.x, self.position.y), self.radius, width = 2)
    
    def update(self, dt):
        delta_pos = self.velocity * dt
        self.position += delta_pos