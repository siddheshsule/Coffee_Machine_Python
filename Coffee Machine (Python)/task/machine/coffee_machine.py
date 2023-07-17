class CoffeeMachine:
    """
    A simple CoffeeMachine class.
    """
    WATER_PER_CUP = 200
    MILK_PER_CUP = 50
    BEANS_PER_CUP = 15
    ESPRESSO_PRICE = 4
    LATTE_PRICE = 7
    CAPPUCCINO_PRICE = 6

    def __init__(self, available_water, available_milk, available_beans, disposable_cups, money):
        """
        Initialize a CoffeeMachine object.

        Args:
            available_water (int): Initial amount of water in milliliters.
            available_milk (int): Initial amount of milk in milliliters.
            available_beans (int): Initial amount of coffee beans in grams.
            disposable_cups (int): Initial number of disposable cups.
            money (int): Initial amount of money in dollars.
        """
        self._available_water = available_water
        self._available_milk = available_milk
        self._available_beans = available_beans
        self._disposable_cups = disposable_cups
        self._money = money

    def calculate_required_water(self, cups_of_coffee):
        """
        Calculate and print the required amount of water for the specified number of cups.

        Args:
            cups_of_coffee (int): Number of cups of coffee.

        Returns:
            None
        """
        required_water = int(cups_of_coffee) * self.WATER_PER_CUP
        print(f"{required_water} ml of water")

    def calculate_required_milk(self, cups_of_coffee):
        """
        Calculate and print the required amount of milk for the specified number of cups.

        Args:
            cups_of_coffee (int): Number of cups of coffee.

        Returns:
            None
        """
        required_milk = int(cups_of_coffee) * self.MILK_PER_CUP
        print(f"{required_milk} ml of milk")

    def calculate_required_beans(self, cups_of_coffee):
        """
        Calculate and print the required amount of coffee beans for the specified number of cups.

        Args:
            cups_of_coffee (int): Number of cups of coffee.

        Returns:
            None
        """
        required_beans = int(cups_of_coffee) * self.BEANS_PER_CUP
        print(f"{required_beans} g of coffee beans")

    def add_water_to_machine(self, water_amount):
        """
        Add the specified amount of water to the coffee machine.

        Args:
            water_amount (int): Amount of water to add in milliliters.

        Returns:
            None
        """
        self._available_water += int(water_amount)

    def add_milk_to_machine(self, milk_amount):
        """
        Add the specified amount of milk to the coffee machine.

        Args:
            milk_amount (int): Amount of milk to add in milliliters.

        Returns:
            None
        """
        self._available_milk += int(milk_amount)

    def add_beans_to_machine(self, beans_amount):
        """
        Add the specified amount of coffee beans to the coffee machine.

        Args:
            beans_amount (int): Amount of coffee beans to add in grams.

        Returns:
            None
        """
        self._available_beans += int(beans_amount)

    def add_disposable_cups(self, cups_amount):
        """
        Add the specified number of disposable cups to the coffee machine.

        Args:
            cups_amount (int): Number of disposable cups to add.

        Returns:
            None
        """
        self._disposable_cups += int(cups_amount)

    def calculate_possible_coffee_cups(self):
        """
        Calculate the maximum number of coffee cups that can be made with the available resources.

        Returns:
            int: Maximum number of cups that can be made.
        """
        return min(
            self._available_water / self.WATER_PER_CUP,
            self._available_milk / self.MILK_PER_CUP,
            self._available_beans / self.BEANS_PER_CUP
        )

    def take_money_from_machine(self):
        """
        Take all the money from the coffee machine.

        Returns:
            None
        """
        print(f"I gave you ${self._money}")
        self._money = 0

    def display_summary(self):
        """
        Display the current status of the coffee machine.

        Returns:
            None
        """
        print("The coffee machine has:")
        print(f"{self._available_water} ml of water")
        print(f"{self._available_milk} ml of milk")
        print(f"{self._available_beans} g of coffee beans")
        print(f"{self._disposable_cups} disposable cups")
        print(f"${self._money} of money")

    def check_resources(self, water, beans, milk):
        """
        Check if there are enough resources to make the specified coffee.

        Args:
            water (int): Required amount of water in milliliters.
            beans (int): Required amount of coffee beans in grams.
            milk (int): Required amount of milk in milliliters.

        Returns:
            bool: True if there are enough resources, False otherwise.
        """
        if self._available_water >= water and self._available_beans >= beans:
            if self._available_milk >= milk:
                print("I have enough resources, making you a coffee!")
                return True
            else:
                print("Sorry, not enough milk!")
        elif self._available_beans < beans:
            print("Sorry, not enough coffee beans!")
        else:
            print("Sorry, not enough water!")
        return False

    def buy_coffee(self, user_selection):
        """
        Buy coffee based on the user's selection.

        Args:
            user_selection (str): User's selection of coffee type.

        Returns:
            None
        """
        if user_selection == "1":
            if self.check_resources(250, 16, 0):
                self._available_water -= 250
                self._available_beans -= 16
                self._disposable_cups -= 1
                self._money += self.ESPRESSO_PRICE
        elif user_selection == "2":
            if self.check_resources(350, 75, 20):
                self._available_water -= 350
                self._available_milk -= 75
                self._available_beans -= 20
                self._disposable_cups -= 1
                self._money += self.LATTE_PRICE
        elif user_selection == "3":
            if self.check_resources(200, 100, 12):
                self._available_water -= 200
                self._available_milk -= 100
                self._available_beans -= 12
                self._disposable_cups -= 1
                self._money += self.CAPPUCCINO_PRICE

    def fill_machine(self, water_amount, milk_amount, beans_amount, cups_amount):
        """
        Fill the coffee machine with the specified amounts of water, milk, coffee beans, and disposable cups.

        Args:
            water_amount (int): Amount of water to add in milliliters.
            milk_amount (int): Amount of milk to add in milliliters.
            beans_amount (int): Amount of coffee beans to add in grams.
            cups_amount (int): Number of disposable cups to add.

        Returns:
            None
        """
        self.add_water_to_machine(water_amount)
        self.add_milk_to_machine(milk_amount)
        self.add_beans_to_machine(beans_amount)
        self.add_disposable_cups(cups_amount)

def main():
    coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
    while True:
        user_input = input("Write action (buy, fill, take, remaining, exit): ")
        if user_input.lower() == "buy":
            coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
            coffee_machine.buy_coffee(coffee_type)
        elif user_input.lower() == "fill":
            water = input("Write how many ml of water you want to add: ")
            milk = input("Write how many ml of milk you want to add: ")
            beans = input("Write how many grams of coffee beans you want to add: ")
            cups = input("Write how many disposable cups you want to add: ")
            coffee_machine.fill_machine(water, milk, beans, cups)
        elif user_input.lower() == "take":
            coffee_machine.take_money_from_machine()
        elif user_input.lower() == "remaining":
            coffee_machine.display_summary()
        elif user_input.lower() == "exit":
            return

if __name__ == "__main__":
    main()
