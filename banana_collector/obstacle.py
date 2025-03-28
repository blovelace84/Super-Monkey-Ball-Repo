# obstacle.py
import pygame
import random
from game_settings import SCREEN_WIDTH, SCREEN_HEIGHT, OBSTACLE_SPEED

class Obstacle:
    def __init__(self):
        self.type = random.choice(["rock", "snake"])
        self.image = pygame.image.load(f"images/{self.type}.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -50  # Spawn above the screen

    def move(self):
        self.rect.y += OBSTACLE_SPEED
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -50
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
