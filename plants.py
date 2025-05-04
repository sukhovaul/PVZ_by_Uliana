import pygame as pg
import time


class Plants():
    def __init__(self, screen):
        self.screen = screen
        self.sunflower_card = pg.image.load('pictures/cards/card_sunflower.png')
        self.sunflower_card = pg.transform.scale(self.sunflower_card, (58, 73))
        self.peashooter_card = pg.image.load('pictures/cards/card_peashooter.png')
        self.peashooter_card = pg.transform.scale(self.peashooter_card, (58, 73))
        self.wallnut_card = pg.image.load('pictures/cards/card_wallnut.png')
        self.wallnut_card = pg.transform.scale(self.wallnut_card, (58, 73))

        self.gray_sunflower = pg.image.load('pictures/cards/card_sunflower-gray.png')
        self.gray_sunflower = pg.transform.scale(self.gray_sunflower, (58, 73))
        self.gray_peashooter = pg.image.load('pictures/cards/card_peashooter-gray.png')
        self.gray_peashooter = pg.transform.scale(self.gray_peashooter, (58, 73))
        self.gray_wallnut = pg.image.load('pictures/cards/card_wallnut-gray.png')
        self.gray_wallnut = pg.transform.scale(self.gray_wallnut, (58, 73))

        self.sunflower_time = 0  # Доступны сразу
        self.wallnut_time = 0
        self.peashooter_time = 0

        self.level = None

        self.sunflower_rect = pg.Rect(64, 0, 64, 89)
        self.wallnut_rect = pg.Rect(192, 0, 64, 89)
        self.peashooter_rect = pg.Rect(128, 0, 64, 89)
        self.cards = [
            {"rect": self.sunflower_rect, "amount": 50, "plant": 'sunflower', "availible": False},
            {"rect": self.wallnut_rect, "amount": 50, "plant": 'wallnut', "availible": False},
            {"rect": self.peashooter_rect, "amount": 100, "plant": 'peashooter', "availible": False}
        ]

        self.active_plant = None
        self.plant_amount = 0

    def draw_cards(self, suns_amount):
        current_time = time.time()
        if self.level >= 1:
            self.screen.blit(self.gray_sunflower, (74, 5))
            self.screen.blit(self.gray_peashooter, (132, 5))
        elif self.level >= 2:
            self.screen.blit(self.gray_wallnut, (190, 5))

        for card in self.cards:
            if card["plant"] == 'sunflower':
                card["availible"] = (suns_amount >= card["amount"] and current_time >= self.sunflower_time)
                if card["availible"] and self.level>=1:
                    self.screen.blit(self.sunflower_card, (74, 5))

            elif card["plant"] == 'peashooter':
                card["availible"] = (suns_amount >= card["amount"] and
                                     current_time >= self.peashooter_time)
                if card["availible"]  and self.level >= 1:
                    self.screen.blit(self.peashooter_card, (132, 5))

            elif card["plant"] == 'wallnut':
                card["availible"] = (suns_amount >= card["amount"] and
                                     current_time >= self.wallnut_time)
                if card["availible"] and self.level >= 2:
                    self.screen.blit(self.wallnut_card, (190, 5))

    def choose_plant(self, pos):
        for card in self.cards:
            if card["rect"].collidepoint(pos) and card["availible"]:
                self.active_plant = card["plant"]
                self.plant_amount = card["amount"]

    def plant_placed(self):
        if self.active_plant:
            if self.active_plant == 'sunflower':
                self.sunflower_time = time.time() + 5
            elif self.active_plant == 'peashooter':
                self.peashooter_time = time.time() + 5
            elif self.active_plant == 'wallnut':
                self.wallnut_time = time.time() + 5