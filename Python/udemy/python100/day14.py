import data

def gen_random_person(dic_list, end):
    try:
        import random
        rand_index = random.randint(0, len(dic_list) - 1)
        poplist = dic_list.pop(rand_index)
        return poplist
    except ValueError:
        print("\nYou got it all right!")
        poplist = {}
        return poplist


def q_more_followers():
    while True:
        answer = input('\nWho has more follwers? Type "A" or "B" : ').lower()
        if answer == 'a' or answer == 'b':
            return answer
        else:
            continue


def compare(compare_a, compare_b):
    win_compare_a = True
    if int(compare_a['follower_count']) < int(compare_b['follower_count']):
        win_compare_a = False
    return win_compare_a

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
        return in_line

def q_try_again():
    while True:
        answer = input('\nTry again? Type "Y" or "N" : ').lower()
        if answer == 'y' or answer == 'n':
            return answer
        else:
            continue


print(data.logo)
print("\nWelcome to Higher Lower!\n\nGuess who's follower is higher or lower!")
end = False
while True:
    round = 1
    point = 0
    compare_a = {}
    data_2 = data.data
    while end is False:
        if round == 1:
            print(data.logo)
            compare_a = gen_random_person(data_2, end)
            print(
                f"\n{compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}"
            )
        elif len(data_2) == 1:
            pass
        else:
            print(data.logo)
            print(
                f"\n{compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}"
            )
        print(data.vs)

        compare_b = gen_random_person(data.data, end)
        if compare_b == {}:
            end = True
        else:
            print(
                f"\n{compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}"
            )
        try:
            a = int(compare_b['follower_count'])+1
        except KeyError:
            break

        more_follwers_answer = q_more_followers()
        a_win = compare(compare_a, compare_b)
        in_line = win_lose(more_follwers_answer, a_win)

        if in_line:
            round+=1
            compare_a = compare_b
            continue

    print(f'\nYour score is: {point}!')
    answer_try_again = q_try_again()
    if answer_try_again == 'y':
        end = False
        continue
    else:
        break

print('Thank you for playing Higher and Lower!')
