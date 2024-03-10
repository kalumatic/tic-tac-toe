'''
Tic-Tac-Toe game for two players
'''


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

    p1 = ''
    p2 = ''

    while p1 not in ('x', 'X', 'o', 'O'):
        p1 = input('Player 1, choose X or O: ')

    p1 = p1.upper()

    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'

    print(f'OK! Player 2 is {p2} then!\n')

    return p1, p2


def init_game():
    '''Initializes the table and prints the instruction.'''

    print('The game can begin!\n')

    print('You play by picking numbers which represent fields of the table.\n')
    print(' 7 | 8 | 9 ')
    print('-----------')
    print(' 4 | 5 | 6 ')
    print('-----------')
    print(' 1 | 2 | 3 ')
    print()

    return {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ',
            '6': ' ', '7': ' ', '8': ' ', '9': ' '}


def display_table(tab):
    '''Prints the current status of the table.'''

    print('Current status of the tab:\n')
    print(f' {tab["7"]} | {tab["8"]} | {tab["9"]} ')
    print('-----------')
    print(f' {tab["4"]} | {tab["5"]} | {tab["6"]} ')
    print('-----------')
    print(f' {tab["1"]} | {tab["2"]} | {tab["3"]} ')
    print()


def check_win(tab):
    '''Checks if the player who last played won the game'''

    for i in range(1, 4):
        # check for horizontal and vertical win
        if (tab[f'{1 + (i - 1) * 3}'] == tab[f'{2 + (i - 1) * 3}']
                == tab[f'{3 + (i - 1) * 3}'] and tab[f'{1 + (i - 1) * 3}'] != ' '):
            return True
        if (tab[f'{i}'] == tab[f'{i + 3}'] == tab[f'{i + 6}']
                and tab[f'{i}'] != ' '):
            return True

    # check for diagonal win
    if tab['1'] == tab['5'] == tab['9'] != ' ':
        return True
    if tab['3'] == tab['5'] == tab['7'] != ' ':
        return True

    return False


def player_input(tab, trn):
    '''Retrieves the field that the player has chosen.'''

    field = 0
    while field not in range(1, 10):
        try:
            field = int(input(f'Player {trn}, choose one of the remaining fields: '))
            if field not in range(1, 10):
                print('That field doesn\'t exist! Try again.')
            elif tab[f'{field}'] != ' ':
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
