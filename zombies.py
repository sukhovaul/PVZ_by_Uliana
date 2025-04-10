import pygame as pg
import random
import time

class Zombies():
    def __init__(self, level, screen):
        self.zombies = []
        self.level = level
        self.screen = screen
        self.ways = [20,120,220,320,420]

        self.zombies_move = True

        self.zombies_pictures = [pg.image.load(f'pictures/zombies/Zombie_{i}.png') for i in range(22)]
        self.zombies_attack_pictures = [pg.image.load(f'pictures/zombies/ZombieAttack_{j}.png') for j in range(21)]

        self.picture_time = time.time()
        self.zombie_index = 0
        self.zombie_move = time.time()
        self.hit_time = time.time()
        self.zombie_attack = time.time()

    def create_zombies(self):
        if self.level == 1:
            for zombie in range(5):
                zombie_y = random.choice(self.ways)
                zombie_x = float(random.randint(890,940))
                zombie_rect = pg.Rect(int(zombie_x)+80,zombie_y, 40,144)
                self.zombies.append({"x": zombie_x, "y": zombie_y, "rect": zombie_rect, "attack_index":0, "points": 20})
        print(self.zombies)

    def hit_plant(self, cells):
        for zombie in self.zombies:
            for plant in cells.plants:
                if zombie["rect"].colliderect(plant["rect"]):
                    self.zombies_move = False
                    if time.time()-self.zombie_attack>=0.3:
                        zombie["attack_index"]=(zombie["attack_index"]+1)%len(self.zombies_attack_pictures)
                        self.zombie_attack = time.time()
                    if time.time()-self.hit_time>=2:
                        if plant["points"]<=0:
                            plant["active"] = False
                        else:
                            plant["points"]-=10
                            self.hit_time = time.time()
    def draw_zombies(self, cells):
        for zombie in self.zombies:
            if any(zombie["rect"].colliderect(plant["rect"]) for plant in cells.plants):
                self.screen.blit(self.zombies_attack_pictures[zombie["attack_index"]], (zombie["x"], zombie["y"]))
            else:
                if time.time() - self.picture_time >= 0.1:
                    self.zombie_index = (self.zombie_index + 1) % len(self.zombies_pictures)
                    self.picture_time = time.time()
                self.screen.blit(self.zombies_pictures[self.zombie_index], (zombie["x"], zombie["y"]))

    def move(self):
        if self.zombies_move:
            if time.time()-self.zombie_move>=1.5:
                for zombie in self.zombies:
                    zombie["x"]-=0.3
                    zombie["rect"].x=int(zombie["x"])+80
                    if zombie["x"]<=100:
                        print("вы проиграли")
    def pea_hit(self, cells):
        for pea in cells.peas:
            for zombie in self.zombies:
                if zombie["rect"].colliderect(pea["rect"]):
                    if not pea["shot"]:
                        zombie["points"]-=5
                        print(zombie["points"])
                        pea["shot"]=True

        self.zombies = [zombie for zombie in self.zombies if zombie["points"]>0]