# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? : "))

# if height >= 120:
#   print("You can ride the rollercoaster!")
# else:
#   print("Sorry, you have to grow taller before you can ride.")

###

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? : "))

# if height >= 120:
#   age = int(input("What is your age? : "))
#   if age <=12:
#     print("please pay $5")
#   elif age<=18:
#     print("please pay $7")
#   else:
#     print("please pay $12")
# else:
#   print("Sorry, you have to grow taller before you can ride.")

###

# bmi = weight / height**2
# if True:
#   if bmi <18.5:
#     print (f"Your BMI is {bmi}, you are underweight."
#   elif bmi<25:
#     print (f"Your BMI is {bmi}, you are normal weight."
#   elif bmi<30:
#     print (f"Your BMI is {bmi}, you are slightly overweight."
#   elif bmi<35:
#     print (f"Your BMI is {bmi}, you are obese."
#   else:
#     print (f"Your BMI is {bmi}, you are clinically obese."
# else: break
####

# Which year do you want to check?
# year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# if year%100 ==0 and year%400 ==0:
#   print("Leap year")
# elif year%100 ==0 and year%400 !=0:
#   print("Not leap year")
# elif year%4==0:
#   print("Leap year")
# else:
#   print("Not leap year")
# ###

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? : "))
# bill = 0

# if height >= 120:
#   age = int(input("What is your age? : "))
#   if age < 12:
#     bill += 5
#     print(f"Child tickets are ${bill}")
#   elif age <= 18:
#     bill += 7
#     print(f"Youth tickets are ${bill}")
#   else:
#     bill += 12
#     print(f"Adult tickets are ${bill}")

#   wants_photo = input("Do you want a photo taken? Y or N : ")
#   if wants_photo == "Y":
#     bill += 3

#   print(f"Your total ticket fee is {bill}")

# else:
#   print("Sorry, you have to grow taller before you can ride.")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? : "))
# bill = 0

# if height >= 120:
#   age = int(input("What is your age? : "))
#   if age < 12:
#     bill += 5
#     print(f"Child tickets are ${bill}")
#   elif age <= 18:
#     bill += 7
#     print(f"Youth tickets are ${bill}")

#   elif age>=45 and age<=55:
#     bill +=0
#     print("Everything is going to be OK. Have a free ride on us!")
    
#   else:
#     bill += 12
#     print(f"Adult tickets are ${bill}")

#   wants_photo = input("Do you want a photo taken? Y or N : ")
#   if wants_photo == "Y" or "y":
#     bill += 3

#   print(f"Your total ticket fee is {bill}")

####

# l_name1 = name1.lower()
# l_name2 = name2.lower()

# count_t = l_name1.count("t") + l_name2.count("t")
# count_r = l_name1.count("r") + l_name2.count("r")
# count_u = l_name1.count("u") + l_name2.count("u")
# count_e = l_name1.count("e") + l_name2.count("e")

# count_true = count_t+count_r+count_u+count_e

# count_l = l_name1.count("l") + l_name2.count("l")
# count_o = l_name1.count("o") + l_name2.count("o")
# count_v = l_name1.count("v") + l_name2.count("v")

# count_love = count_l+count_o+count_v+count_e

# love_score_str = str(count_true) + str(count_love)
# love_score = int(love_score_str)

# if love_score<10 or love_score>90:
#   print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score>40 and love_score<50:
#   print(f"Your score is {love_score}, you are alright together.")
# else:
#   print(f"Your score is {love_score}.")  




print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")


lr = input("\nThere is a cross road in front of you. What direction should you go?\nleft or right: ").lower()

if lr == "left":
  
  sw = input("\nYou walk down the road and faced in front of an unnamed lake. Would you swim or wait?\nswim or wait: ").lower()

  if sw == "wait":
    print("\nYou waited in front of lake. A fairy appeared and magically wraped you to a abandoned castle.")
    rby = input("\nThere are 3 doors: Red, Blue and Yellow. What color of door would like you to choose?\nred, blue or yellow: ").lower()
  
    if rby == "red":
      print("\nYou opened the red door. Door shuts and FIRE EVERYWHERE!! You died. Try again\n\n*******************************************************************************")
    elif rby == "blue":
      print("\nYou opened the blue door. Door shuts and ICE EVERYWHERE!! You died. Try again\n\n*******************************************************************************")
    elif rby =="yellow":
      print("\nYou opened the yellow door. There are a fortune of gold and jeweries EVERYWHER!! You won!!\n\n*******************************************************************************")
    else:
      print("\nYou acted pretty stupid right there and fell over a rock. You died. Try again!\n\n*******************************************************************************")
    
  elif sw=="swim":
    print("\nYou tried to swim acrss the lake but a giant lake-topus attacks you. You died. Try again!\n\n*******************************************************************************")
  else:
    print("\nYou acted pretty stupid right there and fell over a rock. You died. Try again!\n\n*******************************************************************************")

elif lr == "right":
  print("\nYou stepped into a hole. You died. Try again!\n\n*******************************************************************************")

else:
  print("\nYou acted pretty stupid right there and fell over a rock. You died. Try again!\n\n*******************************************************************************")


