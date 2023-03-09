import pygame

baseWidth = 512
baseHeight = 512
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


class ChessboardView:

    def __init__(self, board, width=baseWidth, height=baseHeight):
        self.board = board
        self.width = width
        self.height = height
        self.cell_size = width / 8
        self.screen = pygame.display.set_mode(board.get_size())

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
            cell_size = self.cell_size
            column = columns.index(move[0]) + 1
            line = 9 - int(move[1])
            x = (column - 1) * cell_size + cell_size / 2
            y = (line - 1) * cell_size + cell_size / 2
            pygame.draw.circle(self.screen, (220, 20, 60), (x, y), cell_size / 8)

    def draw_board(self):
        cell_size = self.cell_size
        window = self.screen
        window.fill((255, 255, 200), pygame.Rect(0, 0, 700, 700))
        counter = 0
        for x in range(0, 8):
            for y in range(0, 8):
                color = (238, 238, 210) if counter % 2 == 0 else (118, 150, 86)
                pygame.draw.rect(window, color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))
                counter += 1
            counter -= 1

    # exemple fen: 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    def draw_pieces(self, fen):
        cell_size = self.cell_size
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
                self.screen.blit(piece, (x * cell_size, y * cell_size))
                x += 1
