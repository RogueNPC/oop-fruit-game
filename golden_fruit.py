from random import randint
from fruit import Fruit

class Golden_fruit(Fruit):
    original_value = 50
    point_value = 50

    def __init__(self, name):
        self.name = "golden-apple"
        self.speed = randint(30,45)

    @classmethod
    def change_value(cls, new_point_value):
        cls.point_value = new_point_value
        print(f"The new point value of golden fruits is {new_point_value}.")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    pass