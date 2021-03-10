from math import cos, sin, radians
import random

import pygame
import sys


def score_display(score_left, score_right):
    score_left_surface = game_font.render('%02d' % score_left, True, (255, 255, 255))
    score_left_rect = score_left_surface.get_rect(center=(300, 50))
    screen.blit(score_left_surface, score_left_rect)
    score_right_surface = game_font.render('%02d' % score_right, True, (255, 255, 255))
    score_right_rect = score_right_surface.get_rect(center=(900, 50))
    screen.blit(score_right_surface, score_right_rect)


def do_it():
    # Game vars
    game_active = False
    score_left = 0
    score_right = 0
    vel = 15
    angle = 90
    bx = 600
    by = 400
    max_bounce = 60

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_active:
            # Movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                paddle_right_rect.centery -= 20
            if keys[pygame.K_DOWN]:
                paddle_right_rect.centery += 20
            if keys[pygame.K_w]:
                paddle_left_rect.centery -= 20
            if keys[pygame.K_s]:
                paddle_left_rect.centery += 20

            # Ball Movement
            if ball_rect.bottom >= 800 or ball_rect.top <= 0:
                angle = 180 - angle

            if ball_rect.colliderect(paddle_right_rect):
                angle = 90 - (((ball_rect.centery - paddle_right_rect.centery) / 75.0) * max_bounce)
                angle = -angle

            if ball_rect.colliderect(paddle_left_rect):
                angle = 90 - (((ball_rect.centery - paddle_left_rect.centery) / 75.0) * max_bounce)

            bx = bx + vel * sin(radians(angle))
            by = by + vel * cos(radians(angle))
            ball_rect.centerx = int(bx)
            ball_rect.centery = int(by)

            # Draw
            screen.blit(bg_surface, (0, 0))
            screen.blit(paddle_left, paddle_left_rect)
            screen.blit(paddle_right, paddle_right_rect)
            screen.blit(ball, ball_rect)

            if ball_rect.centerx >= 1300:
                score_left += 1
                game_active = False

            if ball_rect.centerx <= -100:
                score_right += 1
                game_active = False

            score_display(score_left, score_right)
        else:
            ball_rect.center = (600, 400)
            bx = 600
            by = 400
            vel = 15
            if random.randint(0, 10) < 5:
                angle = 90
            else:
                angle = -90

            paddle_left_rect.centery = 400
            paddle_right_rect.centery = 400
            game_active = True
            pygame.time.wait(1000)

        pygame.display.update()
        clock.tick(120)


pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19__.TTF', 100)

# Paddles
paddle_left = pygame.image.load('paddle.png').convert_alpha()
paddle_left_rect = paddle_left.get_rect(center=(50, 400))
paddle_right = pygame.image.load('paddle.png').convert_alpha()
paddle_right_rect = paddle_right.get_rect(center=(1150, 400))

bg_surface = pygame.image.load('background.png')

# Ball
ball = pygame.image.load('Screenshot_2.png').convert_alpha()
ball_rect = ball.get_rect(center=(600, 400))

INCREASEVELOCITY = pygame.USEREVENT
pygame.time.set_timer(INCREASEVELOCITY, 1000)

do_it()
