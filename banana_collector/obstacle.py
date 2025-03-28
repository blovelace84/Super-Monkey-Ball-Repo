import pygame
import random

class Obstacle:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("images/rock.png")
        self.rect = self.image.get_rect()

        # Randomize position within screen bounds
        self.rect.x = random.randint(50, screen_width - 50)
        self.rect.y = random.randint(50, screen_height - 50)

        # Movement speed for obstacles
        self.speed = random.randint(1, 3)

    def move(self):
        # Example movement (move left and respawn if out of bounds)
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = random.randint(50, 800 - 50)  # Reappear on the right

    def draw(self, screen):
        screen.blit(self.image, self.rect)
