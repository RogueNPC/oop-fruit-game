from random import randint
from fruit import Fruit

class Golden_fruit(Fruit):
    def __init__(self, img, point_value=-100):
        super().__init__(point_value)
        self.img = "golden-apple"
        self.speed = randint(30,40)