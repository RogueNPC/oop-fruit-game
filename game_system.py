from fruit import Fruit
from basket import Basket
from golden_fruit import Golden_fruit
from rotten_fruit import Rotten_fruit
from random import randint

class Game_system:
    def __init__(self):
        self.__basket = self.__create_basket()

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

    def reset_fruit_value(self):
        return Fruit.reset_value()

    def reset_golden_value(self):
        return Golden_fruit.reset_value()

    def reset_rotten_value(self):
        return Rotten_fruit.reset_value()

    def catch_fruit(self):
        examplefruit = self.__create_fruit()
        Basket.catch_fruit(self.__basket, examplefruit.point_value, examplefruit.fruit_info())

    def check_contents(self):
        Basket.check_contents(self.__basket)

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