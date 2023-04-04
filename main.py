import chess.pgn
import pygame
from pygame import QUIT, MOUSEBUTTONUP

# const
initialFen = 'rnbqkbnr/pppppppQ/8/8/8/8/PPPPPPPP/RNBQKBNR'
widthBoard = 512
heightBoard = 512
cell_size = heightBoard / 8
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

chessboard = None
last_pos = None


def draw_possible_moves(window):
    # Get clicked pos
    if last_pos is None:
        return
    print(last_pos)
    # Get possibles moves from that piece
    possible_moves = list(map(lambda value: value.__str__()[-2:], filter(lambda move: move.__str__()[:2] == last_pos, chessboard.legal_moves)))
    # Show them
    for move in possible_moves:
        column = columns.index(move[0]) + 1
        line = 9 - int(move[1])
        x = (column - 1) * cell_size + cell_size / 2
        y = (line - 1) * cell_size + cell_size / 2
        pygame.draw.circle(window, (220, 20, 60), (x, y), cell_size / 8)

def draw_board(window, width, height):
    window.fill((255, 255, 200), pygame.Rect(0, 0, 700, 700))
    counter = 0
    for x in range(0, 8):
        for y in range(0, 8):
            color = (238, 238, 210) if counter % 2 == 0 else (118, 150, 86)
            pygame.draw.rect(window, color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))
            counter += 1
        counter -= 1


# exemple fen: 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
def draw_pieces(window, fen):
    x = 0
    y = 0
    for char in fen:
        if char == '/':
            y += 1
            x = 0
        elif char.isnumeric():
            x += int(char)
        elif char == ' ':
            break
        else:
            before = 'w' if char.isupper() else 'b'
            piece = pygame.image.load('images/' + before + char + '.png')
            piece = pygame.transform.scale(piece, (cell_size, cell_size))
            window.blit(piece, (x * cell_size, y * cell_size))
            x += 1


def get_piece_from_pos(pos):
    col = pos[0] // cell_size
    row = pos[1] // cell_size
    return columns[int(col)] + int(8 - row).__str__()


if __name__ == "__main__":
    # initialFen = 'r1bqkb1r/pppp1Qpp/2n2n2/4p3/4P3/8/PPPP1PPP/RNB1K1NR w KQkq - 0 4'
    chessboard = chess.Board(initialFen)
    pygame.init()

    # Création de la fenêtre
    window = pygame.display.set_mode((700, 700))

    draw_board(window, widthBoard, heightBoard)
    draw_pieces(window, initialFen)

    pygame.display.update()

    continuer = 1

    last_pos = None

    while continuer:
        # checkmate
        if chessboard.is_checkmate():
            print("CHECKMATE")
            break
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked = get_piece_from_pos(pos)
                if last_pos is not None:
                    if last_pos == clicked:
                        continue
                    # test if move is valid
                    # TODO: roque ne fonctionne pas
                    uci = chess.Move.from_uci(last_pos + clicked)
                    if uci in chessboard.legal_moves:
                        chessboard.push(uci)
                        draw_board(window, widthBoard, heightBoard)
                        draw_pieces(window, chessboard.fen())
                        pygame.display.update()
                    else:
                        print("invalid move")
                        for move in chessboard.legal_moves:
                            print(chess.SQUARE_NAMES[move.to_square])
                    last_pos = None
                else:
                    last_pos = clicked
                    print('clicked', clicked)
                    draw_possible_moves(window)
                    pygame.display.update()
            if event.type == QUIT:
                continuer = 0
