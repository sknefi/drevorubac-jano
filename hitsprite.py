# hit_sprite.py
import pygame

class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height, scale_width, scale_height):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (scale_width, scale_height))
        return image

    def get_circular_image(self, x, y, width, height, scale_width, scale_height):
        image = self.get_image(x, y, width, height, scale_width, scale_height)
        circular_image = pygame.Surface((scale_width, scale_height), pygame.SRCALPHA)
        pygame.draw.ellipse(circular_image, (255, 255, 255), circular_image.get_rect())
        circular_image.blit(image, (0, 0), None, pygame.BLEND_RGBA_MULT)
        return circular_image

class HitSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.frames = []
        self.frame_index = 0
        self.attacking = False
        self.animation_speed = 5
        self.animation_counter = 0

        # Load the sprite sheet
        sprite_sheet = Spritesheet('pixel_art/slashes1.png')

        # Assuming each frame in the sprite sheet is 100x100 pixels
        frame_width, frame_height = 100, 100

        # Extract frames from the sprite sheet (assuming a single row of frames)
        for i in range(10):  # Assuming there are 10 frames in the row
            frame = sprite_sheet.get_circular_image(i * 80, 0, frame_width, frame_height, frame_width, frame_height)
            self.frames.append(frame)

        # Initial image is an empty surface
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

    def update(self):
        if self.attacking:
            self.animation_counter += 1
            if self.animation_counter >= self.animation_speed:
                self.animation_counter = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.image = self.frames[self.frame_index]
        else:
            self.image = pygame.Surface((100, 100), pygame.SRCALPHA)

    def attack(self):
        self.attacking = True
        self.image = self.frames[self.frame_index]

    def stop_attacking(self):
        self.attacking = False
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
