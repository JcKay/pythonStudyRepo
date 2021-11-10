# MODULES
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu, MenuItem

# OBJECTS LIST
cMaker = CoffeeMaker()
mMachine = MoneyMachine()
cMenu = Menu()

while True:
    options = cMenu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        cMaker.report()
        mMachine.report()
    else:
        # check resource / check payment / make coffee
        drink = cMenu.find_drink(choice)
        if cMaker.is_resource_sufficient(drink) and mMachine.make_payment(drink.cost):
            cMaker.make_coffee(drink)
