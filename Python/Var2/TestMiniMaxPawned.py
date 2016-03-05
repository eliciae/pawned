from a2.Python.Var2.Pawned import Pawned
from a2.Python.Var2.MiniMaxPawn import minimax
from a2.Python.Var2.State import State
import numpy as np

board = np.array([["." for x in range(6)] for x in range(6)], str)

board[4][0] = "b"
board[3][2] = "b"

# board[0][2] = "w"
board[5][0] = "w"
board[5][2] = "w"
# board[][] = "w"
s = State(board,"B")
p = Pawned(s)

print(minimax(p))
