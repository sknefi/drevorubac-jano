import pygame
import sys
from settings import Game_setting
from drevorubac import Drevorubac
from skeleton import Skeleton
from hitsprite import HitSprite

pygame.init()

settings = Game_setting()

screen_width = settings.screen_width
screen_height = settings.screen_height

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drevorubač Jano")

background_image = pygame.image.load('./pixel_art/bckground.png').convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Create instances of Drevorubac and Skeleton
skeleton = Skeleton()
drevorubac = Drevorubac([skeleton])
all_sprites = pygame.sprite.Group()
all_sprites.add(skeleton, drevorubac.hit_sprite, drevorubac)

# Font initialization
pygame.font.init()
font = pygame.font.SysFont('Arial', 24)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    # Draw everything
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    # Render and display statistics
    damage_text = font.render(f"Damage Given: {drevorubac.damage_given}", True, (255, 255, 255))
    kills_text = font.render(f"Kills: {drevorubac.kills}", True, (255, 255, 255))
    screen.blit(damage_text, (20, 20))
    screen.blit(kills_text, (20, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
