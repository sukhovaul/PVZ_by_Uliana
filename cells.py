import pygame as pg
import pytmx

class Cells():
    def __init__(self, tmx_map, screen):
        self.tmx_map = tmx_map
        self.cells = []
        self.screen = screen

        for layer in self.tmx_map:
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == 'cells':
                    for obj in layer:
                        new_cell = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                        self.cells.append({"rect": new_cell, "empty": True})
        print(self.cells)

        self.sunflower_picture = pg.image.load('pictures/plants/SunFlower.png')
    def fill_cell(self, pos, active_plant, plant_amount, sun_object):
        for cell in self.cells:
            if cell["rect"].collidepoint(pos) and active_plant:
                if cell["empty"]:

                    if sun_object.suns_total >= plant_amount:
                        cell["empty"] = False
                        sun_object.suns_total -= plant_amount
                        print(sun_object.suns_total)
                        if active_plant == 'sunflower':
                            self.screen.blit(self.sunflower_picture,(cell["rect"].x, cell["rect"].y))
                    else:
                        print('Недостаточно солнц для покупки растения')
                else:
                    print('Клетка уже занята')