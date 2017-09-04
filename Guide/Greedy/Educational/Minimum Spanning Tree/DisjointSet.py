class DisjointSet(object):

    class Node(object):
        def __init__(self, node_id, rank=0):
            self.id = node_id
            self.parent = self
            self.rank = rank

    __disjoint_set_dict = dict()

    def make_set(self, x):
        """
        Add a new set disjoint from all others to the list
        :param x: the id of the set to add
        :return: the new node or None if the node already exists in the set
        """
        node = None
        if x not in self.__disjoint_set_dict.keys():
            node = self.Node(x)
            self.__disjoint_set_dict[x] = node
        return node

    def make_sets(self, array):
        """
        Add new disjoint sets for each id in the array
        :param array: list of id's to make sets out of
        :return: the new list of disjoint sets
        """
        new_sets = []
        for x in array:
            if x not in self.__disjoint_set_dict.keys():
                node = self.Node(x)
                new_sets.append(node)
                self.__disjoint_set_dict[x] = node
        return new_sets


    def find(self, x):
        """
        Find the root node of a set with id x in it
        :param x: the id of the node to find the root of
        :return: the root node
        """
        node = self.__disjoint_set_dict[x]  # get node representation of x
        if node.parent != node:
            node.parent = self.find(node.parent.id)
        return node.parent

    def union(self, x, y):
        """
        Union two sets together, preferably smaller to bigger
        :param x: id of the first node
        :param y: id of the second node
        """

        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if x_root.rank < y_root.rank:  # if y is bigger
            x_root.parent = y_root
        elif x_root.rank > y_root.rank:  # if x is bigger
            y_root.parent = x_root
        else:
            y_root.parent = x_root
            x_root.rank += 1

    def print(self):
        """
        Print each disjoint set and it's connections
        """
        for k, v in self.__disjoint_set_dict.items():
            print(k, end='')
            while v.parent != v:
                print('-> {}'.format(v.parent.id), end='')
                v = v.parent
            print('')


def main():
    d = DisjointSet()
    d.make_set('a')
    d.make_set('b')
    d.make_set('c')
    d.union('a', 'b')
    d.union('b', 'c')
    d.print()




if __name__ == '__main__':
    main()