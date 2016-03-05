from functions.core_functions import create_matrix, create_chain, lay_chain, create_global_matrix_references
from classes.LatticeDraw import LatticeDraw
import globals

create_global_matrix_references(["tile", "lattice"], [create_matrix([5, 5], "triangular"), create_matrix([5, 5], "triangular")])

for i in globals.matrices["tile"]:
    print(i)

lay_chain("tile", create_chain("ab", [0]), 0, 2, 0)
lay_chain("tile", create_chain("ab", [60]), 0, 2, 0)
lay_chain("tile", create_chain("ab", [120]), 0, 2, 0)
lay_chain("tile", create_chain("ab", [180]), 0, 2, 0)
lay_chain("tile", create_chain("ab", [240]), 0, 2, 0)
lay_chain("tile", create_chain("ab", [300]), 0, 2, 0)
for i in globals.matrices["tile"]:
    print(i)


# a = LatticeDraw(create_matrix([5, 5], "rectangular"), [500, 500], "rectangular", ["abcd", "efgh"])
# a.draw()



