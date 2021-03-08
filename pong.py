import pygame
import sys


def score_display():
    score_left_surface = game_font.render('%02d' % score_left, True, (255,255,255))
    score_left_rect = score_left_surface.get_rect(center = (300, 50))
    screen.blit(score_left_surface, score_left_rect)
    score_right_surface = game_font.render('%02d' % score_right, True, (255,255,255))
    score_right_rect =score_right_surface.get_rect(center = (900, 50))
    screen.blit(score_right_surface, score_right_rect)

pygame.init()

screen = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19__.TTF', 100)


# Paddles
paddle_left = pygame.image.load('paddle.png').convert_alpha()
paddle_left_rect = paddle_left.get_rect(center = (50, 400))
paddle_right = pygame.image.load('paddle.png').convert_alpha()
paddle_right_rect = paddle_right.get_rect(center = (1150, 400))

bg_surface = pygame.image.load('background.png')

# Ball
ball = pygame.image.load('Screenshot_2.png').convert_alpha()
ball_rect = ball.get_rect(center=(600,400))
ball_x_velocty = 15
ball_y_velocity = 15

INCREASEVELOCITY = pygame.USEREVENT
pygame.time.set_timer(INCREASEVELOCITY, 1000)

# Game vars
game_active = True
score_left = 0
score_right = 0

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
            ball_y_velocity = -ball_y_velocity

        if ball_rect.colliderect(paddle_right_rect):
            ball_x_velocty = -ball_x_velocty


        if ball_rect.colliderect(paddle_left_rect):
            ball_x_velocty = -ball_x_velocty

        ball_rect.centerx += ball_x_velocty
        ball_rect.centery += ball_y_velocity

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

        score_display()
    else:
        ball_rect.center = (600,400)
        paddle_left_rect.centery = 400
        paddle_right_rect.centery = 400
        game_active = True
        pygame.time.wait(1000)

    pygame.display.update()
    clock.tick(120)