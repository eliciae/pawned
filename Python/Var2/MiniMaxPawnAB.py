# The search space is a tree, but the state space is a graph: there may be several different ways to
# reach a given game state.  The transposition table is a dictionary (hash table) that remembers if
# a game state was seen before, and it it was, what its minimax value is.
# Warning: The transposition table can fill up quickly!
from a2.Python.Var2.Pawned import Pawned

transpositionTable = dict()
class AlphaBeta:

    def __init__(self):
        self.alpha = -100000000000
        self.beta = 1000000000000000


    def minimax(self, node, depth):
        """
        :param depth: BOOO FREAKING wHOOo
        :param node:  a Game object responding to the following methods:
            str(): return a unique string describing the state of the game (for use in hash table)
            isTerminal(): checks if the game is at a terminal state
            successors(): returns a list of all legal game states that extend this one by one move
                          in this version, the list consists of a move,state pair
            isMinNode(): returns True if the node represents a state in which Min is to move
            isMaxNode(): returns True if the node represents a state in which Max is to move
        :return: a pair, u,m consisting of the minimax utility, and a move that obtains it
        """
        global transpositionTable

        s = node.str()

        if s in transpositionTable:
            return transpositionTable[s]
        elif node.isTerminal() or depth >= 4:
            u = node.utility()
            m = None
        else:
            vs = [(self.minimax(c, depth + 1)[0],m) for (m,c) in node.successors()]  # strip off the move returned by minimax!
            if node.isMaxNode():
                u,m = self.argmax(vs)
            elif node.isMinNode():
                u,m = self.argmin(vs)
            else:
                print("Something went horribly wrong")
                return None
        transpositionTable[s] = u,m  # store the move and the utility in the tpt
        return u,m

    def argmax(self, ns):
        """
        find the highest utility,move pair
        :param ns: a list of utility,move pairs
        :return:  the utility,move pair with the highest utility
        """
        maxv,maxm = ns[0]
        for v,m in ns:
            if v > maxv:
                if v >= self.beta:
                    return v, m
                maxv, maxm = v, m
                self.alpha = max(self.alpha, maxv)
        return maxv, maxm


    def argmin(self, ns):
        """
        find the lowest utility,move pair
        :param ns: a list of utility,move pairs
        :return:  the utility,move pair with the lowest utility
        """
        minv,minm = ns[0]
        for v,m in ns:
            if v < minv:
                if v <= self.alpha:
                    return v, m
                minv,minm = v,m
                self.beta = min(self.beta, minv)
        return minv,minm

    def getTran(self):
        return len(transpositionTable)

