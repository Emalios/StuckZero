import chess

from ia.minmax.min_max import find_best_move


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


if __name__ == "__main__":
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    board = chess.Board(fen)
    depth = 8
    best_move = find_best_move(board, depth, evaluate_board)
    print("Best move", best_move)
