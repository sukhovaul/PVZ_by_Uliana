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
    def fill_cell(self, pos, active_plant, suns_amount, plant_amount):
        self.suns_amount = suns_amount
        for cell in self.cells:
            if cell["rect"].collidepoint(pos) and active_plant:
                if cell["empty"]:
                    cell["empty"]=False
                    self.suns_amount-=plant_amount
                    print(self.suns_amount)
                    if active_plant == 'sunflower':
                        self.screen.blit(self.sunflower_picture,(cell["rect"].x, cell["rect"].y))
                else:
                    print('Клетка уже занята')