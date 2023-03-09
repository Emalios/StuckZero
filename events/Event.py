class BaseEvent:
    """
    Base event
    """

    def __init__(self):
        self.name = "Base event"

    def __str__(self):
        return self.name


class QuitEvent(BaseEvent):
    """
    Quit event.
    """
    def __init__(self):
        self.name = "Quit event"


class ClickBoardEvent(BaseEvent):
    """
    When we click on the chess board.
    """
    def __init__(self):
        self.name = "Click on board event"
