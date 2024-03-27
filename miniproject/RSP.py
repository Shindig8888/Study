print("*"*50)
print("가위바위보 시물레이터에 오신걸 환영합니다!\n")
while True:

    rsp_input = input("가위, 바위, 보 중 하나를 입력해주세요 : \n")

    rsp_list = ["가위", '바위', '보']

    import random
    rsp_random = random.choice(rsp_list)
   

    winning = False
    losing = False

    if rsp_input=="가위" and rsp_random=='보':
        winning = True
        losing = False
    elif rsp_input=="바위" and rsp_random=='가위':
        winning = True
        losing = False
    elif rsp_input=="보" and rsp_random=='바위':
        winning = True
        losing = False
    elif rsp_input == rsp_random:
        winning = True
        losing = True
    elif winning == False and losing == False:
        winning = False
        losing = False
    else : 
        winning = False
        losing = True

    if winning != False and losing!=False:
        print(f'상대는 {rsp_random}을 냈습니다!\n')
    else:
        print("제대로된 글자를 입력해주세요\n")
        break
    

    if winning and not losing:
        print("당신은 이겼습니다! 축하합니다!\n") 
    elif winning and losing:
        print("비겼습니다!")
    else:
        print("당신은 졌습니다! 다시 시도해보세용~!\n")


    a = input("Y를 입력하시면 한 판 더! 한 판 더 하시겠습니까? : \n").lower()
    
    print("*"*50)
    if a != 'y':
        break

print("이용해주셔서 감사합니다. 프로그램을 종료합니다!")
print("*"*50)

# import random

# print("*" * 50)
# print("가위바위보 시물레이터에 오신걸 환영합니다!\n")

# while True:
#     rsp_input = input("가위, 바위, 보 중 하나를 입력해주세요 : \n").strip().lower()
#     rsp_list = ["가위", '바위', '보']
#     rsp_random = random.choice(rsp_list)

#     if rsp_input not in rsp_list:
#         print("제대로된 글자를 입력해주세요\n")
#         break
    
#     print(f'상대는 {rsp_random}을 냈습니다!\n')

#     if (rsp_input, rsp_random) in [('가위', '보'), ('바위', '가위'), ('보', '바위')]:
#         print("당신은 이겼습니다! 축하합니다!\n") 
#     elif rsp_input == rsp_random:
#         print("비겼습니다!")
#     else:
#         print("당신은 졌습니다! 다시 시도해보세요~!\n")

#     if input("Y를 입력하시면 한 판 더! 한 판 더 하시겠습니까? : \n").strip().lower() != 'y':
#         break

#     print("*" * 50)

# print("이용해주셔서 감사합니다. 프로그램을 종료합니다!")
# print("*" * 50)
# 주요 변경 사항:

# import random 문을 코드 상단으로 이동하여 코드의 가독성을 높였습니다.
# 입력을 받을 때 strip().lower() 메서드를 사용하여 공백을 제거하고 소문자로 변환했습니다.
# 승패 판단 부분을 간결하게 변경하여 코드를 더 읽기 쉽게 만들었습니다.
# input() 함수를 사용하여 한 판 더 진행할지 여부를 더 간결하게 처리했습니다.

