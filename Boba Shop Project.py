def greeting():
    user_name = input("Hello! Welcome to PyBoba. What is the name for the order? ")
    print("Thank you, ", user_name, ". What can I get for you today?", sep='')
    print("")
    boba_menu()


def boba_menu():
    print_menu()
    my_first_drink = input("Please select a drink from the menu using a number: ")
    try:
        non_answer = int(my_first_drink)
    except ValueError:
        print("Please enter a valid numerical number.")


def print_menu():
    print("Drink Menu:")
    print("1 - Classic Milk Tea")
    print("2 - Passion Fruit Green Tea")
    print("3 - Mango Smoothie")
    print("")


if __name__ == "__main__":
    greeting()