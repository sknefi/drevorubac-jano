import pygame

class HitSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((120, 120), pygame.SRCALPHA)  # Create a surface with alpha transparency
        self.rect = self.image.get_rect()

    def update(self):
        pass

    def attack(self):
        self.image = pygame.Surface((120, 120), pygame.SRCALPHA)  # Create a surface with alpha transparency
        self.image.fill((255, 0, 0, 64))

    def stop_attacking(self):
        self.image = pygame.Surface((120, 120), pygame.SRCALPHA)  # Create a surface with alpha transparency
