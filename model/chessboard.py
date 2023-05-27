import chess

initialFen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq'


def evaluate_board(board):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            if piece.color == chess.WHITE:
                score += board.piece_value(piece)
            else:
                score -= board.piece_value(piece)
    return score


def piece_value(piece):
    if piece is None:
        return 0
    values = {"P": 100, "N": 320, "B": 330, "R": 500, "Q": 900, "K": 20000}
    return values[piece.symbol().upper()]


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


def start():
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    board = chess.Board(fen)
    depth = 3
    score = minimax_alpha_beta(board, depth, -float('inf'), float('inf'), board.turn)
    print("Evaluation of the FEN position after", depth, "plies:", score)


class Chessboard:

    def __init__(self, stockfish, fen=initialFen):
        self.stockfish = stockfish
        self.list = []
        self.board = chess.Board(fen)
        self.last_pos = None
        self.observators = []

    def get_last_pos(self):
        return self.last_pos

    def get_evaluation(self):
        fen = self.board.fen()
        self.stockfish.set_fen_position(fen)
        return self.stockfish.get_evaluation()

    def click_on(self, pos):
        if self.last_pos is not None:
            if self.last_pos == pos:
                return
            uci = chess.Move.from_uci(self.last_pos + pos)
            if uci in self.board.legal_moves:
                self.board.push(uci)
                self.list.append(self.board.fen())
                self.notify_observators()
            else:
                print("invalid move")
            self.last_pos = None
        else:
            self.last_pos = pos
            self.notify_observators(True)

    def fen(self):
        return self.board.fen()

    def is_ended(self):
        if self.board.is_checkmate():
            print(self.list)
        return self.board.is_checkmate()

    def get_possible_moves(self):
        return self.board.legal_moves

    def get_board(self):
        return self.board

    def notify_observators(self, draw_possibles_moves=False):
        for observator in self.observators:
            observator.render_all(draw_possibles_moves)

    def register_observator(self, graphics):
        self.observators.append(graphics)
