# Black Jack Program
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def sum(arr):
    t=0
    for x in arr:
        t=t+x
    return t

def compare(computer_score, user_score):
    if computer_score<user_score and user_score<=21:
        return "You Won"
    elif computer_score>21 and user_score<=21:
        return "You Won"
    elif computer_score==user_score:
        return "The game is a draw"
    elif computer_score>21 and user_score>21:
        return "The game is a draw"
    else:
        return "You Lost"
    
def blackjack():
    user_score=0
    computer_score=0
    hit=True
    setBust=False
    user_card_list=[]
    computer_card_list=[]
    
    user_card_index1=random.randint(0,12)
    user_card_index2=random.randint(0,12)
    
    user_card_list.append(cards[user_card_index1])
    user_card_list.append(cards[user_card_index2])
    
    computer_card_index1=random.randint(0,12)
    computer_card_list.append(cards[computer_card_index1])
    
    print(f"Your cards are: {user_card_list}")
    print(f"First card of the computer is: {computer_card_list}")
    while hit:
        user_score=sum(user_card_list)

        if user_score>21:
            setBust=True
            break
        users_choice=input("\nPress 'y' for hit.Press 'n' for stand:  ")
        if users_choice=='y':
            user_card_index=random.randint(0,12)
            user_card_list.append(cards[user_card_index])
            print(user_card_list)
        elif users_choice=='n':
            hit=False

    while computer_score<17:
        if setBust:
            print("You have lost")
            break
        computer_card_index=random.randint(0,12)
        computer_card_list.append(cards[computer_card_index])
        computer_score=sum(computer_card_list)
    
    print(f"Computer score is {computer_score}")
    print(compare( computer_score, user_score ))
    restart=input("\nDo you want to continue the game. Press 'y' for yes and 'n' for no: ")
    if restart=='y':
        user_card_list=[]
        computer_card_list=[]
        blackjack()
    
blackjack()      
