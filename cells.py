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
        self.wallnut_pictures = [pg.image.load(f'pictures/plants/wallnut/WallNut_{i}.png') for i in range(16)]
        self.peashooter_pictures = [pg.image.load(f'pictures/plants/peashooter/Peashooter_{i}.png') for i in range(13)]

        self.peas = []
        self.pea_image = pg.image.load('pictures/plants/peashooter/PeaNormal_0.png')

        for layer in self.tmx_map:
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == 'cells':
                    for obj in layer:
                        new_cell = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                        self.cells.append({"rect": new_cell, "empty": True})

    def fill_cell(self, pos, plant, plant_amount, sun_object):
        for cell in self.cells:
            if cell["rect"].collidepoint(pos) and plant.active_plant:
                if cell["empty"]:

                    if sun_object.suns_total >= plant_amount:
                        cell["empty"] = False
                        sun_object.suns_total -= plant_amount
                        if plant.active_plant == 'sunflower':
                            self.plants.append({"index":0, "image":self.sunflower_pictures,"x":cell["rect"].x, "y":cell["rect"].y, "rect": cell["rect"], "points": 20, "type": 'sunflower', "active": True})
                            plant.active_plant = None
                        elif plant.active_plant == 'wallnut':
                            self.plants.append({"index":0, "image": self.wallnut_pictures, "x":cell["rect"].x, "y":cell["rect"].y, "rect": cell["rect"], "points": 50, "type": 'wallnut', "active": True})
                            plant.active_plant = None
                        elif plant.active_plant == 'peashooter':
                            self.plants.append({"index":0, "image": self.peashooter_pictures, "x": cell["rect"].x, "y": cell["rect"].y, "rect": cell["rect"], "points": 20, "type": 'peashooter', "active": True})
                            plant.active_plant = None
                            pea_rect = pg.Rect(cell["rect"].x, cell["rect"].y, 23, 23)
                            self.peas.append({"x":cell["rect"].x, "y": cell["rect"].y, "rect": pea_rect})
                    else:
                        print('Недостаточно солнц для покупки растения')
                else:
                    print('Клетка уже занята')

    def draw_plants(self):
        if time.time()-self.plant_time>=0.07:
            for plant in self.plants:
                plant["index"] = (plant["index"] + 1) % len(plant["image"])
            self.plant_time = time.time()

        for plant in self.plants:
            self.screen.blit(plant["image"][plant["index"]], (plant["x"], plant["y"]))
        for pea in self.peas:
            pea["x"]+=5
            self.screen.blit(self.pea_image, (pea["x"], pea["y"]))

        self.plants = [plant for plant in self.plants if plant["active"]]