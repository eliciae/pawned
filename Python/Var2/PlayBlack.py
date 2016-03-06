from a2.Python.Var2.Pawned import Pawned
from a2.Python.Var2.MiniMaxPawnAB import AlphaBeta
from a2.Python.Var2.State import State
import numpy as np

board = np.array([["." for x in range(6)] for x in range(6)], str)

board[2][2] = "b"
board[2][3] = "b"
board[2][4] = "b"
board[2][5] = "b"

board[5][3] = "w"
board[5][4] = "w"
board[5][5] = "w"
board[5][2] = "w"
s = State(None,"W")
p = Pawned(s)
ab = AlphaBeta()
while not p.isTerminal():

    print(p.validSpaces())
    p.display()
    fromRow, fromCol = input("Piece to move: ").split()
    who = (int(fromRow),int(fromCol))
    toRow, toCol = input("Move to space: ").split()
    where = (int(toRow), int(toCol))
    moved = p.move(who, where)
    p = Pawned(moved[1])
    p.display()
    if p.isTerminal():
        print("Broke")
        p.display()
        break

    minmax = ab.minimax(p, 0)
    print(p.validSpaces())
    print(minmax)
    print(ab.getTran())
    newMove = p.move(minmax[1][0], minmax[1][1])
    p = Pawned(newMove[1])
    print("___________")

