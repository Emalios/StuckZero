from math import exp

import chess
import chess.engine
import matplotlib.pyplot as plt

from stockfish import Stockfish

stockfish = Stockfish(path="../stockfish-windows-2022-x86-64-avx2.exe", depth=14,
                          parameters={"Threads": 6})

def win(fen):
    stockfish.set_fen_position(fen)
    centipaws = stockfish.get_evaluation()['value']
    print(stockfish.get_evaluation())
    return centipaws
    #centipaws convertie en pourcentage de victoire pour les blancs
    #return 50 + 50 * (2 / (1 + exp(-0.00368208 * centipaws)) - 1)

def evaluate_game(fen_list):
    engine = chess.engine.SimpleEngine.popen_uci("../stockfish-windows-2022-x86-64-avx2.exe")

    board = chess.Board()
    evaluation = 0

    for fen in fen_list:
        board.set_fen(fen)

        # Évaluer la position avec Stockfish
        result = engine.play(board, chess.engine.Limit(time=2))
        evaluation += result.info["score"].relative.score()

        board.push(result.move)

    engine.quit()

    return evaluation


if __name__ == "__main__":
    # Exemple d'utilisation
    fen_list = ['rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1', 'rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2', 'rnbqkbnr/ppp1pppp/8/3P4/8/8/PPPP1PPP/RNBQKBNR b KQkq - 0 2', 'rnb1kbnr/ppp1pppp/8/3q4/8/8/PPPP1PPP/RNBQKBNR w KQkq - 0 3', 'rnb1kbnr/ppp1pppp/8/3q4/8/2N5/PPPP1PPP/R1BQKBNR b KQkq - 1 3', 'rnbqkbnr/ppp1pppp/8/8/8/2N5/PPPP1PPP/R1BQKBNR w KQkq - 2 4', 'rnbqkbnr/ppp1pppp/8/8/3P4/2N5/PPP2PPP/R1BQKBNR b KQkq - 0 4', 'rnbqkb1r/ppp1pppp/5n2/8/3P4/2N5/PPP2PPP/R1BQKBNR w KQkq - 1 5', 'rnbqkb1r/ppp1pppp/5n2/8/3P4/2NB4/PPP2PPP/R1BQK1NR b KQkq - 2 5', 'rnb1kb1r/ppp1pppp/5n2/8/3q4/2NB4/PPP2PPP/R1BQK1NR w KQkq - 0 6', 'rnb1kb1r/ppp1pppp/5n2/1B6/3q4/2N5/PPP2PPP/R1BQK1NR b KQkq - 1 6', 'rnb1kb1r/pp2pppp/2p2n2/1B6/3q4/2N5/PPP2PPP/R1BQK1NR w KQkq - 0 7', 'rnb1kb1r/pp2pppp/2p2n2/1B6/3Q4/2N5/PPP2PPP/R1B1K1NR b KQkq - 0 7', 'rnb1kb1r/pp2pppp/5n2/1p6/3Q4/2N5/PPP2PPP/R1B1K1NR w KQkq - 0 8', 'rnb1kb1r/pp2pppp/5n2/1N6/3Q4/8/PPP2PPP/R1B1K1NR b KQkq - 0 8', 'r1b1kb1r/pp2pppp/2n2n2/1N6/3Q4/8/PPP2PPP/R1B1K1NR w KQkq - 1 9', 'r1b1kb1r/ppN1pppp/2n2n2/8/3Q4/8/PPP2PPP/R1B1K1NR b KQkq - 2 9']
    accuracies = []

    for value in fen_list:
        accuracies.append(win(value))

    x = range(1, len(accuracies) + 1)
    y = accuracies

    plt.plot(x, y)
    plt.xlabel('i ème coup')
    plt.ylabel('Accuracy')
    plt.title('Game Accuracy')
    plt.grid(True)
    plt.show()