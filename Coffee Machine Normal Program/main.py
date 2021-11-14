MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coin_values = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


# Functions Collection

def resource_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${bounty}")


def check_resources():
    can_make = True
    for item in drink["ingredients"]:
        if drink["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            can_make = False
    return can_make


def process_coins(money_received):
    print("Please insert coins.")
    for coin in coin_values:
        money_received += int(input(f"How many {coin}?: ")) * coin_values[coin]
    return money_received


def transaction(money_received):
    money_received = process_coins(money_received)  # process coins
    if money_received >= drink["cost"]:
        change = round(money_received - drink["cost"], 2)
        print(f"Here is ${change} change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_coffee():
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]
    print(f"Here is your {choice} ☕️. Enjoy!")


# Variables list
bounty = 0
money_received = 0
__restore__ = resources.copy()

# Main Line
while True:
    choice = input("What would you like? (espresso/ latte/ cappuccino): ").lower()
    try:
        if choice == "off":
            break
        elif choice == "report":
            resource_report()
        elif choice == "restore":
            resources = __restore__.copy()
        else:
            drink = MENU[choice]
            if check_resources() and transaction(money_received):
                bounty += drink["cost"]
                money_received = 0
                make_coffee()
    except KeyError:
        print("Invalid input, Check again.")
        continue
