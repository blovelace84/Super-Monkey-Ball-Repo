import pygame
import random
from game_settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Banana:
    def __init__(self):
        # Load the banana image
        self.image = pygame.image.load("images/banana.png")
        self.rect = self.image.get_rect(
            topleft=(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50))
        )

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def relocate(self):
        self.rect.x = random.randint(50, SCREEN_WIDTH - 50)
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 50)
