import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock() #create clock object to help manage framerate and keep track of game time
    dt = 0

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player1.draw(screen)
        pygame.display.flip()
        clock.tick(60) # set framerate to 60 fps
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
