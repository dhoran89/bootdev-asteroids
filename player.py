import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
#create player
class Player(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.rotation = 0
        
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        super().draw(screen)
        #draw player triangle (screen obj, color, list of points, line width)
        pygame.draw.polygon(screen,"white", self.triangle(), 2)
    