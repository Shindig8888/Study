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