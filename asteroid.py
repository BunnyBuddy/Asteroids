import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, PLAYER_SPEED
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super(). __init__(x, y, radius)
                
    def draw(self, screen):
        pygame.draw.circle(screen, "white" ,self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, dt):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(rand_angle)
        vector2 = self.velocity.rotate(-rand_angle)
        new_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid1.velocity = vector1 * 1.2
        new_asteroid2.velocity = vector2 * 1.2