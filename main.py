import pygame as pg
import pytmx
from settings import *
import main_menu
import suns
import cells
import plants
import zombies
import levels_menu

pg.init()
pg.mixer.init()

class Game:
    def __init__(self):
        self.time = None
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('Plants vs Zombies')

        self.tmx_map = pytmx.load_pygame('maps/level1.tmx')
        self.map = 'main_menu'

        self.main_menu = main_menu.Menu(SCREEN_WIDTH, SCREEN_HEIGHT, 'maps/MainMenu.png')
        self.levels_menu = levels_menu.Level_menu(self.screen)

        self.clock = pg.time.Clock()

        self.suns_count = pg.image.load('pictures/suns_count.png')
        self.suns_count_rect = pg.Surface((54, 21))
        self.suns_count_rect.fill((227, 203, 170))
        self.amount_font = pg.font.Font('fonts/main_font.ttf', 20)

        self.run()

    def init_level(self, level_num):
        self.tmx_map = pytmx.load_pygame(f'maps/level{level_num}.tmx')
        self.sun = suns.Sun(self.screen)
        self.cells = cells.Cells(self.tmx_map, self.screen)
        self.plants = plants.Plants(self.screen)
        self.zombies_1 = zombies.Zombies(level_num, self.screen)

    def run(self):
        running = True
        self.time = 0
        while running:
            self.clock.tick(60)  # устанавливаем 60 fps
            self.time += 1
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.map == 'level1':
                self.sun.check_click(event.pos)
                self.cells.fill_cell(event.pos, self.plants, self.plants.plant_amount, self.sun)
                self.plants.choose_plant(event.pos)

            elif self.map == 'levels_menu' and event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.levels_menu.level1_icon_rect.collidepoint(event.pos):
                    self.levels_menu.level = 1

        if self.main_menu.action == 'start_game':
            self.map = 'levels_menu'
            self.main_menu.action = None

        elif self.levels_menu.level == 1:
            self.map = 'level1'
            self.init_level(1)
            self.levels_menu.level = None

        elif self.map == 'level1' and self.zombies_1.victory:
            self.map = 'levels_menu'

    def update(self):
        if self.map == 'level1':
            self.zombies_1.create_zombies()
            self.zombies_1.move()
            self.zombies_1.hit_plant(self.cells)
            self.sun.update_suns_amount(self.cells)
            self.zombies_1.pea_hit(self.cells)
            self.cells.peashooter(self.zombies_1)

    def draw(self):
        self.screen.fill('black')

        if self.map == 'main_menu':
            self.main_menu.run()

        if self.map == 'levels_menu':
            self.levels_menu.run()

        if self.map == 'level1':
            for layer in self.tmx_map:
                if isinstance(layer, pytmx.TiledTileLayer):
                    for x, y, gid in layer:
                        tile = self.tmx_map.get_tile_image_by_gid(gid)

                        if tile:
                            self.screen.blit(tile, (x * self.tmx_map.tilewidth, y * self.tmx_map.tileheight))
            self.cells.draw_plants()

            self.sun.draw()
            self.screen.blit(self.suns_count, (0, 0))
            self.screen.blit(self.suns_count_rect, (10, 61))
            amount = self.amount_font.render(str(self.sun.suns_total), True, (30, 30, 30))
            self.screen.blit(amount, (32, 60))

            self.plants.draw_cards(self.sun.suns_total)
            self.zombies_1.draw_zombies(self.cells)

        pg.display.flip()


if __name__ == '__main__':
    game1 = Game()