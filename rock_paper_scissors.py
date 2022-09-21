import random

def play():
    user = input("what's your choice?: 'r' for rock , 'p' for paper, 's' for scissors: \n")
    #random.choice choses an item from a list
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It is a tie'
    
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'
    

def is_win(player, opponent):
    #function returns true if player wins
    #r> s, s> p, p > r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True

print(play())