#필요 모듈 import
import sys
sys.path.append('C:\\Users\\claix\\OneDrive\\Desktop\\codes\\Study')
import random

from miniproject.Hangman import hang_list #행맨 아스키아트, 퀴즈단어리스트, 알파벳리스트
from miniproject.Hangman.try_again import try_again #다시하기 모듈
from miniproject.Hangman.clear_windows import clear_screen #윈도우즈용 클리어 모듈

#게임 루프시작
while True:
  #인삿말
  clear_screen()
  print("행맨 게임에 오신걸 환영합니다!\n\n총 6번의 기회가 주어지며, 알파벳을 입력해 단어를 맞추시면 됩니다!")
  
  #초기화해야할 변수
  win = False
  lose = False
  life = 6
  hang_round = 1

  #무작위함수들이기때문에 초기화
  random.shuffle(hang_list.word_list)
  ran_num = random.randint(1, len(hang_list.word_list))
  target_word = list(hang_list.word_list[ran_num-1])

  #-디버그용-
  #print(target_word)

  #보여줄 디스플레이 설정
  display = list('_'*len(target_word))

#초기화 하지않고 반복: 본게임
  #input
  while win is False and lose is False:  
    
    #입력
    if hang_round == 1:
      print(hang_list.stages[6-life])
      print(" ".join(display))
    guess = input(f"\n 당신의 {hang_round}번째 추측은?(한글자의 알파벳으로만 답해주세요) : ").lower().replace(" ","")
    clear_screen()
    if guess not in hang_list.letters:
        clear_screen()
        print("\n\n한글자의 알파벳으로 답해주세요!")
        if hang_round!=1:
          print(hang_list.stages[6-life]) 
          print(" ".join(display))
        continue
    if guess in display:
        clear_screen()
        print(f"\n\n{guess}는 이미 맞춘 알파벳입니다!")
        if hang_round!=1:
          print(hang_list.stages[6-life]) 
          print(" ".join(display))
        continue
    clear_screen()
    
  #입력검정   
    if guess in target_word:
     print("\n\n맞췄습니다!")
    else:
      life -= 1
      print(f"\n\n틀렸습니다! 남은 목숨은 {life}개입니다!")
    hang_round+=1

  #입력 기록 및 출력  
    print(hang_list.stages[6-life])
    for i in range(0, len(target_word)):
      if guess == target_word[i]:
        display[i] = guess
    print(" ".join(display))

  #승패판정 및 본게임종료
    if '_' not in display:
     win = True
     clear_screen()
     print(f"\n축하합니다! 승리하셨습니다! 점수는 {int(life/6*100)}점입니다!")
     break
    if life == 0:
     clear_screen()
     lose = True
     print("\n졌습니다 ㅠㅠ다시한번 도전해보세요!")
     break
  #본게임 종료 후 다시하기 질문
  try_answer = try_again() 
  if try_answer == 'n':
      break
  
#맺음말
clear_screen()      
print("\n플레이해주셔서 감사합니다!")