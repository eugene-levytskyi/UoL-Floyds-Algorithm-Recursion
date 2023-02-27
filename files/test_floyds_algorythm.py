import pytest

from floyds_algorithm_imperative import floydWarshall
from floyds_algorithm_recursion import floyd


# Unit tests

def test_floyd():
    # Define a graph with known shortest path distances
    graph = [
        [0, 1, 3],
        [1, 0, 1],
        [3, 1, 0]
    ]

    # Compute the shortest path distances using Floyd's algorithm
    shortest_paths = floyd(graph)

    # Verify that the computed distances match the expected values
    assert shortest_paths == [
        [0, 1, 2],
        [1, 0, 1],
        [2, 1, 0]
    ]

# Performance tests

@pytest.fixture(scope="session")
def graph():
    """ Returns a graph with 10 nodes """
    return [[0] * 10 for _ in range(10)]


def test_floyd(benchmark, graph):
    result = benchmark(floyd, graph)
    assert result is not None


def test_floydWarshall(benchmark, graph):
    result = benchmark(floydWarshall, graph)
    assert result is not None
