"""
"A-B": (distance, toll)
"A-B":(1,5) => A->B with distance 1km and toll 5tk
"""

nodes = ['A', 'B', 'C', 'D', 'E', 'F']

graph_data = {
    # Start Node A
    "A-B": (1, 5),
    "A-C": (2, 2),
    "A-E": (3, 1),

    # Start Node B
    "B-A": (1, 6),
    "B-D": (3, 3),
    "B-E": (4, 4),

    # Start Node C
    "C-A": (2, 3),
    "C-E": (3, 2),
    "C-F": (4, 2),

    # Start Node D
    "D-B": (3, 4),
    "D-E": (4, 3),
    "D-F": (5, 1),

    # Start Node E
    "E-A": (3, 1),
    "E-B": (4, 4),
    "E-C": (3, 2),
    "E-D": (4, 3),
    "E-F": (5, 2),

    # Start Node F
    "F-C": (4, 2),
    "F-D": (5, 1),
    "F-E": (5, 2)
}


# Generate coordinates for from start node A to end node E
def generate_coordinates(start_node, end_node):
    """
    Generate coordinates for from start node A to end node E
    """
    initial_path = f'{start_node}-{end_node}'
    distance = 0
    toll = 0
    _next_start_node = None
    if graph_data.get(initial_path):
        distance, toll = graph_data.get(initial_path)
    else:
        for node in nodes:
            for path, value in graph_data.items():
                if not path.startswith(start_node):
                    continue
                _next_start_node = path.split('-')[1]
                print(_next_start_node)

                _t = f'{_next_start_node}-{node}'
                distance, toll = graph_data.get(_t, (0, 0))
                print(_t, distance, toll)
                if _next_start_node == end_node:
                    break
    return distance, toll


coorditate = generate_coordinates('A', 'F')

print(coorditate)
