import heapq  # python's priority queue data structure


# extremely primitive graph object
class Graph(object):
    vertices = []  # list of vertices in graph
    neighbors = dict()  # keep track of vertices neighbors
    adj = dict()  # keep track of distances between vertices

    def insert(self, id):
        self.neighbors[id] = []
        self.vertices.append(id)

    def add_edge(self, ida, idb, cost):
        # add edge for undirected graph
        self.neighbors[ida].append(idb)
        self.neighbors[idb].append(ida)
        self.adj[(ida, idb)] = cost
        self.adj[(idb, ida)] = cost

    def distance(self, ida, idb):
        # return the distance between ida and idb
        return self.adj[(ida, idb)]


def dijkstra(graph, source):
    dist = dict()  # v:d where d is the distance from source to vertex v
    prev = dict()  # u:v where (u, v) is an edge min distance between u and v
    queue = []  # a list to hold a fibonacci heap

    dist[source] = 0  # distance to source is 0
    prev[source] = None  # source will never have a parent

    # initialization of distances and previous for each vertex
    for v in graph.vertices:
        if v is not source:
            dist[v] = None  # unknown distance from source
            prev[v] = None  # no parent initially
        heapq.heappush(queue, (v, dist[v]))  # push (v, dist[v]) onto queue

    while queue:
        u = heapq.heappop(queue)  # u = (v, d) where v is the vertex and d is distance from source node
        for v in graph.neighbors[u[0]]:
            alt = dist[u[0]] + graph.distance(u[0], v)  # try to find a shorter path from source
            if dist[v] is None or alt < dist[v]:
                queue[queue.index((v, dist[v]))] = (v, alt)
                heapq.heapify(queue)
                dist[v] = alt  # replace the distance from source to v with alt
                prev[v] = u[0]  # v's previous vertex is now u

    return dist, prev




def main():
    g = Graph()

    g.insert('a')
    g.insert('b')
    g.insert('c')
    g.insert('d')
    g.insert('e')

    g.add_edge('a', 'b', 1)
    g.add_edge('b', 'c', 3)
    g.add_edge('c', 'd', 4)
    g.add_edge('a', 'd', 2)
    g.add_edge('d', 'e', 3)
    g.add_edge('b', 'e', 2)

    source = 'a'
    dist, prev = dijkstra(g, source)

    print('Distances from source: {}'.format(dist))
    print('Connections to source: {}'.format(prev))

if __name__ == '__main__':
    main()