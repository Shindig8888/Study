print("Welcome to the tip calculator.")
total = float(input("What was the total bill? : "))
people = int(input("How many people to split the bii? : "))
tip = int(input("What percentage tip would you like to give? : "))

dollor_for_person = total * (1 + tip / 100) / people

print(f"Each person should pay {round(dollor_for_person, 2)} dollars")

#round는 실제로 값을 변환하고, :.4f와 같은 방식은 보이는것만 바꿔줌. 둘 다 반올림
#tip과 people은 int로 지정하는게 옵티마이징
