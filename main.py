import pygame
import sys
from settings import Game_setting
from drevorubac import Drevorubac
from skeleton import Skeleton
from display_screen import Display_screen
from skeleton_spawner import SkeletonSpawner

pygame.init()

settings = Game_setting()

screen_width = settings.screen_width
screen_height = settings.screen_height

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drevorubač Jano")

background_image = pygame.image.load('./pixel_art/bckground1.png').convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Create initial skeletons
skeleton = Skeleton()
skeleton1 = Skeleton()
drevorubac = Drevorubac([skeleton, skeleton1])

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(skeleton, skeleton1, drevorubac.hit_sprite, drevorubac)

# Create skeleton spawner
skeleton_spawner = SkeletonSpawner(all_sprites, drevorubac)

pygame.font.init()
font = pygame.font.SysFont('Arial', 24)
clock = pygame.time.Clock()

# DISPLAY SCREEN
SHOW_INFO_SCREEN = 0
SHOW_TITLE_SCREEN = 1
PLAYING_GAME = 2

display_screen = Display_screen(screen)

current_state = SHOW_INFO_SCREEN

while True:
    dt = clock.tick(60)  # dt is the time since the last frame in milliseconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if current_state == SHOW_INFO_SCREEN:
                if event.key == pygame.K_SPACE:
                    current_state = SHOW_TITLE_SCREEN
            elif current_state == SHOW_TITLE_SCREEN:
                if event.key == pygame.K_SPACE:
                    current_state = PLAYING_GAME

    if current_state == SHOW_INFO_SCREEN:
        display_screen.intro_screen()
    elif current_state == SHOW_TITLE_SCREEN:
        display_screen.title_screen()
    elif current_state == PLAYING_GAME:
        # Update all sprites and spawner
        all_sprites.update()
        skeleton_spawner.update(dt)

        # Draw everything
        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)

        # Render and display statistics
        display_screen.gaming_screen(drevorubac)

    pygame.display.flip()
