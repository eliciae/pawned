class TicTacToe:
    # Represent the gamestate for tic tac toe.
    #  Minimax assumes objects that respond to the following methods:
    #     str(): return a unique string describing the state of the game (for use in hash table)
    #     isTerminal(): checks if the game is at a terminal state
    #     successors(): returns a list of all legal game states that extend this one by one move
    #     isMinNode(): returns True if the node represents a state in which Min is to move
    #     isMaxNode(): returns True if the node represents a state in which Max is to move

    def __init__(self, state, player='X'):
        """
        Create a new object
        :param state: a description of the board for the current state
        :param player: whose turn it isto play in the current state
        :return:
        """
        if state is None:
            self.gameState = dict()
            for r in range(1,4):
                 for c in range(1,4):
                    self.gameState[r,c] = '.'
        else:
            self.gameState = state
        self.whoseTurn = player
        self.cachedWin = False  # set to True in winFor() if
        self.cachedWinner = None

    def str(self):
        """ *** needed for search ***
        Translate the board description into a string.  Could be used as for a hash table...
        :return: A string that describes the board in the current state.
        """
        s = ""
        for r in range(1,4):
            for c in range(1,4):
                s += self.gameState[r,c]
        return s


    def isMinNode(self):
        """ *** needed for search ***
        :return: True if it's Min's turn to play
        """
        return self.whoseTurn == 'O'


    def isMaxNode(self):
        """ *** needed for search ***
        :return: True if it's Max's turn to play
        """
        return self.whoseTurn == 'X'


    def isTerminal(self):
        """ *** needed for search ***
        :param node: a game tree node with stored game state
        :return: a boolean indicating if node is terminal
        """
        return self.winFor('X') or self.winFor('O') or (len(self.allBlanks()) == 0)

    def successors(self):
        """ *** needed for search ***
        :param node:  a game tree node with stored game state
        :return: a list of game tree nodes that are the next possible states
        """
        blanks = self.allBlanks()
        next = self.togglePlayer(self.whoseTurn)
        states = map(lambda v: self.move(v,self.whoseTurn), blanks)
        nodes = [TicTacToe(s,next) for s in states]
        return nodes


    def utility(self):
        """ *** needed for search ***
        :return: 1 if win for X, -1 for win for O, 0 for draw
        """
        if self.winFor('X'):
            self.display()
            return 1
        elif self.winFor('O'):
            self.display()
            return -1
        else:
            self.display()
            return 0


    # all remaining methods are to assist in the calculatiosn

    def winFor(self, player):
        """
        Check if it's a win for player.
        Note the use of a cache.  This prevents re-computation in functions isTerminal() and utility()
        :param player: either 'X' or 'O'
        :return: True if player appears 3 in a row, column, diagonal
        """
        if self.cachedWin is False:
            # rows columns diagonals
            won =     any([all([self.gameState[r,c]==player for r in range(1,4) ]) for c in range(1,4)])\
                   or any([all([self.gameState[r,c]==player for c in range(1,4) ]) for r in range(1,4)])\
                   or all([self.gameState[d,d] == player for d in range(1,4)])\
                   or all([self.gameState[d,4-d] == player for d in range(1,4)])
            if won:
                self.cachedWin = True
                self.cachedWinner = player
                return True
            else:
                return False
        else:
            return player == self.cachedWinner



    def togglePlayer(self,p):
        """
        :param p: either 'X' or 'O'
        :return:  the other player's symbol
        """
        if p == 'X':
            return 'O'
        else:
            return 'X'


    def move(self,where,who):
        """
        Create a new board description adding the given move.
        :param where: Where the move was
        :param who: who moved there
        :return: a copy of the current state with the additional move included
        """
        gs = self.gameState.copy()
        gs[where] = who
        return gs


    def allBlanks(self):
        """
        :return: a list of available places to put a marker
        """
        return [v for v in self.gameState if self.gameState[v] == ' ']


    def display(self):
        """
        A pleasant view of the current game state
        :return: nothing
        """
        for r in range(1, 4):
            print("+-+-+-+")
            print("|", end="")
            for c in range(1, 3):
                print(self.gameState[r,c], end="")
                print("|",end="")
            print(self.gameState[r,3], end="")
            print("|")
        print("+-+-+-+")
