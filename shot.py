from circleshape import CircleShape
import pygame
from constants import *
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)
        
    
    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)