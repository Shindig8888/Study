import data #리스트들
from replit import clear #리플렛_클리어

def gen_random_person(dic_list, end):
    import random
    rand_index = random.randint(0, len(dic_list) - 1)
    poplist = dic_list.pop(rand_index)
    return poplist#랜덤뽑기

def q_more_followers():
    while True:
        answer = input('\nWho has more follwers? Type "A" or "B" : ').lower()
        if answer == 'a' or answer == 'b':
            return answer
        else:
            continue ##팔로워 예상 질문

def compare(compare_a, compare_b):
    win_compare_a = True
    if int(compare_a['follower_count']) < int(compare_b['follower_count']):
        win_compare_a = False
    return win_compare_a#내부적으로 누가 더 팔로워 높은지 계산

def win_lose(more_follwers_answer, a_win):
    in_line = True
    if more_follwers_answer == 'a' and a_win:
        print('\nYou got it right!')
        in_line = True
        return in_line
    elif more_follwers_answer == 'b' and not a_win:
        print('\nYou got it right!')
        in_line = True
        return in_line
    else:
        print('\nWrong!')
        in_line = False
        return in_line#승패#승패

def q_try_again():
    while True:
        answer = input('\nTry again? Type "Y" or "N" : ').lower()
        if answer == 'y' or answer == 'n':
            return answer
        else:
            continue#다시하기 질문

clear()
print("\nWelcome to Higher Lower!\n\nGuess who's follower is higher or lower!") #greetings
end = False
while True:
    round = 1
    point = 0
    compare_a = {} #setting defualt
    data_2 = data.data[:] #assigning different id to data2 so that can set defualt
    while end is False:
        if len(data_2) == 1: #end-of-list 1
            pass
        elif len(data_2) ==0: #end-of-list 2
            print("\nEnd of list I have!")
            break
        elif round == 1: #only random gen a on first start
            print(data.logo)
            compare_a = gen_random_person(data_2, end)
            print(
                f"\ncompare A : {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}"
            )
        else: #only print information if not first start
            print(
                f"\ncompare A : {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}"
            )
            
        print(data.vs)

        compare_b = gen_random_person(data_2, end)
        if compare_b == {}:
            end = True #end if end-of-list
        else:
            print(
                f"\nagainst B : {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}"
            ) # gen b
 
        
        more_follwers_answer = q_more_followers()
        print(data.logo)
        a_win = compare(compare_a, compare_b)
        in_line = win_lose(more_follwers_answer, a_win)
        clear()
        if in_line:
            round+=1
            point+=1
            print(data.logo)
            print(f'\nYour score is ... {point}')
            compare_a = compare_b #b => a
            continue
        else:
            round+=1
            print('You lose!')
            end = True
    
    print(f'\nYour final score is...{point}!')
    
    answer_try_again = q_try_again() #재시작
    if answer_try_again == 'y':
        end = False #end = False로 만들어서 루프가능
        clear()
        continue    
    else:
        break
        

clear()
print(data.logo)
print('\nThank you for playing Higher and Lower!')
