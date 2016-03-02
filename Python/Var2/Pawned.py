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
        if state is None:
            self.gameState = State(None, None)
        else:
            self.gameState = state
        self.display()


    def str(self):
        """ *** needed for search ***
        Translate the state into a string.  Could be used as for a hash table...
        :return: A string that describes the current state.
        """
        return self.gameState

    def validSpaces(self, state):
        """
        returns a list of tuples (the start and end coord pair) of tuples (the row and col values)
        """
        validSpaces = []
        player = state.getPlayer()
        board = state.getBoard()
        if player == "W":
            currentLocations = list(zip(*np.where(board == "w")))
            for coord in currentLocations:
                # forward one
                if board[coord[0]-1][coord[1]] == ".":
                    validSpaces.append(((coord[0], coord[1]), (coord[0]-1, coord[1])))
                # diagonal attack to right
                if coord[1]+1 < 6:
                    if board[coord[0]-1][coord[1]+1] == "b":
                        validSpaces.append(((coord[0], coord[1]), (coord[0]-1, coord[1]+1)))
                # diagonal attack to left
                if coord[1]-1 > -1:
                    if board[coord[0]-1][coord[1]-1] == "b":
                        validSpaces.append(((coord[0], coord[1]), (coord[0]-1, coord[1]-1)))
        else:
            currentLocations = list(zip(*np.where(board == "b")))
            for coord in currentLocations:
                # forward one
                if board[coord[0]+1][coord[1]] == ".":
                    validSpaces.append(((coord[0], coord[1]), (coord[0]+1, coord[1])))
                # diagonal attack to right
                if coord[1]+1 < 6:
                    if board[coord[0]+1][coord[1]+1] == "w":
                        validSpaces.append(((coord[0], coord[1]), (coord[0]+1, coord[1]+1)))
                # diagonal attack to left
                if coord[1]-1 > -1:
                    if board[coord[0]+1][coord[1]-1] == "w":
                        validSpaces.append(((coord[0], coord[1]), (coord[0]+1, coord[1]-1)))
        return validSpaces

    def pieceLocations(self, board, color):
        # get the piece type to look for and return all locations
        return list(zip(*np.where(board == color)))


    def move(self, who, where, state):
        """
        Create a new board with the given move.
        :param where: Where the move was
        :param who: who moved there
        returns the resulting board of the given move
        """
        board = state.getBoard().copy()
        # the coordinate you are moving to gets the value of the coordinate you are moving from
        board[where[0]][where[1]] = board[who[0]][who[1]]
        # set the value you are moving from to .
        board[who[0]][who[1]] = "."
        return State(board, self.togglePlayer(state.getPlayer()))


    def isMinNode(self, state):
        """ *** needed for search ***
        :return: True if it's Min's turn to play
        """
        return state.getPlayer() == human


    def isMaxNode(self, state):
        """ *** needed for search ***
        :return: True if it's Max's turn to play
        """
        return state.getPlayer() == AI


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


    def isTerminal(self, state):
        """ *** needed for search ***
        :param node: a game tree node with stored game state
        :return: a boolean indicating if node is terminal
        """
        return self.winFor(state, 'b') or self.winFor(state, 'w') or (len(self.validSpaces(state)) == 0)


    def successors(self, state):
        """ *** needed for search ***
        :param node:  a game tree node with stored game state
        :return: a list of move,state pairs that are the next possible states
        """
        spaces = self.validSpaces(state)
        states = list(map(lambda v: self.move(v[0], v[1], state), spaces))
        return states

    def togglePlayer(self, player):
        if player == "B":
            return "W"
        else:
            return "B"


    def utility(self, state):
        """ *** needed for search ***
        :return: 1 if win for X, -1 for win for O, 0 for draw
        """
        if self.winFor(state, "w"):
            return 1
        if self.winFor(state, "b"):
            return -1
        if len(self.validSpaces(state)) == 0:
            return 0


    # all remaining methods are to assist in the calculatiosn


    def display(self):
        """
        A pleasant view of the current game state
        :return: nothing
        """
        # prints the entire board in one print statement, row by row
        print('\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in self.gameState.getBoard()]))
