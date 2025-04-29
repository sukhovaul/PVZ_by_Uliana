import pygame as pg

class Level_menu:
    def __init__(self, screen):
        self.screen = screen
        self.level_menu_image = pg.image.load('maps/level_menu.png')

        self.level1_icon = pg.image.load('maps/level_icons/level1_icon.png')

        self.level1_icon_rect = self.level1_icon.get_rect(topleft=(100, 100))

        self.level = None

    def draw(self):
        self.screen.blit(self.level_menu_image, (0,0))

        self.screen.blit(self.level1_icon,(100,100))

    def run(self):
        self.draw()