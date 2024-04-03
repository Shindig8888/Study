#Scope(유효범위)

################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# #local scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

#glabl scope
# player_health = 10 #global

# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()

#block scope
#python does not have block scope
# game_level = 3
# enemies = ['s','z','a']
# if game_level <5:
#     new_enemy = enemies[0]

# print(new_enemy)

#modifying global scope
# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies+=1
#     print(f'inside: {enemies}')

# increase_enemies()
# print(f'outside {enemies}')

#global constants

# PI = 3.14159

# def calc():
#     print(PI)
import random
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
life = 0

while end is False:
    target = random.randint(1,100)
    harsh = input('Choose a difficulty. Type "easy" or "hard".')
    if harsh == 'easy':
        life = 10
    elif harsh == 'hard':
        life = 5
    while True:
        print(f"You have {life} attempts remaining to guess the number.")
        guess = int(input('Make a guess. : '))
        if guess > target:
            print("Too high.")
        elif guess < target:
            print("Too low.")
        life -= 1
        if guess == target or life == 0:
            break    
            
    if life == 0:
        print(f"Try again! The number was: {target}")
    elif guess == target:
        print(f"You got it! The number was: {target}")

    answer = input("try again? : ").lower()
    if answer == 'y':
       continue
    else:
        break

print('thank you')
        

