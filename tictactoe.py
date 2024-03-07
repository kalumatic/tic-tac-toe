
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

#  7 | 8 | 9
# -----------
#  4 | 5 | 6
# -----------
#  1 | 2 | 3


def choose_sides():
    '''Assigns sides to players.'''
    
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
    
    return player1, player2


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
    print()
    
    
def check_win(table):
    '''Checks if the player who last played won the game'''
    
    for i in range(1, 4):
        # check for horizontal and vertical win
        if table[f'{1 + (i - 1) * 3}'] == table[f'{2 + (i - 1) * 3}'] == table[f'{3 + (i - 1) * 3}'] and table[f'{1 + (i - 1) * 3}'] != ' ':
            return True
        if table[f'{i}'] == table[f'{i + 3}'] == table[f'{i + 6}'] and table[f'{i}'] != ' ':
            return True
    
    # check for diagonal win
    if table['1'] == table['5'] == table['9'] != ' ':
        return True
    if table['3'] == table['5'] == table['7'] != ' ':
        return True
    
    return False
    
    
def player_input(table, turn):
    '''Retrieves the field that the player has chosen.'''
    
    field = 0
    while field not in range(1, 10):
        try:
            field = int(input(f'Player {turn}, choose one of the remaining fields: '))
            if field not in range(1, 10):
                print('That field doesn\'t exist! Try again.')
            elif table[f'{field}'] != ' ':
                print('That field is occupied! Try again.')
                field = 0
        except ValueError:
            print('Not a number! Try again.')
    
    return field


def play_on():
    '''
    Checks if players wish to play another game.
    '''
    
    answer = ''
    
    while answer not in ('Y', 'y', 'N', 'n'):
        answer = input('Do you want to play again (Y/N)? ')
        
    if answer.lower() == 'n':
        print('Goodbye!\n')
        return False
    else:
        print('Alright then!\n')
        return True
    


# main function

print()
print('Welcome to Tic-Tac-Toe game!\n')

game_on = True

while game_on:
    
    # Player 1 gets to choose X or O, Player 2 gets assigned the remaining one

    player1, player2 = choose_sides()
    
    # start of the game
    
    table = init_game()
        
    # display the table
    
    display_table(table)
    
    # players make their moves until someone wins
    
    # 1 for Player 1 --- 2 for Player 2
    turn = 1
    while not check_win(table) and turn < 10:
        
        field_chosen = player_input(table, turn)
        
        if turn % 2 == 1:
            table[f'{field_chosen}'] = player1
        else:
            table[f'{field_chosen}'] = player2
        
        turn += 1      
        display_table(table)
        
    
    if not check_win(table) and turn == 10:
        print('IT\'S A DRAW!\n')
    elif turn % 2 == 1:
        print('PLAYER 2 WINS! CONGRATS!\n')
    else:
        print('PLAYER 1 WINS! CONGRATS!\n')
            
    game_on = play_on()


