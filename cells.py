import pygame as pg
import pytmx

class Cells():
    def __init__(self, tmx_map):
        self.tmx_map = tmx_map
        self.cells = []

        for layer in self.tmx_map:
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == 'cells':
                    for obj in layer:
                        new_cell = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                        self.cells.append({"rect": new_cell, "empty": True})
        print(self.cells)
    def fill_cell(self, pos):
        for cell in self.cells:
            if cell["rect"].collidepoint(pos):
                if cell["empty"]:
                    cell["empty"]=False
                else:
                    print('Клетка уже занята')