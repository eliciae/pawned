
from Python.Var1.GameTreeSearch import minimax
from Python.Var1.TTTT import TicTacToe

a = TicTacToe(None)
print(a.str())
#minimax(a)
"""
from Python.Var2 import Pawned
import numpy as np
from Python.Var1.GameTreeSearch import minimax
from Python.Var2.State import State

'''
a = Pawned.Pawned(None)
spaces = a.validSpaces(a.gameState)
state = a.move(spaces[0][0], spaces[0][1], a.gameState)
print(state.getBoard())
s = State(state.getBoard(), "W")
spaces = a.validSpaces(s)
print(spaces)
state = a.move(spaces[0][0], spaces[0][1], s)
print(state.getBoard())
s = State(state.getBoard(), "W")
spaces = a.validSpaces(s)
state = a.move(spaces[0][0], spaces[0][1], s)
print(state.getBoard())
s = State(state.getBoard(), "W")
spaces = a.validSpaces(s)
state = a.move(spaces[0][0], spaces[0][1], s)
print(state.getBoard())
s = State(state.getBoard(), "B")
spaces = a.validSpaces(s)
print(spaces)
state = a.move(spaces[1][0], spaces[1][1], s)
print(state.getBoard())
print(spaces)
'''

board = np.array([["." for x in range(6)] for x in range(6)], str)

board[2][1] = "b"
board[3][4] = "b"

# board[0][2] = "w"
board[3][1] = "w"
board[4][4] = "w"
# board[][] = "w"

state = State(board, None)
a = Pawned.Pawned(state)
print(a.isTerminal(a.gameState))
print(a.winFor(state, "w"))
print(a.isMinNode(state))



'''
a = Pawned.Pawned(None)
print("successor start!!")
stateList = a.successors(a.gameState)
for s in stateList:
    print(s.getBoard())
    print(a.isTerminal(s))

more = a.successors(stateList[1])
print("More states and should switch player")
for s in more:
    print(s.getBoard())
    print(a.isTerminal(s))
more = a.successors(stateList[1])
print("More states and should switch player")
for s in more:
    print(s.getBoard())
    print(a.isTerminal(s))
more = a.successors(stateList[0])
print("More states and should terminate")
for s in more:
    print(s.getBoard())
    print(a.isTerminal(s))
'''
"""