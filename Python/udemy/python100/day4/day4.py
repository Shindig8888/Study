import random
# random_interger = random.randint(1,10)
# print(random_interger)

# import my_module
# print(my_module.pi)

# import random
# rfloat = random.random()
# print(rfloat*5)

# import random
# love_score = random.randint(1,100)
# print(f"Your love score is {love_score}")

# states_of_america = ['Delaware', 'pensyvania']
# states_of_america[1] = "Pensylvania"
# states_of_america.append("Calixland")
# print(states_of_america)
# states_of_america.extend(["Angelaland", "CALIX"])
# print(states_of_america)
# print(states_of_america[0])
# print(states_of_america[1])
# print(states_of_america[2])
# print(states_of_america[-1])

# print(random.randint(1,5))

# fruits = ['strawberries', 'apple']
# vegetable = ['spanich', 'kale']

# dirty_dozen = [fruits, vegetable]

# print(dirty_dozen)

# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# # Your code below
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"

# print(f"{line1}\n{line2}\n{line3}")








# import random

print("가위바위보 시뮬레이터에 오신 것을 환영합니다!!\n")

def retryq():
  while True:
    retry = input("다시 하시겠습니까? (Y/N): \n").lower()
    if retry == 'y' or retry == 'n':
      return retry
    else:
      print("Y 혹은 N만 입력해주세요")
      continue
  
while True:
  

  user_input : str = input("가위, 바위, 보 중에 입력해주세요 : \n")
  randomlist = ['가위', '바위', '보']
  computer_input = random.choice(randomlist)

  if user_input not in randomlist:
    print("가위, 바위, 보 중에 입력해주세요\n")
    continue
  else:
    print(f"\n당신은 {user_input}를 냈습니다!\n")
    print(f"컴퓨터는 {computer_input}를 냈습니다!\n")
    
  
  if (user_input, computer_input) in [('가위', '보') , ('바위', '가위') , ('보', '바위')]:
    print("당신의 승리!\n")
  elif user_input == computer_input:
    print("비겼습니다!\n")
  else:
    print("졌습니다ㅠㅠ\n")

  retry = retryq()
  if retry =='n':
    break

print("\n가위바위보 게임을 즐겨주셔서 감사합니다. 프로그램 종료합니다.\n")



  