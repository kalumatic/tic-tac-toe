
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

#  7 | 8 | 9
# -----------
#  4 | 5 | 6
# -----------
#  1 | 2 | 3

def init_game():
    '''Initializes the table and prints the instruction.'''
    print('The game can begin!\n')
    
    print('You play by picking numbers which represent fields of the table.\n')
    print(f' 7 | 8 | 9 ')
    print('-----------')
    print(f' 4 | 5 | 6 ')
    print('-----------')
    print(f' 1 | 2 | 3 ')
    print()

    return {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}


def display_table(table):
    '''Prints the current status of the table.'''
    print('Current status of the table:\n')
    print(f' {table["7"]} | {table["8"]} | {table["9"]} ')
    print('-----------')
    print(f' {table["4"]} | {table["5"]} | {table["6"]} ')
    print('-----------')
    print(f' {table["1"]} | {table["2"]} | {table["3"]} ')


print('Welcome to Tic-Tac-Toe game!\n')

game_on = True

while game_on:
    
    # Player 1 gets to choose X or O, Player 2 gets assigned the remaining one

    player1 = ''
    player2 = ''
    while player1 not in ('x', 'X', 'o', 'O'):
        player1 = input('Player 1, choose X or O: ')
    
    player1 = player1.upper()
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    print(f'OK! Player 2 is {player2} then!\n')
    
    ############################################
    
    # start of the game
    
    table = init_game()
        
    # display the table
    
    display_table(table)
    
    game_on = False
        
            



