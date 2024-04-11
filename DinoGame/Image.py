class Image:
    name = ""
    file = ""
    height = 0
    width = 0

    def __init__(self, name, file,  height, width):
        self.name = name
        self.file = file
        self.height = height
        self.width = width

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_file(self):
        return self.file
