"""
This module implements Floyd's algorithm to compute the shortest distance
between all pairs of nodes in a graph.

It provides a function called floyd(), which takes in a square matrix
representing the graph and returns a square matrix
representing the shortest distance between all pairs of nodes in the graph.
"""


def floyd(dist):
    """
    Computes the shortest distance between all pairs of nodes in a graph using
     Floyd's algorithm.

    Args:
        dist (list): A square matrix representing the graph. Each element
        [i][j] in the matrix represents
        the weight of the edge between nodes i and j.

    Returns:
        list: A square matrix representing the shortest distance between all
        pairs of nodes in the graph.
        Each element [i][j] in the matrix represents the shortest distance
        between nodes i and j.
    """

    def calc_dist(start_node, end_node, inter_node):
        """
        Helper function that recursively calculates the shortest distance
         between two nodes.

        Args:
            start_node (int): The starting node.
            end_node (int): The ending node.
            inter_node (int): The intermediate node to consider.

        Returns:
            int: The shortest distance between start_node and end_node using
            intermediate as the intermediate node.
        """

        if start_node == end_node:
            return 0
        elif inter_node == 0:
            return dist[start_node][end_node]
        else:
            return min(calc_dist(start_node, end_node, inter_node - 1),
                       calc_dist(start_node, inter_node - 1,
                                 inter_node - 1) + calc_dist(
                           inter_node - 1,
                           end_node, inter_node - 1))

    # Iterate over all pairs of nodes and call calc_dist() to compute
    # the shortest distance.
    for i in range(len(dist)):
        for j in range(len(dist)):
            dist[i][j] = calc_dist(i, j, len(dist))

    return dist


# Example usage

# Define matrix size
N = 8

MAX_LENGTH = N

# Create a new graph matrix with N rows and N columns
graph = [[0] * MAX_LENGTH for _ in range(MAX_LENGTH)]
for a in range(MAX_LENGTH):
    for b in range(MAX_LENGTH):
        graph[a][b] = abs(a - b)

# Call floyd() with the updated graph
result = floyd(graph)

# Print the matrix row by row
for row in result:
    print(row)
