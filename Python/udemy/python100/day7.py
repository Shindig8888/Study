print("행맨 게임에 오신걸 환영합니다!\n 총 6번의 기회가 주어지며, 알파벳을 입력해 단어를 맞추시면 됩니다!")

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_list = ['apple', 'beekeeper', 'santa']


# def try_again():
#   while True:
#     try_answer = input("다시하시겠습니까? : ")
#     if try_answer == 'y' or try_answer == 'n':
#      return try_answer
#     else:
#       continue

def try_again():
  while True:
      try_answer = input("다시 하시겠습니까? (Y/N): ").lower()
      if try_answer == 'y' or try_answer == 'n':
          return try_answer
      else:
          print("Y 혹은 N만 입력해주세요")
          
    

while True:

  win = False
  lose = False
  life = 6
  round = 1
  
  random.shuffle(word_list)
  ran_num = random.randint(1, len(word_list))
  target_word = list(word_list[ran_num-1])
  print("\n 단어가 정해졌습니다!")
  print(target_word)
  target_list = list('_'*len(target_word))

  while win is False and lose is False:  
    guess = input(f"\n 당신의 {round}번째 추측은?(한글자의 알파벳으로만 답해주세요) : ").lower().replace(" ","")
    if guess not in letters:
      print("한글자의 알파벳으로 답해주세요!")
      continue
      
    if guess in target_word:
     print("맞췄습니다!")
    else:
      life -= 1
      print(f"틀렸습니다! 남은 목숨은 {life}개입니다!")
    round+=1
    
    for i in range(0, len(target_word)):
      if guess == target_word[i]:
        target_list[i] = guess

    print(target_list)
    
    if '_' not in target_list:
     win = True
     print("축하합니다! 승리하셨습니다!")
     break
    if life == 0:
     lose = True
     print("다시한번 도전해보세요!")
     break
  
  try_answer = try_again()   
  if try_answer == 'n':
      break
  else:
    life = 6
    round = 1
      
print("플레이해주셔서 감사합니다!")