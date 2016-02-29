class State:
    board = None
    player = "W"

    def __init__(self):
        # Creates a completely empty board
        self.board = [["." for x in range(6)] for x in range(6)]
        # adds pieces at start points
        for i in range(6):
            # black across top - [row][col]
            self.board[0][i] = "b"
            # white across bottom
            self.board[5][i] = "w"
        # makes white start
        self.player = "W"

    def getBoard(self):
        return self.board

    def getPlayer(self):
        return self.player
