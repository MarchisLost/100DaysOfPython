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
    "money": 0
}


# Gets drink resources
def getResources(coffeeType):
    water = MENU[coffeeType]['ingredients']['water']
    if coffeeType == 'espresso':
        milk = 0
    else:
        milk = MENU[coffeeType]['ingredients']['milk']
    coffee = MENU[coffeeType]['ingredients']['coffee']
    cost = MENU[coffeeType]['cost']

    return (water, milk, coffee, cost)


# Checks if it has enough resources
def checkResources(resourcesDrink2):
    if resources['water'] < resourcesDrink2[0]:
        print('Sorry there is not enough water')
    if resources['milk'] < resourcesDrink2[1]:
        print('Sorry there is not enough milk')
    if resources['coffee'] < resourcesDrink2[2]:
        print('Sorry there is not enough coffee')


# Add data to resources
def addDataResources(water, milk, coffee, money):
    resources.update({'water': resources['water'] - water, "milk": resources['milk'] - milk, "coffee": resources['coffee'] - coffee, "money": resources['money'] + money})
    return


# keep asking what the user wants
while True:
    coffeeType = input('What would you like? (espresso/latte/cappuccino): ')

    # Turn off the machine
    if coffeeType == 'off':
        break

    # Show the report data
    if coffeeType == 'report':
        print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}')
        continue
    
    # Works the work for each drink
    if coffeeType == 'espresso' or 'latte' or 'cappuccino':
        resourcesDrink = getResources(coffeeType)
        checkResources(resourcesDrink)

    print('Please insert coins.')
    quarters = 0.25 * float(input('How many quarters? '))
    dimes = 0.1 * float(input('How many dimes? '))
    nickles = 0.05 * float(input('How many nickles? '))
    pennies = 0.01 * float(input('How many pennies? '))
    total = quarters + dimes + nickles + pennies

    if resourcesDrink[3] > total:
        print('Sorry thats not enough money. Money refunded')
    elif resourcesDrink[3] == total:
        addDataResources(resourcesDrink[0], resourcesDrink[1], resourcesDrink[2], resourcesDrink[3])
        print(f'here is your {coffeeType}, enjoy!')
    elif resourcesDrink[3] < total:
        addDataResources(resourcesDrink[0], resourcesDrink[1], resourcesDrink[2], resourcesDrink[3])
        change = total - resourcesDrink[3]
        print(f'Here is ${change} in change.')
        print(f'here is your {coffeeType}, enjoy!')
