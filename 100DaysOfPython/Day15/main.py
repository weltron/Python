logo = """
_________         _____  _____                  _____                .__    .__               
\_   ___ \  _____/ ____\/ ____\____   ____     /     \ _____    ____ |  |__ |__| ____   ____  
/    \  \/ /  _ \   __\\   __\/ __ \_/ __ \   /  \ /  \\__  \ _/ ___\|  |  \|  |/    \_/ __ \ 
\     \___(  <_> )  |   |  | \  ___/\  ___/  /    Y    \/ __ \\  \___|   Y  \  |   |  \  ___/ 
 \______  /\____/|__|   |__|  \___  >\___  > \____|__  (____  /\___  >___|  /__|___|  /\___  >
        \/                        \/     \/          \/     \/     \/     \/        \/     \/ 
        """

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

money = 0

menu = {
   'espresso': {
        'ingredients': {
            'water': 50,
            'milk': 0,
            'coffee': 18},
        'cost': 1.50
    },
   'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24},
        'cost': 2.50
    },
   'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24},
        'cost': 3.00
    },   
}


def process_coins():
    """This function processes the coins insterted and converts them to dollars"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    return total

def enough_resources(ingredients):
    """This function takes the ingredients of the chosen drink and compares to the available resources"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True
        

def transaction(amount, cost):
    """This function confirms if user has inserted enough money to buy the desired coffee"""
    if amount > cost:
        change = round(amount - cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += cost
        return True
    else:
       print("Sorry that's not enough money. Money refunded.")
       return False


def make_coffee(beverage, ingredient):
    """This function reduces the amount of resources based on drink taken"""
    for item in ingredient:
        resources[item] -= ingredient[item]
    print(f"Here is your {beverage} ☕️. Enjoy!")


machine_on = True
print(logo)

while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order =='off':
        machine_on = False
    elif order == 'report':
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: {money}")
    else:
        drink = menu[order]
        if enough_resources(drink['ingredients']):
            amt = process_coins()
            if transaction(amt, drink['cost']):
                make_coffee(order, drink['ingredients'])
