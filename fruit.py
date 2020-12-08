import random
from random import randint

class Fruit:
    fruit_list = ["grape", "apple", "melon", "mango", "lemon", "orange", "banana"]
    original_value = 10
    point_value = 10

    def __init__(self):
        self.name = random.choice(Fruit.fruit_list)
        self.speed = randint(15,30)

    @classmethod
    def change_value(cls, new_point_value):
        cls.point_value = new_point_value
        print(f"The new point value of normal fruits is {new_point_value}.")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    testfruit = Fruit()