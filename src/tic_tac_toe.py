from utils import print_board, check_winner
from minimax import find_best_move

def initialize_board():
    return [' ' for _ in range(9)]

def display_instructions():
    print("Welcome to Tic-Tac-Toe!")
    print("You will play against an AI opponent.")
    print("The board positions are numbered as follows:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

def player_move(board):
    move = int(input("Enter your move (1-9): ")) - 1
    while board[move] != ' ':
        print("Invalid move. Try again.")
        move = int(input("Enter your move (1-9): ")) - 1
    board[move] = 'X'

def ai_move(board):
    print("AI is making its move...")
    best_move = find_best_move(board)
    board[best_move] = 'O'

def is_full(board):
    return ' ' not in board

def main():
    display_instructions()
    board = initialize_board()
    print_board(board)
    
    while True:
        player_move(board)
        print_board(board)
        
        if check_winner(board, 'X'):
            print("You win!")
            break
        
        if is_full(board):
            print("It's a tie!")
            break
        
        ai_move(board)
        print_board(board)
        
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        
        if is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
