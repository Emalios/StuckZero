import chess

initialFen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq'


class Chessboard:

    def __init__(self, stockfish, fen=initialFen):
        self.stockfish = stockfish
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
        print(self.board.fen())
        print(self.board.move_stack)
        print(self.board.legal_moves)
        if self.last_pos is not None:
            if self.last_pos == pos:
                return
            # test if move is valid
            # TODO: roque ne fonctionne pas
            uci = chess.Move.from_uci(self.last_pos + pos)
            if uci in self.board.legal_moves:
                self.board.push(uci)
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
