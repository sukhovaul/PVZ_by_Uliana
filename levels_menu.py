import pygame as pg

class Level_menu:
    def __init__(self, screen):
        self.screen = screen
        self.level_menu_image = pg.image.load('maps/level_menu.png')
        self.level_menu_image = pg.transform.scale(self.level_menu_image, (1400,600))

        self.level1_icon = pg.image.load('maps/level_icons/level1_icon.png')
        self.level2_icon = pg.image.load('maps/level_icons/level2_icon.png')
        self.level3_icon = pg.image.load('maps/level_icons/level3_icon.png')
        self.level4_icon = pg.image.load('maps/level_icons/level4_icon.png')
        self.level4_icon = pg.transform.scale(self.level4_icon, (182, 259))

        self.level2_blocked_icon = pg.image.load('maps/level_icons/level2_locked.png')
        self.level3_blocked_icon = pg.image.load('maps/level_icons/level3_locked.png')
        self.level4_blocked_icon = pg.image.load('maps/level_icons/Level1-4Locked.png')

        self.level1_icon_rect = self.level1_icon.get_rect(topleft=(100, 100))
        self.level2_icon_rect = self.level2_icon.get_rect(topleft=(350, 100))
        self.level3_icon_rect = self.level3_icon.get_rect(topleft=(600, 100))
        self.level4_icon_rect = self.level4_icon.get_rect(topleft=(850, 100))

        self.level = None
        self.level2_availible = False
        self.level3_availible = False
        self.level4_availible = False

    def draw(self):
        self.screen.blit(self.level_menu_image, (0,0))

        self.screen.blit(self.level1_icon, (100, 100))
        self.screen.blit(self.level2_blocked_icon, (350, 100))
        self.screen.blit(self.level3_blocked_icon, (600, 100))
        self.screen.blit(self.level4_blocked_icon, (850, 100))

        if self.level2_availible:
            self.screen.blit(self.level2_icon, (350, 100))

        if self.level3_availible:
            self.screen.blit(self.level3_icon, (600, 100))

        if self.level4_availible:
            self.screen.blit(self.level4_icon, (850, 100))

    def run(self):
        self.draw()