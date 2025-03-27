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
        self.scale = 1.0 #scale for pulsing animation
        self.grow = True

    def draw(self, screen):
        # banana pulsing animation
        if self.grow:
            self.scale += 0.01
            if self.scale >= 1.3:
                self.grow = False
        else:
            self.scale -= 0.01
            if self.scale <= 1.0:
                self.grow = True

        # Resize the banana image
        scaled_image = pygame.transform.scale(
            self.image,
            (int(self.rect.width * self.scale), int(self.rect.height * self.scale))
        )

        screen.blit(scaled_image, self.rect)

    def relocate(self):
        self.rect.x = random.randint(50, SCREEN_WIDTH -50)
        self.rect.y = random.randint(50, SCREEN_HEIGHT -50)