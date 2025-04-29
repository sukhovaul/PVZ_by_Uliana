import pygame as pg

class Level_menu:
    def __init__(self, screen):
        self.screen = screen
        self.level_menu_image = pg.image.load('maps/level_menu.png')

    def draw(self):
        self.screen.blit(self.level_menu_image, (0,0))