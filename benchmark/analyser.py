import csv
import sys
import chess
import chess.engine
import chess.pgn
import matplotlib.pyplot as plt

from stockfish import Stockfish

stockfish = Stockfish(path="../stockfish-windows-2022-x86-64-avx2.exe", depth=20,
                      parameters={"Threads": 8})


def analyse_pgn(path, output):
    pgn = open(path)
    game = chess.pgn.read_game(pgn)
    board = game.board()

    # On "recré" la partie pour pouvoir récupérer les positions FEN
    fen_list = []

    for move in game.mainline_moves():
        # Ajout de la position FEN actuelle à la liste
        fen_list.append(board.fen())

        # Application du coup sur le plateau
        board.push(move)

    # Ajout de la dernière position FEN à la liste
    fen_list.append(board.fen())

    # Data format
    # ["Move number", "Advantage", "Analyse Number"]
    # [1,             -5.98,        1]
    final_data = ["Move number", "Advantage", "Analyse number"]

    for i in range(0, 21):
        [x, y] = process_data(fen_list)
        for move_number in x:
            # Because move_number start at one
            final_data.append([move_number, y[move_number - 1], i])
        print("Result", i, "added!")

    export_data(final_data, output, "result.csv")


def process_data(fen_list):
    # Exemple d'utilisation
    accuracies = []

    for value in fen_list:
        accuracies.append(win(value))

    x = range(1, len(accuracies) + 1)
    y = accuracies

    return [x, y]


def export_data(data, output, filename="result.csv"):
    path = output + "/" + filename
    with open(path, mode='w', newline='') as csv_file:
        # Création d'un objet writer pour écrire dans le fichier CSV
        writer = csv.writer(csv_file)

        # Écriture des données dans le fichier CSV
        for line in data:
            writer.writerow(line)

    print("Data succesfully writed in", path)


def plot_data(data):
    x = data[0]
    y = data[1]

    plt.plot(x, y)
    plt.xlabel('i ème coup')
    plt.ylabel('Accuracy')
    plt.title('Game Accuracy')
    plt.grid(True)
    plt.show()


def win(fen):
    stockfish.set_fen_position(fen)
    json = stockfish.get_evaluation()
    if json['type'] == 'mate':
        return
    centipaws = json['value'] / 100
    return centipaws
    # centipaws convertie en pourcentage de victoire pour les blancs
    # return 50 + 50 * (2 / (1 + exp(-0.00368208 * centipaws)) - 1)


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 2:
        pgn_file = args[1]
        dir_out = args[2]
        analyse_pgn(pgn_file, dir_out)
    else:
        print("Please enter file input and a folder for the output.")
