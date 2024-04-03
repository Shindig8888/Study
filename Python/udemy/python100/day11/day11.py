import random
cardlist = ['A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K']



def dealer_picks(dealerhand, displayhand, b_cardlist):
    random_index = random.randint(1,len(b_cardlist))
    card = b_cardlist.pop(random_index-1)
    dealerhand.append(card)
    if len(dealerhand)==1:
        displayhand.append(dealerhand[0])
    else:
        displayhand.append('-')
    
def player_picks(playerhand, b_cardlist):
    random_index = random.randint(1,len(b_cardlist))
    card = b_cardlist.pop(random_index-1)
    playerhand.append(card)
    

def sum_hand(any_list):
    result = 0
    for items in range(0,len(any_list)):
        if any_list[items] == 'J' or any_list[items] == 'Q' or any_list[items] == 'K':
            result += 10
        elif any_list[items] =='A':
            result += 1
        else:
            result += int(any_list[items])
    return result

def hit():
    hit = False
    while True:
        answer = input("\nWould you Hit or Stand : ").lower()
        if answer != 'hit' and answer != 'stand':
            print('\nPlease enter "Hit" or "Stand"')
            continue
        elif answer == 'hit':
            hit = True
            break
        else:
            hit = False
            break
    return hit

def ace():
    while True:
        answer = input('\nWould you treat your ace card as "1" or "11 ? (1 or 11): ')
        if answer == '1' or answer == '11':
            break
        else:
            print('\nPlease enter "Y" or "N"')
            continue
    return answer

while True:
    cardlist =         ['A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K']
    dealers_hand = []
    display_dealer_hand = []
    players_hand = []
    dealer_picks(dealers_hand, display_dealer_hand, cardlist)
    dealer_picks(dealers_hand, display_dealer_hand, cardlist)
    player_picks(players_hand, cardlist)
    player_picks(players_hand, cardlist)
 

    while sum_hand(dealers_hand) < 17:
        dealer_picks(dealers_hand, display_dealer_hand, cardlist)
    print(f"\nPlayer's hand is : {players_hand}")
    print(f"\nDealer's hand is : {display_dealer_hand}")
    
    answer_hit = True
    while answer_hit:
        answer_hit = hit()
        if answer_hit:
            print('\nHIT!!')
            player_picks(players_hand, cardlist)
            print(f"\nPlayer's hand is : {players_hand}")
            print(f"\nDealer's hand is : {display_dealer_hand}")
        else:
            break
            
    dealer_sum = sum_hand(dealers_hand)
    player_sum = sum_hand(players_hand)

    for i in players_hand:
        if i == 'A':
            print(f'\n플레이어의 {players_hand.index(i)+1}번째 카드가 에이스입니다!')
            a = ace()
            if a =='11':
                player_sum += 10
                
    print(f"\nPlayer's hand is : {players_hand}")
    print(f"\nDealer's hand is : {dealers_hand}")
    print(f'\n플레이어의 총 점은 {player_sum}, 딜러의 총 점은 {dealer_sum} 입니다!')
    if player_sum == 21:
        print('\n플레이어 블랙잭!')
    if dealer_sum == 21:
        print('\n딜러 블랙잭!')

    if player_sum > 21:
        print('\n플레이어 버스트!')
    if dealer_sum > 21:
        print('\n딜러 버스트!')

    if dealer_sum <= 21 and player_sum <= 21 and dealer_sum>player_sum:
        print("\n딜러 승!")
    elif dealer_sum <= 21 and player_sum <= 21 and dealer_sum<player_sum:
        print("\n플레이어 승!")
    elif dealer_sum > 21 and player_sum <= 21:
        print("\n플레이어 승!")
    elif dealer_sum <= 21 and player_sum > 21:
        print("\n딜러 승!")
    elif dealer_sum > 21 and player_sum > 21:
        print("\n무승부!")
    elif dealer_sum == player_sum:
        print("\n무승부!")
    
    retry = input("\n다시 하시겠습니까?(Y/N) : ").lower()
    if retry == 'y':
        continue
    else:
        break

print('\n블랙잭을 플레이해주셔서 감사합니다!')
    


print(cardlist)
print(dealers_hand)
print(players_hand)