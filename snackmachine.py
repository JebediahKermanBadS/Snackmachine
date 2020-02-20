"""Module for the class Snackmachine
"""

import sys
from product import Product

class BankBalanceException(Exception):
    """Raise if there is a problem with the bank balance
    """

class ProductException(Exception):
    """Raise if there is a problem with a product.
    """

class Snackmachine():
    """The class Snackmachine
    """

    bank_balance = 0.0
    products = None

    def __init__(self):
        self.products = {
            0x00: Product("Mars", 1.20, 2),
            0x01: Product("Twix", 1.20, 3),
            0x02: Product("Duplo", 0.60, 9),
            0x03: Product("Pringels", 1.50, 7),
            0x04: Product("Raffaello", 0.80, 8),
            0x05: Product("PickUp", 0.80, 11),
            0x06: Product("Hanuta", 0.80, 5),
            0x07: Product("Kinder Riegel", 0.60, 0),
            0x08: Product("Corny", 1.20, 3),
            0x09: Product("Kinder Country", 1.20, 1),
            0x0A: Product("Bueno", 1.20, 0),
        }

    def buy_product(self, p_id):
        """Method to buy a product
        Arguments:
            p_id {int} -- The id from the product.
        """
        if not isinstance(p_id, int):
            raise ValueError("The id must be an integer.")

        if not self.product_exist(p_id):
            raise ProductException(
                f"The product with the id '{p_id}' doesn't exist. Please try another id.")

        product = self.products[p_id]

        if self.bank_balance < product.price:
            raise BankBalanceException(
                f"Not enought money to buy the product with the ID "
                f"'{p_id}'. Missing money: {(product.price - self.bank_balance):.2f}€")

        if product.amount <= 0:
            raise ProductException(
                f"The product with the id '{p_id}' is empty. Please try another one.")

        self.products[p_id].dec_amount()
        self.bank_balance -= product.price

    def pay_money_in(self, amount):
        """Method to may money in and and to the bank balance.
        Arguments:
            amount {int, float} -- The amount of money you want to pay in.
        """
        if amount >= 0:
            self.bank_balance += amount

    def get_bank_balance(self):
        """Method to get the current bank balance.
        Returns:
            str -- The bank balance. Format = 0.00€
        """
        return f"{self.bank_balance:.2f}€"

    def get_product_list(self):
        """Method to get the complete list of all products.
        Returns:
            str -- The list in string format.
        """

        str_list = ""
        for p_id in self.products:
            str_list += f"ID:'{p_id}'\t{self.products[p_id].to_string()}\n"

        return str_list[:-1]

    def product_exist(self, p_id):
        """Check if the product is existing
        Arguments:
            p_id {int} -- The id of the product to check
        Returns:
            bool -- returns True if the product exists and False if not.
        """
        return self.products.keys().__contains__(p_id)

def main():
    """Main method
    """

    machine = Snackmachine()

    machine.pay_money_in(200)
    try:
        machine.buy_product(9)
    except BankBalanceException:
        print(sys.exc_info()[1])

if __name__ == "__main__":
    main()
