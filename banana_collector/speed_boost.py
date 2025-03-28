import pygame

class SpeedBoost:
    def __init__(self, x, y):
        self.image = pygame.image.load("images/speed_boost.png")
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

