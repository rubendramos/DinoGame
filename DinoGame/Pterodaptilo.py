from Picture import Picture as Picture
from EstateEnum import EstateEnum as EstateEnum
import math


class Pterodaptilo(Picture):
    velocidad_x = 1
    alterna = 1

    def __init__(self, velocidad, imgUp, imgDown, pos_x, pos_y):
        self.imgUp = imgUp
        self.imgDown = imgDown
        self.velocidad_x = velocidad
        self.imgUp.pos_x = pos_x
        self.imgUp.pos_y = pos_y

        self.imgDown.pos_x = pos_x
        self.imgDown.pos_y = pos_y
        self.set_obstaculo(True)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.set_image(self.imgUp.image)
        self.height = self.imgUp.image.height
        self.width = self.imgUp.image.width
        print("Ini pos_x", self.pos_x)
        print("Ini pos_y", self.pos_x)
        print("Ini imgup_pos_x", self.imgUp.pos_x)
        print("Ini imgup_pos_y", self.imgUp.pos_x)
        print("Ini imgdow_pos_x", self.imgDown.pos_x)
        print("Ini imgdow_pos_y", self.imgDown.pos_x)

    def set_image(self, image):
        self.image = image

    #Asigna la velocidade de pterodaptilo
    def set_velocidad(self, velocidad):
        self.velocidad_x = velocidad

    #Realiza un retardo de retardo ciclos de reloj
    def retarder(self, retardo):
        if self.alterna == retardo:
            self.alterna = 0

        self.alterna = self.alterna + 1

        if self.alterna < retardo / 2:
            return False
        else:
            return True

    def pinta_pterodaptilo(self):
        if self.retarder(50):
            self.set_image(self.imgUp)
            self.set_position_and_paint(self.pos_x + self.velocidad_x, self.pos_y)
            #self.imgDown.pos_x = self.imgUp.pos_x + self.velocidad_x
            #self.pos_x = self.imgUp.pos_x + self.velocidad_x
            print("Uimgup_pos_x", self.imgUp.pos_x)
            print("Uimgup_pos_y", self.imgUp.pos_y)
            print("UimDown_pos_x", self.imgUp.pos_x)
            print("UimDown_pos_y", self.imgUp.pos_y)
            print("Upos_x", self.pos_x)
            print("Upos_y", self.pos_y)

        else:
            self.set_image(self.imgDown)
            self.set_position_and_paint(self.pos_x + self.velocidad_x, self.pos_y)
            #self.imgUp.pos_x = self.imgDown.pos_x + self.velocidad_x
            #self.pos_x = self.imgUp.pos_x + self.velocidad_x
            print("Dimgup_pos_x", self.imgDown.pos_x)
            print("Dimgup_pos_y", self.imgDown.pos_y)
            print("DimDown_pos_x", self.imgDown.pos_x)
            print("DimDown_pos_y", self.imgDown.pos_y)
            print("Dpos_x", self.pos_x)
            print("Dpos_y", self.pos_y)
