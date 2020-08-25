import pygame
from constants import *

class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.SPEED = 5
        self.vx = self.SPEED
        self.vy = self.SPEED
        self.radius = 10

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

    def update(self, left_paddle, right_paddle, done):
        self.x += self.vx
        self.y += self.vy

        if self.y > SCREEN_HEIGHT - self.radius * 2:
            self.vy *= -1

        if self.y < self.radius * 2:
            self.vy *= -1

        if self.x < self.radius * 2:
            done[0] = True

        if self.x > SCREEN_WIDTH - self.radius * 2:
            done[0] = True

        if self.get_rect().colliderect(right_paddle.rect):
            self.vx *= -1

        if self.get_rect().colliderect(left_paddle.rect):
            self.vx *= -1
