from data import MENU

resources = {"water": 300, "milk": 200, "coffee": 100}
money = 0.0


def ask_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")


def has_enough_resources(drink_name):
    for item, amount in MENU[drink_name]["ingredients"].items():
        if amount > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def make_payment(cost):
    print("Please insert coins.")
    total = (
        ask_int("How many quarters? ") * 0.25
        + ask_int("How many dimes? ") * 0.10
        + ask_int("How many nickels? ") * 0.05
        + ask_int("How many pennies? ") * 0.01
    )
    total = round(total, 2)
    if total < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return None
    return total


def main():
    global money
    while True:
        choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").strip().lower()

        if choice == "off":
            break
        if choice == "report":
            print_report()
            continue
        if choice not in MENU:
            print("Unknown drink, please try again.")
            continue
        if not has_enough_resources(choice):
            continue

        cost = MENU[choice]["cost"]
        paid = make_payment(cost)
        if paid is None:
            continue

        money += cost
        for item, amount in MENU[choice]["ingredients"].items():
            resources[item] -= amount

        change = round(paid - cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {choice}. Enjoy!")


main()
