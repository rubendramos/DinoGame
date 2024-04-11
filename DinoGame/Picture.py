from Image import Image as Image


class Picture:

    pos_x = 0
    pos_y = 0
    alto = 0
    ancho = 0
    visible = True
    obstaculo: bool = False

    def __init__(self, image, pos_x, pos_y, display, obstaculo):
        self.image = image
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.display = display
        self.obstaculo = obstaculo

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def set_pos_x(self, pos_x):
        self.pos_x = pos_x

    def set_pos_y(self, pos_y):
        self.pos_y = pos_y

    def get_image(self):
        return self.image

    def es_obstaculo(self):
        return self.obstaculo

    def set_obstaculo(self, esObstaculo):
        self.obstaculo = esObstaculo

    def paint(self):
        self.display.blit(self.image.file, (self.pos_x, self.pos_y))

    def set_position_and_paint(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.paint()

    def es_visible(self):
        if 0 <= self.pos_x <= 800:
            self.visible = True
        else:
            self.visible = False
