from Picture import Picture as Picture
from EstateEnum import EstateEnum as EstateEnum
import math


class Dino(Picture):
    estate = 0
    JUMP_HEIGHT = 20
    jump_angle = 30
    JUMP_SPEED = 20
    DINO_X = 124
    DINO_Y = 300
    dino_x = 124
    dino_y = 300
    dino_y_bend = 0
    dino_x_bend = 0
    alterna = 1


    def __init__(self, estate, imgJump, imgRunL, imgRunR, imgBendL, imgBendR, imgDead):
        self.estate = estate
        self.imgJump = imgJump
        self.imgRunL = imgRunL
        self.imgRunR = imgRunR
        self.imgBendL = imgBendL
        self.imgBendR = imgBendR
        self.imgDead = imgDead
        self.set_image(imgRunL)
        self.dino_y_bend = self.dino_y+(self.imgRunR.image.height-self.imgBendR.image.height)
        self.dino_x_bend = self.dino_x - (self.imgRunR.image.width - self.imgBendR.image.width)
        self.speed = 0

    def get_estate(self):
        return self.estate

    def set_estate(self, estate):
        self.estate = estate

    def get_estate(self):
        return self.estate

    def reset_jump_speed(self):
        Dino.JUMP_SPEED = Dino.JUMP_HEIGHT

    def set_image(self, image):
        self.image = image

    def get_speed(self):
        return self.speed

    def set_speed(self,speed):
        self.speed = speed

    def jump(self, gravity):
        if self.get_estate() == EstateEnum.JUMP:
            self.pos_y -= self.JUMP_SPEED * math.sin(math.radians(self.jump_angle))
            Dino.JUMP_SPEED -= gravity
            if self.JUMP_SPEED < -self.JUMP_HEIGHT:
                self.set_estate(EstateEnum.RUN)
                Dino.JUMP_SPEED = Dino.JUMP_HEIGHT

    #Realiza un retardo de retardo ciclos de reloj
    def retarder(self, retardo):
        if self.alterna == retardo:
            self.alterna = 0

        self.alterna = self.alterna + 1

        if self.alterna < retardo / 2:
            return False
        else:
            return True

    def pinta_dino(self, gravity):
        self.set_image(self.imgRunL)
        if self.get_estate() == EstateEnum.JUMP:
            self.jump(gravity)
            self.imgJump.set_position_and_paint(self.get_pos_x(), self.get_pos_y())
        elif self.get_estate() == EstateEnum.BEND:
            if self.retarder(50):
                self.imgBendL.set_position_and_paint(self.dino_x_bend, self.dino_y_bend)
                self.set_image(self.imgBendR)
                self.set_pos_y(self.dino_y_bend)
                self.set_pos_x(self.dino_x_bend)
            else:
                self.imgBendR.set_position_and_paint(self.dino_x_bend, self.dino_y_bend)
                self.set_image(self.imgBendR)
                self.set_pos_y(self.dino_y_bend)
                self.set_pos_x(self.dino_x_bend)
        elif self.get_estate() == EstateEnum.RUN:
            self.set_pos_y(self.DINO_Y)
            self.set_pos_x(self.DINO_X)
            if self.retarder(50):
                self.imgRunL.set_position_and_paint(self.get_pos_x(), self.dino_y)
            else:
                self.imgRunR.set_position_and_paint(self.get_pos_x(), self.dino_y)
        elif self.get_estate() == EstateEnum.DEAD:
            self.imgDead.set_position_and_paint(self.get_pos_x(), self.dino_y)

    def reset(self, speed):
        self.set_pos_x(self.DINO_X)
        self.set_pos_y(self.DINO_Y)
        self.set_speed(speed)
        self.velocidad_x = self.get_speed()
        self.set_estate(EstateEnum.RUN)
        self.set_image(self.imgRunL)
        Dino.JUMP_SPEED = Dino.JUMP_HEIGHT
