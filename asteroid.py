import pygame
import random
from logger import log_event
from CircleShape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        speed_a = self.velocity.rotate(angle)
        speed_b = self.velocity.rotate(-angle)
        newradius = self.radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position.x, self.position.y, newradius)
        new_ast_2 = Asteroid(self.position.x, self.position.y, newradius)
        new_ast_1.velocity = speed_a * 1.2
        new_ast_2.velocity = speed_b * 1.2
