"""Module for the class Snackmachine
"""

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
    def __init__(self):
        self.current_user = None
        self.products = Product.get_product_dic()

    def buy_product(self, p_id):
        """Method to buy a product
        Arguments:
            p_id {int} -- The id from the product.
        """
        if isinstance(p_id, float):
            p_id = int(p_id)

        if not isinstance(p_id, int):
            raise ValueError("The id must be an integer.")

        if not self.product_exist(p_id):
            raise ProductException(
                f"The product with the id '{p_id}' doesn't exist. "
                f"Please try another id.")

        product = self.products[p_id]

        if self.current_user.bank_balance < product.price:
            raise BankBalanceException(
                f"Not enought money to buy the product with the ID "
                f"'{p_id}'. Missing money: "
                f"{(product.price - self.current_user.bank_balance):.2f}€")

        if product.amount <= 0:
            raise ProductException(
                f"The product with the id '{p_id}' is empty."
                f"Please try another one.")

        self.products[p_id].buy_product()
        self.current_user.bank_balance -= product.price

    def pay_money_in(self, amount):
        """Method to may money in and and to the bank balance.
        Arguments:
            amount {int, float} -- The amount of money you want to pay in.
        """
        if amount >= 0:
            self.current_user.bank_balance += amount

    def get_bank_balance(self):
        """Method to get the current bank balance.
        Returns:
            str -- The bank balance. Format = 0.00€
        """
        return (f"Hello '{self.current_user.name}'"
                f"Your bank balance is: {self.current_user.bank_balance:.2f}€")

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
