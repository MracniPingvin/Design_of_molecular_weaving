from functions.core_functions import create_matrix, create_chain, lay_chain, get_positions, create_global_matrix_references, check_positions
from classes.LatticeDraw import LatticeDraw
import globals

create_global_matrix_references(["tile", "lattice"], [create_matrix([6, 5], "rectangular"), create_matrix([6, 5], "rectangular")])
for i in globals.matrices["tile"]:
    print(i)
# lay_chain("tile", create_chain("a", []), 1, 2, 0)
# lay_chain("tile", create_chain("a", []), 1, 2, 90)
# lay_chain("tile", create_chain("a", []), 1, 2, 180)
# lay_chain("tile", create_chain("a", []), 1, 2, 270)

# lay_chain("tile", create_chain("a", []), 1, 2, 0)
# lay_chain("tile", create_chain("a", []), 1, 2, 60)
# lay_chain("tile", create_chain("a", []), 1, 2, 120)
# lay_chain("tile", create_chain("a", []), 1, 2, 180)
# lay_chain("tile", create_chain("a", []), 1, 2, 240)
# lay_chain("tile", create_chain("a", []), 1, 2, 300)
a = get_positions("tile", create_chain("abcd", [90, 90, 0]), 4, -1, 0)
print(check_positions(a))
lay_chain(a)

a = LatticeDraw(globals.matrices["tile"], [1000, 700], "rectangular", ["abcd", "efgh"])
a.draw()



