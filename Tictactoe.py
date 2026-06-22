import math

# Board
board = [' ' for _ in range(9)]

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(b, player):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for w in wins:
        if b[w[0]] == b[w[1]] == b[w[2]] == player:
            return True
    return False

def is_full(b):
    return ' ' not in b

def minimax(b, is_maximizing):
    if check_winner(b, 'O'):
        return 1
    if check_winner(b, 'X'):
        return -1
    if is_full(b):
        return 0
    
    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                best = max(best, minimax(b, False))
                b[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                best = min(best, minimax(b, True))
                b[i] = ' '
        return best

def computer_move():
    best_score = -math.inf
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

def play_game():
    print("Welcome to Tic Tac Toe!")
    print("You are X, Computer is O")
    print("Board positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:
        print_board()
        
        # Player move
        while True:
            try:
                move = int(input("Your move (1-9): ")) - 1
                if board[move] == ' ':
                    board[move] = 'X'
                    break
                else:
                    print("That spot is taken!")
            except:
                print("Please enter a number 1-9")
        
        if check_winner(board, 'X'):
            print_board()
            print("Congratulations! You won!")
            break
        if is_full(board):
            print_board()
            print("It's a draw!")
            break
        
        # Computer move
        print("Computer is thinking...")
        computer_move()
        
        if check_winner(board, 'O'):
            print_board()
            print("Computer wins!")
            break
        if is_full(board):
            print_board()
            print("It's a draw!")
            break

play_game()
