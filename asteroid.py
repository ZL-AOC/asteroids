from circleshape import *
import pygame
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        old_radius = self.radius
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50)
        split_1 = self.velocity.rotate(new_angle)
        split_2 = self.velocity.rotate(-new_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_1.velocity = split_1 * 1.2
        new_ast_2.velocity = split_2 * 1.2
