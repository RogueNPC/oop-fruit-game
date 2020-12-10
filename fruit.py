import random
from random import randint

class Fruit:
    # fruit_list attribute contains all possible fruits generatable (private, should not be modified)
    __fruit_list = ["grape", "apple", "melon", "mango", "lemon", "orange", "banana"]
    # original_value attribute used to reset point_value attribute (private, should not be modified)
    __original_value = 10
    # point_value attribute (public, can be accessed when printing score in Game_system)
    point_value = 10

    def __init__(self):
        # Fruit attributes (protected)
        self._name = random.choice(Fruit.__fruit_list)
        self._speed = randint(15,30)

    # classmethods that change/reset the point_value (public, accessed by Game_system)
    @classmethod
    def change_value(cls, new_pts_value):
        cls.point_value = new_pts_value
        print(f"The new point value of normal fruits is {new_pts_value}.")

    @classmethod
    def reset_value(cls):
        cls.point_value = cls.__original_value
        print(f"The point value of normal fruits have been reset to {cls.__original_value}.")

    # instance method to print out fruit info (public, used by Game_system and inherited by subclasses)
    def fruit_info(self):
        return f"A {self._name} worth {self.point_value} points."


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    testfruit = Fruit()
    print(testfruit.point_value)
    print(testfruit.fruit_info())
    Fruit.change_value(15)
    testfruit1 = Fruit()
    print(testfruit1.point_value)