import pygame
import random
from banana import Banana
from obstacle import Obstacle
from speed_boost import SpeedBoost

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Monkey Banana Collector")

# Colors
WHITE = (255, 255, 255)

# Load assets
monkey_img = pygame.image.load("images/monkey.png")
background_img = pygame.image.load("images/background.jpg")

# Load sounds
pygame.mixer.init()
collect_sound = pygame.mixer.Sound("sounds/collect.mp3")
hit_sound = pygame.mixer.Sound("sounds/hit.mp3")
boost_sound = pygame.mixer.Sound("sounds/boost.mp3")

# Sound channels (to prevent overlapping sounds)
collect_channel = pygame.mixer.Channel(0)
hit_channel = pygame.mixer.Channel(1)
boost_channel = pygame.mixer.Channel(2)

# Monkey setup
monkey_rect = monkey_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
monkey_speed = 5

# Object lists (Bananas, Obstacles, Speed Boosts)
bananas = [Banana(SCREEN_WIDTH, SCREEN_HEIGHT) for _ in range(5)]
obstacles = [Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT) for _ in range(3)]
boosts = [SpeedBoost(SCREEN_WIDTH, SCREEN_HEIGHT) for _ in range(1)]

# Score and timer
score = 0
time_left = 60  # Countdown in seconds
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get user input for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        monkey_rect.x -= monkey_speed
    if keys[pygame.K_RIGHT]:
        monkey_rect.x += monkey_speed
    if keys[pygame.K_UP]:
        monkey_rect.y -= monkey_speed
    if keys[pygame.K_DOWN]:
        monkey_rect.y += monkey_speed

    # Keep monkey within bounds
    monkey_rect.x = max(0, min(SCREEN_WIDTH - monkey_rect.width, monkey_rect.x))
    monkey_rect.y = max(0, min(SCREEN_HEIGHT - monkey_rect.height, monkey_rect.y))

    # Collision detection with bananas
    for banana in bananas[:]:
        if monkey_rect.colliderect(banana.rect):
            score += banana.points
            bananas.remove(banana)
            bananas.append(Banana(SCREEN_WIDTH, SCREEN_HEIGHT))
            if not collect_channel.get_busy():
                collect_channel.play(collect_sound)

    # Collision detection with obstacles
    for obstacle in obstacles[:]:
        if monkey_rect.colliderect(obstacle.rect):
            score -= 3  # Lose points
            obstacles.remove(obstacle)
            obstacles.append(Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT))
            if not hit_channel.get_busy():
                hit_channel.play(hit_sound)

    # Collision detection with speed boosts
    for boost in boosts[:]:
        if monkey_rect.colliderect(boost.rect):
            monkey_speed += 2  # Temporary speed boost
            boosts.remove(boost)
            boosts.append(SpeedBoost(SCREEN_WIDTH, SCREEN_HEIGHT))
            if not boost_channel.get_busy():
                boost_channel.play(boost_sound)

    # Countdown timer
    time_left -= clock.get_time() / 1000
    if time_left <= 0:
        running = False

    # Draw everything
    screen.blit(background_img, (0, 0))  # Background
    screen.blit(monkey_img, monkey_rect)  # Monkey

    for banana in bananas:
        banana.draw(screen)

    for obstacle in obstacles:
        obstacle.draw(screen)
        obstacle.draw(screen)

    for boost in boosts:
        boost.draw(screen)

    # Display score and timer
    score_text = font.render(f"Score: {score}", True, WHITE)
    timer_text = font.render(f"Time: {int(time_left)}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(timer_text, (10, 50))

    # Debugging (Track object counts and score)
    print(f"Bananas: {len(bananas)}, Obstacles: {len(obstacles)}, Boosts: {len(boosts)}, Score: {score}")

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS

pygame.quit()

