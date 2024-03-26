# fruits = ['appele', 'peach', 'pear']
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " pie")

# a = [1,2,3,4,5]
# print(sum(a))


# for number in range(1,11, 3):
#   print(number, end=" ")
# i = 0
# for number in range(1,101):
#   i += number
# print(i)

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_numbers = int(input("How many numbers would you like?\n"))

# password = []
# for letter in range(1,nr_letters+1):
#   ranletter = random.choice(letters)
#   password.append(ranletter)

# for symbol in range(1,nr_symbols+1):
#   ransymbols = random.choice(symbols)
#   password.append(ransymbols)

# for number in range(1,nr_numbers+1):
#   rannumber = random.choice(numbers)
#   password.append(rannumber)


# random.shuffle(password)

# print(f"Your password is : {''.join(password)}")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []
password.extend(random.choices(letters, k = nr_letters))
password.extend(random.choices(symbols, k = nr_symbols))
password.extend(random.choices(numbers, k = nr_numbers))

random.shuffle(password)

print(f"Your password is : {''.join(password)}")

