# --- Minimax Algorithm ---

def minimax(board, depth, is_maximizing):
    """Recursive Minimax algorithm to choose the optimal move."""
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (i, j) in available_moves(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for (i, j) in available_moves(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(best_score, score)
        return best_score