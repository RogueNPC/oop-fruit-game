from random import randint

class fruit:
    def __init__(self, img, speed, point_value=10):
        self.img = img
        self.speed = randint(15,30)
        self.point_value = point_value