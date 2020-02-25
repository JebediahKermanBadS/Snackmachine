"""The main script for the snackmachine.
"""

import sys
import getpass
import my_snackmachine
import user

def set_user(machine):
    """TODO Doku"""
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ", None)

    machine.set_user(username, password)
    print(f"Succesfully set the user to '{machine.current_user.name}'.")

def pay_in(machine):
    """TODO Doku"""
    amount = input("Enter an amount: ")
    if amount.isdigit():
        machine.pay_money_in(float(amount))
    else:
        print(f"{amount} is not a digit. Please try again.")

def buy_prod(machine):
    """TODO Doku"""
    product_id = input("Enter product ID: ")
    if product_id.isdigit():
        machine.buy_product(int(product_id))
        print((f"Succesfully bought the product. "
               f"Your new bank balance is {machine.get_bank_balance()}."))
    else:
        print(f"The entered id '{product_id}' wasn't a digit.")

def bank_balance(machine):
    """TODO Doku"""
    print(f"Your bank balance is: {machine.get_bank_balance()}")

def product_list(machine):
    """TODO Doku"""
    print("-" * 50)
    print(machine.get_product_list())
    print("-" * 50)

def main():
    """The main method for the snackmachine script.
    """

    machine = my_snackmachine.Snackmachine()

    cmd_func_dic = {
        "setuser": [set_user, " - SetUser <username> \t\tSet the current user."],
        "payin": [pay_in, " - PayIn <amount>\t\t\tPay money into your bank account."],
        "buypr": [buy_prod, " - BuyPr <pr_id>\t\t\tBuy a product."],
        "bb": [bank_balance, " - bb\t\t\t\t\tGet your current bank balance."],
        "pl": [product_list, " - pl\t\t\t\t\tGet a list of all products."],
        "exit": [exit, " - exit\t\t\t\t\tExit"]
    }

    while True:
        cmd = input(" - ")

        if cmd_func_dic.keys().__contains__(cmd):
            func = cmd_func_dic[cmd]

            try:
                if cmd == "exit":
                    func[0]()
                else:
                    func[0](machine)

            except my_snackmachine.BankBalanceException:
                print(sys.exc_info()[1])

            except my_snackmachine.ProductException:
                print(sys.exc_info()[1])

            except user.UserException:
                print(sys.exc_info()[1])

            except ValueError:
                print(sys.exc_info()[1])

        elif cmd == "help":
            print("-" * 21 + "COMMANDS" + "-" * 21)
            for func in cmd_func_dic.values():
                print(func[1])
            print("-" * 50)

        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
