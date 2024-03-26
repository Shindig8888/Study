#필요 리스트
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_list = ['apple', 'beekeeper', 'santa'] #늘려도 가능
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#다시하기 함수 정의
def try_again():
  while True:
      try_answer = input("다시 하시겠습니까? (Y/N): ").lower()
      if try_answer == 'y' or try_answer == 'n':
          return try_answer
      else:
          print("Y 혹은 N만 입력해주세요")

#인삿말
print("행맨 게임에 오신걸 환영합니다!\n\n총 6번의 기회가 주어지며, 알파벳을 입력해 단어를 맞추시면 됩니다!")
import random

#게임 루프시작
while True:
  #초기화해야할 변수
  win = False
  lose = False
  life = 6
  round = 1

  #무작위함수들이기때문에 초기화
  random.shuffle(word_list)
  ran_num = random.randint(1, len(word_list))
  target_word = list(word_list[ran_num-1])

  #본문시작
  print("\n 단어가 정해졌습니다!")
  #-디버그용-
  #print(target_word)
  target_list = list('_'*len(target_word))

#초기화 하지않고 반복: 본게임
  #input
  while win is False and lose is False:  
    guess = input(f"\n 당신의 {round}번째 추측은?(한글자의 알파벳으로만 답해주세요) : ").lower().replace(" ","")
    if guess not in letters:
      print("\n한글자의 알파벳으로 답해주세요!")
      continue
  #입력검정   
    if guess in target_word:
     print("\n맞췄습니다!")
    else:
      life -= 1
      print(f"\n틀렸습니다! 남은 목숨은 {life}개입니다!")
    round+=1
  #입력 기록 및 출력  
    print(stages[6-life])
    for i in range(0, len(target_word)):
      if guess == target_word[i]:
        target_list[i] = guess
    print(target_list)
  #승패판정 및 본게임종료
    if '_' not in target_list:
     win = True
     print("\n축하합니다! 승리하셨습니다!\n")
     break
    if life == 0:
     lose = True
     print("\n다시한번 도전해보세요!\n")
     break
  #본게임 종료 후 다시하기 질문
  try_answer = try_again()   
  if try_answer == 'n':
      break
#맺음말      
print("\n플레이해주셔서 감사합니다!")