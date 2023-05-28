from math import exp

import chess
import chess.engine
import matplotlib.pyplot as plt

from stockfish import Stockfish

stockfish = Stockfish(path="../stockfish-windows-2022-x86-64-avx2.exe", depth=14,
                          parameters={"Threads": 6})

def win(fen):
    stockfish.set_fen_position(fen)
    json = stockfish.get_evaluation()
    if json['type'] == 'mate':
        return
    centipaws = json['value']
    print(stockfish.get_evaluation())

    return centipaws
    #centipaws convertie en pourcentage de victoire pour les blancs
    #return 50 + 50 * (2 / (1 + exp(-0.00368208 * centipaws)) - 1)

if __name__ == "__main__":
    # Exemple d'utilisation
    fen_list = ['rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1', 'rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2', 'rnbqkbnr/ppp1pppp/8/3pP3/8/8/PPPP1PPP/RNBQKBNR b KQkq - 0 2', 'rnbqkbnr/pp2pppp/8/2ppP3/8/8/PPPP1PPP/RNBQKBNR w KQkq - 0 3', 'rnbqkbnr/pp2pppp/8/2ppP3/3P4/8/PPP2PPP/RNBQKBNR b KQkq - 0 3', 'rnbqkbnr/pp2pppp/8/3pP3/2pP4/8/PPP2PPP/RNBQKBNR w KQkq - 0 4', 'rnbqkbnr/pp2pppp/8/3pP3/2pP4/5N2/PPP2PPP/RNBQKB1R b KQkq - 1 4', 'rnbqkbnr/pp3ppp/4p3/3pP3/2pP4/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 5', 'rnbqkbnr/pp3ppp/4p3/3pP1B1/2pP4/5N2/PPP2PPP/RN1QKB1R b KQkq - 1 5', 'rnbqkbnr/pp4pp/4pp2/3pP1B1/2pP4/5N2/PPP2PPP/RN1QKB1R w KQkq - 0 6', 'rnbqkbnr/pp4pp/4pP2/3p2B1/2pP4/5N2/PPP2PPP/RN1QKB1R b KQkq - 0 6', 'rnbqkbnr/pp5p/4pp2/3p2B1/2pP4/5N2/PPP2PPP/RN1QKB1R w KQkq - 0 7', 'rnbqkbnr/pp5p/4pp2/3p4/2pP3B/5N2/PPP2PPP/RN1QKB1R b KQkq - 1 7', 'rnbqk1nr/pp4bp/4pp2/3p4/2pP3B/5N2/PPP2PPP/RN1QKB1R w KQkq - 2 8', 'rnbqk1nr/pp4bp/4pp2/3p4/2pP3B/5N2/PPP1BPPP/RN1QK2R b KQkq - 3 8', 'r1bqk1nr/pp4bp/2n1pp2/3p4/2pP3B/5N2/PPP1BPPP/RN1QK2R w KQkq - 4 9', 'r1bqk1nr/pp4bp/2n1pp2/3p4/2pP3B/5N2/PPP1BPPP/RN1Q1RK1 b kq - 5 9', 'r1b1k1nr/pp4bp/2nqpp2/3p4/2pP3B/5N2/PPP1BPPP/RN1Q1RK1 w kq - 6 10', 'r1b1k1nr/pp4bp/2nqpp2/3p4/2pP3B/N4N2/PPP1BPPP/R2Q1RK1 b kq - 7 10', 'r1b1k1nr/pp4bp/2nqp3/3p1p2/2pP3B/N4N2/PPP1BPPP/R2Q1RK1 w kq - 0 11', 'r1b1k1nr/pp4bp/2nqp3/3p1p2/2pP3B/NP3N2/P1P1BPPP/R2Q1RK1 b kq - 0 11', 'r1b1k1nr/pp4bp/2nqp3/3p1p2/3P3B/Np3N2/P1P1BPPP/R2Q1RK1 w kq - 0 12', 'r1b1k1nr/pp4bp/2nqp3/3p1p2/3P3B/NP3N2/2P1BPPP/R2Q1RK1 b kq - 0 12', 'r1b1k2r/pp4bp/2nqpn2/3p1p2/3P3B/NP3N2/2P1BPPP/R2Q1RK1 w kq - 1 13', 'r1b1k2r/pp4bp/2nqpn2/1B1p1p2/3P3B/NP3N2/2P2PPP/R2Q1RK1 b kq - 2 13', 'r1b1k2r/1p4bp/p1nqpn2/1B1p1p2/3P3B/NP3N2/2P2PPP/R2Q1RK1 w kq - 0 14', 'r1b1k2r/1p4bp/p1nqpn2/3p1p2/B2P3B/NP3N2/2P2PPP/R2Q1RK1 b kq - 1 14', 'r1b1k2r/6bp/p1nqpn2/1p1p1p2/B2P3B/NP3N2/2P2PPP/R2Q1RK1 w kq - 0 15', 'r1b1k2r/6bp/p1nqpn2/1B1p1p2/3P3B/NP3N2/2P2PPP/R2Q1RK1 b kq - 0 15', 'r1b1k2r/6bp/2nqpn2/1p1p1p2/3P3B/NP3N2/2P2PPP/R2Q1RK1 w kq - 0 16', 'r1b1k2r/6bp/2nqpn2/1N1p1p2/3P3B/1P3N2/2P2PPP/R2Q1RK1 b kq - 0 16', '2b1k2r/6bp/2nqpn2/1N1p1p2/3P3B/1P3N2/2P2PPP/r2Q1RK1 w k - 0 17', '2b1k2r/6bp/2nqpn2/1N1p1p2/3P3B/1P3N2/2P2PPP/Q4RK1 b k - 0 17', '2b1k2r/6bp/2nqp3/1N1p1p2/3Pn2B/1P3N2/2P2PPP/Q4RK1 w k - 1 18', 'Q1b1k2r/6bp/2nqp3/1N1p1p2/3Pn2B/1P3N2/2P2PPP/5RK1 b k - 2 18', 'Q1b2rk1/6bp/2nqp3/1N1p1p2/3Pn2B/1P3N2/2P2PPP/5RK1 w - - 3 19', 'Q1b2rk1/6bp/2nNp3/3p1p2/3Pn2B/1P3N2/2P2PPP/5RK1 b - - 0 19', 'Q1br2k1/6bp/2nNp3/3p1p2/3Pn2B/1P3N2/2P2PPP/5RK1 w - - 1 20', '2br2k1/6bp/2QNp3/3p1p2/3Pn2B/1P3N2/2P2PPP/5RK1 b - - 0 20', '2br2k1/7p/2QNp3/3pbp2/3Pn2B/1P3N2/2P2PPP/5RK1 w - - 1 21', '2br2k1/1N5p/2Q1p3/3pbp2/3Pn2B/1P3N2/2P2PPP/5RK1 b - - 2 21', '2br2k1/1N6/2Q1p2p/3pbp2/3Pn2B/1P3N2/2P2PPP/5RK1 w - - 0 22', '2bB2k1/1N6/2Q1p2p/3pbp2/3Pn3/1P3N2/2P2PPP/5RK1 b - - 0 22', '2bB2k1/1N6/2Q1p2p/3pbp2/3P4/1P3N2/2P2nPP/5RK1 w - - 0 23', '2bBQ1k1/1N6/4p2p/3pbp2/3P4/1P3N2/2P2nPP/5RK1 b - - 1 23', '2bBQ3/1N5k/4p2p/3pbp2/3P4/1P3N2/2P2nPP/5RK1 w - - 2 24', '2bB4/1N3Q1k/4p2p/3pbp2/3P4/1P3N2/2P2nPP/5RK1 b - - 3 24', '2bB3k/1N3Q2/4p2p/3pbp2/3P4/1P3N2/2P2nPP/5RK1 w - - 4 25', '2bB3k/1N3Q2/4p2p/3pNp2/3P4/1P6/2P2nPP/5RK1 b - - 0 25', '3B3k/1N1b1Q2/4p2p/3pNp2/3P4/1P6/2P2nPP/5RK1 w - - 1 26', '7k/1N1b1Q2/4pB1p/3pNp2/3P4/1P6/2P2nPP/5RK1 b - - 2 26']
    accuracies = []

    for value in fen_list:
        #print(value)
        accuracies.append(win(value))

    x = range(1, len(accuracies) + 1)
    y = accuracies

    plt.plot(x, y)
    plt.xlabel('i ème coup')
    plt.ylabel('Accuracy')
    plt.title('Game Accuracy')
    plt.grid(True)
    plt.show()