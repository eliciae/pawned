from a2.Python.Var2.State import State
import numpy as np

tree = dict()
AI = "B"
human = "W"


class Pawned:
    # Represent the gamestate for Pawned game tree
    #  Minimax assumes objects that respond to the following methods:
    #     str(): return a unique string describing the state of the game (for use in transposition table)
    #     isTerminal(): checks if the game is at a terminal state
    #     successors(): returns a list of all legal game states that extend this one by one move
    #     isMinNode(): returns True if the node represents a state in which Min is to move
    #     isMaxNode(): returns True if the node represents a state in which Max is to move

    def __init__(self, state):
        """
        Create a new object
        :param state: a description of the board for the current state
        :param player: whose turn it is to play in the current state
        :return:
        """

        self.haspassed = 0
        if state is None:
            self.state = State(None, None)
        else:
            self.state = state

    def str(self):
        """ *** needed for search ***
        Translate the state into a string.  Could be used as for a hash table...
        :return: A string that describes the current state.
        """
        return self.state

    def validSpaces(self):
        """
        returns a list of tuples (the start and end coord pair) of tuples (the row and col values)
        """
        validSpaces = []
        player = self.state.getPlayer()
        board = self.state.getBoard()
        if player == "W":
            currentLocations = list(zip(*np.where(board == "w")))
            for coord in currentLocations:
                # forward one
                if board[coord[0] - 1][coord[1]] == ".":
                    validSpaces.append(((coord[0], coord[1]), (coord[0] - 1, coord[1])))
                # diagonal attack to right
                if coord[1] + 1 < 6:
                    if board[coord[0] - 1][coord[1] + 1] == "b":
                        validSpaces.append(((coord[0], coord[1]), (coord[0] - 1, coord[1] + 1)))
                # diagonal attack to left
                if coord[1] - 1 > -1:
                    if board[coord[0] - 1][coord[1] - 1] == "b":
                        validSpaces.append(((coord[0], coord[1]), (coord[0] - 1, coord[1] - 1)))
        else:
            currentLocations = list(zip(*np.where(board == "b")))
            for coord in currentLocations:
                # forward one
                if board[coord[0] + 1][coord[1]] == ".":
                    validSpaces.append(((coord[0], coord[1]), (coord[0] + 1, coord[1])))
                # diagonal attack to right
                if coord[1] + 1 < 6:
                    if board[coord[0] + 1][coord[1] + 1] == "w":
                        validSpaces.append(((coord[0], coord[1]), (coord[0] + 1, coord[1] + 1)))
                # diagonal attack to left
                if coord[1] - 1 > -1:
                    if board[coord[0] + 1][coord[1] - 1] == "w":
                        validSpaces.append(((coord[0], coord[1]), (coord[0] + 1, coord[1] - 1)))
        return validSpaces

    def pieceLocations(self, board, color):
        # get the piece type to look for and return all locations
        return list(zip(*np.where(board == color)))

    def move(self, who, where):
        """
        Create a new board with the given move.
        :param where: Where the move was
        :param who: who moved there
        returns the resulting board of the given move
        """
        board = self.state.getBoard().copy()
        # set the value you are moving from to .
        board[who[0]][who[1]] = "."
        # the coordinate you are moving to gets the value of the coordinate you are moving from
        board[where[0]][where[1]] = self.state.getPlayer().lower()
        s = State(board, self.togglePlayer(self.state.getPlayer()))

        return (who, where), s

    def isMinNode(self):
        """ *** needed for search ***
        :return: True if it's Min's turn to play
        """
        return self.state.getPlayer() == human

    def isMaxNode(self):
        """ *** needed for search ***
        :return: True if it's Max's turn to play
        """
        return self.state.getPlayer() == AI

    def winFor(self, state, color):
        """ *** needed for search ***
        :param node: a game tree node with stored game state
        :return: a boolean indicating if node is terminal
        """
        # if black is at the 5 row
        if color == "b":
            winRow = 5
        else:
            winRow = 0
        for p in self.pieceLocations(state.getBoard(), color):
            if p[0] == winRow:
                return True
        return False

    def isTerminal(self):
        """ *** needed for search ***
        :param node: a game tree node with stored game state
        :return: a boolean indicating if node is terminal
        """
        s = State(self.state.getBoard(), self.togglePlayer(self.state.getPlayer()))
        pi = Pawned(s)
        return self.winFor(self.state, 'b') or self.winFor(self.state, 'w') or (len(self.validSpaces()) == 0 and len(pi.validSpaces()) == 0)

    def successors(self):
        """ *** needed for search ***
        :param node:  a game tree node with stored game state
        :return: a list of move,state pairs that are the next possible states
        """

        spaces = self.validSpaces()
        if spaces:
            states = list(map(lambda v: self.move(v[0], v[1]), spaces))
            nodes = [(m, Pawned(s)) for m, s in states]
        else:
            s = State(self.state.getBoard(),self.togglePlayer(self.state.getPlayer()))
            nodes = [((None, None), Pawned(s))]
        return nodes

    def togglePlayer(self, player):
        if player == "B":
            return "W"
        else:
            return "B"

    def utility(self):
        """ *** needed for search ***
        :return: 1 if win for X, -1 for win for O, 0 for draw
        """
        if self.winFor(self.state, human.lower()):
            return -10
        if self.winFor(self.state, AI.lower()):
            return 10
        if len(self.validSpaces()) == 0:
            return 0
        return len(self.pieceLocations(self.state.getBoard(), AI.lower())) - len(self.pieceLocations(self.state.getBoard(), human.lower()))

    # all remaining methods are to assist in the calculatiosn

    def setState(self, state):
        self.state = state

    def display(self):
        """
        A pleasant view of the current game state
        :return: nothing
        """
        # prints the entire board in one print statement, row by row
        s = "    "
        for i in range(len(self.state.getBoard())):
            s += str(i) + "   "
        print(s)
        for i, j in enumerate(self.state.getBoard()):
            print(i, j)

