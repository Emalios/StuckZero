import pygame
import model

class Click:
    """
    Handles click input.
    """

    def __init__(self, model):
        self.model = model

    def notify(self, pos, graphics):
        """
        Receive events posted to the message queue.
        :param graphics:
        """
        if graphics.is_click_on_component(pos):
            board_pos = graphics.get_board_pos(pos)
            self.model.click_on(board_pos)
