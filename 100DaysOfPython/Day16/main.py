from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_on = True
money = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()

while machine_on:
  options = menu.get_items()
  order = input(f"What would you like to drink? ({options}): ")
  if order == "off":
    machine_on = False
  elif order == 'report':
    coffee.report()
    money.report()
  else:
    drink = menu.find_drink(order)
    if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
      coffee.make_coffee(drink)
