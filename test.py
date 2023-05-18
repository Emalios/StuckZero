import chess


def evaluate_board(board):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            if piece.color == chess.WHITE:
                score += piece_value(piece)
            else:
                score -= piece_value(piece)
    return score


def piece_value(piece):
    if piece is None:
        return 0
    values = {"P": 100, "N": 320, "B": 330, "R": 500, "Q": 900, "K": 20000}
    return values[piece.symbol().upper()]

# Evalue la position avec une profondeur depth, si le résultat est positif la position est avantageuse pour les blanc, si néative pour les noirs, si 0 équilibrée
def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    moves = list(board.legal_moves)
    if maximizing_player:
        value = -float('inf')
        for move in moves:
            board.push(move)
            value = max(value, minimax_alpha_beta(board, depth - 1, alpha, beta, False))
            board.pop()
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # Élagage beta
            return value
    else:
        value = float('inf')
        for move in moves:
            board.push(move)
            value = min(value, minimax_alpha_beta(board, depth - 1, alpha, beta, True))
            board.pop()
            beta = min(beta, value)
            if alpha >= beta:
                break  # Élagage alpha
            return value


if __name__ == "__main__":
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    board = chess.Board(fen)
    depth = 3
    score = minimax_alpha_beta(board, depth, -float('inf'), float('inf'), board.turn)
    print("Evaluation of the FEN position after", depth, "plies:", score)
