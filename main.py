from constants import *
import pygame
# allows us to use code from open-source pygame library
# throughout this file

def main():
    pygame.init()
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
        pygame.display.flip()
        dt = clock.tick(60) / 1000
# dt updating to delta time, limiting frame rate
# for resource efficiency


if __name__ == "__main__":
    main()
# this line ensures the main() function is only called
# when this file is run directly; it won't run if it's
# imported as a module.