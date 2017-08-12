
class Graph(object):
    """
    Simple dict representation of a weighted graph that can be 
    directed or undirected.
    """

    def __init__(self, connections, directed=False):
        self.__graph = dict() # vertex : [(vertex,  distance),...]
        self.__directed = directed
        self.add_connections(connections)  # initialize graph

    def add_vertex(self, v):
        """
        add a vertex to the graph dictionary if it doesnt exist
        :param v: id of vertex to add
        """
        existing = list(self.__graph.keys())
        if v not in existing:
            self.__graph[v] = []

    def add_connections(self, connections):
        """
        add list of tuple pairs to graph
        :param connections: list of tuples in form (vertexa, vertexb, distance)
        """
        for vertex1, vertex2, distance in connections:
            self.add_vertex(vertex1)
            self.add_vertex(vertex2)

            self.__graph[vertex1].append((vertex2, distance))
            if not self.__directed:
                self.__graph[vertex2].append((vertex1, distance))

    def get_neighbors(self, vertex):
        """
        get all neighboring nodes of a vertex
        :param vertex: the id of vertex to get neighbors from
        :return: list of neighboring vertices by id
        """
        return [x[0] for x in self.__graph[vertex]]

    def get_distance(self, vertex1, vertex2):
        """
        get distance between two vertices in a graph
        :param vertex1: first vertex
        :param vertex2: second vertex
        :return: integer distance
        """
        return [x[1] for x in self.__graph[vertex1] if x[0] == vertex2][0]

    def get_vertices(self):
        """
        Get all vertices in a graph
        :return: list of all vertices in a graph by id
        """
        return list(self.__graph.keys())


def main():
    g = Graph([
        ('A', 'B', 5),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('A', 'D', 5),
        ('D', 'C', 1),
        ('C', 'E', 1)
    ], directed=True)

    print(g.get_neighbors('A'))
    print(g.get_vertices())


if __name__ == '__main__':
    main()