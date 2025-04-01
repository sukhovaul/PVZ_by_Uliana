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
        self.hit_time = time.time()

    def create_zombies(self):
        if self.level == 1:
            for zombie in range(5):
                zombie_y = random.choice(self.ways)
                zombie_x = float(random.randint(890,940))
                zombie_rect = pg.Rect(int(zombie_x)+80,zombie_y, 40,144)
                self.zombies.append({"x": zombie_x, "y": zombie_y, "rect": zombie_rect})
                print(self.zombies)
    def draw_zombies(self):
        if time.time()-self.picture_time>=0.1:
            self.zombie_index = (self.zombie_index+1)%len(self.zombies_pictures)
            self.picture_time = time.time()

        for zombie in self.zombies:
            self.screen.blit(self.zombies_pictures[self.zombie_index], (zombie["x"], zombie["y"]))
            pg.draw.rect(self.screen, 'red', zombie["rect"])

    def move(self):
        if time.time()-self.zombie_move>=1.5:
            for zombie in self.zombies:
                zombie["x"]-=0.3
                zombie["rect"].x=int(zombie["x"])+80
                if zombie["x"]<=100:
                    print("вы проиграли")

    def hit_plant(self, cells):
        for zombie in self.zombies:
            for plant in cells.plants:
                if zombie["rect"].colliderect(plant["rect"]):
                    if time.time()-self.hit_time>=2:
                        plant["points"]-=10
                        print(plant["rect"])
                        print(zombie["rect"])
                        print(plant["points"])
                        self.hit_time = time.time()