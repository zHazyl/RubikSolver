from rubik import app
import rubik.cube as cube
from rubik.optimize import dict_state_move, optimize_moves
from rubik.solve import Solver
import numpy as np

if __name__ == "__main__":
    app.run()
    
    
# if __name__ == '__main__':
#     DEBUG = True
#     c = cube.Cube("DLURRDFFUBBLDDRBRBLDLRBFRUULFBDDUFBRBBRFUDFLUDLUULFLFR")
#     print("Solving:\n", c)
#     orig = cube.Cube(c)
#     solver = Solver(c)
#     solver.solve()

#     print(f"{len(solver.moves)} moves: {' '.join(solver.moves)}")
#     print(c)

#     check = cube.Cube(orig)
#     check.sequence(" ".join(solver.moves))
#     assert check.is_solved()

# if __name__ == '__main__':
#     DEBUG = True
#     c = cube.Cube('YYYYYYYYYBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGOOOWWWWWWWWW') 
#     c.R()
#     c.D()
#     c.Ri()
#     c.D()
#     c.L()
#     c.F()
#     c.F()
#     c.Ri()
#     c.B()
#     c.U()
#     c.E()
#     cc = cube.Cube(c)
#     solver = Solver(cc)
#     solver.solve()
#     opt_moves = optimize_moves(solver.moves)
#     stmove = dict_state_move(cc, opt_moves)
#     print(stmove)