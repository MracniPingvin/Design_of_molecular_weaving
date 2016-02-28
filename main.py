__author__ = 'FAMILY'


def create_node_matrix(width, height):
    node_matrix = []
    for i in range(height):
        node_matrix.append([])
        for j in range(width):
            node_matrix[i].append(0)
    return node_matrix


def create_edge_matrix(width, height, tessellation):
    edge_matrix = []
    directions = 0

    if tessellation == "triangular":
        directions = 3
    elif tessellation == "rectangular":
        directions = 2

    for i in range(height):
        edge_matrix.append([])
        for j in range(width):
            edge_matrix[i].append([])
            for k in range(directions):
                edge_matrix[i][j].append([0])
    return edge_matrix


def create_chain(alphabet, length, shape):
    chain = {'alphabet': alphabet,
             'length': length,
             'shape': shape}
    return chain


