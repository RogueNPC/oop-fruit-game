from fruit import Fruit
from basket import Basket
from golden_fruit import Golden_fruit
from rotten_fruit import Rotten_fruit

class Game_system:
    def __init__(self):
        self.start_game()

    def start_game(self):
        self.create_basket()

    def create_basket(self):
        return Basket()

    def create_fruit(self):
        return Fruit()

    def change_fruit_value(self):
        print(f"The current value of normal fruits is {Fruit.point_value}. The original value of normal fruits is {Fruit.original_value}")
        new_value = input("What would you like the new point value for normal fruits to be? ")
        return Fruit.change_value(new_value)

    def change_golden_value(self):
        print(f"The current value of normal fruits is {Golden_fruit.point_value}. The original value of normal fruits is {Golden_fruit.original_value}")
        new_value = input("What would you like the new point value for normal fruits to be? ")
        return Fruit.change_value(new_value)

    def change_rotten_value(self):
        print(f"The current value of normal fruits is {Rotten_fruit.point_value}. The original value of normal fruits is {Rotten_fruit.original_value}")
        new_value = input("What would you like the new point value for normal fruits to be? ")
        return Fruit.change_value(new_value)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    # Instantiate Game
    game = Game_system()
    game.change_fruit_value()