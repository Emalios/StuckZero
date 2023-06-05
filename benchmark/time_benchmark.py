import csv

from chess import Board
import time

from ia.minmax.eval import evaluate_board
from ia.minmax.min_max import *

random_fen_list = [
    "7R/8/5BP1/P2k1p2/p4q1p/8/Pp1p1P2/3K2QR w - - 0 1",
    "b1k5/1pn5/1p1n1KP1/r2p4/1p4q1/N1P2P2/3R4/8 w - - 0 1",
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
    "r3k2r/ppp2ppp/3p4/8/4P3/8/PPP2PPP/R3K2R b KQkq - 0 1",
    "2r1k3/pp4pp/2p1p3/8/4P3/1P3P2/P4P1P/2R1K3 b - - 0 1",
    "r3kb1r/ppp2ppp/2np4/8/3pP3/2N5/PPP2PPP/R3KB1R w KQkq - 0 1",
    "rnbqk2r/ppp2ppp/3p4/8/4P3/8/PPP2PPP/RNBQK2R b KQkq - 0 1",
    "rnbqkb1r/pppp1ppp/5n2/4p3/3P4/8/PPP2PPP/RNBQKBNR w KQkq - 0 1",
    "rnbqkbnr/ppp2ppp/8/3p4/3P4/8/PPP2PPP/RNBQKBNR w KQkq - 0 1",
    "rnbqkb1r/pppp1ppp/5n2/4p3/3P4/8/PPP2PPP/RNBQK2R b KQkq - 0 1",
    "rnbqkbnr/ppppp1pp/8/5p2/8/8/PPPPPPP1/RNBQKBNR w KQkq - 0 1",
    "r1bqk2r/pppp1ppp/2n2n2/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 1",
    "r1bqkbnr/ppp2ppp/2n5/8/4P3/2N5/PPP2PPP/R1BQKBNR b KQkq - 0 1",
    "r1bqkb1r/ppp2ppp/2n2n2/4p3/4P3/2N2N2/PPP2PPP/R1BQKB1R b KQkq - 0 1",
    "rnbqkbnr/pppp1ppp/8/4p3/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
    "r1bqkb1r/ppp2ppp/2n2n2/4p3/4P3/2N5/PPP2PPP/R1BQKBNR w KQkq - 0 1",
    "rnbqkbnr/ppp2ppp/3p4/4p3/3P4/8/PPP2PPP/RNBQKBNR w KQkq - 0 1",
    "rnbqkb1r/pppp1ppp/4pn2/8/3P4/8/PPP2PPP/RNBQKBNR w KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/8/PPP2PPP/RNBQKBNR w KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/8/PPP2PPP/RNBQ1BNR w KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/8/PPP1BPPP/RNBQK1NR b KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/8/PPP1BPPP/RN1QK1NR w KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/2N5/PPP1BPPP/R1BQK1NR b KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/2N5/PPP1BPPP/R1BQ1KNR w KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/2N5/PPP1BPPP/R1BQ1K1R b KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/2N2B2/PPP2PPP/R1BQ1K1R b KQkq - 0 1"
]

random_fen_list_10 = [
    "rnbqkbnr/ppp2ppp/3p4/4p3/3P4/8/PPP2PPP/RNBQKBNR w KQkq - 0 1",
    "rnbqkb1r/pppp1ppp/4pn2/8/3P4/8/PPP2PPP/RNBQKBNR w KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/8/PPP2PPP/RNBQKBNR w KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/8/PPP2PPP/RNBQ1BNR w KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/8/PPP1BPPP/RNBQK1NR b KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/8/PPP1BPPP/RN1QK1NR w KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/2N5/PPP1BPPP/R1BQK1NR b KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/2N5/PPP1BPPP/R1BQ1KNR w KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/2N5/PPP1BPPP/R1BQ1K1R b KQkq - 0 1",
    "rnbqkb1r/ppp2ppp/4pn2/8/3P4/2N2B2/PPP2PPP/R1BQ1K1R b KQkq - 0 1"
]



def preprocess():
    # On vérifie que les fen sont biens valides
    print("Start checking...")
    for fen in random_fen_list:
        try:
            board = Board(fen)
        except:
            print("Error with fen", fen)
    print("Ended")


def time_benchmark(minimax, evaluate_board, depth, algorithm_name, evaluation_function):
    start_global_time = time.time()
    for fen in random_fen_list:
        board = Board(fen)
        move = find_best_move(board, depth, evaluate_board, minimax)
        #print("OK.")
    end_global_time = time.time()

    global_execution_time = end_global_time - start_global_time
    return [algorithm_name, evaluation_function, depth, global_execution_time, global_execution_time / len(random_fen_list), len(random_fen_list_10)]

def print_result(result):
    print("======> Global time:", result[0])
    print("======> Mean time:", result[1])

def save_result(file, result):
    try:
        with open(file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(result)
        print("Résultats", result, "ajoutés au fichier CSV avec succès.")
    except IOError:
        print("Erreur lors de l'écriture des résultats dans le fichier CSV.")


if __name__ == "__main__":
    preprocess()
    csv_path = "../csv/time_per_depth"
    save_result(csv_path, ["algorithm_name", "evaluation_function", "depth", "global_execution_time", "mean_execution_time", "number_of_fen"])
    for i in range(1, 7):
        print("Benchmark with depth of", i, "on", len(random_fen_list), "positions")
        print("[Alpha Beta and depth]")
        alpha_result = time_benchmark(minimax_alpha_beta, evaluate_board, i, "alpha_beta", 1)
        save_result(csv_path, alpha_result)
        print("-----------------------")
        print("[Only depth]")
        depth_result = time_benchmark(minmax_depth, evaluate_board, i, "only_depth", 1)
        save_result(csv_path, depth_result)
