import pygame
from game_settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR
from player import Player
from banana import Banana

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Create player and banana
player = Player(100, 100)
banana = Banana()

score = 0
running = True

while running:
    screen.fill(BACKGROUND_COLOR)

    keys = pygame.key.get_pressed()
    player.move(keys)

    player.draw(screen)
    banana.draw(screen)

    # Check collision
    if player.rect.colliderect(banana.rect):
        score += 1
        banana.relocate()
        print(f"Score: {score}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
