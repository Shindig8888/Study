# coffee machine


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
    "water": 500,
    "milk": 1,
    "coffee": 500,
}


def coffee_asking():
    while True:
        coffee_type = input('What would you like? (espresso / latte / cappuccino): ').lower()
        if coffee_type in {'espresso', 'latte', 'cappuccino', 'report'}:
            return coffee_type
        else:
            print('Please enter a valid option!')


def check_resources(coffee_type):
    if coffee_type == 'report':
        print(resources)
    else:
        ingredients_needed = MENU[coffee_type]['ingredients']
        for ingredient, amount in ingredients_needed.items():
            if resources.get(ingredient, 0) < amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True


def retry_asking():
    while True:
        re_ask = input('Do you need another drink?(Y / N)').lower()
        if re_ask == 'y' or re_ask == 'n':
            return re_ask
        else:
            print('Please enter Y or N!')
            continue

# o_water = int(MENU[coffee_type]['ingredients']['water'])
#     o_milk = int(MENU[coffee_type]['ingredients']['milk'])
#     o_coffee = int(MENU[coffee_type]['ingredients']['coffee'])
#     c_water = resources['water']
#     c_milk = resources['milk']
#     c_coffee = resources['coffee']


end = False
while True:
    while True:
        coffee__type = coffee_asking()

        checker = check_resources(coffee__type)
        if not checker:
            continue
        if coffee__type == 'report':
            continue

        print('Please insert coins.')
        quarters = int(input('How many quarters?'))
        dimes = int(input('How many dimes?'))
        nickles = int(input('How many nickles?'))
        pennies = int(input('How many pennies?'))

        total_in_money = (quarters*25 + dimes*10 + nickles*5 + pennies*1)/100

        print(f"You have inserted ${total_in_money}.")

        if total_in_money == MENU[coffee__type]['cost']:
            print(f'Here is your {coffee__type}! enjoy!')
        elif total_in_money > MENU[coffee__type]['cost']:
            print(f'Here is ${round(total_in_money-MENU[coffee__type]['cost'], 2)} exchange')
            print(f'Here is your {coffee__type}! enjoy!')
        else:
            print(f'Not enough money')
            print(f'Here is ${round(total_in_money, 2)} exchange')

        resources['water'] -= MENU[coffee__type]['ingredients']['water']
        try:
            resources['milk'] -= MENU[coffee__type]['ingredients']['milk']
        except KeyError:
            pass
        resources['coffee'] -= MENU[coffee__type]['ingredients']['coffee']

        break
    retry_answer = retry_asking()
    if retry_answer == 'y':
        end = False
        continue
    else:
        break

print('Thank you for using coffee machine!')
#
# def coffee_asking():
#     while True:
#         coffee_type = input('What would you like? (espresso / latte / cappuccino / report): ').lower()
#         if coffee_type in {'espresso', 'latte', 'cappuccino', 'report'}:
#             return coffee_type
#         else:
#             print('Please enter a valid option!')
#
# def check_resources(coffee_type):
#     if coffee_type == 'report':
#         print(resources)
#     else:
#         ingredients_needed = MENU[coffee_type]['ingredients']
#         for ingredient, amount in ingredients_needed.items():
#             if resources.get(ingredient, 0) < amount:
#                 print(f"Sorry, there is not enough {ingredient}.")
#                 return False
#         return True
#
# def process_payment(coffee_type):
#     quarters = int(input('How many quarters? '))
#     dimes = int(input('How many dimes? '))
#     nickels = int(input('How many nickels? '))
#     pennies = int(input('How many pennies? '))
#     total_in_money = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
#     return total_in_money - MENU[coffee_type]['cost']
#
# def make_coffee(coffee_type):
#     resources_used = MENU[coffee_type]['ingredients']
#     for ingredient, amount in resources_used.items():
#         resources[ingredient] -= amount
#     print(f"Here is your {coffee_type}. Enjoy!")
#
# def retry_asking():
#     while True:
#         re_ask = input('Do you need another drink? (Y / N): ').lower()
#         if re_ask in {'y', 'n'}:
#             return re_ask
#         else:
#             print('Please enter Y or N!')
#
# resources = {
#     "water": 500,
#     "milk": 500,
#     "coffee": 500,
# }
#
# while True:
#     coffee_type = coffee_asking()
#
#     if coffee_type == 'report':
#         check_resources(coffee_type)
#         continue
#
#     if check_resources(coffee_type):
#         change = process_payment(coffee_type)
#         if change >= 0:
#             if change > 0:
#                 print(f"Here is ${change:.2f} in change.")
#             make_coffee(coffee_type)
#         else:
#             print("Sorry, that's not enough money. Money refunded.")
#     else:
#         continue
#
#     if retry_asking() == 'n':
#         break
#
# print('Thank you for using the coffee machine!')
