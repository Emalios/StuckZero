import chess
import chess.svg
import chess.pgn
import pygame
from pygame import QUIT, MOUSEBUTTONUP

widthBoard = 512
heightBoard = 512
cell_size = heightBoard / 8
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def draw_board(window, width, height):
    cellSize = width / 8
    window.fill((255, 255, 200), pygame.Rect(0, 0, 700, 700))
    counter = 0
    for x in range(0, 8):
        for y in range(0, 8):
            color = (238, 238, 210) if counter % 2 == 0 else (118, 150, 86)
            pygame.draw.rect(window, color, pygame.Rect(x * cellSize, y * cellSize, cellSize, cellSize))
            counter += 1
        counter -= 1


#exemple fen: 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
def draw_pieces(window, fen, size):
    cellSize = size / 8
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
            print("current: " + char)
            before = 'w' if char.isupper() else 'b'
            piece = pygame.image.load('images/' + before + char + '.png').convert_alpha()
            piece = pygame.transform.scale(piece, (cellSize, cellSize))
            window.blit(piece, (x * cellSize, y * cellSize))
            x += 1


def get_piece_from_pos(pos):
    print("x: " + pos[0].__str__() + ",y=" + pos[1].__str__())
    col = pos[0] // cell_size
    row = pos[1] // cell_size
    return columns[int(col)] + int(8 - row).__str__()

if __name__ == "__main__":
    #initialFen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
    initialFen = 'r1bqkb1r/pppp1Qpp/2n2n2/4p3/4P3/8/PPPP1PPP/RNB1K1NR w KQkq - 0 4'
    chessboard = chess.Board(initialFen)
    pygame.init()

    # Création de la fenêtre
    window = pygame.display.set_mode((700, 700))

    draw_board(window, 512, 512)
    draw_pieces(window, initialFen, 512)

    pygame.display.update()

    continuer = 1
    
    last_pos = None

    while continuer:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked = get_piece_from_pos(pos)
                print("pos: " + clicked)
                if last_pos is not None:
                    if last_pos == clicked:
                        continue
                    #test if move is valid
                    uci = chess.Move.from_uci(last_pos + clicked)
                    if uci in chessboard.legal_moves:
                        print("valid: " + uci.__str__())
                        chessboard.push(uci)
                        draw_pieces(window, chessboard.fen(), 512)
                        pygame.display.update()
                    else:
                        print("invalid")
                        for move in chessboard.legal_moves:
                            print(move)
                    last_pos = None
                else:
                    last_pos = clicked
            if event.type == QUIT:
                continuer = 0
