from menu_item import Menu, MenuItem
from coffeemaker_class import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


end_game = False

while end_game != True:

    available = menu.get_items()

    request = input(f"What would you like? {available}: ").lower()

    if request == 'report':
        coffee_maker.report()
        money_machine.report()
    elif request == "off": 
        print("Switching off....")
        print("Have a good one!")
        end_game = True
    else:
        my_choice = menu.find_drink(request)
        if my_choice == None:
            print("Valid order needed!")
        elif coffee_maker.is_resource_sufficient(my_choice) == True:
            if money_machine.make_payment(my_choice.cost) == True:
                coffee_maker.make_coffee(my_choice)