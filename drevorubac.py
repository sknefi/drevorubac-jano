import pygame
from settings import Game_setting
from hitsprite import HitSprite

class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height, scale_width=None, scale_height=None):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        if scale_width and scale_height:
            image = pygame.transform.scale(image, (scale_width, scale_height))
        return image

class Drevorubac(pygame.sprite.Sprite):
    def __init__(self, all_skeletons):
        super().__init__()
        self.SPEED = 3
        self.SIZE = 70
        self.settings = Game_setting()
        sprite_sheet = Spritesheet('pixel_art/drevorubac1.png')

        # STANDING animation
        self.idle_frame = sprite_sheet.get_image(0, 0, self.SIZE, self.SIZE, self.SIZE, self.SIZE)
        self.idle_flipped_frame = pygame.transform.flip(self.idle_frame, True, False)

        # WALKING animation
        self.walk_frames = [sprite_sheet.get_image(i * self.SIZE, 180, self.SIZE, self.SIZE, self.SIZE, self.SIZE) for i in range(6)]
        self.walk_flipped_frames = [pygame.transform.flip(frame, True, False) for frame in self.walk_frames]

        # ATTACKING animation
        self.attack_frames = [sprite_sheet.get_image(i * self.SIZE, 260, self.SIZE, self.SIZE, self.SIZE, self.SIZE) for i in range(4)]
        self.attack_flipped_frames = [pygame.transform.flip(frame, True, False) for frame in self.attack_frames]

        self.current_frame = 0
        self.image = self.idle_frame
        self.rect = self.image.get_rect()
        self.rect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2)

        self.is_moving = False
        self.is_attacking = False
        self.frame_delay = 4
        self.update_count = 0
        self.facing_right = True
        self.attack_delay = 3

        self.hit_sprite = HitSprite()
        self.hit_sprite.rect.center = self.rect.center

        self.all_skeletons = all_skeletons
        self.damage_given = 0
        self.kills = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.is_moving = False

        # this must be here, because as parameter in update it doesn't work, idk why
        self.hit_sprite.rect.center = self.rect.center

        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.SPEED
            self.is_moving = True
            if self.facing_right:
                self.facing_right = False
        if keys[pygame.K_d] and self.rect.x < self.settings.screen_width - self.rect.width:
            self.rect.x += self.SPEED
            self.is_moving = True
            if not self.facing_right:
                self.facing_right = True
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.SPEED
            self.is_moving = True
        if keys[pygame.K_s] and self.rect.y < self.settings.screen_height - self.rect.height:
            self.rect.y += self.SPEED
            self.is_moving = True

        if keys[pygame.K_SPACE] and not self.is_attacking:
            self.is_attacking = True
            self.current_frame = 0
            self.update_count = 0
            self.hit_sprite.attack()

            # KOLISIONS
            for skeleton in self.all_skeletons:
                if pygame.sprite.collide_rect(self.hit_sprite, skeleton):
                    skeleton.hit(10)  # damage
                    self.damage_given += 10
                    if skeleton.health <= 0:
                        self.kills += 1
                        self.all_skeletons.remove(skeleton)

        if not keys[pygame.K_SPACE] and not self.is_attacking:
            self.hit_sprite.stop_attacking()

        # HITSPRITE
        if self.is_attacking:
            self.update_count += 1
            if self.update_count >= self.attack_delay:
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
                self.image = self.idle_frame
            else:
                self.image = self.idle_flipped_frame
