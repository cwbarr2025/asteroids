import pygame
from constants import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock() #create clock object to help manage framerate and keep track of game time
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        clock.tick(60) # set framerate to 60 fps
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
