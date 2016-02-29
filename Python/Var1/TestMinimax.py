"""
from a2.Python.Var1.GameTreeSearch import minimax
from a2.Python.Var1.TTTT import TicTacToe

a = TicTacToe(None)
minimax(a)
"""
from a2.Python.Var2 import Pawned
from a2.Python.Var1.GameTreeSearch import minimax
from a2.Python.Var2.State import State

a = Pawned.Pawned(None)
spaces = a.validSpaces(a.gameState)
board = a.move(spaces[0][0], spaces[0][1], a.gameState)
print(board)
s = State(board, "W")
spaces = a.validSpaces(s)
board = a.move(spaces[0][0], spaces[0][1], s)
print(board)
s = State(board, "W")
spaces = a.validSpaces(s)
board = a.move(spaces[0][0], spaces[0][1], s)
print(board)
s = State(board, "W")
spaces = a.validSpaces(s)
board = a.move(spaces[0][0], spaces[0][1], s)
print(board)
s = State(board, "B")
spaces = a.validSpaces(s)
print(spaces)
board = a.move(spaces[1][0], spaces[1][1], s)
print(board)