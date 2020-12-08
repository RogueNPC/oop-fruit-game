from random import randint
from fruit import Fruit

class Rotten_fruit(Fruit):
    original_value = -20
    point_value = -20

    def __init__(self):
        self.name = "durian"
        self.speed = randint(15,30)

    @classmethod
    def change_value(cls, new_point_value):
        cls.point_value = new_point_value
        print(f"The new point value of rotten fruits is {new_point_value}.")

    @classmethod
    def reset_value(cls):
        cls.point_value = cls.original_value
        print(f"The point value of golden fruits have been reset to {cls.original_value}")

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    rotfruit = Rotten_fruit()
    print(rotfruit.point_value)
    print(rotfruit.fruit_info())
    Rotten_fruit.change_value(-35)
    rotfruit1 = Rotten_fruit()
    print(rotfruit1.point_value)