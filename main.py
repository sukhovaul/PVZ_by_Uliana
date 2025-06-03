import pygame as pg
import pytmx
from settings import *
import main_menu
import suns
import cells
import plants
import zombies
import levels_menu

pg.init()
pg.mixer.init()

class Game:
    def __init__(self):
        self.time = None
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('Plants vs Zombies')

        self.tmx_map = pytmx.load_pygame('maps/level1.tmx')
        self.map = 'main_menu'

        self.main_menu = main_menu.Menu(SCREEN_WIDTH, SCREEN_HEIGHT, 'maps/MainMenu.png')
        self.levels_menu = levels_menu.Level_menu(self.screen)

        self.clock = pg.time.Clock()

        self.sound_on = True
        self.sound_on_image = pg.image.load('music/volume_on.png')
        self.sound_on_image = pg.transform.scale(self.sound_on_image,(50,50))
        self.sound_off_image = pg.image.load('music/volume_off.png')
        self.sound_off_image = pg.transform.scale(self.sound_off_image,(50,50))
        self.sound_rect = pg.Rect(1350, 550, 50, 50)

        pg.mixer.music.load('music/plants_vs_zombies_02 - Crazy Dave (Intro Theme).mp3')
        pg.mixer.music.play(-1)

        self.background4 = pg.image.load('maps/Background_1.png')

        self.suns_count = pg.image.load('pictures/suns_count.png')
        self.suns_count_rect = pg.Surface((54, 21))
        self.suns_count_rect.fill((227, 203, 170))
        self.amount_font = pg.font.Font('fonts/main_font.ttf', 20)

        self.fumeshroom_victory = pg.image.load('pictures/cards/fume_shroom_victory.png')
        self.fumeshroom_victory = pg.transform.scale(self.fumeshroom_victory, (798,597))

        self.rect_wallnut_victory = pg.Rect(595, 515 , 185, 35)

        self.availible_level = self.check_level()
        print(self.availible_level)

        self.run()

    def init_level(self, level_num):
        self.tmx_map = pytmx.load_pygame(f'maps/level1.tmx')
        self.sun = suns.Sun(self.screen)
        self.cells = cells.Cells(self.tmx_map, self.screen)
        self.plants = plants.Plants(self.screen, self.cells)
        self.zombies = zombies.Zombies(level_num, self.screen)
        self.zombies.zombies_killed = 0

    def run(self):
        running = True
        self.time = 0
        while running:
            self.clock.tick(60)  # устанавливаем 60 fps
            self.time += 1
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and (self.map == 'level1' or self.map == 'level2' or self.map == 'level3' or self.map == 'level4'):
                self.sun.check_click(event.pos)
                self.cells.fill_cell(event.pos, self.plants, self.plants.plant_amount, self.sun)
                self.plants.choose_plant(event.pos)

                if self.sound_rect.collidepoint(event.pos):
                    if self.sound_on:
                        pg.mixer.music.pause()
                    else:
                        pg.mixer.music.unpause()
                    self.sound_on = not self.sound_on

                if self.zombies.victory:
                    if self.rect_wallnut_victory.collidepoint(event.pos):
                        self.map = 'levels_menu'

            elif self.map == 'levels_menu' and event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.levels_menu.level1_icon_rect.collidepoint(event.pos):
                    self.levels_menu.level = 1

                elif self.levels_menu.level2_icon_rect.collidepoint(event.pos):
                    self.levels_menu.level = 2

                elif self.levels_menu.level3_icon_rect.collidepoint(event.pos):
                    self.levels_menu.level = 3

                elif self.levels_menu.level4_icon_rect.collidepoint(event.pos):
                    self.levels_menu.level = 4

                elif self.levels_menu.menu_button_rect.collidepoint(event.pos):
                    self.map = 'main_menu'

                if self.sound_rect.collidepoint(event.pos):
                    if self.sound_on:
                        pg.mixer.music.pause()
                    else:
                        pg.mixer.music.unpause()
                    self.sound_on = not self.sound_on

        if self.main_menu.action == 'start_game':
            self.map = 'levels_menu'
            self.main_menu.action = None

        elif self.levels_menu.level == 1:
            self.map = 'level1'
            self.init_level(1)
            self.levels_menu.level = None
            self.plants.level = 1

        elif self.levels_menu.level == 2:
            self.map = 'level2'
            self.init_level(2)
            self.levels_menu.level = None
            self.plants.level = 2

        elif self.levels_menu.level == 3:
            self.map = 'level3'
            self.init_level(3)
            self.levels_menu.level = None
            self.plants.level = 3

        elif self.levels_menu.level == 4:
            self.map = 'level4'
            self.init_level(4)
            self.levels_menu.level = None
            self.plants.level = 4

        if self.availible_level == '2':
            self.levels_menu.level2_availible = True

        if self.availible_level == '3':
            self.levels_menu.level2_availible = True
            self.levels_menu.level3_availible = True

        if self.availible_level == '4':
            self.levels_menu.level2_availible = True
            self.levels_menu.level3_availible = True
            self.levels_menu.level4_availible = True

    def update(self):
        if self.map == 'level1' or self.map == 'level2' or self.map == 'level3' or self.map == 'level4':
            self.zombies.create_zombies()
            self.zombies.move()
            self.zombies.hit_plant(self.cells)
            self.sun.update_suns_amount(self.cells)
            self.zombies.pea_hit(self.cells)
            self.cells.peashooter(self.zombies)
            self.cells.cherrybomb(self.zombies)
            self.cells.FumeShroom(self.zombies)
            self.zombies.fume_hit(self.cells)
            self.zombies.zomboss(self.cells)

    def check_level(self):
        with open('level_progress.txt', "r") as file:
            level_progress = file.read() #прочитали файл и сохранили в level_progress
            return level_progress #функция возвращает прочитанный файл

    def draw(self):
        self.screen.fill('black')

        if self.map == 'main_menu':
            self.main_menu.run()

        if self.map == 'levels_menu':
            self.levels_menu.run()

        if self.map == 'level1' or self.map == 'level2' or self.map == 'level3' or self.map == 'level4':
            for layer in self.tmx_map:
                if isinstance(layer, pytmx.TiledTileLayer):
                    for x, y, gid in layer:
                        tile = self.tmx_map.get_tile_image_by_gid(gid)

                        if tile:
                            self.screen.blit(tile, (x * self.tmx_map.tilewidth, y * self.tmx_map.tileheight))

            if self.map == 'level4' or self.map == 'level3':
                self.screen.blit(self.background4, (0, 0))

            self.cells.draw_plants()

            self.sun.draw()
            self.screen.blit(self.suns_count, (0, 0))
            self.screen.blit(self.suns_count_rect, (10, 61))
            amount = self.amount_font.render(str(self.sun.suns_total), True, (30, 30, 30))
            self.screen.blit(amount, (32, 60))

            self.plants.draw_cards(self.sun.suns_total)
            self.zombies.draw_zombies(self.cells)

            if self.zombies.victory and self.map == 'level1':
                self.screen.blit(pg.image.load('pictures/cards/wallnut_victory.png'),(300,0))
                self.levels_menu.level2_availible = True
                self.zombies.level = 2
                with open('level_progress.txt', "w") as file:
                    file.write('2') #переписали значение в файле для сохранения прогресса
                    self.plants.level = 2
                    file.close()

            if self.zombies.victory and self.map == 'level2':
                self.screen.blit(pg.image.load('pictures/cards/cherrybomb_victory.png'),(300,0))
                self.levels_menu.level3_avaiible = True
                self.zombies.level = 3
                with open('level_progress.txt', "w") as file:
                    file.write('3') #переписали значение в файле для сохранения прогресса
                    self.plants.level = 3
                    file.close()

            if self.zombies.victory and self.map == 'level3':
                self.screen.blit(self.fumeshroom_victory, (300,0))
                self.levels_menu.level4_avaiible = True
                self.zombies.level = 4
                with open('level_progress.txt', "w") as file:
                    file.write('4') #переписали значение в файле для сохранения прогресса
                    self.plants.level = 4
                    file.close()

            if self.zombies.victory and self.map == 'level4':
                self.map = 'levels_menu'

        if self.sound_on:
            self.screen.blit(self.sound_on_image, (1350,550))
        else:
            self.screen.blit(self.sound_off_image, (1350, 550))

        pg.display.flip()


if __name__ == '__main__':
    game1 = Game()