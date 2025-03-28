import pygame
import random


class Banana:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("images/regular_banana.png")
        self.rect = self.image.get_rect()

        # Set random position within screen bounds
        self.rect.x = random.randint(50, screen_width - 50)
        self.rect.y = random.randint(50, screen_height - 50)

        # Randomize points for banana types (regular, golden, rotten)
        self.points = random.choice([1, 5, -2])

    def draw(self, screen):
        screen.blit(self.image, self.rect)

