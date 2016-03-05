from a2.Python.Var2.Pawned import Pawned
from a2.Python.Var2.MiniMaxPawn import minimax
from a2.Python.Var2.State import State
import numpy as np

board = np.array([["." for x in range(6)] for x in range(6)], str)

board[4][0] = "b"
board[1][2] = "b"

# board[0][2] = "w"
board[5][0] = "w"
board[3][2] = "w"
# board[][] = "w"
s = State(None,"W")
p = Pawned(s)

while not p.isTerminal():
    print(p.validSpaces())
    p.display()
    fromRow, fromCol = input("Piece to move: ").split()
    who = (int(fromRow),int(fromCol))
    toRow, toCol = input("Move to space: ").split()
    where = (int(toRow), int(toCol))
    moved = p.move(who, where)
    p = Pawned(moved[1])
    if p.isTerminal():
        print("Broke")
        p.display()
        break

    print("----Black-Turn----")
    minmax = minimax(p)
    print(p.validSpaces())
    print(p.state.getPlayer())
    print(minmax)
    newMove = p.move(minmax[1][0], minmax[1][1])
    p = Pawned(newMove[1])
    p.display()
    print(p.state.getPlayer())
    print("___________")
