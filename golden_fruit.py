from random import randint
from fruit import Fruit

class Golden_fruit(Fruit):
    # original_value attribute used to reset point_value attribute (private, should not be modified)
    __original_value = 50
    # point_value attribute (public, can be accessed when printing score in Game_system)
    point_value = 50

    def __init__(self):
        # Golden_fruit attributes (public, accessable by super Fruit class)
        self._name = "golden-apple"
        self._speed = randint(30,45)

    # classmethods that change/reset the point_value (public, accessed by Game_system)
    @classmethod
    def change_value(cls, new_pts_value):
        cls.point_value = new_pts_value
        print(f"The new point value of golden fruits is {new_pts_value}.")

    @classmethod
    def reset_value(cls):
        cls.point_value = cls.__original_value
        print(f"The point value of golden fruits have been reset to {cls.__original_value}.")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    goldfruit = Golden_fruit()
    print(goldfruit.point_value)
    print(goldfruit.fruit_info())
    Golden_fruit.change_value(40)
    goldfruit1 = Golden_fruit()
    print(goldfruit1.point_value)