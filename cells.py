import pygame as pg
import pytmx

class Cells():
    def __init__(self, tmx_map, screen):
        self.tmx_map = tmx_map
        self.cells = []
        self.screen = screen
        self.plants = []

        for layer in self.tmx_map:
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == 'cells':
                    for obj in layer:
                        new_cell = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                        self.cells.append({"rect": new_cell, "empty": True})
        print(self.cells)

        self.sunflower_picture = pg.image.load('pictures/plants/SunFlower.png')
    def fill_cell(self, pos, plant, plant_amount, sun_object):
        for cell in self.cells:
            if cell["rect"].collidepoint(pos) and plant.active_plant:
                if cell["empty"]:

                    if sun_object.suns_total >= plant_amount:
                        cell["empty"] = False
                        sun_object.suns_total -= plant_amount
                        print(sun_object.suns_total)
                        if plant.active_plant == 'sunflower':
                            self.plants.append({"image":self.sunflower_picture,"x":cell["rect"].x, "y":cell["rect"].y})
                            plant.active_plant = None
                    else:
                        print('Недостаточно солнц для покупки растения')
                else:
                    print('Клетка уже занята')

    def draw_plants(self):
        for plant in self.plants:
            self.screen.blit(plant["image"],(plant["x"], plant["y"]))