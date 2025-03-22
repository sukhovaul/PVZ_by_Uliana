import pygame as pg

class Menu():
    def __init__(self, width, height, image = None):
        self.width = width
        self.height = height

        self.screen = pg.display.set_mode((self.width, self.height))
        try:
            self.image = pg.image.load(image)
            self.image = pg.transform.scale(self.image, (1400,600))
        except:
            self.image = pg.Surface((1400,600))
            self.image.fill((0,100,0))

        self.font_title = pg.font.Font('fonts/main_font.ttf', 78)
        self.font_button = pg.font.Font('fonts/main_font.ttf', 45)

        self.button1 = pg.Rect(780, 200, 300, 75)
        self.button2 = pg.Rect(780, 300, 300, 75)

        self.action = None

        pg.mixer.init()

        pg.mixer.music.load('music/plants_vs_zombies_02 - Crazy Dave (Intro Theme).mp3')
        pg.mixer.music.play(-1)

    def draw(self):
        self.screen.blit(self.image,(0,0))

        title = self.font_title.render('Plants vs Zombies', True, (30,30,30))
        self.screen.blit(title, (740,100))

        pg.draw.rect(self.screen, (70,70,70), self.button1, 0, border_radius=5)
        pg.draw.rect(self.screen, (70,70,70), self.button2, 0, border_radius=5)

        button1_text = self.font_button.render('Начать игру', True, (180,180,180))
        button2_text = self.font_button.render('Выйти', True, (180,180,180))

        self.screen.blit(button1_text,(self.button1[0]+65, self.button1[1] + 12))
        self.screen.blit(button2_text, (self.button2[0]+95, self.button2[1] + 12))

        pg.display.flip()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.button2.collidepoint(event.pos):
                    self.action = 'exit_game'
                    pg.quit()
                    exit()
                    return False
                elif self.button1.collidepoint(event.pos):
                    self.action = 'start_game'
                    return False
        return True
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.draw()