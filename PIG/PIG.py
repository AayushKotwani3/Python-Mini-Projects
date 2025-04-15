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
     
        