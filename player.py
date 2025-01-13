from constants import *
from circleshape import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
# Player only needs x, y, but CircleShape has a radius parameter. 
# forcing PLAYER_RADIUS as a constant for Player class
        self.rotation = 0
        self.x = x
        self.y = y
        self.cooldown_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.polygon(screen, white, self.triangle(), 2) # draws player based on calculations of triangle() method

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown_timer -= dt
        if keys[pygame.K_a]: # rotate left when 'a' key is pressed
            self.rotate(dt * -1)
        if keys[pygame.K_d]: # rotate right when 'd' key is pressed
            self.rotate(dt)
        if keys[pygame.K_w]: # move player sprite forward when 'w' key is pressed
            self.move(dt)
        if keys[pygame.K_s]: # move player sprite backward when 's' key is pressed
            self.move(dt * -1)
        if keys[pygame.K_SPACE] and self.cooldown_timer <= 0: # calls shoot method, spawning projectile at player's position and rotation
            self.shoot(dt)
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # set method for when keys are pressed to move forward or backward
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self, dt):
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED # Creates a new shot object at the player's current position
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = shot_velocity # set shot velocity based on current player's direction/rotation
        self.cooldown_timer = 0.3
        
