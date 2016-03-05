# The search space is a tree, but the state space is a graph: there may be several different ways to
# reach a given game state.  The transposition table is a dictionary (hash table) that remembers if
# a game state was seen before, and it it was, what its minimax value is.
# Warning: The transposition table can fill up quickly!
from a2.Python.Var2.Pawned import Pawned
transpositionTable = dict()

def minimax(node):
    """
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
    s = str(node)

    if s in transpositionTable:
        return transpositionTable[s]
    elif node.isTerminal():
        u = node.utility()
        m = None
    else:

        vs = [(minimax(c)[0],m) for (m,c) in node.successors()]  # strip off the move returned by minimax!
        if node.isMaxNode():
            u,m = argmax(vs)
        elif node.isMinNode():
            u,m = argmin(vs)
        else:
            print("Something went horribly wrong")
            return None
    transpositionTable[s] = u,m  # store the move and the utility in the tpt
    return u,m

def argmax(ns):
    """
    find the highest utility,move pair
    :param ns: a list of utility,move pairs
    :return:  the utility,move pair with the highest utility
    """
    maxv,maxm = ns[0]
    for v,m in ns:
        if v > maxv:
            maxv,maxm = v,m
    return maxv,maxm


def argmin(ns):
    """
    find the lowest utility,move pair
    :param ns: a list of utility,move pairs
    :return:  the utility,move pair with the lowest utility
    """
    minv,minm = ns[0]
    for v,m in ns:
        if v < minv:
            minv,minm = v,m
    return minv,minm

