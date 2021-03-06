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
find a minimum spanning tree of G.

### Overview
There are many algorithms to find the minimum spanning tree of a graph G. The one we will be using is [Kruskal's Algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm#Pseudocode).
We will implement the most-optimized version of the algorithm in Dr. Gelfond's lecture slides using disjoint-set data structure with Union() and Find() functions.

**[Disjoint-set data structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure#MakeSet)**:  is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets.

Here is a disjoint-set of 8 elements taken from the above Wikipedia page:

![Initial Disjoint Set](assets/disjoint_set_individual.png "8 individual disjoint sets")

As we add edges (comprised of vertices) to our minimum spanning tree, we will also Union() the two vertices in the edge together. After numerous iterations of this, the
above initial disjoint set would now look something like this:

![Disjoint Set Grouped](assets/disjoint_set_group.png "8 overlapping / partially grouped disjoint sets")

The reason for doing this will be discussed further in the Analysis section of this guide. For a more in-depth discussion of disjoint-set data types and
related topics, please visit the [Disjoint-set](https://en.wikipedia.org/wiki/Disjoint-set_data_structure#MakeSet) Wikipedia page.


### Input Format
Our input format will a graph G using our custom Graph class,

The graph data structure will just be a simple representation of a directed or undirected graph using key-value pairs in dictionaries. A graph is represented by a single dictionary with entries in the form: v : [(u, d), (u1, d),..., (un, d)] where the key v is the id of a vertex in the graph (i.e., 'A'), and the value (a list of tuples) contain u: a connected node and d: the distance from v to u.

### Constraints
Due to our disjoint-set data structure being a crucial part to solving this problem, each vertex existing anywhere in our input graph G
must also have a corresponding set in our DisjointSet data structure, so that we can perform `union()` and `find()` operations on them.

### Output Format
Each edge that is included in the minimum spanning tree of our graph separated by a new line and shown in the form _u--w--v_ where _u_ and _v_ are vertices and w is the edge's weight.

## Algorithm
### Overview
The basic idea to create a minimum spanning tree using Kruskal's algorithm is to sort all edges in increasing weight, and then
loop through each edge checking to see if adding it to the solution would cause a cycle.

By pre-sorting all edges, we guarantee that we are looking at the minimum weight paths first, and by checking to see if the edge would create a cycle
before adding it to our minimum spanning tree, we are avoiding creating just another graph.

### Pseudo Code

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

1. Edge (A, 5, D):
* Disjoint sets: [(A) (B) (C) (D) (E) (F) (G)]
* Find(A) will return A, and Find(D) will return D, because initially all vertices are disjoint sets. A != D so,
* The edge (A, D, 5) will be added to the solution set
* The disjoint-set containing vertex A in it will be unioned with the disjoint set containing vertex D

![Step 1](assets/iter1.png "Examining the first edge")

----

 
 2. Edge C, E, 5):
* Disjoint sets: [(A, D) (B) (C) (E) (F) (G)]
* Find(C) will return C, and Find(E) will return E, and C != E so,
* The edge (C, E, 5) will be added to the solution set
* The disjoint-set containing vertex C in it will be unioned with the disjoint set containing vertex E

![Step 2](assets/iter2.png "Examining the second edge")

----

3. Edge (D, F, 6):
* Disjoint sets: [(A, D) (B) (C, E) (F) (G)]
* Find(D) will return A because it is the parent of the set D is in, and Find(F) will return F, and A != F so,
* The edge (D, F, 6) will be added to the solution set
* The disjoint-set containing vertex D will be unioned with the disjoint set containing vertex F

![Step 3](assets/iter3.png "Examining the third edge")

----

4. Edge (A, B, 7):
* Disjoint sets: [(A, D, F) (B) (C, E) (G)]
* Find(A) will return A, and Find(B) will return B, and A != B so,
* The edge (A, B, 7) will be added to the solution set
* The disjoint-set containing vertex A will be unioned with the disjoint set containing vertex B

![Step 4](assets/iter4.png "Examining the fourth edge")

----

5. Edge (B, E, 7):
* Disjoint sets: [(A, D, F, B) (C, E) (G)]
* Find(B) will return A, and Find(E) will return E, and A != E so,
* The edge (B, E, 7) will be added to the solution set
* The disjoint-set containing vertex A will be unioned with the disjoint set containing vertex E

5a. Edge (B, C, 8):
* Disjoint sets: [(A, D, F, B, C, E, C, E) (G)]
* Find(B) will return A, and Find(E) will return A, and A == A, so
* go to next edge

5a. Edge (F, E, 8):
* Disjoint sets: [(A, D, F, B, C, E, C, E) (G)]
* Find(F) will return A, and Find(E) will return A, and A == A, so
* go to next edge

5b. Edge (B, C, 8):
* Disjoint sets: [(A, D, F, B, C, E, C, E) (G)]
* Find(B) will return A, and Find(E) will return A, and A == A, so
* go to next edge

![Step 5](assets/iter5.png "Examining the fifth edge")

----


6. Edge (E, G, 9):
* Disjoint sets: [(A, D, F, B, C, E) (G)]
* Find(E) will return A, and Find(G) will return G, and A != G so,
* The edge (E, G, 9) will be added to the solution set
* The disjoint-set containing vertex E will be unioned with the disjoint set containing vertex G

![Step 6](assets/iter6.png "Examining the sixth edge")


NOTE: All edges after this point would only create a cycle if added to the solution, our Minimum Spanning tree is found.

----

## Conclusion
Our minimum spanning tree is found, and it is of minimal weight. For a further in-depth proof of Kruskal's algorithm, see [Proof of correctness](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm#Proof_of_correctness)
