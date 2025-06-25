import pygame
from constants import *
from circleshape import CircleShape
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    r = PLAYER_RADIUS
    player = Player(x, y, r)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        #limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

        #instantiate player obj

if __name__ == "__main__":
    main()