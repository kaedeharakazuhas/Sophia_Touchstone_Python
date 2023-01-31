def greeting():
    print(" *~~~~~~~~~~~~~~~~~~~~~~~~~~~* ")
    print(" |        Welcome to         |")
    print(" |          PyBoba!          |")
    print(" |    ☆*.｡.o(≧▽≦)o.｡.*☆      |")
    print(" *~~~~~~~~~~~~~~~~~~~~~~~~~~~* ")
    user_name = input("What is the name for the order? ")
    print("Thank you, ", user_name, ".", sep='')
    get_money()


def get_money():
    customer_money = float(input("How much do you have to spend at Pyboba "
                                 "today? Please enter your money without the "
                                 "dollar sign and with decimals: "))
    boba_ordering(customer_money)


def display_menu():
    py_menu = {
        "1 - Classic Milk Tea (16oz)": 3.00,
        "2 - Classic Milk Tea (24oz)": 4.00,
        "3 - Passion Fruit Green Tea (16oz)": 5.00,
        "4 - Passion Fruit Green Tea (24oz)": 6.00,
        "5 - Mango Smoothie (24oz only)": 7.00
               }

    print("*~*~*~*~*~*~* PyBoba Menu *~*~*~*~*~*~*~*")
    for item, price in py_menu.items():
        print(f"{item:30}: ${price:.2f}")
    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")


def boba_ordering(customer_money):
    customer_order = []
    prices = []
    customer_subtotal = 0.00
    still_a_customer = True
    while still_a_customer:
        display_menu()
        my_first_drink = input("Please select a drink from the menu using a "
                               "number or press 0 to cancel/quit: ")
        try:
            customer_answer = int(my_first_drink)
        except ValueError:
            print("Please enter a valid numerical value.")
            continue
        if customer_answer == 1:
            print("")
            print("Classic Milk Tea will be $3.00 for 16oz. ")
            customer_order.append("Classic Milk Tea (16oz)")
            price = float(input("Please enter the price of the item: "))
            prices.append(price)
            continue_order = input("Would you like to order something else? "
                                   "Please Enter 'Yes' or 'No'. ")
            if continue_order.capitalize() == "Yes":
                still_a_customer = True
            elif continue_order.capitalize() == "No":
                still_a_customer = False
            else:
                print("Please enter 'Yes' or 'No' only.")
                still_a_customer = True
        elif customer_answer == 2:
            print("")
            print("Classic Milk Tea will be $4.00 for 24oz. ")
            customer_order.append("Classic Milk Tea (24oz)")
            price = float(input("Please enter the price of the item: "))
            prices.append(price)
            continue_order = input("Would you like to order something else? "
                                   "Please Enter 'Yes' or 'No'. ")
            if continue_order.capitalize() == "Yes":
                still_a_customer = True
            elif continue_order.capitalize() == "No":
                still_a_customer = False
            else:
                print("Please enter 'Yes' or 'No' only.")
                still_a_customer = True
        elif customer_answer == 3:
            print("")
            print("Passion Fruit Green Tea (16oz) will be $5.00 for 16oz. ")
            customer_order.append("Passion Fruit Green Tea (16oz)")
            price = float(input("Please enter the price of the item: "))
            prices.append(price)
            continue_order = input("Would you like to order something else? "
                                   "Please Enter 'Yes' or 'No'. ")
            if continue_order.capitalize() == "Yes":
                still_a_customer = True
            elif continue_order.capitalize() == "No":
                still_a_customer = False
            else:
                print("Please enter 'Yes' or 'No' only.")
                still_a_customer = True
        elif customer_answer == 4:
            print("")
            print("Passion Fruit Green Tea (24oz) will be $6.00 for 24oz. ")
            customer_order.append("Passion Fruit Green Tea (24oz)")
            price = float(input("Please enter the price of the item: "))
            prices.append(price)
            continue_order = input("Would you like to order something else? "
                                   "Please Enter 'Yes' or 'No'. ")
            if continue_order.capitalize() == "Yes":
                still_a_customer = True
            elif continue_order.capitalize() == "No":
                still_a_customer = False
            else:
                print("Please enter 'Yes' or 'No' only.")
                still_a_customer = True
        elif customer_answer == 5:
            print("")
            print("Mango Smoothie will be $7.00 for 24oz. ")
            customer_order.append("Mango Smoothie (24oz)")
            price = float(input("Please enter the price of the item: "))
            prices.append(price)
            continue_order = input("Would you like to order something else? "
                                   "Please Enter 'Yes' or 'No'. ")
            if continue_order.capitalize() == "Yes":
                still_a_customer = True
            elif continue_order.capitalize() == "No":
                still_a_customer = False
            else:
                print("Please enter 'Yes' or 'No' only.")
                still_a_customer = True
        elif customer_answer == 0:
            farewell()
            break
        else:
            print("Please choose a valid option from the menu.")

    print("")
    print("Customer Order:")
    for total_order in customer_order:
        print(total_order)

    for price in prices:
        customer_subtotal = float(customer_subtotal) + float(price)

    customer_tax = customer_subtotal * float(0.0625)
    customer_total = customer_tax + customer_subtotal

    print(f"The total comes out to: ${customer_total:.2f} after tax.")
    print("")

    if customer_money >= customer_total:
        customer_change = customer_money - customer_total
        print("Great! You have enough money for this order.")
        print(f"Your change is: ${customer_change:.2f}.")
        print("")
        farewell()
    else:
        print("Sorry, but you don't have enough money for this order. Please "
              "restart this program again.")
        print("")


def farewell():
    print(" *~~~~~~~~~~~~~~~~~~~~~~~~~~~* ")
    print(" |        Thank you          |")
    print(" |       for visiting        |")
    print(" |       PyBoba today!       |")
    print(" |    See you next time!     |")
    print(" |    ☆*.｡.o(≧▽≦)o.｡.*☆      |")
    print(" *~~~~~~~~~~~~~~~~~~~~~~~~~~~* ")


if __name__ == "__main__":
    greeting()
