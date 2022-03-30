



from random import choice

choices = ["rock", "paper", "scissors"]

# USER SELECTION
#

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in choices:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(choices)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

# function to determine winner of game
def winnerDetermination(computer,user):

    win = None
    if user == computer:
        print("It's a tie!")
    elif ((user == "rock" and computer == "scissors") or 
        (user == "paper" and computer == "rock") or 
        (user == "scissors" and computer == "paper")):
        win = True
    else:
        win = False

    if win == True:
        print("The user wins!")
    elif win == False:
        print("The computer wins.")

winnerDetermination(c,u)
