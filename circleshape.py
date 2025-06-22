import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass
    
    def colisionCheck(self,anotherCircle):
        distance = pygame.math.Vector2.distance_to(self.position, anotherCircle.position)
        if distance > (self.radius + anotherCircle.radius):
            return False
        else:
            return True


