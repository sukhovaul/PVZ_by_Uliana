import pygame as pg
import random
import time


class Zombies:
    def __init__(self, level, screen):
        self.zombies = []
        self.level = level
        self.screen = screen
        self.ways = [20, 120, 220, 320, 420]

        self.zombies_killed = 11

        self.zombies_move = True

        self.zombies_pictures = [pg.image.load(f'pictures/zombies/NormalZombie/NormalZombieWalk/Zombie_{i}.png') for i
                                 in range(22)]
        self.zombies_attack_pictures = [
            pg.image.load(f'pictures/zombies/NormalZombie/NormalZombieAttack/ZombieAttack_{j}.png') for j in range(21)]
        self.zombies_lost_head_pictures = [
            pg.image.load(f'pictures/zombies/NormalZombie/ZombieLostHead/ZombieLostHead_{f}.png') for f in range(18)]
        self.zombies_die = [pg.image.load(f'pictures/zombies/NormalZombie/ZombieDie/ZombieDie_{i}.png') for i in
                            range(10)]

        self.buckethead_zombie_pictures = [pg.image.load(f'pictures/zombies/BucketheadZombie/BucketheadZombie_{i}.png')
                                           for i in range(15)]

        self.coneheaad_zombie_pictures = [pg.image.load(f'pictures/zombies/ConeheadZombie/ConeheadZombie_{i}.png') for i
                                          in range(21)]

        self.zombie_move = time.time()
        self.hit_time = time.time()
        self.zombie_attack = time.time()

        self.complete_rect = pg.Rect(1003, 556, 0, 10)
        self.complete_line = pg.image.load('pictures/Level_progress.png')

        self.victory = False

        self.last_zombie_spawn_time = time.time()
        self.zombie_spawn_index = 0  # переменная отвечает за индекс количество зомби и время их добавления

    def create_zombies(self):
        if self.level == 1:
            zombies_pairs = [1, 1, 1, 0, 1, 0, 1, 6]  # количество зомби в каждой волне
            zombie_time = [10, 30, 20, 25, 30, 30, 25, 30]  # время между созданием зомби
            zombie_types = [1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1]
            zombie_type_index = 0

            if self.zombie_spawn_index < len(zombies_pairs):
                if time.time() - self.last_zombie_spawn_time >= zombie_time[self.zombie_spawn_index]:
                    for i in range(zombies_pairs[self.zombie_spawn_index]):
                        zombie_y = random.choice(self.ways)
                        zombie_x = float(random.randint(890, 940))
                        zombie_rect = pg.Rect(int(zombie_x) + 80, zombie_y, 40, 144)

                        if zombie_types[zombie_type_index] == 1:
                            zombie_points = 20
                            zombie_images = self.zombies_pictures
                        elif zombie_types[zombie_type_index]:
                            zombie_points = 40
                            zombie_images = self.coneheaad_zombie_pictures

                        self.zombies.append({"x": zombie_x, "y": zombie_y, "rect": zombie_rect, "points": zombie_points,
                                             "zombie_pictures": zombie_images, "index": 0, "attack_index": 0,
                                             "picture_time": time.time(), "line": ((zombie_y - 20) // 100) + 1,
                                             "die_animation": False, "dead": False, "dead_animation_index": 0,
                                             "die_time": time.time()})

                        self.complete_rect.x -= 13
                        self.complete_rect.width += 13
                        zombie_type_index += 1
                    self.last_zombie_spawn_time = time.time()
                    self.zombie_spawn_index += 1

    def hit_plant(self, cells):
        for zombie in self.zombies:
            for plant in cells.plants:
                if zombie["rect"].colliderect(plant["rect"]):
                    self.zombies_move = False
                    if time.time() - self.zombie_attack >= 0.3:
                        zombie["attack_index"] = (zombie["attack_index"] + 1) % len(self.zombies_attack_pictures)
                        self.zombie_attack = time.time()
                    if time.time() - self.hit_time >= 2:
                        if plant["points"] <= 0:
                            plant["active"] = False
                        else:
                            plant["points"] -= 10
                            self.hit_time = time.time()

    def draw_zombies(self, cells):
        for zombie in self.zombies:
            if zombie["die_animation"]:
                if time.time()-zombie["die_time"] >= 0.2:
                    zombie["dead_animation_index"] += 1
                    zombie["die_time"] = time.time()
                    if zombie["dead_animation_index"] == 9:
                        zombie["dead"] = True
                        zombie["die_animation"] = False
                        self.zombies_killed += 1
                self.screen.blit(self.zombies_die[zombie["dead_animation_index"]], (zombie["x"], zombie["y"]))

            if zombie["zombie_pictures"]:
                if any(zombie["rect"].colliderect(plant["rect"]) for plant in cells.plants):
                    self.screen.blit(self.zombies_attack_pictures[zombie["attack_index"]], (zombie["x"], zombie["y"]))
                else:
                    if time.time() - zombie["picture_time"] >= 0.1:
                        zombie["index"] = (zombie["index"] + 1) % len(zombie["zombie_pictures"])
                        zombie["picture_time"] = time.time()
                    self.screen.blit(zombie["zombie_pictures"][zombie["index"]], (zombie["x"], zombie["y"]))

        self.screen.blit(self.complete_line, (850, 550))
        pg.draw.rect(self.screen, (0, 255, 0), self.complete_rect, 0, border_radius=3)

    def move(self):
        if self.zombies_move:
            if time.time() - self.zombie_move >= 1.5:
                for zombie in self.zombies:
                    zombie["x"] -= 0.15
                    zombie["rect"].x = int(zombie["x"]) + 80
                    if zombie["x"] <= 100:
                        print("вы проиграли")

    def pea_hit(self, cells):
        for pea in cells.peas:
            for zombie in self.zombies:
                if zombie["rect"].colliderect(pea["rect"]):
                    if not pea["shot"]:
                        zombie["points"] -= 2
                        pea["shot"] = True

                    if zombie["points"] <= 20 and zombie["zombie_pictures"] == self.coneheaad_zombie_pictures:
                        zombie["zombie_pictures"] = self.zombies_pictures
                    if zombie["points"] <= 4 and zombie["zombie_pictures"] == self.zombies_pictures:
                        zombie["zombie_pictures"] = self.zombies_lost_head_pictures
                        zombie["index"] = 0
                    if zombie["points"] <= 0:
                        zombie["die_animation"] = True
                        zombie["zombie_pictures"] = None
        cells.peas = [pea for pea in cells.peas if not pea["shot"]]

        self.zombies = [zombie for zombie in self.zombies if not zombie["dead"]]
        if self.zombies_killed == 11:
            self.victory = True