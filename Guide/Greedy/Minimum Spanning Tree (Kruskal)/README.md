# Minimum Spanning Tree

This problem is discussed in [Dr. Gelfond Applied Algorithms](http://redwood.cs.ttu.edu/~mgelfond/FALL-2012/slides.pdf) and in [Wikipedia](https://en.wikipedia.org/wiki/Minimum_spanning_tree)


Category: Greedy

Difficulty: N/A

## Problem
Given a graph G = (V, E) with positive cost c<sub>e</sub> associated with every edge e and:
* An undirected graph is a _tree_ if it is connected and has no cycles (a cycle must include at least two different edges),
* _Spanning tree_ of G is a set T of edges such that (V, T) is a tree,
* _Cost_ of T is the sum of costs of its edges,
* _Minimum spanning tree_ of G is a spanning tree of G with minimal cost,
Find a minimum spanning tree of G.

### Overview
The total number of spanning trees in a graph G is O(n<sup>n</sup>). An exhaustive search is impossible.

### Input Format


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

