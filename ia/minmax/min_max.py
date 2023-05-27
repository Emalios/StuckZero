# Evalue la position avec une profondeur depth, si le résultat est positif la position est avantageuse pour les blanc, si néative pour les noirs, si 0 équilibrée
def minimax_alpha_beta(board, depth, evaluate_board, alpha=-float('inf'), beta=float('inf'), maximizing_player=False):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    moves = list(board.legal_moves)
    if maximizing_player:
        value = -float('inf')
        for move in moves:
            board.push(move)
            value = max(value, minimax_alpha_beta(board, depth - 1, evaluate_board, alpha, beta, False))
            board.pop()
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # Élagage beta
            return value
    else:
        value = float('inf')
        for move in moves:
            board.push(move)
            value = min(value, minimax_alpha_beta(board, depth - 1, evaluate_board, alpha, beta, True))
            board.pop()
            beta = min(beta, value)
            if alpha >= beta:
                break  # Élagage alpha
            return value


def find_best_move(board, depth, evaluate_board):
    best_move = None
    max_score = -float('inf')

    for move in board.legal_moves:
        board.push(move)
        score = minimax_alpha_beta(board, depth - 1, evaluate_board)
        board.pop()

        if score > max_score:
            max_score = score
            best_move = move

    return best_move
