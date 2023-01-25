def greeting():
    user_name = input("Hello! Welcome to PyBoba. What is the name for the order? ")
    customer_ordering = True
    while customer_ordering:
        customer_money = input("How much do you have to spend today at PyBoba? ")
        try:
            customer_int = int(customer_money)
        except ValueError:
            print("Please enter numbers only.")
            continue
        if customer_int <= 10:
            print("Thank you, ", user_name, ". What can I get for you today?", sep='')
            break
        else:
            print("Whoa there! Too much money for this simple project! Hint: try entering a number at or below 10.")
    print("")
    boba_menu()


def boba_menu():
    customer_ordering = True
    while customer_ordering:
        print_menu()
        my_first_drink = input("Please select a drink from the menu using a number or press 0 to cancel: ")
        try:
            customer_answer = int(my_first_drink)
        except ValueError:
            print("Please enter a valid numerical value.")
            continue
        if customer_answer == 1:
            customer_size = input("Classic Milk Tea will be $3 for 16oz or $4 for 24oz. What size would you like? ")
            if customer_size == "16oz":
                print("That will be $3.")
            elif customer_size == "24oz":
                print("That would be $4.")
            else:
                print("Please choose a valid size.")
            break
        elif customer_answer == 2:
            customer_size = input("Passion Fruit Green Tea will be $5 for 16oz or $6 24oz. What size would you like? ")
            if customer_size == "16oz":
                print("That will be $5.")
            elif customer_size == "24oz":
                print("That would be $6.")
            else:
                print("Please choose a valid size.")
            break
        elif customer_answer == 3:
            customer_size = input("Mango Smoothie will be $6 and it only comes in 24oz. Is that okay? ")
            if customer_size == "Yes":
                print("That will be $3.")
            elif customer_size == "No":
                print("Please choose another drink!")
            else:
                print("Please use 'Yes' or 'No' as a response.")
            break
        elif customer_answer == 0:
            print("Thank you for visiting PyBoba. See you next time!")
            break
        else:
            print("Please choose a valid option from the menu.")


def print_menu():
    print("Drink Menu:")
    print("1 - Classic Milk Tea")
    print("2 - Passion Fruit Green Tea")
    print("3 - Mango Smoothie")
    print("")


if __name__ == "__main__":
    greeting()
