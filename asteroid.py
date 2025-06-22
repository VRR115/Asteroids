import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)

    def update(self, dt):
        self.position +=(self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius<= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            v1 = self.velocity.rotate(random_angle)
            v2 =self.velocity.rotate(-random_angle)
            r1 = self.radius - ASTEROID_MIN_RADIUS
            r2 =self.radius -ASTEROID_MIN_RADIUS

            x, y = self.position.x, self.position.y

            a1 = Asteroid(x, y, r1)
            a1.velocity = v1*1.2

            a2 = Asteroid(x, y, r2)
            a2.velocity = v2*1.2