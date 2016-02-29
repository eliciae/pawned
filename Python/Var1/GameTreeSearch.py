# The search space is a tree, but the state space is a graph: there may be several different ways to
# reach a given game state.  The transposition table is a dictionary (hash table) that remembers if
# a game state was seen before, and it it was, what its minimax value is.

transpositionTable = dict()

def minimax(node):
    """
    :param node:  a Game object responding to the following methods:
        str(): return a unique string describing the state of the game (for use in hash table)
        isTerminal(): checks if the game is at a terminal state
        successors(): returns a list of all legal game states that extend this one by one move
        isMinNode(): returns True if the node represents a state in which Min is to move
        isMaxNode(): returns True if the node represents a state in which Max is to move
    :return: the value of the game state
    """
    global transpositionTable
    s = node.str()
    if s in transpositionTable:
        return transpositionTable[s]
    elif node.isTerminal():
        u = node.utility()
    else:
        vs = [minimax(c) for c in node.successors()]
        if node.isMaxNode():
            u = max(vs)
        elif node.isMinNode():
            u = min(vs)
        else:
            print("Something went horribly wrong")
            return None
    transpositionTable[s] = u
    return u

