import pygame
from pygame import locals
pygame.init()
from constants import *
from ball import Ball
from paddle import Paddle
from inputs import handle_input

TICK_RATE = 30
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Pong Game")
clock = pygame.time.Clock()
done = [False]

ball = Ball()
left_paddle = Paddle()
left_paddle.rect.x = left_paddle.rect.x + 20
right_paddle = Paddle()
right_paddle.rect.x = SCREEN_WIDTH - right_paddle.rect.width


while not done[0]:
    clock.tick(TICK_RATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    handle_input(left_paddle, right_paddle)
    screen.fill(BLACK)
    ball.draw(screen)
    ball.update(left_paddle, right_paddle, done)
    left_paddle.draw(screen)
    right_paddle.draw(screen)

    pygame.display.flip()

pygame.quit()