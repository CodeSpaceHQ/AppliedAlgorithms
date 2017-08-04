# Minimum Spanning Tree

This problem is discussed in [Dr. Gelfond Applied Algorithms](http://redwood.cs.ttu.edu/~mgelfond/FALL-2012/slides.pdf) and in [Wikipedia](https://en.wikipedia.org/wiki/Minimum_spanning_tree)


Category: Greedy

Difficulty to Understand: Hard

## Problem
Given a graph G = (V, E) with positive cost c<sub>e</sub> associated with every edge e and:
* An undirected graph is a _tree_ if it is connected and has no cycles (a cycle must include at least two different edges),
* _Spanning tree_ of G is a set T of edges such that (V, T) is a tree,
* _Cost_ of T is the sum of costs of its edges,
* _Minimum spanning tree_ of G is a spanning tree of G with minimal cost,
Find a minimum spanning tree of G.

### Overview
There are many algorithms to find the minimum spanning tree of a graph G. The one we will be using is [Kruskal's Algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm#Pseudocode).
We will implement the most-optimized version of the algorithm in Dr. Gelfond's lecture slides using disjoint-set data structure with Union() and Find() functions.

**[Disjoint-set data structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure#MakeSet)**:  is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets.

Here is a disjoint-set of 8 elements taken from the above Wikipedia page:

![Initial Disjoint Set](https://github.com/CodeSpaceHQ/AppliedAlgorithms/blob/interval-partitioning/Guide/Greedy/Interval%20Partitioning/Assets/step1.PNG "8 individual disjoint sets")

As we add edges (comprised of vertices) to our minimum spanning tree, we will also Union() the two vertices in the edge together. After numerous iterations of this, the
above initial disjoint set would now look something like this:

![Disjoint Set Grouped](https://github.com/CodeSpaceHQ/AppliedAlgorithms/blob/interval-partitioning/Guide/Greedy/Interval%20Partitioning/Assets/step1.PNG "8 overlapping / partially grouped disjoint sets")

The reason for doing this will be discussed further in the Analysis section of this guide. For a more in-depth discussion of disjoint-set data types and
related topics, please visit the [Disjoint-set](https://en.wikipedia.org/wiki/Disjoint-set_data_structure#MakeSet) Wikipedia page.


### Input Format
Our input format will a graph G = [V, E] such that:
* V is a set of vertices and,
* E is a set of edges with their corresponding weights in the form _(u, w, v)_ where _u_ and _v_ are vertices and _w_ is the weight of the edge

### Constraints
Due to our disjoint-set data structure being a crucial part to solving this problem, each vertex existing anywhere in our input graph G
must have three members/properties:
    1. id - this is an identifier for the visual name of the vertex, i.e. 'a', or 'b', or 'c', etc.
    2. rank - the rank will be used in the Union() function when bringing two disjoint sets together, initially it is 0
    3. parent - the parent node in the vertices disjoint-set. Initially the parent is the vertex itself, until Union() is called on the vertices disjoint-set

This is the format we will follow for our disjoint-set data structure, an example input graph to our algorithm might look like this:

```Python
    vertex_a = Vertex('a')  # 'a' is the id of vertex_a, and initially vertex_a is it's own parent
    vertex_b = Vertex('b')

    # our input graph G
    G = [
        [a, b],  # set of vertices
        [(vertex_a, 4, vertex_b)]  # set of edges, with one edge from vertex_a to vertex_b with a weight of 4
    ]
```

### Output Format
Each edge that is included in the minimum spanning tree of our graph separated by a new line and shown in the form _u--w--v_ where _u_ and _v_ are vertices and w is the edge's weight.

## Algorithm
### Overview
The basic idea to create a minimum spanning tree using Kruskal's algorithm is to sort all edges in increasing weight, and then
loop through each edge checking to see if adding it to the solution would cause a cycle.

By pre-sorting all edges, we garuntee that we are looking at the minimum weight paths first, and by checking to see if the edge would create a cycle
before adding it to our minimum spanning tree, we are avoiding creating just another graph.

### Pseudo Code

## Version 1

```python

    def minimum_spanning_tree(G):
        solution = []
        1. sort all edges in G by weight
        2. For e in sorted edges:
            a. if solution unioned with e causes no cycles:
                i. add e to solution
        3. return solution
```


### Analysis
Kruskal's algorithm to find a minimum spanning tree utilizes the union-find disjoint-set data structure to avoid adding vertices to the minimum spanning tree
that would cause a cycle, and therefore would disqualify the solution (it would no longer be a tree).

The steps are:
```
1. Sort all edges in G by weight
2. For each edge (u, w, v)
    a. if u is not in the same disjoint-set as v
        i. combine u and v's disjoint-sets
        ii. add (u, w, v) to the solution set
```

Step 1 is done using a comparison sort - in our case quick sort.
Step 2a is done by using the Find() function on both vertices. Because each vertice is represented as a node with an id, rank, and 'pointer' to another parent node,
each vertex that is in a set will be represented by the first vertex of that set. If _u_ and _v_ are in the same set, Find() will return the same parent vertex.
Step 2a part i is done by calling the Union() function with both vertices. This function utilizes the rank to append the smaller of the two disjoint sets containing the vertices to the end of the larger one.
Step 2a part ii is simply adding the current edge to the solution - our minimum spanning tree.

Much like other greedy algorithms, Kruskal's algorithmic time complexity is largely determined by the pre-sort method used. In our case, quick sort would have
an average case of O(E log E), where E is the number of edges in a graph G.

If we use counting sort or radix sort to sort our edges by weight in linear time, the complexity decreases to O(E alpha(V)) time, where _alpha_ is the inverse of the
[Ackermann Function](https://en.wikipedia.org/wiki/Ackermann_function).

## Example
This excellent example is a slightly modified version from the Wikipedia page on Kruskal's algorithm. The images are unmodified.



## Conclusion

