# this allows us to use code from
# the open-source pygame library
# throughout this file

import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main ():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() 
    dt = 0
    
    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    
    asteroid_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # player.draw(screen)
        # player.update(dt)
        
        for item in updatable:
            item.update(dt)
        
        for aster in asteroids:
            if player.is_colliding(aster):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if aster.is_colliding(bullet):
                    aster.split(dt)
                    bullet.kill()
        
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
