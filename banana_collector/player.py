import pygame
from game_settings import BALL_SPEED

class Player:
    def __init__(self, x, y):
        # Load the monkey image
        self.image = pygame.image.load("images/player.png")
        self.rect = self.image.get_rect(topleft=(x, y))

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= BALL_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += BALL_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= BALL_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += BALL_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)
