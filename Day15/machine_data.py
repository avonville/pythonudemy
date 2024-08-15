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


def print_report():
    """Prints a report of the current resource values"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")


def check_resources(drink):
    """Returns True if there are enough resources to make the drink"""
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins(choice):
    """Returns the total calculated from coins inserted"""
    print(f"{choice} costs ${MENU[choice]['cost']}.")
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def check_transaction(money_received, drink_cost):
    """Returns True if the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink):
    """Deducts the required ingredients from the resources"""
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f"Here is your {drink} ☕️. Enjoy!")


profit = 0
machine_on = True

while machine_on:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print_report()
    else:
        if check_resources(choice):
            payment = process_coins(choice)
            if check_transaction(payment, MENU[choice]["cost"]):
                make_coffee(choice)

print(f"Total profit: ${profit}")
