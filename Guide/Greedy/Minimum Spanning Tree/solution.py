from Graph import Graph
from DisjointSet import DisjointSet


def partition(s, begin, end):
    """
    Partially sort an array using a pivot value. Everything to the 
    left of the pivot will be less than the pivot. Everything to the right
    will be greater than the pivot.
    :param s: the array to sort
    :param begin: the beginning of the section of the array to sort
    :param end: the end of the section of the array to sort
    :return: the array with sorted section begin-end
    """
    pivot = end  # set the pivot to the end of the array
    pivot_holder_index = begin  # place holder for where the pivot will end up
    for i in range(begin, end):
        if s[i][2] < s[pivot][2]:  # if s[i] < s[pivot]
            # switch s[i] and pivot place holder
            s[i], s[pivot_holder_index] = s[pivot_holder_index], s[i]
            pivot_holder_index += 1  # increase pivot place holder

    # finally, put pivot in its placeholder
    s[pivot_holder_index], s[end] = s[end], s[pivot_holder_index]
    return pivot_holder_index


def quick_sort(s, begin, end):
    """
    Quick sort 
    :param s: the array to sort
    :param begin: the beginning of the array
    :param end: the ending of the array
    :return: the sorted array
    """
    # Quick sort
    if begin < end:
        pivot = partition(s, begin, end)  # find a pivot place
        quick_sort(s, begin, pivot - 1)  # recursive sort sub array on the left
        quick_sort(s, pivot + 1, end)  # recursive sort sub array on the right
    return s


def minimum_spanning_tree(graph):
    """
    Find the minimum spanning tree in the given graph using 
    Kruskal's algorithm
    :param graph: the graph to find the MST in
    :return: the set of all edges in the MST
    """
    d = DisjointSet()  # initialize disjoint set data structure
    d.make_sets(graph.get_vertices())
    edges = graph.get_edges()  # All edges in graph
    solution = set()  # Set of edges in MST
    quick_sort(edges, 0, len(edges)-1)  # Sort by edge weight in asc

    for e in edges:
        if d.find(e[0]) != d.find(e[1]):  # if the vertices wont make a cycle
            d.union(e[0], e[1])  # union them
            solution.add(e)  # add the edge to the solution
    return solution


def main():

    graph = Graph([
        ('a', 'b', 7),
        ('b', 'c', 8),
        ('b', 'd', 9),
        ('d', 'a', 5),
        ('b', 'e', 7),
        ('c', 'e', 5),
        ('e', 'd', 15),
        ('d', 'f', 6),
        ('f', 'g', 11),
        ('g', 'e', 9),
        ('f', 'e', 8)
    ], directed=False)

    mst = minimum_spanning_tree(graph)

    # pretty print all of the edges in the mst
    for e in mst:
        print('{}--{}--{}'.format(e[0], e[2], e[1]))


if __name__ == '__main__':
    main()