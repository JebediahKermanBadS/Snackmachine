"""Module for the class Product
"""

class Product():
    """A class to store data from a product
    """

    name = ""
    price = 0.0
    amount = 0

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def inc_amount(self):
        """Increase the amount of the product by 1
        """
        self.amount = self.amount + 1

    def dec_amount(self):
        """Decrease the amount of the product by 1
        """
        self.amount = self.amount - 1

    def to_string(self):
        """Write the data from the class into a string.

        Returns:
            string -- The string
        """

        return f"Name:'{self.name}' Price:{self.price}€ Amount:{self.amount}"
