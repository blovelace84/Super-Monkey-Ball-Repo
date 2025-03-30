import pygame
import random
from banana import Banana
from obstacle import Obstacle

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Load player (monkey)
monkey = pygame.image.load("images/monkey.png")
monkey_rect = monkey.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Initialize first banana and obstacle
current_banana = Banana(SCREEN_WIDTH, SCREEN_HEIGHT)
current_obstacle = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT)

# Game variables
score = 0
obstacle_timer = 0
OBSTACLE_DELAY = 100  # Time before a new obstacle spawns

running = True
while running:
    screen.fill((255, 255, 255))  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement (arrow keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        monkey_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        monkey_rect.x += 5
    if keys[pygame.K_UP]:
        monkey_rect.y -= 5
    if keys[pygame.K_DOWN]:
        monkey_rect.y += 5

    # 🟡 Check for banana collection
    if monkey_rect.colliderect(current_banana.rect):
        score += 1  # Increase score
        current_banana = Banana(SCREEN_WIDTH, SCREEN_HEIGHT)  # Spawn new banana

    # 🪨 Obstacle delay before appearing
    obstacle_timer += 1
    if obstacle_timer > OBSTACLE_DELAY:
        current_obstacle = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT)
        obstacle_timer = 0  # Reset timer

    # Draw everything
    screen.blit(monkey, monkey_rect)
    current_banana.draw(screen)
    current_obstacle.draw(screen)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)  # Control FPS

pygame.quit()
