import pygame
import random

class Obstacle:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("images/rock.png")
        self.rect = self.image.get_rect()

        # Randomize a fixed position within the screen bounds
        self.rect.x = random.randint(50, screen_width - 50)
        self.rect.y = random.randint(50, screen_height - 50)

    def draw(self, screen):
        screen.blit(self.image, self.rect)