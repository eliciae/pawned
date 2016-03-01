import numpy as np

class State:
    board = None
    player = "W"

    def __init__(self, board, player):
        # Creates a completely empty board
        if board is None:
            self.board = np.array([["." for x in range(6)] for x in range(6)], str)
            # adds pieces at start points
            """
            for i in range(6):
                # black across top - [row][col]
                self.board[0][i] = "b"
                # white across bottom
                self.board[5][i] = "w"
            """
            self.board[3][1] = "w"
            self.board[4][4] = "w"

            self.board[2][1] = "b"
            self.board[3][4] = "b"
        else:
            self.board = board
        if player is None:
            # makes white start
            self.player = "B"
        else:
            self.player = player

    def getBoard(self):
        return self.board

    def getPlayer(self):
        return self.player
