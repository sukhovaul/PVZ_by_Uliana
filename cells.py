import pygame as pg
import pytmx
import time


class Cells:
    def __init__(self, tmx_map, screen):
        self.tmx_map = tmx_map
        self.cells = []
        self.screen = screen
        self.plants = []

        self.plant_time = time.time()

        self.sunflower_pictures = [pg.image.load(f'pictures/plants/sunflower/SunFlower_{i}.png') for i in range(18)]
        self.wallnut_pictures = [pg.image.load(f'pictures/plants/wallnut/WallNut_{i}.png') for i in range(16)]
        self.peashooter_pictures = [pg.image.load(f'pictures/plants/peashooter/Peashooter_{i}.png') for i in range(13)]
        self.cherrybomb_pictures = [pg.image.load(f'pictures/plants/cherrybomb/CherryBomb_{i}.png') for i in range(7)]

        self.peas = []
        self.pea_image = pg.image.load('pictures/plants/peashooter/PeaNormal_0.png')

        for layer in self.tmx_map:
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == 'cells':
                    for obj in layer:
                        new_cell = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                        self.cells.append({"rect": new_cell, "empty": True})
        print(self.cells)

    def fill_cell(self, pos, plant, plant_amount, sun_object):
        for cell in self.cells:
            if cell["rect"].collidepoint(pos) and plant.active_plant and cell["empty"]:
                if sun_object.suns_total >= plant_amount:
                    sun_object.suns_total -= plant_amount
                    cell["empty"] = False

                    new_plant = {
                        "index": 0,
                        "x": cell["rect"].x,
                        "y": cell["rect"].y,
                        "rect": cell["rect"],
                        "active": True
                    }

                    if plant.active_plant == 'sunflower':
                        new_plant.update({
                            "image": self.sunflower_pictures,
                            "type": 'sunflower',
                            "last_sun_spawn_time": time.time(),
                            "points": 20
                        })
                    elif plant.active_plant == 'peashooter':
                        new_plant.update({
                            "image": self.peashooter_pictures,
                            "type": 'peashooter',
                            "last_shot": time.time(),
                            "line": ((cell["rect"].y - 60) // 100) + 1,
                            "points":20
                        })
                    elif plant.active_plant == 'wallnut':
                        new_plant.update({
                            "image": self.wallnut_pictures,
                            "type": 'wallnut',
                            "points":40
                        })

                    elif plant.active_plant == "cherrybomb":
                        new_plant.update(({
                            "image":self.cherrybomb_pictures,
                            "type":'cherrybomb',
                            "points":20,
                            "time": time.time()
                        }))

                    self.plants.append(new_plant)
                    plant.plant_placed()
                    plant.active_plant = None

    def draw_plants(self):
        if time.time() - self.plant_time >= 0.07:
            for plant in self.plants:
                plant["index"] = (plant["index"] + 1) % len(plant["image"])
            self.plant_time = time.time()

        for plant in self.plants:
            self.screen.blit(plant["image"][plant["index"]], (plant["x"], plant["y"]))

        self.plants = [plant for plant in self.plants if plant["active"]]

        for pea in self.peas:
            pea["rect"].x += 5
            self.screen.blit(self.pea_image, (pea["rect"].x, pea["rect"].y))

    def peashooter(self, zombies):
        for plant in self.plants:
            if plant["type"] == 'peashooter':
                for zombie in zombies.zombies:
                    if zombie["line"] == plant["line"]:
                        if time.time() - plant["last_shot"] >= 1.4:
                            pea_rect = pg.Rect(plant["rect"].x, plant["rect"].y, 23, 23)
                            self.peas.append({"rect": pea_rect, "shot": False})
                            plant["last_shot"] = time.time()
                        break


    def cherrybomb(self, zombies):
        for plant in self.plants:
            if plant["type"] == 'cherrybomb':
                if time.time()-plant["time"] >= 1:
                    for zombie in zombies.zombies:
                        if abs(plant["rect"].x - zombie["x"]) <= 100 and abs(plant["rect"].y - zombie["y"]) <= 120:
                            zombie["points"] = 0
                            zombie["die_animation"] = True
                            zombie["zombie_pictures"] = None
                    plant["active"] = False