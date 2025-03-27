import pygame
from game_settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE, FONT_COLOR, COLLECT_SOUND
from player import Player
from banana import Banana

# Initialize pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load background and sound
background = pygame.image.load(BACKGROUND_IMAGE)
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
collect_sound = pygame.mixer.Sound(COLLECT_SOUND)

# Set up font
font = pygame.font.Font(None, 50)  # Default font, size 50

# Create player and banana
player = Player(100, 100)
banana = Banana()

score = 0
running = True

while running:
    # Draw background image
    screen.blit(background, (0, 0))

    # Handle movement
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Draw player and banana
    player.draw(screen)
    banana.draw(screen)

    # Collision detection
    if player.rect.colliderect(banana.rect):
        score += 1
        banana.relocate()
        collect_sound.play()  # Play sound on banana collection

    # Display score on screen
    score_text = font.render(f"Score: {score}", True, FONT_COLOR)
    screen.blit(score_text, (20, 20))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
