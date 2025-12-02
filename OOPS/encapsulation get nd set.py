class Wallet:
    def __init__(self):
        self.__money = 0  # private variable

    # Getter method
    def get_money(self):
        return self.__money

    # Setter method
    def set_money(self, amount):
        if amount >= 0:
            self.__money = amount
        else:
            print("Invalid amount! Cannot set negative balance.")

# Create an object of the Wallet class
my_wallet = Wallet()

# Set money using setter
my_wallet.set_money(1000)

# Get money using getter
print("Current Balance:", my_wallet.get_money())  # Output: Current Balance: 1000

# Try setting a negative amount
my_wallet.set_money(-500)  # Output: Invalid amount! Cannot set negative balance.

# Check balance again to confirm it didn't change
print("Updated Balance:", my_wallet.get_money())  # Output: Updated Balance: 1000

