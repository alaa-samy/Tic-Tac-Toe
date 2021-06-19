
board = [' ' for i in range(10)]

def insert_letter(letter,position):
    board[position] = letter

def space_is_free(position):
    return board[position] == ' '

def print_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('----------------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def is_winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal


def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def player_move():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if (move > 0 and move < 10):
                if space_is_free(move):
                    run = False
                    insert_letter('X' , move)
                else:
                    print('This position is already occupied')
            else:
                print('Please type a number within range 10')
        except:
            print('Please type a number')

def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def computer_move():
    possible_moves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for letter in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = letter
            if is_winner(board_copy, letter):
                move = i
                return move

    # Take one of the corner
    corners_open = []
    for i in possible_moves:
        if i in [1,3,7,9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    # Try to take the center
    if 5 in possible_moves:
        move = 5
        return move

    # Take one of the edges
    edges_open = []
    for i in [2,4,6,8]:
        edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)
        return move
    
def main():
    print('Welcome to Tic Tac Toe!')
    print_board(board)

    while not(is_board_full(board)):
        if not(is_winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not(is_winner(board, 'X')):
            move = computer_move()
            if move == 0:
                print('Tie Game!')
            else:
                insert_letter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                print_board(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if is_board_full(board):
        print('Tie Game!')
 
while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break

