
# A simple class for a vertex in our graph
# we represent each vertex as a node with an id, a rank, and a pointer
# to a parent node (like a linked list) for our disjoint-set data structure
# see https://en.wikipedia.org/wiki/Disjoint-set_data_structure
class Vertex:
    def __init__(self, id, rank=0):
        self.id = id  # identification of the vertex
        self.rank = rank  # rank of the vertex (for the union function)
        self.parent = self  # parent or "root" vertex of this vertex


# Part of Union-Find disjoint-set data structure
# Find the 'topmost' parent of the disjoint-set
def find(node):
    if node.parent != node:
        # reassign the parent so we can flatten the structure
        node.parent = find(node.parent)
    return node.parent


# Part of Union-Find disjoint-set data structure
# Union the two disjoint sets, always union the shorter of the two
# to the longer if possible.
def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root.rank < y_root.rank:
        x_root.parent = y_root
    elif y_root.rank < x_root.rank:
        y_root.parent = x_root
    else:
        y_root.parent = x_root
        x_root.rank += 1


def partition(s, begin, end):
    # Lomuto partition scheme worst case O(n^2)
    # this version of partition may not be the most efficient in
    # terms of edge cases - but will do for our purpose of demonstration.
    pivot = end
    pivot_holder_index = begin
    for i in range(begin, end):
        if s[i][1] < s[pivot][1]:
            s[i], s[pivot_holder_index] = s[pivot_holder_index], s[i]
            pivot_holder_index += 1
    s[pivot_holder_index], s[end] = s[end], s[pivot_holder_index]
    return pivot_holder_index


def quick_sort(s, begin, end):
    if begin < end:
        pivot = partition(s, begin, end)
        # sort sub array on the left
        quick_sort(s, begin, pivot - 1)
        # sort sub array on the right
        quick_sort(s, pivot + 1, end)
    return s


def minimum_spanning_tree(graph):
    solution = set()  # set of edges for MST
    quick_sort(graph[1], 0, len(graph[1])-1)  # sort by weight
    for e in graph[1]:
        # if the two vertex are not apart of the same disjoint-set
        # and therefore won't make a cycle
        if find(e[0]) != find(e[2]):
            # make them apart of the same disjoint-set
            union(e[0], e[2])
            # add the edge to the solution
            solution.add(e)
    return solution


def main():
    # Create each vertex in our graph
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')

    # Represent our graph G as a pair of vertecies and edges with weights.
    G = [
        [a, b, c, d, e],  # vertecies
        [(a, 10, b), (b, 1, c), (c, 2, d), (d, 3, e), (d, 1, a)]  # edges
    ]

    # find the min spanning tree
    mst = minimum_spanning_tree(G)

    # pretty print
    for e in mst:
        print('{}--{}--{}'.format(e[0].id, e[1], e[2].id))


if __name__ == '__main__':
    main()
