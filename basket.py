class Basket:
    def __init__(self):
        self.__pts = 0
        self.__caught_fruits = 0
        self.__basket_contents = []

    def catch_fruit(self, point_value, name):
        self.__pts += point_value
        self.__caught_fruits += 1
        self.__basket_contents.append(name)
        print("You caught a fruit!")

    def check_contents(self):
        print(f"You have {self.__caught_fruits} fruits in your basket.")
        for fruit in self.__basket_contents:
            print(fruit)

    def check_points(self):
        print(f"You have {self.__pts} points in total.")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    testbasket = Basket()
    testbasket.catch_fruit(10, "melon")
    testbasket.catch_fruit(10, "banana")
    testbasket.catch_fruit(50, "golden-apple")
    testbasket.catch_fruit(-20, "durian")
    testbasket.check_contents()
    testbasket.check_points()