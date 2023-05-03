import pygame
from pygame import MOUSEBUTTONUP, QUIT

from model.Chessboard import Chessboard
from view.ChessboardView import ChessboardView
from controller.Click import Click
from stockfish import Stockfish


def game_loop(model, graphics):
    end = False
    click = Click(model)
    while not model.is_ended() and not end:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                click.notify(pos, graphics)
            if event.type == QUIT:
                end = True


def run():
    stockfish = Stockfish(path="stockfish-windows-2022-x86-64-avx2.exe", depth=18,
                          parameters={"Threads": 2})

    model = Chessboard(stockfish)
    graphics = ChessboardView(model)
    model.register_observator(graphics)
    pygame.init()

    # Game loop
    game_loop(model, graphics)


if __name__ == '__main__':
    run()
