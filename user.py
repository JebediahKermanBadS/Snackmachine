"""Module for the user class.
"""

from xml.etree import ElementTree


class User():
    """User class
    """

    _tree = ElementTree.parse("./saves/users.xml")
    _root = _tree.getroot()

    def __init__(self, username):
        user = User.get_user_element(username)
        self.name = username
        self.bank_balance = float(user.find("bank_balance").text)

    @staticmethod
    def check_user_password(username, password):
        """Method"""
        user = User.get_user_element(username)
        xml_password = user.find("password").text

        return xml_password == password

    @staticmethod
    def get_user_element(username):
        """Method"""
        for user in list(User._root):
            if username.lower() == user.attrib["name"].lower():
                return user

    @staticmethod
    def add_user(username, password):
        """Method"""
        attributes = {
            "id": f'{len(User._root) + 1}',
            "name": username
        }
        user = ElementTree.SubElement(User._root, "user", attributes)
        user.text = "\n\t\t"
        user.tail = "\n"

        element_password = ElementTree.SubElement(user, "password")
        element_password.text = password
        element_password.tail = "\n\t\t"

        element_salt = ElementTree.SubElement(user, "salt")
        element_salt.text = " "
        element_salt.tail = "\n\t\t"

        element_salt = ElementTree.SubElement(user, "bank_balance")
        element_salt.text = 0.0
        element_salt.tail = "\n\t"

        User._tree.write("users.xml")


if __name__ == "__main__":
    pass
