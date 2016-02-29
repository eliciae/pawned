from a2.Python.Var2 import State
import numpy as np

tree = dict()


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
            self.gameState = State.State()
        else:
            self.gameState = state
        self.display()


    def str(self):
        """ *** needed for search ***
        Translate the state into a string.  Could be used as for a hash table...
        :return: A string that describes the current state.
        """
        return self.gameState

    def validSpaces(self, state, player):
        """
        returns a list of all possible spaces (row,col) to move from the current state
        """
        validSpaces = []
        board = self.gameState.getBoard()
        if player == "W":
            currentLocations = zip(*np.where(self.gameState.getBoard() == "W"))
            for coord in currentLocations:
                # forward one
                if board[coord[0]-1][coord[1]] == ".":
                    validSpaces.append((coord[0]-1, coord[1]))
                # diagonal attack to right
                if coord[1]+1 < 6:
                    if board[coord[0]-1][coord[1]+1] == "b":
                        validSpaces.append((coord[0]-1, coord[1]+1))
                # diagonal attack to left
                if coord[1]-1 > -1:
                    if board[coord[0]-1][coord[1]-1] == "b":
                        validSpaces.append((coord[0]-1, coord[1]-1))
        else:
            currentLocations = zip(*np.where(self.gameState.getBoard() == "B"))
            for coord in currentLocations:
                # forward one
                if board[coord[0]+1][coord[1]] == ".":
                    validSpaces.append((coord[0]+1, coord[1]))
                # diagonal attack to right
                if coord[1]+1 < 6:
                    if board[coord[0]+1][coord[1]+1] == "w":
                        validSpaces.append((coord[0]-1, coord[1]+1))
                # diagonal attack to left
                if coord[1]-1 > -1:
                    if board[coord[0]+1][coord[1]-1] == "w":
                        validSpaces.append((coord[0]-1, coord[1]-1))




    def isMinNode(self):
        """ *** needed for search ***
        :return: True if it's Min's turn to play
        """
        return self.gameState in "BCD"


    def isMaxNode(self):
        """ *** needed for search ***
        :return: True if it's Max's turn to play
        """
        return self.gameState in "AEFGHIJK"


    def isTerminal(self):
        """ *** needed for search ***
        :param node: a game tree node with stored game state
        :return: a boolean indicating if node is terminal
        """
        return self.gameState in "LMNOPQRSTUVWXY"

    def successors(self):
        """ *** needed for search ***
        :param node:  a game tree node with stored game state
        :return: a list of game tree nodes that are the next possible states
        """
        global tree
        return [Pawned(c) for c in tree[self.gameState]]


    def utility(self):
        """ *** needed for search ***
        :return: 1 if win for X, -1 for win for O, 0 for draw
        """
        global tree
        return tree[self.gameState]


    # all remaining methods are to assist in the calculatiosn


    def display(self):
        """
        A pleasant view of the current game state
        :return: nothing
        """
        # prints the entire board in one print statement, row by row
        print('\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in self.gameState.getBoard()]))
