import chess
import chess.pgn

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


def generate_pgn(fen_list):
    moves_list = [chess.Move.from_uci(move_str) for move_str in [
        'e2e4', 'd7d5', 'e4e5', 'c7c5', 'd2d4', 'c5c4', 'g1f3', 'e7e6', 'c1g5',
        'f7f6', 'e5f6', 'g7f6', 'g5h4', 'f8g7', 'f1e2', 'b8c6', 'e1g1', 'd8d6',
        'b1a3', 'f6f5', 'b2b3', 'c4b3', 'a2b3', 'g8f6', 'e2b5', 'a7a6', 'b5a4',
        'b7b5', 'a4b5', 'a6b5', 'a3b5', 'a8a1', 'd1a1', 'f6e4', 'a1a8', 'e8g8',
        'b5d6', 'f8d8', 'a8c6', 'g7e5', 'd6b7', 'h7h6', 'h4d8', 'e4f2', 'c6e8',
        'g8h7', 'e8f7', 'h7h8', 'f3e5', 'c8d7', 'd8f6'
    ]]

    # Create a new PGN game
    game = chess.pgn.Game()

    game = chess.pgn.Game()
    game.headers["Event"] = "Example"
    node = game.add_variation(moves_list[0])

    for move in moves_list[1::]:
        node = node.add_variation(move)
    #node = node.add_variation(chess.Move.from_uci("e7e5"))

    # Export the game to a PGN file
    pgn_file = open("game.pgn", "w")
    exporter = chess.pgn.FileExporter(pgn_file)
    game.accept(exporter)
    pgn_file.close()


if __name__ == "__main__":
    fens = ['rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1', 'rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2', 'rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2', 'r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3', 'r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3', 'r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4', 'r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/2N2N2/PPPP1PPP/R1BQK2R b KQkq - 5 4', 'r1bqkb1r/ppp2ppp/2np1n2/4p3/2B1P3/2N2N2/PPPP1PPP/R1BQK2R w KQkq - 0 5', 'r1bqkb1r/ppp2ppp/2np1n2/4p3/2B1P3/2N2N2/PPPP1PPP/R1BQ1RK1 b kq - 1 5', 'r2qkb1r/ppp2ppp/2np1n2/4p3/2B1P1b1/2N2N2/PPPP1PPP/R1BQ1RK1 w kq - 2 6', 'r2qkb1r/ppp2ppp/2np1n2/4p3/2B1P1b1/1PN2N2/P1PP1PPP/R1BQ1RK1 b kq - 0 6', 'r2qkb1r/ppp2ppp/2np1n2/4p3/2B1P3/1PN2b2/P1PP1PPP/R1BQ1RK1 w kq - 0 7', 'r2qkb1r/ppp2ppp/2np1n2/4p3/2B1P3/1PN2Q2/P1PP1PPP/R1B2RK1 b kq - 0 7', 'r2qk2r/ppp1bppp/2np1n2/4p3/2B1P3/1PN2Q2/P1PP1PPP/R1B2RK1 w kq - 1 8', 'r2qk2r/ppp1bppp/2np1n2/3Np3/2B1P3/1P3Q2/P1PP1PPP/R1B2RK1 b kq - 2 8', 'r2q1rk1/ppp1bppp/2np1n2/3Np3/2B1P3/1P3Q2/P1PP1PPP/R1B2RK1 w - - 3 9', 'r2q1rk1/ppp1Nppp/2np1n2/4p3/2B1P3/1P3Q2/P1PP1PPP/R1B2RK1 b - - 0 9', 'r4rk1/ppp1qppp/2np1n2/4p3/2B1P3/1P3Q2/P1PP1PPP/R1B2RK1 w - - 0 10', 'r4rk1/ppp1qppp/2np1n2/4p3/2B1P3/1P1P1Q2/P1P2PPP/R1B2RK1 b - - 0 10', 'r4rk1/ppp1qppp/3p1n2/4p3/2BnP3/1P1P1Q2/P1P2PPP/R1B2RK1 w - - 1 11', 'r4rk1/ppp1qppp/3p1n2/4p3/2BnP3/1P1P4/P1P2PPP/R1BQ1RK1 b - - 2 11', '3r1rk1/ppp1qppp/3p1n2/4p3/2BnP3/1P1P4/P1P2PPP/R1BQ1RK1 w - - 3 12', '3r1rk1/ppp1qppp/3p1n2/4p3/2BnP3/1P1PB3/P1P2PPP/R2Q1RK1 b - - 4 12', '3r1rk1/ppp1qppp/2np1n2/4p3/2B1P3/1P1PB3/P1P2PPP/R2Q1RK1 w - - 5 13', '3r1rk1/ppp1qppp/2np1n2/4p3/2B1P3/1P1PB3/P1PQ1PPP/R4RK1 b - - 6 13', '3r1rk1/1pp1qppp/p1np1n2/4p3/2B1P3/1P1PB3/P1PQ1PPP/R4RK1 w - - 0 14', '3r1rk1/1pp1qppp/p1np1n2/4p3/2B1P3/1P1PB2P/P1PQ1PP1/R4RK1 b - - 0 14', '3r1rk1/2p1qppp/p1np1n2/1p2p3/2B1P3/1P1PB2P/P1PQ1PP1/R4RK1 w - - 0 15', '3r1rk1/2p1qppp/p1np1n2/1p1Bp3/4P3/1P1PB2P/P1PQ1PP1/R4RK1 b - - 1 15', '3r1rk1/2p1qppp/p1np4/1p1np3/4P3/1P1PB2P/P1PQ1PP1/R4RK1 w - - 0 16', '3r1rk1/2p1qppp/p1np4/1p1Pp3/8/1P1PB2P/P1PQ1PP1/R4RK1 b - - 0 16', '3r1rk1/2p1qppp/p2p4/1p1Pp3/3n4/1P1PB2P/P1PQ1PP1/R4RK1 w - - 1 17', '3r1rk1/2p1qppp/p2p4/1p1Pp3/3B4/1P1P3P/P1PQ1PP1/R4RK1 b - - 0 17', '3r1rk1/2p1qppp/p2p4/1p1P4/3p4/1P1P3P/P1PQ1PP1/R4RK1 w - - 0 18', '3r1rk1/2p1qppp/p2p4/1p1P4/3p4/1P1P3P/P1PQ1PP1/R3R1K1 b - - 1 18', '3r1rk1/2p2ppp/p2p1q2/1p1P4/3p4/1P1P3P/P1PQ1PP1/R3R1K1 w - - 2 19', '3r1rk1/2p2ppp/p2p1q2/1p1P4/3pR3/1P1P3P/P1PQ1PP1/R5K1 b - - 3 19', '3rr1k1/2p2ppp/p2p1q2/1p1P4/3pR3/1P1P3P/P1PQ1PP1/R5K1 w - - 4 20', '3rr1k1/2p2ppp/p2p1q2/1p1P4/3pR3/1P1P3P/P1PQ1PP1/4R1K1 b - - 5 20', '2r1r1k1/2p2ppp/p2p1q2/1p1P4/3pR3/1P1P3P/P1PQ1PP1/4R1K1 w - - 6 21', '2r1R1k1/2p2ppp/p2p1q2/1p1P4/3p4/1P1P3P/P1PQ1PP1/4R1K1 b - - 0 21', '4r1k1/2p2ppp/p2p1q2/1p1P4/3p4/1P1P3P/P1PQ1PP1/4R1K1 w - - 0 22', '4R1k1/2p2ppp/p2p1q2/1p1P4/3p4/1P1P3P/P1PQ1PP1/6K1 b - - 0 22']
    generate_pgn(fens)
