# speed_boost.py
import pygame
import random
from game_settings import SCREEN_WIDTH, SCREEN_HEIGHT

class SpeedBoost:
    def __init__(self):
        self.image = pygame.image.load("images/speed_boost.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

