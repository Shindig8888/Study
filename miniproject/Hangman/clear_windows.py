import os

# 화면 지우기
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')