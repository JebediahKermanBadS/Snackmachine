"""The main script for the snackmachine.
"""

import sys
import my_snackmachine

def main():
    """The main method for the snackmachine script.
    """

    machine = my_snackmachine.Snackmachine()

    cmd_func_dic = {
        "payin": [machine.pay_money_in, 1, " - PayIn <amount>\tPay money into your bank account."],
        "buypr": [machine.buy_product, 1, " - BuyPr <pr_id>\tBuy a product."],
        "bb": [machine.get_bank_balance, 0, " - bb\t\t\tGet your current bank balance."],
        "pl": [machine.get_product_list, 0, " - pl\t\t\tGet a list of all products."],
        "exit": [exit, 0, " - exit\t\t\tExit"]
    }

    while True:
        inp = input(" - ").lower().split(" ")
        cmd = inp[0]

        if cmd_func_dic.keys().__contains__(cmd):
            func = cmd_func_dic[cmd]

            try:
                if func[1] == 1:
                    parameter = float(inp[1])
                    func[0](parameter)
                else:
                    print(func[0]())

            except my_snackmachine.BankBalanceException:
                print(sys.exc_info()[1])

            except my_snackmachine.ProductException:
                print(sys.exc_info()[1])

            except ValueError:
                print(sys.exc_info()[1])
        elif cmd == "help":
            print("------COMMANDS---------------------------------------------------")
            for func in cmd_func_dic.values():
                print(func[2])
            print("-----------------------------------------------------------------")
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
