from random import randint

class Golden_fruit:
    def __init__(self, img, point_value=50):
        super().__init__(img, point_value)
        self.speed = randint(30,40)