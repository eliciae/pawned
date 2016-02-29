# this example is the game tree in lecture notes 6 - Game Playing, slide 23
# I gave the nodes in that graph an alphabetic label A-Y, working in BFS order
# The dictionary here stores the edges, and the terminal nodes, which makes the
# implementation of the game object easier
# the minimax value of the tree is 5
# the purpose of this example is to test minimax and alphabeta pruning!

tree = dict()
tree['A'] = "BCD" # max node A has 3 successors BCD
tree['B'] = "EF"  # min node B has 2 successors EF
tree['C'] = "GHI" # min
tree['D'] = "JK" # min
tree['E'] = "LM" # max
tree['F'] = "NO" # max
tree['G'] = "PQ" # max
tree['H'] = "RS" # max
tree['I'] = "TU" # max
tree['J'] = "VW" # max
tree['K'] = "XY" # max
tree['L'] = 4    # terminal
tree['M'] = 3    # terminal
tree['N'] = 6    # terminal
tree['O'] = 2    # terminal
tree['P'] = 2    # terminal
tree['Q'] = 1    # terminal
tree['R'] = 9    # terminal
tree['S'] = 5    # terminal
tree['T'] = 3    # terminal
tree['U'] = 1    # terminal
tree['V'] = 5    # terminal
tree['W'] = 4    # terminal
tree['X'] = 7    # terminal
tree['Y'] = 5    # terminal


class Simple:
    # Represent the gamestate for a simple 4 level game tree.
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
        :param player: whose turn it isto play in the current state
        :return:
        """
        if state is None:
            self.gameState = 'A'
        else:
            self.gameState = state


    def str(self):
        """ *** needed for search ***
        Translate the state into a string.  Could be used as for a hash table...
        :return: A string that describes the current state.
        """
        return self.gameState


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
        return [Simple(c) for c in tree[self.gameState]]


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
        print("In state: ", self.gameState)
