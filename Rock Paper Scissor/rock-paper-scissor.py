'''           1  2  3
  computer    R  P  S
  player  1 R D  L  W
          2 P W  D  L
          3 S L  W  D
'''
import random # Importing random module for computer's choice

# Function to return the corresponding string for a numerical choice
def choice(choice):
    if choice==1:
        return "Rock"
    elif choice==2:
        return "Paper"
    elif choice==3:
        return "Scissor"
    
# Function to check the outcome of the round    
def check(comp,user):   # If both choices are the same
    if (comp==user): # If both choices are the same
        return "Draw"
    elif (comp==1 and user==2) or (comp==2 and user==3) or (comp==3 and user==1):
        return "Win"    # Player wins
    else:
        return "Lose"   # Computer wins

# Main function to play Rock-Paper-Scissors
def rps():
    user_counter=0
    computer_counter=0

    for i in range(1,rounds+1):

        comp=random.randint(1,3)    # Computer randomly selects Rock, Paper, or Scissors
        print(f"Round {i}")
        print("I chose my value your turn")
        user=int(input("Type 1 for Rock ,2 for Paper ,3 for scissor\n"))    # User input

        if check(comp,user)=='Draw':
            user_counter+=0
            computer_counter+=0
            print(f"Round {i} is Draw, You both chose {choice(user)}\n") 
        elif check(comp,user)=='Win':
            user_counter+=1
            computer_counter+=0
            print(f"Winner of Round {i} is {name}\n\nYou chose - {choice(user)}\nComputer chose - {choice(comp)}\n")
        else:
            user_counter+=0
            computer_counter+=1  
            print(f"Winner of  Round {i} is Computer\n\nComputer chose{choice(comp)}\nYou chose{choice(user)}\n")
    print()        
    print(f"Final Scores:\n Player:{user_counter}\n Computer:{computer_counter}")  

    # Display final scores and the winner      
    if user_counter==computer_counter:
        print("The Game is draw")
    elif user_counter>computer_counter:
        print(f"Winner of this game is {name}")
    else:
        print("Winner of this game is Computer")
            
# Game Introduction
print("Welcome to the game: Rock-Paper-scissor \n")
name=input("Enter your name to start - ")
rounds=int(input("Choose the no of rounds You want to play - "))
print()

rps()        
