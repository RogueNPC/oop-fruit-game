import random
from random import randint

class Fruit:
    def __init__(self, img, point_value=10):
        self.img = img
        self.speed = randint(15,30)
        self.point_value = point_value

    def create_fruit(self):
        imgs = ["test"]
        rand_img = random.choice(imgs)
        return Fruit(rand_img)
