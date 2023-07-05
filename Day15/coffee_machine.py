import os


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

profit = 0

def coffee():

    os.system('cls')

    def current_materials(needs):
        """gets the ingredients of the order"""
        for item in MENU:
            if item == needs:
                requirements = MENU[item]["ingredients"]
        return requirements


    def current_price (needs):
        """gets the cost of the order"""
        for item in MENU:
            if item == needs:
                cost = MENU[item]["cost"]
        return cost

    def sufficient_check(needs, available):
        """Checks if the available resources are sufficient to produce the order"""
        num = len(needs)
        for item in needs:
            if needs[item] <= available[item]:
                num -= 1
                if num == 0:
                    return True
            elif needs[item] > available[item]:
                return item

    turn_off = False
    report = resources
    report['Money'] = profit


    while turn_off != True:

        request = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if request == "report":
            print(f"Water: {report['water']}ml \nMilk: {report['milk']}ml \nCoffee: {report['coffee']}ml \nMoney: ${report['Money']}")
        elif request == 'off':
            turn_off = True
        elif request == 'espresso' or request == 'latte' or request == 'cappuccino':

            order_materials = current_materials(request)

            order_price = current_price(request)

            stock = sufficient_check(order_materials, resources)


            if stock == True:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: ")) * 0.25
                dimes = int(input("How many dimes?: ")) * 0.10
                nickels = int(input("How many nickels?: ")) * 0.05
                pennies = int(input("How many pennies?: ")) * 0.01

                total_sum = round((quarters + dimes + nickels + pennies),2)
            else:
                print(f"Sorry, there is not enough {stock}")

            if total_sum < order_price:
                print("Sorry, that's not enough. Money refunded")
            elif total_sum > order_price:
                balance = round((total_sum - order_price), 2)

            if total_sum >= order_price:
                report["Money"] += order_price

            if stock == True and total_sum >= order_price:
                for items in order_materials:
                    if items in resources:
                        resources[items] -= order_materials[items]
                if total_sum > order_price:
                    print(f"Here is ${balance} in change")
                print("Here is your coffee ☕, Enjoy!")        
        else:
            print("Please, enter a valid order")

coffee()
