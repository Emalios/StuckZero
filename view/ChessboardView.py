import pygame

from events.Event import *

baseWidth = 512
baseHeight = 512
cell_size = baseHeight / 8
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


class ChessboardView:

    def __init__(self, board, width=baseWidth, height=baseHeight):
        self.board = board
        self.width = width
        self.height = height
        self.cell_size = width / 8
        self.screen = pygame.display.set_mode((width, height))
        self.notify()

    def notify(self, pos=None):
        self.render_all()

    def is_click_on_component(self, pos):
        (x, y) = pos
        return x >= 0 & y >= 0 & x <= self.width & x < self.height

    def get_board_pos(self, pos):
        col = pos[0] // cell_size
        row = pos[1] // cell_size
        return columns[int(col)] + int(8 - row).__str__()

    def render_all(self, draw_possibles_moves=False):
        """
        Draw the current game state on screen.
        """
        self.draw_board()
        self.draw_pieces(self.board.fen())
        print("graphics update", draw_possibles_moves)
        if draw_possibles_moves:
            print("draw possible moves")
            self.draw_possible_moves()
        pygame.display.update()

    def draw_possible_moves(self):
        # Get clicked pos
        last_pos = self.board.get_last_pos()
        if last_pos is None:
            return
        print(last_pos)
        # Get possibles moves from that piece
        possible_moves = list(map(lambda value: value.__str__()[-2:],
                                  filter(lambda move: move.__str__()[:2] == last_pos, self.board.get_possible_moves())))
        # Show them
        for move in possible_moves:
            # TODO: crash when we click on the line before the last column with a pawn
            column = columns.index(move[0]) + 1
            line = 9 - int(move[1])
            x = (column - 1) * self.cell_size + self.cell_size / 2
            y = (line - 1) * self.cell_size + self.cell_size / 2
            pygame.draw.circle(self.screen, (220, 20, 60), (x, y), self.cell_size / 8)

    def draw_board(self):
        window = self.screen
        window.fill((255, 255, 200), pygame.Rect(0, 0, 700, 700))
        counter = 0
        for x in range(0, 8):
            for y in range(0, 8):
                color = (238, 238, 210) if counter % 2 == 0 else (118, 150, 86)
                pygame.draw.rect(window, color, pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                counter += 1
            counter -= 1

    # exemple fen: 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    def draw_pieces(self, fen):
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
                piece = pygame.transform.scale(piece, (self.cell_size, self.cell_size))
                self.screen.blit(piece, (x * self.cell_size, y * self.cell_size))
                x += 1
