#다시하기 함수 정의
def try_again():
  import sys
  sys.path.append('C:\\Users\\claix\\OneDrive\\Desktop\\codes\\Study\\miniproject\\Hangman')
  from clear_windows import clear_screen
  
  while True:
        try_answer = input(" \n다시 하시겠습니까? (Y/N): ").lower()
        if try_answer == 'y' or try_answer == 'n':
            return try_answer
        else:
            clear_screen()
            print("\nY 혹은 N만 입력해주세요")
            

if __name__ == "__main__":
    print("다시하기 함수입니다.")