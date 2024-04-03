from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



def coffee_asking():
    while True:
        coffee_type = input('What would you like? (espresso / latte / cappuccino): ').lower()
        if coffee_type in {'espresso', 'latte', 'cappuccino', 'report', 'off'}:
            return coffee_type
        else:
            print('Please enter a valid option!')



def retry_asking():
    while True:
        re_ask = input('Do you need another drink?(Y / N)').lower()
        if re_ask == 'y' or re_ask == 'n':
            return re_ask
        else:
            print('Please enter Y or N!')
            continue

menu_list = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
is_on = True

while True:
    while is_on:
        coffee_type = coffee_asking()
        if coffee_type == 'off':
            is_on = False
            print('Turning off Coffee Machine. Restart the process.')
            continue

        findcoffee = menu_list.find_drink(coffee_type)

        if coffee_type =='report':
            coffeemaker.report()
            moneymachine.report()
            continue
        else:
            if_can_make = coffeemaker.is_resource_sufficient(findcoffee)

        if if_can_make:
            enough_money = moneymachine.make_payment(findcoffee.cost)
        else:
            print(f'Current Menu "{coffee_type.title()}" is not availbe right now due to ingrdient insufficient. \n Try other options or Please contact manager.')
            break

        if enough_money:
            coffeemaker.make_coffee(findcoffee)
            break
        else:
            break

            
    retry_answer = retry_asking()
    if retry_answer == 'y':
        continue
    else:
        break

print('Thank you for using our coffee machine!')


