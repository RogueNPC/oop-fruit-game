from random import randint
from fruit import Fruit

class Rotten_fruit(Fruit):
    # original_value attribute used to reset point_value attribute (private, should not be modified)
    __original_value = -20
    # point_value attribute (public, can be accessed when printing score in Game_system)
    point_value = -20

    def __init__(self):
        # Rotten_fruit attributes (protected, accessable by super Fruit class)
        self._name = "rotten-banana"
        self._speed = randint(15,30)

    # classmethods that change/reset the point_value (public, accessed by Game_system)
    @classmethod
    def change_value(cls, new_pts_value):
        cls.point_value = new_pts_value
        print(f"The new point value of rotten fruits is {new_pts_value}.")

    @classmethod
    def reset_value(cls):
        cls.point_value = cls.__original_value
        print(f"The point value of rotten fruits have been reset to {cls.__original_value}.")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    rotfruit = Rotten_fruit()
    print(rotfruit.point_value)
    print(rotfruit.fruit_info())
    Rotten_fruit.change_value(-35)
    rotfruit1 = Rotten_fruit()
    print(rotfruit1.point_value)