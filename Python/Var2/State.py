import numpy as np

class State:
    board = None
    player = "W"

    def __init__(self, board, player):
        # Creates a completely empty board
        if board is None:
            self.board = np.array([["." for x in range(6)] for x in range(6)], str)
            # adds pieces at start points
            for i in range(6):
                # black across top - [row][col]
                self.board[0][i] = "b"
                # white across bottom
                self.board[5][i] = "w"
        else:
            self.board = board
        if player is None:
            # makes white start
            self.player = "B"
        else:
            self.player = player

    def __str__(self):
        return "(%s, %s)" % (self.board, self.player)

    __repr__ = __str__

    def getBoard(self):
        return self.board

    def getPlayer(self):
        return self.player
