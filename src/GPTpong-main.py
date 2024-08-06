import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random

# Initialize Pygame
pygame.init()
os.system("cls")

# Constants for screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GPTpong")
window_icon = pygame.image.load("img/GPTpong.png")
pygame.display.set_icon(window_icon)

# Paddle attributes
"GPTpong.pyw" [dos] 122L, 3837B
import pygame
import random
import os

# Initialize Pygame
pygame.init()
os.system("cls")

# Constants for screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GPTpong")
window_icon = pygame.image.load("C:/Users/vivek/Documents/images/GPTpong.png")
pygame.display.set_icon(window_icon)

# Paddle attributes
paddle_width = 15
paddle_height = 100
left_paddle_x = 30
right_paddle_x = WIDTH - 30 - paddle_width
left_paddle_y = (HEIGHT - paddle_height) // 2
right_paddle_y = (HEIGHT - paddle_height) // 2
paddle_speed = 5

# Ball attributes
ball_size = 20
ball_x = WIDTH // 2 - ball_size // 2
ball_y = HEIGHT // 2 - ball_size // 2
ball_speed_x = 10 * random.choice((1, -1))
ball_speed_y = 10 * random.choice((1, -1))

# Score variables
left_score = 0
right_score = 0

# Create fonts for displaying the score
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle_y = max(0, left_paddle_y - paddle_speed)
    if keys[pygame.K_s]:
        left_paddle_y = min(HEIGHT - paddle_height, left_paddle_y + paddle_speed)
    if keys[pygame.K_UP]:
        right_paddle_y = max(0, right_paddle_y - paddle_speed)
    if keys[pygame.K_DOWN]:
        right_paddle_y = min(HEIGHT - paddle_height, right_paddle_y + paddle_speed)
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT - ball_size:
        ball_speed_y *= -1

    # Ball collision with paddles
    if (
        ball_x <= left_paddle_x + paddle_width
        and left_paddle_y <= ball_y <= left_paddle_y + paddle_height
    ) or (
        ball_x >= right_paddle_x
        and right_paddle_y <= ball_y <= right_paddle_y + paddle_height
    ):
        ball_speed_x *= -1

    # Ball out of bounds (score)
    if ball_x < 0:
        right_score += 1
        ball_x = WIDTH // 2 - ball_size // 2
        ball_y = HEIGHT // 2 - ball_size // 2
        ball_speed_x = 5 * random.choice((1, -1))
        ball_speed_y = 5 * random.choice((1, -1))
    elif ball_x > WIDTH:
        left_score += 1
        ball_x = WIDTH // 2 - ball_size // 2
        ball_y = HEIGHT // 2 - ball_size // 2
        ball_speed_x = 5 * random.choice((1, -1))
        ball_speed_y = 5 * random.choice((1, -1))

    # Clear the screen
    screen.fill(WHITE)

    # Draw paddles and ball
    pygame.draw.rect(screen, BLACK, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, BLACK, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, BLACK, (ball_x, ball_y, ball_size, ball_size))

    # Draw the score
    left_text = font.render(str(left_score), True, BLACK)
    right_text = font.render(str(right_score), True, BLACK)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (3 * WIDTH // 4 - left_text.get_width(), 20))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
