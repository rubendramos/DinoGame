from enum import Enum
from Image import Image



class EstateEnum(Enum):
    STAY = ("STAY")
    RUN = ("RUN")
    JUMP = ("JUMP")
    BEND = ("BEND")
    DEAD = ("DEAD")

    @property
    def value(self):
        return super().value[0]

    @property
    def price(self):
        return super().value[1]