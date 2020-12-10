from fruit import Fruit
from basket import Basket
from golden_fruit import Golden_fruit
from rotten_fruit import Rotten_fruit
from random import randint

class Game_system:
    def __init__(self):
        # basket attribute to hold Basket obj (private, only modified/accessed within class)
        self.__basket = self.__create_basket()

    # constructors (private)
    def __create_basket(self):
        return Basket()

    def __create_fruit(self):
        random_fruit = randint(1, 10)
        if (random_fruit < 8):
            return Fruit()
        elif (random_fruit == 8):
            return Golden_fruit()
        else:
            return Rotten_fruit()

    # changes class variables (public and should be available in the options menu)
    def change_fruit_value(self):
        print(f"The current value of normal fruits is {Fruit.point_value}.")
        new_value = input("What would you like the new point value for normal fruits to be? ")
        return Fruit.change_value(new_value)

    def change_golden_value(self):
        print(f"The current value of normal fruits is {Golden_fruit.point_value}.")
        new_value = input("What would you like the new point value for normal fruits to be? ")
        return Golden_fruit.change_value(new_value)

    def change_rotten_value(self):
        print(f"The current value of normal fruits is {Rotten_fruit.point_value}.")
        new_value = input("What would you like the new point value for normal fruits to be? ")
        return Rotten_fruit.change_value(new_value)

    # resets class variables (public and should be available in the options menu)
    def reset_fruit_value(self):
        return Fruit.reset_value()

    def reset_golden_value(self):
        return Golden_fruit.reset_value()

    def reset_rotten_value(self):
        return Rotten_fruit.reset_value()

    # fills up basket with randomly created fruit
    # (public for user to call for now, but should be private for system to call when user catches a fruit)
    def catch_fruit(self):
        fruit = self.__create_fruit()
        Basket.catch_fruit(self.__basket, fruit.point_value, fruit.fruit_info())

    # prints out how many and what fruits are caught in the basket
    # (public for user to call for now, but should be private for system to call when user catches a fruit)
    def check_contents(self):
        Basket.check_contents(self.__basket)

    # prints out how many points the user has
    # (public for user to call for now, but should be private for system to call when user catches a fruit)
    def check_points(self):
        Basket.check_points(self.__basket)


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    # Instantiate Game
    game = Game_system()

    print("---------------------------------")
    game.change_fruit_value()
    print("---------------------------------")
    game.change_golden_value()
    print("---------------------------------")
    game.change_rotten_value()
    print("---------------------------------")
    game.reset_fruit_value()
    game.reset_golden_value()
    game.reset_rotten_value()

    print("---------------------------------")
    for foo in range(1,11):
        game.catch_fruit()
    print("---------------------------------")
    game.check_contents()
    print("---------------------------------")
    game.check_points()