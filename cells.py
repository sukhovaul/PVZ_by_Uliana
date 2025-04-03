import pygame as pg
import pytmx
import time

class Cells():
    def __init__(self, tmx_map, screen):
        self.tmx_map = tmx_map
        self.cells = []
        self.screen = screen
        self.plants = []

        self.plant_time = time.time()

        self.sunflower_pictures = [pg.image.load(f'pictures/plants/sunflower/SunFlower_{i}.png') for i in range(18)]

        for layer in self.tmx_map:
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == 'cells':
                    for obj in layer:
                        new_cell = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                        self.cells.append({"rect": new_cell, "empty": True})

        self.wallnut_pictures = [pg.image.load('pictures/plants/WallNut_0.png')]
        self.peashooter_pictures = [pg.image.load('pictures/plants/Peashooter_0.png')]
    def fill_cell(self, pos, plant, plant_amount, sun_object):
        for cell in self.cells:
            if cell["rect"].collidepoint(pos) and plant.active_plant:
                if cell["empty"]:

                    if sun_object.suns_total >= plant_amount:
                        cell["empty"] = False
                        sun_object.suns_total -= plant_amount
                        if plant.active_plant == 'sunflower':
                            self.plants.append({"index":0, "image":self.sunflower_pictures,"x":cell["rect"].x, "y":cell["rect"].y, "rect": cell["rect"], "points": 20, "type": 'sunflower'})
                            plant.active_plant = None
                        elif plant.active_plant == 'wallnut':
                            self.plants.append({"index":0, "image": self.wallnut_pictures, "x":cell["rect"].x, "y":cell["rect"].y, "rect": cell["rect"], "points": 50, "type": 'wallnut'})
                            plant.active_plant = None
                        elif plant.active_plant:
                            self.plants.append({"index":0, "image": self.peashooter_pictures, "x": cell["rect"].x, "y": cell["rect"].y, "rect": cell["rect"], "points": 20, "type": 'peashooter'})
                            plant.active_plant = None
                    else:
                        print('Недостаточно солнц для покупки растения')
                else:
                    print('Клетка уже занята')

    def draw_plants(self):
        if time.time()-self.plant_time>=0.05:
            for plant in self.plants:
                plant["index"] = (plant["index"] + 1) % len(plant["image"])
            self.plant_time = time.time()

        for plant in self.plants:
            self.screen.blit(plant["image"][plant["index"]], (plant["x"], plant["y"]))