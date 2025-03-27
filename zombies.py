import pygame as pg
import random

class Zombies():
    def __init__(self, level):
        self.zombie_image_0 = pg.image.load('pictures/zombies/Zombie_0.png')
        self.zombies = []
        self.level = level
        self.ways = [120,220,320,420,520]

    def create_zombies(self):
        if self.level == 1:
            for zombie in range(5):
                self.zombies.append({"x":900, "y": random.choice(self.ways)})
                print(self.zombies)