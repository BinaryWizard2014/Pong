import pygame
from constants import *

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(0, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.SPEED = 10

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)

    def move_up(self):
        self.rect.y -= self.SPEED
        self._keep_in_bounds()

    def move_down(self):
        self.rect.y += self.SPEED
        self._keep_in_bounds()

    def _keep_in_bounds(self):
        self.rect.y = min(self.rect.y, SCREEN_HEIGHT - self.rect.height)
        self.rect.y = max(0, self.rect.y)