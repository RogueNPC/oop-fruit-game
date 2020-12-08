from fruit import Fruit
from basket import Basket
from golden_fruit import Golden_fruit
from rotten_fruit import Rotten_fruit
from random import randint

class Game_system:
    def __init__(self):
        self.basket = self.create_basket()
        self.start_game()

    def start_game(self):
        self.create_basket()

    def create_basket(self):
        return Basket()

    def create_fruit(self):
        random_fruit = randint(1, 10)
        if (random_fruit < 8):
            return Fruit()
        elif (random_fruit == 8):
            return Golden_fruit()
        else:
            return Rotten_fruit()

    def change_fruit_value(self):
        print(f"The current value of normal fruits is {Fruit.point_value}. The original value of normal fruits is {Fruit.original_value}")
        new_value = input("What would you like the new point value for normal fruits to be? ")
        return Fruit.change_value(new_value)

    def change_golden_value(self):
        print(f"The current value of normal fruits is {Golden_fruit.point_value}. The original value of golden fruits is {Golden_fruit.original_value}")
        new_value = input("What would you like the new point value for normal fruits to be? ")
        return Fruit.change_value(new_value)

    def change_rotten_value(self):
        print(f"The current value of normal fruits is {Rotten_fruit.point_value}. The original value of rotten fruits is {Rotten_fruit.original_value}")
        new_value = input("What would you like the new point value for normal fruits to be? ")
        return Fruit.change_value(new_value)

    def catch_fruit(self):
        examplefruit = self.create_fruit()
        Basket.catch_fruit(self.basket, examplefruit.point_value, examplefruit.name)

    def check_contents(self):
        Basket.check_contents(self.basket)

    def check_points(self):
        Basket.check_points(self.basket)


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    # Instantiate Game
    game = Game_system()
    for foo in range(1,11):
        print(game.create_fruit().__dict__)
    # game.change_fruit_value()
    # game.change_golden_value()
    # game.change_rotten_value()
    for foo in range(1,11):
        game.catch_fruit()
    game.check_contents()
    game.check_points()