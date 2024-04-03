import sys

args = sys.argv[1:]

result = 0
for i in list(map(int, args)):
    result += i

print(result)

###map 함수를 이용해도되고 int(i)와 같은 방식으로 계산해도 됨

print("Welcome to the tip calculator.")
total = float(input("What was the total bill? : "))
people = float(input("How many people to split the bii? : "))
tip = float(input("What percentage tip would you like to give? : "))

dollor_for_person = total*(1+tip/100)/people

print(f"each person should pay {dollor_for_person:.4f} dollars")


