from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import pygame
# allows us to use code from open-source pygame library
# throughout this file
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Player.containers = (updatable, drawable)
Shot.containers = (updatable, drawable)

def main():
    pygame.init()
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidfield = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# above line sets window resolution
    black = (0, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            # enables closing the window
        screen.fill(black)
        for item in updatable:
            item.update(dt)
        for ast in asteroids:
            if ast.is_colliding(player):
                print('Game Over!')
                exit()
            if ast.is_colliding(shot):
                shot.kill()
                ast.kill()
        for item in drawable:
            item.draw(screen)
# draw player before flip screen, but after screen draw
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
# dt updating to delta time, limiting frame rate
# for resource efficiency



if __name__ == "__main__":
    main()
# this line ensures the main() function is only called
# when this file is run directly; it won't run if it's
# imported as a module.