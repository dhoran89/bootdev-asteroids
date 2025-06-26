import pygame
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    r = PLAYER_RADIUS
    
    #containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    #create groups
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    #instantiate player obj
    player = Player(x, y, r)
    AsteroidField()  
    #instantiate asteroids

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #fill screen black
        screen.fill("black")
        #update container(updatable)
        updatable.update(dt)
        for a in asteroids:
            if a.collision(player):
                sys.exit("Game over!")
        #draw what is in container(drawable)
        for obj in drawable:
            obj.draw(screen)
        
        #flip display
        pygame.display.flip()
        
        #limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()