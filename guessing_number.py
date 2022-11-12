#Number Guessing Game
import random

def guessing_number_game():
    user_won=False
    print("Welcome to the number guessing Game")
    print("I am thinking of a number between 1 and 100")

    difficulty_level=input("Choose a difficulty level. Type 'easy' or 'hard'").lower()

    if difficulty_level=='easy':
        lives_left=10
    elif difficulty_level=='hard':
        lives_left=5

    selected_number=random.randint(1,100)

    while lives_left > 0:
        print(f"\nNumber of lives left: {lives_left}")
        users_guess=int(input("Enter a number: "))
        result=abs(users_guess- selected_number)

        if result==0:
            print(f"You Have got it. The answer is {selected_number}")
            user_won=True
            break
            
        elif result>10:
            print("\nToo High")
            
        elif result<10:
            print("\nYou are close")
        
        lives_left-=1
        
        
    if user_won==False:
        print("You lost")
        print(f"The number was {selected_number}")

    continue_game=input("Do you wish to play again. Press 'yes' to continue and 'no' to end.\n").lower()
    if continue_game=='yes':
        guessing_number_game()
    
guessing_number_game() 
    
