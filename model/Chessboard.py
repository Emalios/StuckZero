import chess

initialFen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'


class Chessboard:

    def __init__(self, fen=initialFen):
        self.board = chess.Board(fen)
        self.last_pos = None

    def get_last_pos(self):
        return self.last_pos

    def get_possible_moves(self):
        return self.board.legal_moves

    def get_board(self):
        return self.board

    def get_size(self):
        return self.width, self.height
