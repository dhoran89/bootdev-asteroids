import pygame
# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        #draw player triangle (screen obj, color, list of points, line width)
        pygame.draw.polygon(screen,"white", self.triangle(), 2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        distance = self.position.distance_to(other.position)
        r1 = self.radius/2
        r2 = other.radius/2
        if (r1 + r2) < distance:
            return False
        else:
            return True
