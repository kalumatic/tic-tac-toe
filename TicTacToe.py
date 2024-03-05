
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

#  7 | 8 | 9
# -----------
#  4 | 5 | 6
# -----------
#  1 | 2 | 3


print('Welcome to Tic-Tac-Toe game!')

game_on = True

while game_on:
    
    player1 = ''
    player2 = ''
    while player1 not in ('x', 'X', 'o', 'O'):
        player1 = input('Player 1, choose X or O: ')
    
    player1 = player1.upper()
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    print(f'OK! Player 2 is {player2} then!')
    
    game_on = False
        
            



