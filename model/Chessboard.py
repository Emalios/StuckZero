import chess

initialFen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'


class Chessboard:

    def __init__(self, fen=initialFen):
        self.board = chess.Board(fen)
        self.last_pos = None
        self.observators = []

    def get_last_pos(self):
        return self.last_pos

    def click_on(self, pos):
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
                for move in self.board.legal_moves:
                    print(chess.SQUARE_NAMES[move.to_square])
            self.last_pos = None
        else:
            self.last_pos = pos
            print('clicked', pos)
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
        print("notify", draw_possibles_moves)
        print(self.observators)
        for observator in self.observators:
            observator.render_all(draw_possibles_moves)

    def register_observator(self, graphics):
        self.observators.append(graphics)
