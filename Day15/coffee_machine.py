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
