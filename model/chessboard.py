import chess
from stockfish import Stockfish

initialFen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq'

class Chessboard:

    def __init__(self, stockfish=Stockfish(path="stockfish-windows-2022-x86-64-avx2.exe", depth=14,
                          parameters={"Threads": 6}), fen=initialFen):
        self.stockfish = stockfish
        self.list = []
        self.moves_list = []
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
                previous_fen = self.board.fen()
                self.board.push(uci)
                # Affichage des x meilleurs coups
                self.stockfish.set_fen_position(previous_fen)
                best_moves = self.stockfish.get_top_moves(3)
                self.moves_list.append(uci)
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
            print(self.board.turn)
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
