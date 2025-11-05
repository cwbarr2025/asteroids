import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
import sys

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock() #create clock object to help manage framerate and keep track of game time
    dt = 0

    updatable_grp = pygame.sprite.Group() # create empty group to put all the objects that can be updated
    drawable_grp = pygame.sprite.Group() # create empty group to put all objects that can be drawn
    asteroids_grp = pygame.sprite.Group() #create empty group for the asteroids
        
    Asteroid.containers = (asteroids_grp , updatable_grp, drawable_grp)
    AsteroidField.containers = (updatable_grp)

        # added a class variable to put all Player instances in both groups
    Player.containers = (updatable_grp, drawable_grp)
        # create player object after creating class variable (to make sure it is added/ has variable)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        for updatable in updatable_grp: #iterate through all objects in update group
            updatable.update(dt)
        for asteroid in asteroids_grp:
            if player1.check_collision(asteroid):
                sys.exit("Game over!")


        screen.fill("black")
        for drawable in drawable_grp: #iterate throuh all objects in drawable group
            drawable.draw(screen)

        pygame.display.flip()
        clock.tick(60) # set framerate to 60 fps
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
