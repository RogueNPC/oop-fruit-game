from random import randint
from fruit import Fruit

class Golden_fruit(Fruit):
    original_value = 50
    point_value = 50

    def __init__(self):
        self.name = "golden-apple"
        self.speed = randint(30,45)

    @classmethod
    def change_value(cls, new_point_value):
        cls.point_value = new_point_value
        print(f"The new point value of golden fruits is {new_point_value}.")

    @classmethod
    def reset_value(cls):
        cls.point_value = cls.original_value
        print(f"The point value of golden fruits have been reset to {cls.original_value}")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    goldfruit = Golden_fruit()
    print(goldfruit.point_value)
    print(goldfruit.fruit_info())
    Golden_fruit.change_value(40)
    goldfruit1 = Golden_fruit()
    print(goldfruit1.point_value)