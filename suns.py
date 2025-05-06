import pygame as pg
import random
import time


class Sun:
    def __init__(self, screen):
        self.screen = screen
        self.suns_total = 0
        self.suns = []
        self.last_spawn_time = time.time()
        try:
            self.image = pg.image.load('pictures/Sun_0.png')
        except:
            self.image = pg.Surface((78, 78))
            self.image.fill('yellow')

        self.suns.append(self.create_sun())
        self.sunflower_spawn_time = time.time()

        self.sunflower_suns = []

        pg.mixer.init()

        self.sun_collected = pg.mixer.Sound('music/achievement.mp3')

    def draw(self):
        if time.time() - self.last_spawn_time >= 15:
            self.last_spawn_time = time.time()
            self.suns.append(self.create_sun())

        for sun in self.suns:
            if not sun["collected"]:
                sun["float_y"] += 0.5  # Изменяем реальную координату
                sun["rect"].y = int(sun["float_y"])
                self.screen.blit(self.image, sun["rect"].topleft)

        for sun in self.sunflower_suns:
            self.screen.blit(self.image, sun["rect"])

        for sun in self.sunflower_suns:
            if time.time() - sun["time"] >= 5:
                sun["collected"] = True

        self.suns = [sun for sun in self.suns if not sun["collected"]]
        self.sunflower_suns = [sun for sun in self.sunflower_suns if not sun["collected"]]

    def check_click(self, pos):
        for sun in self.suns:
            if not sun["collected"] and sun["rect"].collidepoint(pos):
                sun["collected"] = True
                self.suns_total += 25
                self.sun_collected.play()

        for sun in self.sunflower_suns:
            if not sun["collected"] and sun["rect"].collidepoint(pos):
                sun["collected"] = True
                self.suns_total += 25
                self.sun_collected.play()

    def create_sun(self):
        return {"rect": self.image.get_rect(topleft=(random.randint(250, 1000), 50)), "float_y": float(50),
                "collected": False}

    def update_suns_amount(self, cells):
        for plant in cells.plants:
            if plant["type"] == 'sunflower':
                if time.time() - plant["last_sun_spawn_time"] >= 15:
                    self.sunflower_suns.append(self.sunflower_sun(plant["rect"]))
                    plant["last_sun_spawn_time"] = time.time()

    def sunflower_sun(self, rect):
        return {"rect": pg.Rect(rect.x + 50, rect.y, rect.width, rect.height), "collected": False, "time": time.time()}
