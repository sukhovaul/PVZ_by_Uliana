import pygame as pg
import random
import time

class Zombies():
    def __init__(self, level, screen):
        self.zombies = []
        self.level = level
        self.screen = screen
        self.ways = [20,120,220,320,420]

        self.zombies_pictures = [pg.image.load('pictures/zombies/Zombie_0.png'),
                                 pg.image.load('pictures/zombies/Zombie_1.png'),
                                 pg.image.load('pictures/zombies/Zombie_2.png'),
                                 pg.image.load('pictures/zombies/Zombie_3.png'),
                                 pg.image.load('pictures/zombies/Zombie_4.png'),
                                 pg.image.load('pictures/zombies/Zombie_5.png'),
                                 pg.image.load('pictures/zombies/Zombie_6.png'),
                                 pg.image.load('pictures/zombies/Zombie_7.png'),
                                 pg.image.load('pictures/zombies/Zombie_8.png'),
                                 pg.image.load('pictures/zombies/Zombie_9.png'),
                                 pg.image.load('pictures/zombies/Zombie_10.png'),
                                 pg.image.load('pictures/zombies/Zombie_11.png'),
                                 pg.image.load('pictures/zombies/Zombie_12.png'),
                                 pg.image.load('pictures/zombies/Zombie_13.png'),
                                 pg.image.load('pictures/zombies/Zombie_14.png'),
                                 pg.image.load('pictures/zombies/Zombie_15.png'),
                                 pg.image.load('pictures/zombies/Zombie_16.png'),
                                 pg.image.load('pictures/zombies/Zombie_17.png'),
                                 pg.image.load('pictures/zombies/Zombie_18.png'),
                                 pg.image.load('pictures/zombies/Zombie_19.png'),
                                 pg.image.load('pictures/zombies/Zombie_20.png'),
                                 pg.image.load('pictures/zombies/Zombie_21.png')]

        self.picture_time = time.time()
        self.zombie_index = 0
        self.zombie_move = time.time()

    def create_zombies(self):
        if self.level == 1:
            for zombie in range(5):
                self.zombies.append({"x":float(random.randint(890,940)), "y": random.choice(self.ways)})
                print(self.zombies)
    def draw_zombies(self):
        if time.time()-self.picture_time>=0.1:
            self.zombie_index = (self.zombie_index+1)%len(self.zombies_pictures)
            self.picture_time = time.time()

        for zombie in self.zombies:
            self.screen.blit(self.zombies_pictures[self.zombie_index], (zombie["x"], zombie["y"]))

    def move(self):
        if time.time()-self.zombie_move>=1.5:
            for zombie in self.zombies:
                zombie["x"]-=0.3
                if zombie["x"]<=100:
                    print("вы проиграли")