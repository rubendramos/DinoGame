from Picture import Picture as Picture
from EstateEnum import EstateEnum as EstateEnum
import math


class Cloud(Picture):
    velocidad_x = 1

    def __init__(self, velocidad, img, pos_x, pos_y):
        self.img = img
        self.velocidad_x = velocidad
        self.img.pos_x = pos_x
        self.img.pos_y = pos_y
        self.set_obstaculo(False)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = self.img.image.height
        self.width = self.img.image.width

    #Asigna la velocidade de pterodaptilo
    def set_velocidad(self, velocidad):
        self.velocidad_x = velocidad


    def pinta_cloud(self):
           # self.img.set_position_and_paint(self.img.pos_x + self.velocidad_x, self.img.pos_y)
            self.img.set_position_and_paint(self.get_pos_x() + self.velocidad_x, self.get_pos_y())
            self.pos_x = self.img.pos_x + self.velocidad_x
