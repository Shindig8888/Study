rcp_input = input("가위, 바위, 보 중 하나를 입력해주세요 : \n")
print("/n")
rcp_list = ["가위", '바위', '보']

import random
rcp_random = random.choice(rcp_list)
print(f'상대는 {rcp_random}을 냈습니다!')

winning = True
losing = True


if rcp_input=="바위" and rcp_random=='보':
    winning = True
    losing = False
elif rcp_input=="보" and rcp_random=='가위':
    winning = True
    losing = False
elif rcp_input=="가위" and rcp_random=='바위':
    winning = True
    losing = False
elif rcp_input == rcp_random:
    winning = True
    losing = True
else : 
    winning = False
    losing = True


if winning and not losing:
    print("당신은 이겼습니다! 축하합니다!") 
elif winning and losing:
    print("비겼습니다!")
else:
    print("당신은 졌습니다! 다시 시도해보세용~!")

    