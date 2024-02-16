import random

#get input from user
def get_user_choice():
    print("RULES:\n"
          +"Rock VS Paper: paper wins\n"
          +"Rock VS Scissors: Rock wins \n"
          +"Paper VS Scissors: Scissor wins\n")
    user_choice = input("choose paper , rock, scissor:").lower()
    while user_choice not in["rock", "scissor","paper"]:
        print("INVALID INPUT,Please choose rock,paper,scissor")
        user_choice = input().lower()
   
    return user_choice

#computer choice
def get_computer_choice():
    return random.choice(["rock","paper","scissor"])
    
    

#winner
def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        print("...It's a tie!...")
    elif(user_choice == "paper" and computer_choice == "rock")or (user_choice == "rock" and computer_choice == "scissor")or (user_choice == "paper" and computer_choice == "scissor"):
            print("...You wins!...")
    else:
        print("...computer wins!...")

def play_game():
    user_score = 0
    computer_score=0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("Your choice:",user_choice)
        print("Computer choice:",computer_choice)
        
        result = determine_winner(user_choice,computer_choice)

        if result == "...You wins!...":
            user_score+=1
        elif result == "...computer wins!...":
            computer_score+=1
        play_again  = input("Do You want to play again? (y/n):").lower()
        if play_again != "y":
            break
        
        if __name__ == "__main__":
            print("---WELCOME TO ROCK PAPER SCISSOR GAME---")
            
play_game()            
        
    

    
