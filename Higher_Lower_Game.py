
import os
#os.sysmtem('CLS') ## Clear screen.
from art import logo, vs
from game_data import data
import random
# Generate a random account from the game data.
def random_account():
    """Get data from random account"""
    return random.choice(data)
# Format account data into printable format.
def format_account(account):
    """Format account data into printable format. name, description and country."""
    data_name=account["name"]
    data_description=account["description"]
    data_country=account["country"]
    return f"{data_name} a {data_description}, from {data_country}."

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong."""
    if a_followers>b_followers:
        return guess=="a"
    else:
        return guess=="b"

def play_again():
    """Ask user if they want to play again."""
    play_again=input("Do you want to play again? Type 'Y' or 'N': ").lower()
    if play_again=="y":
        game()
    else:
        print("Thanks for playing!")
        exit()
        
def game():
    # Add art.
    print(logo)  
    score=0
    game_should_continue=True
    game_continue=True
    account_a=random_account()
    account_b=random_account()
    # Make game repeatable.
    while game_should_continue:
        account_a=account_b
        account_b=random_account()
        # Make B become the next A.
        while account_a==account_b:  
            account_b=random_account()

        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Compare B: {format_account(account_b)}")
        # Ask user for a guess.
        guess=input("Who has more followers? Type 'A' or 'B': ").lower()
        # Check if user is correct.
        ## Get follower count.
        a_follower_count=account_a["follower_count"]
        b_follower_count=account_b["follower_count"]
        is_correct=check_answer(guess, a_follower_count, b_follower_count)
        os.system("CLS") # Clear screen between rounds. 
        print(logo)
        ## If Statement

        if is_correct: 
            score+=1 # Score Keeping.
            print(f"You're right! Current score: {score}.")
        else:                                                    # Feedback.
            #game_should_continue=False
            print(f"Sorry, that's wrong. Final score: {score}.")
            play_again()
    
game()
       
