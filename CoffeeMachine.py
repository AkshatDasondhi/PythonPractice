menu = {
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

money = 0


def make_coffee(typeofcoffee, money):
    if typeofcoffee == "espresso":
        resources["water"] -= menu["espresso"]["ingredients"]["water"]
        resources["coffee"] -= menu["espresso"]["ingredients"]["coffee"]
        money += menu["espresso"]["cost"]
    elif typeofcoffee == "latte":
        resources["water"] -= menu["latte"]["ingredients"]["water"]
        resources["coffee"] -= menu["latte"]["ingredients"]["coffee"]
        resources["milk"] -= menu["latte"]["ingredients"]["milk"]
        money += menu["latte"]["cost"]

    else:
        resources["water"] -= menu["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= menu["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] -= menu["latte"]["ingredients"]["milk"]
        money += menu["cappuccino"]["cost"]

flag = 0

while flag == 0:
    choice = input("What would you like ? (espresso/latte/cappuccino): ")
    cash = 0
    cost1 = 0
    if choice != "report":
        print("Please Insert Coins.")
        quarters = int(input("How many quarters? : "))
        dimes = int(input("How many dimes? : "))
        nickles = int(input("How many nickles? : "))
        pennies = int(input("How many pennies? : "))
        cash = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        cost1 = 0

    if cash < cost1:
        flag = 1
        print("Sorry that's not enough money , Money Refunded.")
    elif choice == "espresso" and resources["water"] < menu["espresso"]["ingredients"]["water"]:
        flag = 1
        print("Not Enough Water.")
    elif choice == "latte" and resources["water"] < menu["latte"]["ingredients"]["water"]:
        flag = 1
        print("Not Enough Water.")
    elif choice == "cappuccino" and resources["water"] < menu["cappuccino"]["ingredients"]["water"]:
        flag = 1
        print("Not Enough Water.")
    elif choice == "espresso" and resources["coffee"] < menu["espresso"]["ingredients"]["coffee"]:
        flag = 1
        print("Not Enough coffee.")
    elif choice == "latte" and resources["coffee"] < menu["latte"]["ingredients"]["coffee"]:
        flag = 1
        print("Not Enough coffee.")
    elif choice == "cappuccino" and resources["coffee"] < menu["cappuccino"]["ingredients"]["coffee"]:
        flag = 1
        print("Not Enough coffee.")
    elif choice == "latte" and resources["milk"] < menu["latte"]["ingredients"]["milk"]:
        flag = 1
        print("Not Enough milk.")
    elif choice == "cappuccino" and resources["coffee"] < menu["cappuccino"]["ingredients"]["milk"]:
        flag = 1
        print("Not Enough milk.")
    else:
        if choice == "report":
            print("Water : %s" % resources["water"])
            print("Milk : %s" % resources["milk"])
            print("Coffee : %s" % resources["coffee"])
            print("Money :$%s" % money)
        elif choice == "espresso":
            make_coffee("espresso", money)
            cost1 = menu["espresso"]["cost"]
        elif choice == "latte":
            make_coffee("latte", money)
            cost1 = menu["latte"]["cost"]
        else:
            make_coffee("cappuccino", money)
            cost1 = menu["cappuccino"]["cost"]
        change = cash - cost1
        if choice != "report":
            print("Here is $%s in change." % round(change, 2))
            print("Here is your %s . Enjoy" % choice)
            