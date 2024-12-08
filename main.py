from constants import *
import pygame
# allows us to use code from open-source pygame library
# throughout this file

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0,0,0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
        pygame.display.flip()

if __name__ == "__main__":
    main()
# this line ensures the main() function is only called
# when this file is run directly; it won't run if it's
# imported as a module.