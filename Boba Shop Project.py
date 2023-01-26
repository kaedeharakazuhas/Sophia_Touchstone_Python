def greeting():
    print(" *~~~~~~~~~~~~~~~~~~~~~~~~~~~* ")
    print(" |        Welcome to         |")
    print(" |          PyBoba!          |")
    print(" |    ☆*.｡.o(≧▽≦)o.｡.*☆      |")
    print(" *~~~~~~~~~~~~~~~~~~~~~~~~~~~* ")
    user_name = input("What is the name for the order? ")
    print("Thank you, ", user_name, ". What can I get for you today?", sep='')
    print("")
    boba_menu()


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


def boba_menu():
    customer_order = []
    prices = []
    still_a_customer = True
    while still_a_customer:
        display_menu()
        my_first_drink = input("Please select a drink from the menu using a number or press 0 to cancel/quit: ")
        try:
            customer_answer = int(my_first_drink)
        except ValueError:
            print("Please enter a valid numerical value.")
            continue
        if customer_answer == 1:
            print("")
            print("Classic Milk Tea will be $3 for 16oz. ")
            customer_order.append("Classic Milk Tea (16oz)")
            prices.append("$3.00")
            continue_order = input("Would you like to order something else? Please Enter 'Yes' or 'No'. ")
            if continue_order == "Yes":
                still_a_customer = True
            elif continue_order == "No":
                still_a_customer = False
            else:
                print("Please enter 'Yes' or 'No' only.")
                still_a_customer = True
        elif customer_answer == 2:
            print("Classic Milk Tea will be $4 for 24oz. ")
        elif customer_answer == 3:
            print("Passion Fruit Green Tea will be $5 for 16oz. ")
        elif customer_answer == 4:
            print("Passion Fruit Green Tea will be $6 for 24oz. ")
        elif customer_answer == 5:
            print("Mango Smoothie will be $6 for 24oz.")
        elif customer_answer == 0:
            farewell()
            break
        else:
            print("Please choose a valid option from the menu.")

    for customer_total in customer_order:
        print("")
        print("Customer Order:")
        print(customer_total)
        print(*prices)
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
