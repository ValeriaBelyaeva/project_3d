import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'D:/school/project2/resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')