import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
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
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        #create the bullet
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        #set velocity
        #go in direction player is facing
        #print(self.rotation)
        direction = pygame.Vector2(0,1).rotate(self.rotation)

        direction *= PLAYER_SHOOT_SPEED 
        bullet.velocity = direction
        #bullet.velocity += direction.y
        bullet.position += self.velocity *dt