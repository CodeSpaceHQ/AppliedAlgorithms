# Shortest Path Tree in a Graph

This problem is introduced in [Dr. Gelfond Applied Algorithms](http://redwood.cs.ttu.edu/~mgelfond/FALL-2012/slides.pdf) and is further discussed in [Shortest Path Problem Wikipedia](https://en.wikipedia.org/wiki/Shortest_path_problem)

The algorithm used to solve this problem is [Dijsktra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).

Category: Greedy

Difficulty: Hard to implement, medium to understand.

## Problem
Given a directed graph G = [V, E] where each edge _e_ has a length _l<sub>e</sub>_, and a starting node _s_ in that graph, determine the length
of the shortest path from _s_ to every other node.

![Dijkstra's Visualization](https://github.com/CodeSpaceHQ/AppliedAlgorithms/blob/shortest-path/Guide/Greedy/Shortest%20Path/assets/DijkstraDemo.gif "Visualization of Dijkstra's Algorithm")

### Overview
For this problem we will need to utilize two data structures:
* [Min Priority Queue](https://en.wikipedia.org/wiki/Priority_queue)
* [Graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics))

The implementation of priority queue we will use is the [Fibonacci Heap](https://en.wikipedia.org/wiki/Fibonacci_heap). We will not need to implement all of the functionality
of a fibonacci heap, just those that will allow us to:
1. Add a node consisting of an _id_ and a _key_ to the min heap,
2. Extract the node with the minimum key (the key in our case is the distance from the starting node),
3. Decrease the key of a specified node and re-arrange the min heap accordingly.

The Fibonacci Heap data structure is a task to understand by itself and is not the purpose of this guide. Readers only need to know what the above three functions do on a
high level to understand Dijkstra's algorithm for shortest path. The Fibonacci Heap implementation, as well as the link to the Wikipedia page, are included in this guide for supplemental reading.

The graph data structure will just be a simple representation of a directed or undirected graph using key-value pairs in dictionaries. A graph is represented by a single dictionary
with entries in the form:
    v : [(u, d), (u<sub>1</sub>, d),..., (u<sub>n</sub>, d)]
where the key _v_ is the id of a vertex in the graph (i.e., 'A'), and the value (a list of tuples) contain _u_: a connected node and _d_: the distance from _v_ to _u_.

### Input Format

Dijkstra's algorithm to find the shortest path between a starting node (source node) and all other vertices on a graph will take two inputs:
1. The graph
2. The starting node

In our implementation, the input will be:
1. Our Graph object _g_ discussed in the propblem overview above, directed or undirected.
2. The id of a starting node, i.e. 'A' or 'E', which must be in our input graph _g_

### Constraints
The start node must be a vertex included in the graph _g_.

### Output Format
Our output format will consist of two parts:
1. A dict of distances to each node from the start node, i.e. {'A': 0, 'B': 3, 'C':2,...}
2. A dict representing the path taken from the start node to all other nodes, i.e. {'A':None, 'B': 'A', 'C': 'B',...} where A is the starting node.

## Algorithm
### Overview
Dijkstra's algorithm has these main steps:
1. Initialize two dictionaries - one for distance between a node and a source node, and one for keeping track of a path between nodes.
2. Initialize a priority queue
3. Loop through while the queue is not empty, and extract the node with the minimum key (representing distance)
4. Calculate all distances from the extracted node's corresponding vertex to all of the vertex's neighbors, and put the smallest one in the distance dictionary for that vertex
5. Decrease the key of the node in the queue by the new distance of the vertex
6. continue

The priority queue will eventually empty, because extracting the minimum node will also delete it from the queue.

One other thing to mention in our implementation is the use of one more dictionary to keep track of the nodes we put in our queue. This is so we can get the corresponding
node in the heap in O(1) time by just the id from our vertex. This functionality could be implemented instead in the FibHeap class if desired.

### Pseudo Code

```Python

    def dijsktra(Graph g, String start_id):
        dist, prev = key value dictionaries  # dictionaries to keep track of path and distances
        dist[start_id] = 0  # distance to starting node is 0
        prev[start_id] = None  # starting node is the start, no previous path

        nodes = key value dictionary()  # we need to keep track of the nodes in the fibonacci heap to be able to relate them to the vertices in g in O(1) time
        queue = Priority Queue (Fibonacci Heap Data Structure)

        for each vertex v in g:
            if v is not the starting node:
                dist[v] = infinity  # unknown distance to this node
                prev[v] = None  # unknown path to this node
            queue.add(v, dist[v])  # add to fibonacci heap with key = distance to this node from source

        while queue is not empty:
            u = queue.extract_min()  # get the next minimum node
            for each neighbor v of u in g:
                alternate_distance = dist[u] + distance between vertices u and v in g
                if the alternate_distance < dist[v]:  # if alternate distance is shorter than the current distance we have form source to v
                    dist[v] = alt
                    prev[v] = u  # get to vertex v through vertex u
                    queue.decrease_key(nodes[v], alt)  # change the key of the node representing vertex v to alt

        return dist, prev

```

## Analysis
From Wikipedia:

>Dijkstra's original algorithm does not use a min-priority queue and runs in time O(|V|^{2}) (where |V| is the number of nodes). The idea of this algorithm is also given in Leyzorek et al. 1957. The implementation based on a min-priority queue implemented by a Fibonacci heap and running in O(|E|+|V|\log |V|) (where |E| is the number of edges) is due to Fredman & Tarjan 1984. This is asymptotically the fastest known single-source shortest-path algorithm for arbitrary directed graphs with unbounded non-negative weights.

Our algorithm implements the min-priority queue using the Fibonacci Haep data structure and thus follows the run time of O(|E|+|V|\log |V|).

The difference when using a min-priority queue, specifically the in the form of a Fibonacci Heap, is due to the time O(1) time complexity for inserting a node, finding the minimum node in the heap,
and decreasing the key of a node. Our extract min also deletes the minimum node from the heap, so it's time complexity is really O(n log n).

Another interesting discovery discussed in the Wikipedia page of Fibonacci Heaps is that although they look ver efficient, Fibonacci heaps have two drawbacks:
1. They are complicated when it comes to coding them
2. Also they are not as efficient in practice when compared with the theoretically less efficient forms of heaps, since in their simplest version they require storage and manipulation of four pointers per node, compared to the two or three pointers per node needed for other structures

For a more detailed discussion on the Fibonacci Heap and it's time complexities, see [here](https://en.wikipedia.org/wiki/Fibonacci_heap#Summary_of_running_times).

## Example
For the examples we will avoid the details of the implementation of the priority queue and fibonacci heap. Keeping track of the fibonacci heap
would make this example long and it is not the purpose of this guide to demonstrate the inner workings of the Fibonacci Heap.

### Undirected Graph

![Initial Undirected Graph](https://github.com/CodeSpaceHQ/AppliedAlgorithms/blob/shortest-path/Guide/Greedy/Shortest%20Path/assets/initial_undirected_graph.png "Initial Undirected Graph")

Trace through dijkstra(graph, 'A')

**Step 1: Initialization**

    dist = {'A':0}
    prev = {'A':None}
    nodes = {}
    queue = new FibHeap()

**Step 2: More Initialization**

For each vertex v in the graph, we place it in _dist_ and assign it a distance of infinity (inf). We also place each v in _prev_, and assign it a previous vertex of None.
Lastly, we place a node representation of the vertex and its distance from source ('A') into the queue.

The resulting dictionaries look like this:

    dist = {'A':0, 'B': inf, 'C': inf, 'D': inf, 'E': 'inf', 'F': inf}
    prev = {'A':None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
    nodes = {'A':('A',0), 'B': ('B',inf), 'C': ('C',inf), 'D': ('D',inf), 'E': ('E', inf), 'F': ('F', inf)}

And the visualized graph looks like this:

![Graph after initialization](https://github.com/CodeSpaceHQ/AppliedAlgorithms/blob/shortest-path/Guide/Greedy/Shortest%20Path/assets/iug_0.png "Graph after initialization")

**Step 3 First Loop**

![Graph after loop 1](https://github.com/CodeSpaceHQ/AppliedAlgorithms/blob/shortest-path/Guide/Greedy/Shortest%20Path/assets/iug_1.png "Graph after loop 1")

* All paths found to neighboring nodes are less than infinity, so they are all accepted as minimal paths, shown in red.

        dist = {'A':0, 'B': 14, 'C': 7, 'D': 9, 'E': 'inf', 'F': inf}
        prev = {'A':None, 'B': 'A', 'C': 'A', 'D': 'A', 'E': None, 'F': None}

**Step 4 Second Loop**

![Graph after loop 2](https://github.com/CodeSpaceHQ/AppliedAlgorithms/blob/shortest-path/Guide/Greedy/Shortest%20Path/assets/iug_2.png "Graph after loop 2")

* A second optional path to D (shown in blue) is found, but is not less than the path in dist['D'], so it is not accepted.
* Additionally, a new path from 'C' to 'E' is found, and it's distance is less than infinity, so it is accepted as a minimal path.
* Also the path from 'C' to 'A' is considered since the graph is undirected, but it's distance would be 7 + 7 = 14 (because the current path to 'C' is from 'A'). It is not accepted.

        dist = {'A':0, 'B': 14, 'C': 7, 'D': 9, 'E': 22, 'F': inf}
        prev = {'A':None, 'B': 'A', 'C': 'A', 'D': 'A', 'E': 'C', 'F': None}

**Step 5 Third Loop**

![Graph after loop 3](https://github.com/CodeSpaceHQ/AppliedAlgorithms/blob/shortest-path/Guide/Greedy/Shortest%20Path/assets/iug_3.png "Graph after loop 3")

* A shorter path to 'B' through 'D' is found, and is accepted (prev['B'] now equals 'D', dist['B'] is now 9 + 2 = 11).
* A shorter path to 'E' through 'D' is found, and is accepted (prev['E'] now equald 'D', dist['E'] is now 9 + 11 = 20).
* Another path to 'C' from 'D' is found, but it's distance is not shorter than the current distance in dist['C'], so it is not accepted.

        dist = {'A':0, 'B': 11, 'C': 7, 'D': 9, 'E': 20, 'F': inf}
        prev = {'A':None, 'B': 'D', 'C': 'A', 'D': 'A', 'E': 'D', 'F': None}

**Step 6 Fourth Loop**

![Graph after loop 4](https://github.com/CodeSpaceHQ/AppliedAlgorithms/blob/shortest-path/Guide/Greedy/Shortest%20Path/assets/iug_4.png "Graph after loop 4")

* A new path from 'B' to 'F' is found, it's distance is less than infinity so it is accepted as a minimal path.
* A path from 'B' to 'A' is examined but is not accepted because it's distance (9 + 11 + 14 = 34) is not less than dist['B'].

        dist = {'A':0, 'B': 11, 'C': 7, 'D': 9, 'E': 20, 'F': 20}
        prev = {'A':None, 'B': 'D', 'C': 'A', 'D': 'A', 'E': 'D', 'F': 'B'}

**Step 7 Fifth Loop**

![Graph after loop 5](https://github.com/CodeSpaceHQ/AppliedAlgorithms/blob/shortest-path/Guide/Greedy/Shortest%20Path/assets/iug_5.png "Graph after loop 5")

* Two paths from 'E' to 'F' and 'C' are found, but both's distances would not be less than their respective distances in dist['F'] and dist['C'], so they are not accepted.

        dist = {'A':0, 'B': 11, 'C': 7, 'D': 9, 'E': 20, 'F': 20}
        prev = {'A':None, 'B': 'D', 'C': 'A', 'D': 'A', 'E': 'D', 'F': 'B'}

**Step 8 Sixth Loop**

![Graph after loop 6](https://github.com/CodeSpaceHQ/AppliedAlgorithms/blob/shortest-path/Guide/Greedy/Shortest%20Path/assets/iug_6.png "Graph after loop 6")

* A path from 'F' to 'E' is examined but is not accepted because it's distance is not less than dist['E'].
* All nodes in the graph have been examined and the shortest spanning tree to each node in the graph has been found. The algorithm terminates.

        dist = {'A':0, 'B': 11, 'C': 7, 'D': 9, 'E': 20, 'F': 20}
        prev = {'A':None, 'B': 'D', 'C': 'A', 'D': 'A', 'E': 'D', 'F': 'B'}


**COMPLETED**


### Directed Graph

![Initial Directed Graph](https://github.com/CodeSpaceHQ/AppliedAlgorithms/blob/shortest-path/Guide/Greedy/Shortest%20Path/assets/initial_directed_graph1.png "Initial Directed Graph")


## Conclusion
For this conclusion I will use a quote from the Wikipedia page on Dijkstra's Algorithm in the section _Practical optimizations and infinite graphs_.

>In common presentations of Dijkstra's algorithm, initially all nodes are entered into the priority queue. This is, however, not necessary: the algorithm can start with a priority queue that contains only one item, and insert new items as they are discovered (instead of doing a decrease-key, check whether the key is in the queue; if it is, decrease its key, otherwise insert it). This variant has the same worst-case bounds as the common variant, but maintains a smaller priority queue in practice, speeding up the queue operations.
Moreover, not inserting all nodes in a graph makes it possible to extend the algorithm to find the shortest path from a single source to the closest of a set of target nodes on infinite graphs or those too large to represent in memory. The resulting algorithm is called uniform-cost search (UCS) in the artificial intelligence literature...

