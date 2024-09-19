def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return 10 if board[i] == 'O' else -10
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return 10 if board[i] == 'O' else -10
    if board[0] == board[4] == board[8] != ' ':
        return 10 if board[0] == 'O' else -10
    if board[2] == board[4] == board[6] != ' ':
        return 10 if board[2] == 'O' else -10
    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    if ' ' not in board:
        return 0

    if is_maximizing:
        best = -1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(board, depth+1, False))
                board[i] = ' '
        return best
    else:
        best = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(board, depth+1, True))
                board[i] = ' '
        return best

def find_best_move(board):
    best_val = -1000
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, False)
            board[i] = ' '
            if move_val > best_val:
                best_move = i
                best_val = move_val
    return best_move
