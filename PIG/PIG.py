import random

def roll():
    min_number=1
    max_number=6
    value=random.randint(min_number,max_number)
    return value

while True:
    players=input("Enter the number of players in range (2-4)")
    if players.isdigit():
        players=int(players)
        if(2<=players<=4):
            break
        else:
            print("Enter players between 2 and 4 only")
    else:
        print("Invalid Try again")        

max_score=50
player_score=[0 for _ in range(players)]

while(max(player_score)<max_score):
    for player_index in range(players):
        print("\nPlayer,",player_index+1,"Turn has just started")
        print("Your total score is ",player_score[player_index])
        current_score=0 

        while True:      

            should_roll=input("Would you like to roll the dice (y):")
            if should_roll.lower()!='y':
                break

            value=roll()

            if value==1:
                print("You rolled 1 Turn done!")
                current_score=0
                break
            else:
                current_score+=value
                print("You rolled a ",value)  
            print("your current score is",current_score)      
        player_score[player_index]+=current_score
        print("Your total score is:",player_score[player_index])        

max_score=max(player_score)
winning_index=player_score.index(max_score)        
print("Winner of the game is player",winning_index+1,"with a score of",max_score)