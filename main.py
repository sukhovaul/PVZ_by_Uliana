import pygame as pg
import pytmx
from settings import *
import main_menu
import suns
import cells
import plants

pg.init()
pg.mixer.init()

class Game():
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('Plants vs Zombies')

        self.tmx_map = pytmx.load_pygame('maps/level1.tmx')
        self.map = 'main_menu'
        self.sun = suns.Sun(self.screen)

        self.cells = cells.Cells(self.tmx_map, self.screen)

        self.main_menu = main_menu.Menu(SCREEN_WIDTH, SCREEN_HEIGHT,'maps/MainMenu.png')

        self.clock = pg.time.Clock() #добавляем объект clock для регулирования fps

        self.suns_count = pg.image.load('pictures/suns_count.png')
        self.suns_count_rect = pg.Surface((54, 21))
        self.suns_count_rect.fill((227,203,170))
        self.amount_font = pg.font.Font('fonts/main_font.ttf',20)

        self.plants = plants.Plants(self.screen)

        self.run()
    def run(self):
        running = True
        while running:
            self.clock.tick(60) #устанавливаем 60 fps
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
                self.cells.fill_cell(event.pos, self.plants.active_plant, self.sun.suns_total, self.plants.plant_amount)
                self.plants.choose_plant(event.pos)
        if self.main_menu.action == 'start_game':
            self.map = 'level1'
    def update(self):
        ...
    def draw(self):
        self.screen.fill('black')

        if self.map == 'main_menu':
            self.main_menu.run()

        if self.map == 'level1':
            for layer in self.tmx_map:
                if isinstance(layer, pytmx.TiledTileLayer):
                    for x,y, gid in layer:
                        tile = self.tmx_map.get_tile_image_by_gid(gid)

                        if tile:
                            self.screen.blit(tile, (x*self.tmx_map.tilewidth, y*self.tmx_map.tileheight))
            self.sun.draw()
            self.screen.blit(self.suns_count,(0,0))
            self.screen.blit(self.suns_count_rect,(10,61))
            self.amount = self.amount_font.render(str(self.sun.suns_total),True,(30,30,30))
            self.screen.blit(self.amount,(32,60))

            self.plants.draw_cards(self.sun.suns_total)

        pg.display.flip()

if __name__ == '__main__':
    game1 = Game()