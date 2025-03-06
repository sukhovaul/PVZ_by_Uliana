import pygame as pg
import pytmx
from settings import *
import resource_manager
import main_menu

pg.init()

class Game():
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('Plants vs Zombies')

        self.tmx_map = pytmx.load_pygame('maps/level1.tmx')
        self.cells = []
        self.map = 'main_menu'

        self.main_menu = main_menu.Menu(SCREEN_WIDTH, SCREEN_HEIGHT,'maps/MainMenu.png')

        for layer in self.tmx_map:
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == 'cells':
                    for obj in layer:
                        new_cell = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                        self.cells.append(new_cell)
        print(self.cells)

        self.run()
    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()
            self.main_menu.handle_events()
    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        if self.main_menu.action == 'start_game':
            self.map = 'level1'
    def update(self):
        ...
    def draw(self):
        self.screen.fill('black')

        if self.map == 'main_menu':
            self.main_menu.draw()

        if self.map == 'level1':
            for layer in self.tmx_map:
                if isinstance(layer, pytmx.TiledTileLayer):
                    for x,y, gid in layer:
                        tile = self.tmx_map.get_tile_image_by_gid(gid)

                        if tile:
                            self.screen.blit(tile, (x*self.tmx_map.tilewidth, y*self.tmx_map.tileheight))

        pg.display.flip()

if __name__ == '__main__':
    game1 = Game()