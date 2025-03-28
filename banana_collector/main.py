import time

import pygame

from banana import Banana
from game_settings import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_SPEED, OBSTACLE_SPEED, TIMER_LIMIT
from obstacle import Obstacle
from speed_boost import SpeedBoost

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Monkey Banana Collector")

# Load assets
background = pygame.image.load("images/background.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
monkey_img = pygame.image.load("images/monkey.png")
monkey_rect = monkey_img.get_rect()
monkey_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Sounds
collect_sound = pygame.mixer.Sound("sounds/collect.mp3")
hit_sound = pygame.mixer.Sound("sounds/hit.mp3")
boost_sound = pygame.mixer.Sound("sounds/boost.mp3")

# Game variables
monkey_speed = BALL_SPEED
score = 0
level = 1
running = True

# Create game objects
bananas = [Banana() for _ in range(5)]
obstacles = [Obstacle() for _ in range(3)]
boosts = [SpeedBoost() for _ in range(1)]

# Timer setup
start_time = time.time()

# Speed boost tracking
boost_active = False
boost_timer = 0
BOOST_DURATION = 5

# Main game loop
clock = pygame.time.Clock()

while running:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and monkey_rect.left > 0:
        monkey_rect.x -= monkey_speed
    if keys[pygame.K_RIGHT] and monkey_rect.right < SCREEN_WIDTH:
        monkey_rect.x += monkey_speed
    if keys[pygame.K_UP] and monkey_rect.top > 0:
        monkey_rect.y -= monkey_speed
    if keys[pygame.K_DOWN] and monkey_rect.bottom < SCREEN_HEIGHT:
        monkey_rect.y += monkey_speed

    # Update game objects
    for banana in bananas:
        banana.draw(screen)
        if monkey_rect.colliderect(banana.rect):
            score += banana.get_points()
            collect_sound.play()
            bananas.remove(banana)
            bananas.append(Banana())

    for obstacle in obstacles:
        obstacle.move()
        obstacle.draw(screen)
        if monkey_rect.colliderect(obstacle.rect):
            score -= 1
            hit_sound.play()

    for boost in boosts:
        boost.draw(screen)
        if monkey_rect.colliderect(boost.rect):
            boost_active = True
            boost_timer = time.time()
            boost_sound.play()
            boosts.remove(boost)

    # Handle speed boost duration
    if boost_active and time.time() - boost_timer <= BOOST_DURATION:
        monkey_speed = BALL_SPEED + 5
    else:
        monkey_speed = BALL_SPEED

    # Increase difficulty at level-up
    if score >= level * 20:  # Level up every 20 points
        level += 1
        OBSTACLE_SPEED += 1
        bananas.append(Banana())
        obstacles.append(Obstacle())

    # Timer handling
    elapsed_time = int(time.time() - start_time)
    remaining_time = TIMER_LIMIT - elapsed_time
    if remaining_time <= 0:
        print(f"Game Over! Final Score: {score}")
        running = False

    # Draw everything
    screen.blit(background, (0, 0))
    screen.blit(monkey_img, monkey_rect)

    # Display Score and Timer
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    timer_text = font.render(f"Time: {remaining_time}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))

    screen.blit(score_text, (20, 20))
    screen.blit(timer_text, (20, 60))
    screen.blit(level_text, (20, 100))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
