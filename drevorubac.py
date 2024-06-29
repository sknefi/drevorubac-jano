from settings import Game_setting
import pygame
class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, w, h):
        image = pygame.Surface((w,h))
        image.blit(self.spritesheet, (0,0), (x, y, w, h))
        return image


class Drevorubac(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.SPEED = 3
        self.SIZE = 70
        self.settings = Game_setting()
        sprite_sheet = Spritesheet('pixel_art/drevorubac.png')

        # Load idle animation frames
        self.idle_frames = [sprite_sheet.get_image(i * self.SIZE, 0, self.SIZE, self.SIZE) for i in range(6)]
        self.idle_flipped_frames = [pygame.transform.flip(frame, True, False) for frame in self.idle_frames]

        # Load walking animation frames
        self.walk_frames = [sprite_sheet.get_image(i * self.SIZE, 180, self.SIZE, self.SIZE) for i in range(6)]
        self.walk_flipped_frames = [pygame.transform.flip(frame, True, False) for frame in self.walk_frames]

        # Load attacking animation frames (for simplicity, using the same frames as walking)
        self.attack_frames = [sprite_sheet.get_image(i * self.SIZE, 260, self.SIZE, self.SIZE) for i in range(4)]
        self.attack_flipped_frames = [pygame.transform.flip(frame, True, False) for frame in self.attack_frames]

        self.current_frame = 0
        self.image = self.idle_frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2)

        self.is_moving = False
        self.is_attacking = False
        self.frame_delay = 5  # Number of updates before changing the frame
        self.update_count = 0
        self.facing_right = True

    def update(self):
        keys = pygame.key.get_pressed()
        self.is_moving = False

        if keys[pygame.K_a] and self.rect.x > 0:  # Move left
            self.rect.x -= self.SPEED
            self.is_moving = True
            if self.facing_right:
                self.facing_right = False
        elif keys[pygame.K_d] and self.rect.x < self.settings.screen_width - self.rect.width:  # Move right
            self.rect.x += self.SPEED
            self.is_moving = True
            if not self.facing_right:
                self.facing_right = True
        elif keys[pygame.K_w] and self.rect.y > 0:  # Move up
            self.rect.y -= self.SPEED
            self.is_moving = True
        elif keys[pygame.K_s] and self.rect.y < self.settings.screen_height - self.rect.height:  # Move down
            self.rect.y += self.SPEED
            self.is_moving = True

        if keys[pygame.K_SPACE] and not self.is_attacking:  # Start attack
            self.is_attacking = True
            self.current_frame = 0
            self.update_count = 0

        if self.is_attacking:
            self.update_count += 1
            if self.update_count >= self.frame_delay:
                self.current_frame += 1
                if self.current_frame >= len(self.attack_frames):
                    self.is_attacking = False
                    self.current_frame = 0
                self.update_count = 0
        elif self.is_moving:
            self.update_count += 1
            if self.update_count >= self.frame_delay:
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames)
                self.update_count = 0
        else:
            self.current_frame = 0
            self.update_count = 0

        if self.is_attacking:
            if self.facing_right:
                self.image = self.attack_frames[self.current_frame]
            else:
                self.image = self.attack_flipped_frames[self.current_frame]
        elif self.is_moving:
            if self.facing_right:
                self.image = self.walk_frames[self.current_frame]
            else:
                self.image = self.walk_flipped_frames[self.current_frame]
        else:
            if self.facing_right:
                self.image = self.idle_frames[self.current_frame]
            else:
                self.image = self.idle_flipped_frames[self.current_frame]