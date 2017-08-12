class FibHeap(object):
    """
    Fibonacci Heap
    A data structure for priority queue operations made up of a collection
    of heap-ordered trees (in this case min-heap).
    https://en.wikipedia.org/wiki/Fibonacci_heap
    """

    class Node(object):
        """
        Individual node in the Fibonacci Heap. Each node is set
        up to be apart of a doubly-linked list with other nodes of the 
        same depth.
        """

        def __init__(self, node_id, priority):
            """
            Constructor for a single node. Initially the node's parent, child,
            left, and right should be None or self.
            
            :param node_id: the identifier of the node
            :param priority: the  value for the node (used in min-heap)
            """

            self.node_id = node_id
            self.priority = priority
            self.depth = 0  # number of child nodes
            self.mark = False  # mark indicating if the node has lost children
            self.parent = None  # parent to this node
            self.child = None  # child to this node
            self.right = self  # right neighbor of node
            self.left = self  # left neighbor of node

    # private member variables
    __root_list = None  # list containing the root node of min-heaps
    __min_node = None  # Node in top_list with minimum key value
    __total_nodes = 0  # Count of all nodes in root_list

    @staticmethod
    def __iterate(start):
        """
        Helper function to iterate through a doubly-linked list
        :param start: the start node
        :return: yields the next node in the iteration
        """
        node = stop = start
        flag = False
        while True:

            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right

    def __consolidate(self):
        """
        Combine root nodes with equal depths to create a doubly-linked list
        of trees
        """
        nodes_by_depth = [None] * self.__total_nodes
        # Because we will be changing the nodes, we cannot iterate through
        # each node itself because the __iterate function will never come
        # across the same node again. Instead we iterate through by index.
        original_root_list = [x for x in self.__iterate(self.__root_list)]

        for node_idx in range(0, len(original_root_list)):
            node = original_root_list[node_idx]
            depth = node.depth

            while nodes_by_depth[depth]:
                node_eq_depth = nodes_by_depth[depth]  # node with equal depth


                ## The below lines would assure that no heap where a child
                ## had an equivalent priority as the parent would be made..
                ## instead they would be separate. This however, violates
                ## the min heap properties
                # if node_eq_depth.priority == node.priority:
                #     break


                # Always make the node with greater priority the parent
                if node.priority > node_eq_depth.priority:
                    node, node_eq_depth = node_eq_depth, node  # switch
                self.__merge_with_child_list(node, node_eq_depth)

                nodes_by_depth[depth] = None  # node depth is no longer the same
                depth += 1  # depth of combined trees =+1

            ## The below lines would be used with the above commented out lines
            ## in the while loop to find the new min_node without having to
            ## loop through the root list again.
            # if node.priority < self.min_node.priority:
            #     self.min_node = node

            nodes_by_depth[depth] = node  # add the new or unchanged node

        # find the new min node in the root list
        for node in self.__iterate(self.__root_list):
            if node.priority <= self.__min_node.priority:
                self.__min_node = node

    def __merge_with_child_list(self, parent, node):
        """
        Merge node with doubly linked list of parent's children node
        :param parent: the root node
        :param node: the node to be merged
        """
        self.__remove_from_root_list(node)

        if not parent.child:
            parent.child = node
            node.left = node
            node.right = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node

        parent.depth += 1
        node.parent = parent
        node.mark = False

    @staticmethod
    def __remove_from_child_list(parent, node):
        """
        Helper function to remove a node from the doubly-linked child list
        :param parent: the parent node which has the child to be removed
        :param node: the node to remove in the child list
        """
        parent.depth -= 1
        if parent.child == parent.child.right:
            parent.child = None
        elif parent.child == node:
            parent.child = node.right
            node.right.parent = parent
        node.left.right = node.right
        node.right.left = node.left

    def __merge_with_root_list(self, node):
        """
        Helper function to merge a node with the doubly-linked root list
        :param node: the node to merge in the root list
        """
        node.parent = None  # the child will be root of it's heap
        node.mark = False
        if not self.__root_list:  # if the heap is completely empty
            self.__root_list = node
        else:  # the heap is not empty, insert as new node in doubly-linked list
            node.right = self.__root_list.right
            node.left = self.__root_list
            self.__root_list.right.left = node
            self.__root_list.right = node

    def __remove_from_root_list(self, node):
        """
        Helper function to remove a node from the doubly-linked root list
        :param node: 
        """
        if node == self.__root_list:  # if the node is the head of the root list
            self.__root_list = node.right
        node.left.right = node.right  # reconnect node to the left
        node.right.left = node.left  # reconnect node to the right

    def __cut(self, x, y):
        self.__remove_from_child_list(x, y)
        self.__merge_with_root_list(y)

    def __recursive_cut(self, parent):
        """
        Recursively cut nodes who's priorities are less than their parents
        until we reach root node or an unmarked node
        :param parent: current parent node
        """
        if not parent:  # make sure this isn't already the root node of the heap
            return
        grandparent = parent.parent
        if grandparent:
            if not parent.mark:
                parent.mark = True
            else:
                self.__cut(grandparent, parent)
                self.__recursive_cut(grandparent)

    def is_empty(self):
        """
        Check to see if their are still nodes in root list
        :return: True if root list is empty, False otherwise 
        """
        return self.__root_list is None

    def add_with_priority(self, node_id, priority):
        """
        create and add a node to the top_list of the min-heap. 
        :param node_id: the identifier of the node
        :param priority: the node's priority
        :return: the new node
        """
        new_node = self.Node(node_id, priority)

        # Set the new min node
        if not self.__min_node or new_node.priority < self.__min_node.priority:
            self.__min_node = new_node
        self.__merge_with_root_list(new_node)  # put the node in root list
        self.__total_nodes += 1
        return new_node

    def extract_min(self):
        """
        Extract the minimum node (return and remove it) from the root list.
        Re-attach all of it's children node (if any) to the root list
        :return: the node with the minimum priority value
        """
        node = self.__min_node
        if node:
            if node.child:  # if the node has children we need to re-attach
                # Because we will be changing the nodes, we cannot iterate
                # through each node itself because the __iterate function will
                # never come across the same node again.
                # Instead we iterate through by index.
                children = [x for x in self.__iterate(node.child)]
                for x in range(0, len(children)):
                    child = children[x]
                    self.__merge_with_root_list(child)

            self.__remove_from_root_list(node)  # remove the minimum node

            # set a new min node in root list
            if node == node.right:
                self.__root_list = None
                self.__min_node = None
            else:
                self.__min_node = node.right
                self.__consolidate()

            self.__total_nodes -= 1
        return node

    def decrease_priority(self, node, new_priority):
        """
        Decrease the priority of a node and restructure the fib heap accordingly
        :param node: the targeted node
        :param new_priority: the targeted node's new priority
        :return: None if new_priority > current priority
        """
        if new_priority > node.priority:  # only allow decrease in priority
            return None

        node.priority = new_priority
        if node.parent and node.priority < node.parent.priority:
            # restructure if new priority violates min heap property
            self.__cut(node.parent, node)
            self.__recursive_cut(node.parent)
        if node.priority < self.__min_node.priority:
            # set new min node
            self.__min_node = node


def main():

    f = FibHeap()
    f.add_with_priority('b', 10)
    f.add_with_priority('c', 2)
    f.add_with_priority('d', 1)
    f.add_with_priority('c', 1)
    f.add_with_priority('e', 3)

    print(f.extract_min().priority)
    print(f.extract_min().priority)
    print(f.extract_min().priority)
    print(f.extract_min().priority)
    print(f.extract_min().priority)


if __name__ == '__main__':
    main()
