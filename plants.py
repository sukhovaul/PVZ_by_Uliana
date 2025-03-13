import pygame as pg

class Plants():
    def __init__(self, screen):
        self.screen = screen
        self.sunflower_card = pg.image.load('pictures/cards/card_sunflower.png')
        self.peashooter_card = pg.image.load('pictures/cards/card_peashooter.png')
        self.wallnut_card = pg.image.load('pictures/cards/card_wallnut.png')

        self.sunflower_rect = pg.Rect(64,0,64,89)
        self.wallnut_rect = pg.Rect(192,0,64,89)
        self.peashooter_rect = pg.Rect(128,0,64,89)
        self.cards=[{"rect": self.sunflower_rect, "amount": 50, "plant": 'sunflower', "availible": False}, {"rect":self.wallnut_rect, "amount": 50, "plant": 'wallnut', "availible": False}, {"rect":self.peashooter_rect, "amount": 100, "plant": 'peashooter', "availible": False}]

        self.active_plant = None
        self.active_time = None

    def draw_cards(self, suns_amount):
        self.suns_amount = suns_amount
        if self.suns_amount>=100:
            self.screen.blit(self.peashooter_card, (128, 0))
        if self.suns_amount>=50:
            self.screen.blit(self.sunflower_card, (64, 0))
            self.screen.blit(self.wallnut_card, (192, 0))

        for card in self.cards:
            card["availible"]=self.suns_amount>=card["amount"]
    def choose_plant(self,pos):
        for card in self.cards:
            if card["rect"].collidepoint(pos) and card["availible"]:
                self.active_plant = card["plant"]
                print(self.active_plant)