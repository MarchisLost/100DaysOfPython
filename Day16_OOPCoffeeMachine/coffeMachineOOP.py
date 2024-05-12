from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
while True:
    coffeeType = input('What would you like? (espresso/latte/cappuccino): ')

    # Turn off the machine
    if coffeeType == 'off':
        break

    if coffeeType == 'report':
        coffee_maker.report()
        money_machine.report()
        continue

    # Works the work for each drink
    drink = menu.find_drink(coffeeType)
    if drink is None:
        continue
    else:
        enoughOrNot = coffee_maker.is_resource_sufficient(drink)
        payment = money_machine.make_payment(drink.cost)
        if enoughOrNot and payment:
            coffee_maker.make_coffee(drink)
