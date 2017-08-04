class Node:
    def __init__(self, id, rank=0):
        self.id = id
        self.parent = self
        self.rank = rank

    def __str__(self):
        return self.id


def make_set(vertex):
    return Node(vertex)


def find(node):
    if node.parent != node:
        node.parent = find(node.parent)
    return node.parent


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
    # quicksort
    if begin < end:
        pivot = partition(s, begin, end)
        # sort sub array on the left
        quick_sort(s, begin, pivot - 1)
        # sort sub array on the right
        quick_sort(s, pivot + 1, end)
    return s


def minimum_spanning_tree(graph):
    tree = set()  # set of edges

    for v in graph[0]:
        make_set(v)

    # sort edges by weight
    graph[1] = quick_sort(graph[1], 0, len(graph[1])-1)
    for e in graph[1]:
        if find(e[0]) != find(e[2]):
            union(e[0], e[2])
            tree.add(e)
    return tree


def main():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    G = [
        [a, b, c, d, e],
        [(a, 10, b), (b, 1, c), (c, 2, d), (d, 3, e), (d, 1, a)]
    ]
    mst = minimum_spanning_tree(G)

    for e in mst:
        print('{}--{}--{}'.format(e[0].id, e[1], e[2].id))


if __name__ == '__main__':
    main()
