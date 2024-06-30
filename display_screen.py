import pygame
from settings import Game_setting

class Display_screen:
    def __init__(self, screen):
        self.screen = screen
        self.settings = Game_setting()
        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height

    def change_state(self, state):
        self.state = state

    def intro_screen(self):
        # Display information screen
        self.screen.fill((0, 128, 0))  # Fill screen with green
        font = pygame.font.SysFont('Arial', 24)
        title_text = font.render("Drevorubač Jano!", True, (255, 255, 255))
        info1_text = font.render("Nefunguje ti kód?", True, (255, 255, 255))
        info2_text = font.render("Nevieš si zapamätať vzorec na Taylorov polynom?", True, (255, 255, 255))
        info3_text = font.render("Stále nechápeš aký je rozdiel medzi Frontendom a Backendom?", True, (255, 255, 255))
        info4_text = font.render("Nevieš dostať do hlavy ako funguje useContex a useProvider?", True, (255, 255, 255))
        info5_text = font.render("POTOM JE TU RIEŠENIE", True, (255, 255, 255))
        start_text = font.render("Stlač SPACE a poď odreagovať", True, (255, 255, 255))

        # Position the texts on the screen
        self.screen.blit(title_text, ((self.screen_width - title_text.get_width()) // 2, self.screen_height // 4))
        self.screen.blit(info1_text, ((self.screen_width - info1_text.get_width()) // 2, self.screen_height // 2 - 80))
        self.screen.blit(info2_text, ((self.screen_width - info2_text.get_width()) // 2, self.screen_height // 2 - 40))
        self.screen.blit(info3_text, ((self.screen_width - info3_text.get_width()) // 2, self.screen_height // 2))
        self.screen.blit(info4_text, ((self.screen_width - info4_text.get_width()) // 2, self.screen_height // 2 + 40))
        self.screen.blit(info5_text, ((self.screen_width - info5_text.get_width()) // 2, self.screen_height // 2 + 80))
        self.screen.blit(start_text, ((self.screen_width - start_text.get_width()) // 2, self.screen_height // 2 + 160))

    def title_screen(self):
        # Display title screen
        self.screen.fill((0, 128, 0))  # Fill screen with green
        font = pygame.font.SysFont('Arial', 24)
        title_text = font.render("Drevorubač Jano!", True, (255, 255, 255))
        info1_text = font.render("Táto hra nie je o rúbani stromov...", True, (255, 255, 255))
        info2_text = font.render("Zabi skeletonov a získaj body", True, (255, 255, 255))
        controller_text = font.render("Controller: W A S D", True, (255, 255, 255))
        attack_text = font.render("Attack: SPACE", True, (255, 255, 255))
        info_text = font.render("Stlač SPACE a poď odreagovať", True, (255, 255, 255))

        # Position the texts on the screen
        self.screen.blit(title_text, ((self.screen_width - title_text.get_width()) // 2, self.screen_height // 4))
        self.screen.blit(controller_text, ((self.screen_width - controller_text.get_width()) // 2, self.screen_height // 2))
        self.screen.blit(attack_text, ((self.screen_width - attack_text.get_width()) // 2, (self.screen_height // 2) + 40))
        self.screen.blit(info_text, ((self.screen_width - info_text.get_width()) // 2, (self.screen_height // 2) + 160))

    def gaming_screen(self, drevorubac):
        font = pygame.font.SysFont('Arial', 24)
        kills_text = font.render(f"Kills: {drevorubac.kills}", True, (255, 255, 255))
        damage_text = font.render(f"Damage Given: {drevorubac.damage_given}", True, (255, 255, 255))
        self.screen.blit(damage_text, (20, 20))
        self.screen.blit(kills_text, (20, 50))