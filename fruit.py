import random
from random import randint

class Fruit:
    __fruit_list = ["grape", "apple", "melon", "mango", "lemon", "orange", "banana"]
    original_value = 10
    point_value = 10

    def __init__(self):
        self.name = random.choice(Fruit.__fruit_list)
        self.speed = randint(15,30)

    @classmethod
    def change_value(cls, new_point_value):
        cls.point_value = new_point_value
        print(f"The new point value of normal fruits is {new_point_value}.")

    @classmethod
    def reset_value(cls):
        cls.point_value = cls.original_value
        print(f"The point value of golden fruits have been reset to {cls.original_value}")

    def fruit_info(self):
        return f"A {self.name} worth {self.point_value} points."


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    testfruit = Fruit()
    print(testfruit.point_value)
    print(testfruit.fruit_info())
    Fruit.change_value(15)
    testfruit1 = Fruit()
    print(testfruit1.point_value)