"""The main script for the snackmachine.
"""

import sys
import my_snackmachine


def main():
    """The main method for the snackmachine script.
    """

    machine = my_snackmachine.Snackmachine()

    cmd_func_dic = {
        "payin": [machine.pay_money_in, 1],
        "buyprod": [machine.buy_product, 1],
        "printprod": [machine.get_product_list, 0],
        "printmoney": [machine.get_bank_balance, 0],
        "exit": [exit, 0]
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

        else:
            print("Unknown command. Try again.")


if __name__ == "__main__":
    main()
