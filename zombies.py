import pygame as pg
import random
import time


class Zombies:
    def __init__(self, level, screen):
        self.zombies = []
        self.level = level
        self.screen = screen
        self.ways = [20, 120, 220, 320, 420]

        self.victory_text = None
        self.victory_time = None

        self.zombies_killed = 0

        self.grave = []
        self.grav_image = pg.image.load('pictures/zombies/Zomboss/grav.png')

        self.font = pg.font.SysFont('Arial', 72, bold=True)  # или загрузите свой шрифт
        self.zomboss_text = None
        self.zomboss_text_time = 0
        self.show_zomboss_text = False

        self.zombies_pictures = [pg.image.load(f'pictures/zombies/NormalZombie/NormalZombieWalk/Zombie_{i}.png') for i in range(22)]
        self.zombies_attack_pictures = [pg.image.load(f'pictures/zombies/NormalZombie/NormalZombieAttack/ZombieAttack_{j}.png') for j in range(21)]
        self.zombies_lost_head_pictures = [pg.image.load(f'pictures/zombies/NormalZombie/ZombieLostHead/ZombieLostHead_{f}.png') for f in range(18)]
        self.zombies_die = [pg.image.load(f'pictures/zombies/NormalZombie/ZombieDie/ZombieDie_{i}.png') for i in range(10)]

        self.buckethead_zombie_pictures = [pg.image.load(f'pictures/zombies/BucketheadZombie/BucketheadZombie_{i}.png')for i in range(15)]
        self.coneheaad_zombie_pictures = [pg.image.load(f'pictures/zombies/ConeheadZombie/ConeheadZombie_{i}.png') for i in range(21)]

        self.zomboss_pictures = [pg.image.load(f'pictures/zombies/Zomboss/zomboss_{i}.png') for i in range(1)]

        self.zombie_move = time.time()
        self.hit_time = time.time()
        self.zombie_attack = time.time()

        self.complete_rect = pg.Rect(1003, 556, 0, 10)
        self.life_rect = pg.Rect(1003, 56, 0, 10)
        self.show_line = False
        self.complete_line = pg.image.load('pictures/Level_progress.png')
        self.zombie_line = pg.image.load('pictures/Level_progress_1.png')

        self.victory = False

        self.zombie_image_index = 0
        self.last_zombie_spawn_time = time.time()
        self.zombie_spawn_index = 0  # переменная отвечает за индекс количество зомби и время их добавления

    def create_zombies(self):
        if self.level == 1:
            zombies_pairs = [1, 1, 1, 0, 1, 0, 1, 6]  # количество зомби в каждой волне
            zombie_time = [30, 30, 20, 25, 30, 30, 25, 30]  # время между созданием зомби
            zombie_types = [1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1]

            if self.zombie_spawn_index < len(zombies_pairs):
                if time.time() - self.last_zombie_spawn_time >= zombie_time[self.zombie_spawn_index]:
                    for i in range(zombies_pairs[self.zombie_spawn_index]):
                        zombie_y = random.choice(self.ways)
                        zombie_x = float(random.randint(890, 940))
                        zombie_rect = pg.Rect(int(zombie_x) + 80, zombie_y, 40, 144)

                        if zombie_types[self.zombie_image_index] == 1:
                            zombie_points = 20
                            zombie_images = self.zombies_pictures
                            self.zombie_image_index += 1
                        elif zombie_types[self.zombie_image_index]:
                            zombie_points = 40
                            zombie_images = self.coneheaad_zombie_pictures
                            self.zombie_image_index += 1

                        self.zombies.append({"x": zombie_x, "y": zombie_y, "rect": zombie_rect, "points": zombie_points,
                                             "zombie_pictures": zombie_images, "index": 0, "attack_index": 0,
                                             "picture_time": time.time(), "line": [((zombie_y - 20) // 100) + 1],
                                             "die_animation": False, "dead": False, "dead_animation_index": 0,
                                             "die_time": time.time(), "zombie_move": True, "zomboss": False})
                        self.complete_rect.x -= 13
                        self.complete_rect.width += 13
                    self.last_zombie_spawn_time = time.time()
                    self.zombie_spawn_index += 1


        elif self.level == 2:
            zombies_pairs = [1, 1, 2, 0, 1, 1, 1, 5]  # количество зомби в каждой волне
            zombie_time = [30, 20, 45, 25, 30, 30, 25, 30]  # время между созданием зомби
            zombie_types = [3, 3, 1, 2, 1, 2, 3, 2, 1, 1, 1, 2]

            if self.zombie_spawn_index < len(zombies_pairs):
                if time.time() - self.last_zombie_spawn_time >= zombie_time[self.zombie_spawn_index]:
                    for i in range(zombies_pairs[self.zombie_spawn_index]):

                        if self.zombie_image_index == 1:
                            self.zombie_y = self.zombie_y

                        else:
                            self.zombie_y = random.choice(self.ways)
                        zombie_x = float(random.randint(890, 940))
                        zombie_rect = pg.Rect(int(zombie_x) + 80, self.zombie_y, 40, 144)

                        if zombie_types[self.zombie_image_index] == 1:
                            zombie_points = 20
                            zombie_images = self.zombies_pictures
                            self.zombie_image_index += 1
                        elif zombie_types[self.zombie_image_index] == 2:
                            zombie_points = 40
                            zombie_images = self.coneheaad_zombie_pictures
                            self.zombie_image_index += 1
                        elif zombie_types[self.zombie_image_index] == 3:
                            zombie_points = 60
                            zombie_images = self.buckethead_zombie_pictures
                            self.zombie_image_index += 1

                        self.zombies.append({"x": zombie_x, "y": self.zombie_y, "rect": zombie_rect, "points": zombie_points,
                                             "zombie_pictures": zombie_images, "index": 0, "attack_index": 0,
                                             "picture_time": time.time(), "line": [((self.zombie_y - 20) // 100) + 1],
                                             "die_animation": False, "dead": False, "dead_animation_index": 0,
                                             "die_time": time.time(), "zombie_move": True, "zomboss": False})

                        self.complete_rect.x -= 12
                        self.complete_rect.width += 12
                    self.last_zombie_spawn_time = time.time()
                    self.zombie_spawn_index += 1

        elif self.level == 3:
            zombies_pairs = [1, 1, 1, 1, 1, 1, 1, 5]  # количество зомби в каждой волне
            zombie_time = [0, 45, 30, 0, 5, 35, 25, 30]  # время между созданием зомби
            zombie_types = [1, 1, 3, 3, 3, 2, 3, 2, 1, 1, 1, 2]

            if self.zombie_spawn_index < len(zombies_pairs):
                if time.time() - self.last_zombie_spawn_time >= zombie_time[self.zombie_spawn_index]:
                    for i in range(zombies_pairs[self.zombie_spawn_index]):

                        if self.zombie_image_index == 2:
                            self.zombie_y = 320

                        elif self.zombie_image_index == 3:
                            self.zombie_y -= 200

                        elif self.zombie_image_index == 4:
                            self.zombie_y += 100

                        else:
                            self.zombie_y = random.choice(self.ways)
                        zombie_x = float(random.randint(890, 940))
                        zombie_rect = pg.Rect(int(zombie_x) + 80, self.zombie_y, 40, 144)

                        if zombie_types[self.zombie_image_index] == 1:
                            zombie_points = 20
                            zombie_images = self.zombies_pictures
                            self.zombie_image_index += 1
                        elif zombie_types[self.zombie_image_index] == 2:
                            zombie_points = 40
                            zombie_images = self.coneheaad_zombie_pictures
                            self.zombie_image_index += 1
                        elif zombie_types[self.zombie_image_index] == 3:
                            zombie_points = 60
                            zombie_images = self.buckethead_zombie_pictures
                            self.zombie_image_index += 1

                        self.zombies.append({"x": zombie_x, "y": self.zombie_y, "rect": zombie_rect, "points": zombie_points,
                                             "zombie_pictures": zombie_images, "index": 0, "attack_index": 0,
                                             "picture_time": time.time(), "line": [((self.zombie_y - 20) // 100) + 1],
                                             "die_animation": False, "dead": False, "dead_animation_index": 0,
                                             "die_time": time.time(), "zombie_move": True, "zomboss": False})

                        self.complete_rect.x -= 12
                        self.complete_rect.width += 12
                    self.last_zombie_spawn_time = time.time()
                    self.zombie_spawn_index += 1

        elif self.level == 4:
            zombies_pairs = [1, 1, 2, 2, 2, 2]  # количество зомби в каждой волне
            zombie_time = [0, 30, 30, 30, 30, 40]  # время между созданием зомби
            zombie_types = [1, 1, 2, 1, 3, 1, 2, 3, 2, 3]

            if self.zombie_spawn_index < len(zombies_pairs):
                if time.time() - self.last_zombie_spawn_time >= zombie_time[self.zombie_spawn_index]:
                    for i in range(zombies_pairs[self.zombie_spawn_index]):
                        zombie_y = random.choice(self.ways)
                        zombie_x = float(random.randint(890, 940))
                        zombie_rect = pg.Rect(int(zombie_x) + 80, zombie_y, 40, 144)

                        if zombie_types[self.zombie_image_index] == 1:
                            zombie_points = 20
                            zombie_images = self.zombies_pictures
                            self.zombie_image_index += 1
                        elif zombie_types[self.zombie_image_index] == 2:
                            zombie_points = 40
                            zombie_images = self.coneheaad_zombie_pictures
                            self.zombie_image_index += 1
                        elif zombie_types[self.zombie_image_index] == 3:
                            zombie_points = 60
                            zombie_images = self.buckethead_zombie_pictures
                            self.zombie_image_index += 1

                        self.zombies.append({"x": zombie_x, "y": zombie_y, "rect": zombie_rect, "points": zombie_points,
                                             "zombie_pictures": zombie_images, "index": 0, "attack_index": 0,
                                             "picture_time": time.time(), "line": [((zombie_y - 20) // 100) + 1],
                                             "die_animation": False, "dead": False, "dead_animation_index": 0,
                                             "die_time": time.time(), "zombie_move": True, "zomboss": False})
                        self.complete_rect.x -= 16
                        self.complete_rect.width += 16
                    self.last_zombie_spawn_time = time.time()
                    self.zombie_spawn_index += 1

            if self.zombies_killed == 1:
                if not self.show_zomboss_text:
                    self.zomboss_text = self.font.render("ZOMBOSS IS COMING!", True, (255, 0, 0))
                    self.zomboss_text_time = time.time()
                    self.show_zomboss_text = True
                elif time.time() - self.zomboss_text_time >= 5:

                    self.show_line = True

                    zombie_rect = pg.Rect(940, 120, 290,290)
                    self.zombies.append({"x": 940, "y": 120, "rect": zombie_rect, "points": 10,
                                         "zombie_pictures": self.zomboss_pictures, "index": 0, "zombie_time": time.time() - 25, "grav_time": time.time()-10,
                                         "picture_time": time.time(), "line": [((320 - 20) // 100) + 1, ((220 - 20) // 100) + 1, ((120 - 20) // 100) + 1],
                                         "die_time": time.time(), "zombie_move": False, "zomboss": True, "dead": False, "die_animation": False, "zombie_amount": 3,
                                         "zombie_spawn_time": 25, "grav_spawn_time": 30})
                    self.zombies_killed = 0

    def hit_plant(self, cells):
        for zombie in self.zombies:
            for plant in cells.plants:
                if zombie["rect"].colliderect(plant["rect"]):
                    zombie["zombie_move"] = False
                    if time.time() - self.zombie_attack >= 0.3:
                        zombie["attack_index"] = (zombie["attack_index"] + 1) % len(self.zombies_attack_pictures)
                        self.zombie_attack = time.time()
                    if time.time() - self.hit_time >= 2:
                        if plant["points"] <= 0:
                            plant["active"] = False
                            zombie["move"]= True
                        else:
                            plant["points"] -= 5
                            self.hit_time = time.time()

    def draw_zombies(self, cells):
        for zombie in self.zombies:
            if zombie["die_animation"] and not zombie["zomboss"]:
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

        for grav in self.grave:
            self.screen.blit(self.grav_image, (grav["x"], grav["y"]))

        if self.show_zomboss_text and time.time()- self.zomboss_text_time <= 5:
            text_rect = self.zomboss_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
            self.screen.blit(self.zomboss_text, text_rect)

        if self.victory_text and time.time() - self.victory_time <= 5:  # Показываем 5 секунд
            text_rect = self.victory_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
            self.screen.blit(self.victory_text, text_rect)

        self.screen.blit(self.complete_line, (850, 550))
        pg.draw.rect(self.screen, (0, 255, 0), self.complete_rect, 0, border_radius=3)

        '''if self.show_line:
            self.screen.blit(self.zombie_line, (450, 50))
            pg.draw.rect(self.screen, (255, 0 ,0), self.life_rect, 0, 3)'''

    def move(self):
        for zombie in self.zombies:
            if zombie["zombie_move"]:
                if time.time() - self.zombie_move >= 1.5:
                    zombie["x"] -= 0.15
                    zombie["rect"].x = int(zombie["x"]) + 80
                    if zombie["x"] <= 100:
                        print("вы проиграли")

    def pea_hit(self, cells):
        for pea in cells.peas:
            if len(self.grave)>0:
                for grav in self.grave:
                    if grav["rect"].colliderect(pea["rect"]):
                        if not pea["shot"]:
                            grav["points"]-=2
                            pea["shot"] = True
                        if grav["points"]<=0:
                            grav["alive"] = False

            for zombie in self.zombies:
                if zombie["rect"].colliderect(pea["rect"]):
                    if not pea["shot"]:
                        zombie["points"] -= 2
                        pea["shot"] = True
                        if zombie["zomboss"]:
                            self.life_rect.x -= 1
                            self.life_rect.width += 1

                    if zombie["points"] <= 20 and (zombie["zombie_pictures"] == self.coneheaad_zombie_pictures or zombie["zombie_pictures"]==self.buckethead_zombie_pictures):
                        zombie["zombie_pictures"] = self.zombies_pictures
                    if zombie["points"] <= 4 and zombie["zombie_pictures"] == self.zombies_pictures:
                        zombie["zombie_pictures"] = self.zombies_lost_head_pictures
                        zombie["index"] = 0
                    if zombie["points"] <= 0 and not zombie["zomboss"]:
                        zombie["die_animation"] = True
                        zombie["zombie_pictures"] = None
                    if zombie["points"] <= 0 and zombie["zomboss"]:
                        self.victory_text = self.font.render("VICTORY!", True, (255, 0, 0))
                        self.victory_time = time.time()
                        zombie["dead"] = True
        cells.peas = [pea for pea in cells.peas if not pea["shot"]]

        self.zombies = [zombie for zombie in self.zombies if not zombie["dead"]]
        if self.zombies_killed == 11 and self.level == 1:
            self.victory = True
        if self.zombies_killed == 12 and self.level == 2:
            self.victory = True
        if self.zombies_killed == 12 and self.level == 3:
            self.victory = True
        if  self.level == 4 and self.victory_time != None:
            if time.time() - self.victory_time >= 5:
                self.victory = True

    def fume_hit(self, cells):
        for fume in cells.fumes:
            if len(self.grave)>0:
                for grav in self.grave:
                    if grav["rect"].colliderect(fume["rect"]):
                        if not fume["shot"]:
                            grav["points"]-=1
                            fume["shot"] = True
                        if grav["points"]<=0:
                            grav["alive"] = False

            for zombie in self.zombies:
                if zombie["rect"].colliderect(fume["rect"]):
                    if not fume["shot"]:
                        zombie["points"] -= 2
                        fume["shot"] = True
                        if zombie["zomboss"]:
                            self.life_rect.x -= 1
                            self.life_rect.width += 1

                    if zombie["points"] <= 20 and (zombie["zombie_pictures"] == self.coneheaad_zombie_pictures or zombie["zombie_pictures"]==self.buckethead_zombie_pictures):
                        zombie["zombie_pictures"] = self.zombies_pictures
                    if zombie["points"] <= 4 and zombie["zombie_pictures"] == self.zombies_pictures:
                        zombie["zombie_pictures"] = self.zombies_lost_head_pictures
                        zombie["index"] = 0
                    if zombie["points"] <= 0 and not zombie["zomboss"]:
                        zombie["die_animation"] = True
                        zombie["zombie_pictures"] = None
                    if zombie["points"] <= 0 and zombie["zomboss"]:
                        self.victory_text = self.font.render("VICTORY!", True, (255, 0, 0))
                        self.victory_time = time.time()
                        zombie["dead"] = True

        cells.fumes = [fume for fume in cells.fumes if not fume["shot"]]

    def zomboss(self, cells):
        for zombie in self.zombies:
            if zombie["zomboss"]:
                if time.time() - zombie["zombie_time"] >= 30:
                    for i in range(zombie["zombie_amount"]):
                        zombie_y = random.choice(self.ways)
                        zombie_x = float(random.randint(890, 940))
                        zombie_rect = pg.Rect(int(zombie_x) + 80, zombie_y, 40, 144)
                        self.zombies.append(
                            {"x": zombie_x, "y": zombie_y, "rect": zombie_rect, "points": 20,
                             "zombie_pictures": self.coneheaad_zombie_pictures, "index": 0, "attack_index": 0,
                             "picture_time": time.time(), "line": [((zombie_y - 20) // 100) + 1],
                             "die_animation": False, "dead": False, "dead_animation_index": 0,
                             "die_time": time.time(), "zombie_move": True, "zomboss": False})
                    zombie["zombie_time"] = time.time()
                    zombie["zombie_amount"] = min(5, zombie["zombie_amount"] + 1)
                if time.time() - zombie["grav_time"] >= 35:
                    for i in range(2):
                        for plant in cells.plants[:]:
                            grav_cell = plant["rect"]
                            plant["active"] = False
                            cells.plants.remove(plant)
                            break
                        grav_x = grav_cell.x
                        grav_y = grav_cell.y
                        self.grave.append({"x": grav_x, "y": grav_y, "points": 12, "alive": True, "rect": grav_cell, "line": ((grav_y - 20) // 100) + 1})
                    zombie["grav_time"] = time.time()

        self.grave = [grav for grav in self.grave if grav["alive"]]