import pygame
import sys
from settings import Game_setting
from drevorubac import Drevorubac
from hitsprite import HitSprite

pygame.init()

settings = Game_setting()

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption("Drevorubač Jano")

background_image = pygame.image.load('./pixel_art/bckground.png').convert()
background_image = pygame.transform.scale(background_image, (settings.screen_width, settings.screen_height))

drevorubac = Drevorubac()
#drevorubac1 = Drevorubac()
all_sprites = pygame.sprite.Group()
all_sprites.add(drevorubac)  # Add Drevorubac to sprite group
all_sprites.add(drevorubac.hit_sprite)  # Add HitSprite to sprite group

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    # Draw everything
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()