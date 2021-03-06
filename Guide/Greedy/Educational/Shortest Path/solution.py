from math import inf
from FibHeap import FibHeap
from Graph import Graph


def dijkstra_shortest_paths(graph, source):
    """
    Find the shortest paths between nodes in a graph
    :param graph: graph
    :param source: the starting node
    :return: path and distances of resulting tree in graph
    """
    dist = dict()  # dict to keep track of distances from source node
    prev = dict()  # dict to keep track of a node's previous node in its path
    nodes = dict()  # dict keep track of relationship between vertices in
    # graph and nodes in FibHeap

    # Initialize source node
    dist[source] = 0
    prev[source] = None

    queue = FibHeap()  # Initialize priority queue

    # fill and initialize everything else
    for v in graph.get_vertices():
        if v is not source:
            dist[v] = inf  # distance unknown, inf is infinity from math.py
            prev[v] = None  # no path yet
        nodes[v] = queue.add_with_priority(v, dist[v])

    while not queue.is_empty():
        u = queue.extract_min()  # extract the node with minimum distance
        for v in graph.get_neighbors(u.node_id):
            # for each neighbor, calculate the distance from u to it
            alt = dist[u.node_id] + graph.get_distance(u.node_id, v)
            if alt < dist[v]:  # if the new distance is shorter than old
                dist[v] = alt  # our distance to this node is shorter now
                prev[v] = u.node_id  # the path we take is through this node
                queue.decrease_priority(nodes[v], alt)  # decrease distance
    return dist, prev


def main():
    g = Graph([
        ('A', 'B', 14),
        ('A', 'C', 7),
        ('A', 'D', 9),
        ('C', 'D', 10),
        ('D', 'B', 2),
        ('E', 'D', 11),
        ('C', 'E', 15),
        ('E', 'F', 6),
        ('B', 'F', 9)
    ], directed=True)

    dist, path = dijkstra_shortest_paths(g, 'A')
    print('Directed Graph:\n\tDistances: {}\n\t Path: {}'.format(dist, path))

    g = Graph([
        ('A', 'B', 14),
        ('A', 'C', 7),
        ('A', 'D', 9),
        ('C', 'D', 10),
        ('D', 'B', 2),
        ('E', 'D', 11),
        ('C', 'E', 15),
        ('E', 'F', 6),
        ('B', 'F', 9)
    ], directed=False)

    dist, path = dijkstra_shortest_paths(g, 'A')
    print('Undirected Graph:\n\tDistances: {}\n\t Path: {}'.format(dist, path))


if __name__ == '__main__':
    main()
