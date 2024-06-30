# skeleton.py

import pygame
import random
from settings import Game_setting

class Skeleton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        settings = Game_setting()
        self.screen_width = settings.screen_width
        self.screen_height = settings.screen_height

        self.load_spritesheet('./pixel_art/skeleton1.png', 60, 70)

        self.rect.x = random.randint(0, self.screen_width - self.rect.width)
        self.rect.y = random.randint(0, self.screen_height - self.rect.height)

        self.speed = 2
        self.change_direction_delay = 60
        self.update_count = 0
        self.direction = random.choice(['left', 'right', 'up', 'down'])

        self.frame_delay = 12
        self.current_frame = 0

        self.health = 100

    def load_spritesheet(self, filename, width, height):
        self.spritesheet = pygame.image.load(filename).convert_alpha()
        self.sprite_width = width
        self.sprite_height = height

        # based on movement set animation
        self.idle_frame = self.get_image(0, 0, width, height)
        self.walk_frames_right = [self.get_image(width * i, 0, width, height) for i in range(6)]
        self.walk_frames_left = [pygame.transform.flip(frame, True, False) for frame in self.walk_frames_right]
        self.walk_frames_up = [self.get_image(width * i, 0, width, height) for i in range(6)]
        self.walk_frames_down = [self.get_image(width * i, 0, width, height) for i in range(6)]

        self.image = self.idle_frame
        self.rect = self.image.get_rect()

    def get_image(self, x, y, w, h):
        image = pygame.Surface((w, h), pygame.SRCALPHA).convert_alpha()
        image.blit(self.spritesheet, (0, 0), (x, y, w, h))
        return image

    def update(self):
        self.update_count += 1

        if self.update_count >= self.change_direction_delay:
            self.direction = random.choice(['left', 'right', 'up', 'down'])
            self.update_count = 0

        if self.update_count % self.frame_delay == 0:
            if self.direction == 'left':
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_left)
                self.image = self.walk_frames_left[self.current_frame]
            elif self.direction == 'right':
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_right)
                self.image = self.walk_frames_right[self.current_frame]
            elif self.direction == 'up':
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_up)
                self.image = self.walk_frames_up[self.current_frame]
            elif self.direction == 'down':
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_down)
                self.image = self.walk_frames_down[self.current_frame]

        if self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed

        self.rect.x = max(0, min(self.rect.x, self.screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, self.screen_height - self.rect.height))

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()  # KILLED skeleton

