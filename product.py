"""Module for the class Product
"""

from xml.etree import ElementTree


class Product():
    """A class to store data from a product
    """

    _path_xmlFile = "./saves/products.xml"
    _tree = ElementTree.parse(_path_xmlFile)

    def __init__(self, name, price, amount, product_id=None):
        if id is None:
            self._id = Product.get_id_by_name(name)
        else:
            self._id = product_id

        self.name = name
        self.price = price
        self.amount = amount

    def buy_product(self):
        """Method"""
        self.amount -= 1
        Product.change_amount(Product.get_id_by_name(self.name), self.amount)

    def refill_product(self, amount):
        """Method"""
        self.amount += amount
        Product.change_amount(self._id, self.amount)

    def to_string(self):
        """Method"""
        return (f"Price: {self.price:.2f}€\t"
                f"Amount: {self.amount}\t"
                f"Name: '{self.name}'")

    @staticmethod
    def get_product_dic():
        """Method"""
        dictionary = {}
        for _p in list(Product._tree.getroot()):
            key = int(_p.attrib["id"])

            name = _p.attrib["name"]
            price = float(_p.find("price").text)
            amount = int(_p.find("amount").text)

            dictionary[key] = Product(name, price, amount, key)
        return dictionary

    @staticmethod
    def get_id_by_name(name):
        """Method"""
        for _p in list(Product._tree.getroot()):
            if _p.attrib["name"] == name:
                return int(_p.attrib["id"])

    @staticmethod
    def change_amount(product_id, amount):
        """Method"""
        for _p in list(Product._tree.getroot()):
            if int(_p.attrib["id"]) == product_id:
                _p.find("amount").text = str(amount)
                print(_p.find("amount").text)

                Product._tree.write(Product._path_xmlFile)


if __name__ == "__main__":
    pass
