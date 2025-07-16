from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money = MoneyMachine()

making_coffe = CoffeeMaker()

is_correct =True
menu_bar = Menu()
menu_bar.show_prices()
while is_correct:
    option = menu_bar.get_items()
    choice = input(f"what would you like? {option} : ")
    if choice == "off":
        is_correct = False
    elif choice == "report":
        making_coffe.report()
        my_money.report()
    else:
        drink = menu_bar.find_drink(choice)
        #print(drink)
        if making_coffe.is_resource_sufficient(drink) and my_money.make_payment(drink.cost):
            making_coffe.make_coffee(drink)


