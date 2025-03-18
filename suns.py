import pygame as pg
import random
import time

class Sun():
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

    def draw(self):
        if time.time() - self.last_spawn_time >= 5:
            self.last_spawn_time = time.time()
            self.suns.append(self.create_sun())

        for sun in self.suns:
            if not sun["collected"]:
                sun["float_y"] += 0.5  # Изменяем реальную координату
                sun["rect"].y = int(sun["float_y"])
                self.screen.blit(self.image, sun["rect"].topleft)

    def check_click(self, pos):
        for sun in self.suns:
            if not sun["collected"] and sun["rect"].collidepoint(pos):
                sun["collected"] = True
                self.suns_total += 25

        self.suns = [sun for sun in self.suns if not sun["collected"]]

    def create_sun(self):
        return {"rect": self.image.get_rect(topleft=(random.randint(250, 1000), 50)), "float_y": float(50), "collected": False}