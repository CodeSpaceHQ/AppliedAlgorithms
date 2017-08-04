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

As we add edges (comprised of vertecies) to our minimum spanning tree, we will also Union() the two vertecies in the edge together. After numerous iterations of this, the
above initial disjoint set would now look something like this:

![Disjoint Set Grouped](https://github.com/CodeSpaceHQ/AppliedAlgorithms/blob/interval-partitioning/Guide/Greedy/Interval%20Partitioning/Assets/step1.PNG "8 overlapping / partially grouped disjoint sets")

The reason for doing this will be discussed further in the Analysis section of this guide. For a more in-depth discussion of disjoint-set data types and
related topics, please visit the [Disjoint-set](https://en.wikipedia.org/wiki/Disjoint-set_data_structure#MakeSet) Wikipedia page.


### Input Format
Our input format will a graph G = [V, E] where V is a set of vertecies and E is a set of edges with their corresponding weights such that:
* Each vertex _v_ in V will have a pointer to a parent vertex as well as a rank and an id (i.e. an id of _a_, _b_, _c_...).
* Each edge will be represented in the form _(v, w, v)_ where _v_ is a vertex and w is the edge's weight.

An example input graph to our algorithm might look like this:

```Python
    vertex_a = Vertex('a')  # 'a' is the id of vertex_a, and initially vertex_a is it's own parent
    vertex_b = Vertex('b')

    # our input graph G
    G = [
        [a, b],  # set of vertecies
        [(vertex_a, 4, vertex_b)]  # set of edges, with one edge from vertex_a to vertex_b with a weight of 4
    ]
```

### Constraints

### Output Format

## Algorithm
### Overview



### Pseudo Code

## Version 1

```python

    def interval_scheduling(set_of_requests):
      1. While set_of_requests is not empty
        a. select a request x from set_of_requests with earliest finish time
        b. add x it to the solution set
        c. remove all all sets incompatible with x from set_of_requests including x
      2. return the solution set
```


### Analysis



## Example



## Conclusion

