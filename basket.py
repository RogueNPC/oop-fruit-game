class Basket:
    def __init__(self):
        # Basket attributes (private, only modified/accessed within class)
        self.__pts = 0
        self.__num_fruits = 0
        self.__basket_contents = []

    # fills up basket with randomly created fruit (public for Game_system to call)
    def catch_fruit(self, point_value, name):
        self.__pts += point_value
        self.__num_fruits += 1
        self.__basket_contents.append(name)
        print("You caught a fruit!")

    # prints out how many and what fruits are caught in the basket (public for Game_system to call)
    def check_contents(self):
        print(f"You have {self.__num_fruits} fruits in your basket.")
        for fruit in self.__basket_contents:
            print(fruit)

    # prints out how many points the user has (public for Game_system to call)
    def check_points(self):
        print(f"You have {self.__pts} points in total.")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    testbasket = Basket()
    testbasket.catch_fruit(10, "melon")
    testbasket.catch_fruit(10, "banana")
    testbasket.catch_fruit(50, "golden-apple")
    testbasket.catch_fruit(-20, "rotten-banana")
    testbasket.check_contents()
    testbasket.check_points()