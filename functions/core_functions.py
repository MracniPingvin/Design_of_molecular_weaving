import globals


def create_matrix(size, tessellation):
    edge_matrix = []
    directions = 0
    width = size[0]
    height = size[1]

    if tessellation == "triangular":
        directions = 3
    elif tessellation == "rectangular":
        directions = 2

    for i in range(height):
        edge_matrix.append([])
        for j in range(width):
            edge_matrix[i].append([])
            for k in range(directions):
                edge_matrix[i][j].append([])
            edge_matrix[i][j].append(0)
    return edge_matrix


def create_chain(alphabet, shape):
    chain = {'alphabet': alphabet,
             'shape': shape}
    return chain


def create_global_matrix_references(reference_names, reference_values):
    dictionary = dict(zip(reference_names, reference_values))
    globals.matrices = dictionary


def get_positions(matrix, chain, x, y, angle):
    node_positions = []
    segment_positions = []
    for i in range(len(chain["alphabet"])):
        letter = chain["alphabet"][i]
        if angle >= 180:
            letter = chain["alphabet"][i].upper()
        print("x:", x, "y:", y, "letter:", letter, "angle:", angle)

        if i == 0:
            node_positions.append([matrix, y, x])

        x += globals.directions[str(angle)][0]
        y += globals.directions[str(angle)][1]

        segment_positions.append([matrix, y, x, globals.directions[str(angle)][4], letter])

        x += globals.directions[str(angle)][2]
        y += globals.directions[str(angle)][3]

        if i == len(chain["alphabet"]) - 1:
            node_positions.append([matrix, y, x])

        if i < len(chain["alphabet"]) - 1:
            angle += chain["shape"][i]
        if angle >= 360:
            angle -= 360
    return [segment_positions, node_positions]


def lay_chain(positions):
    for i in positions[0]:
        globals.matrices[i[0]][i[1]][i[2]][i[3]].append(i[4])
    for i in positions[1]:
        globals.matrices[i[0]][i[1]][i[2]][-1] += 1
