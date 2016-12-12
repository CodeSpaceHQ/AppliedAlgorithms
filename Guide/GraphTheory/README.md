# Graph Theory Guide

## Overview
At their core, graphs are sets of objects (vertices) with connections (edges) between them.
For example, a roadmap could be represented by a graph with cities as vertices and highways as edges.
A program dealing with this example would have at least two data structures.
The first would store information about cities, like their name and which highways they are connected to.
The second would store information about highways, like their name, how long they are, and which cities they connect.

## Additional Resources
This section contains links to resources about graphs.

### Introduction
[Examples of Graph Problems] (http://world.mathigon.org/Graph_Theory) -
This webpage discusses some of the common types of problems that can be represented by graphs.

[Video on Graph Basics] (https://www.youtube.com/watch?v=HmQR8Xy9DeM) -
This video covers basic mechanics required to program a graph.

[In-Depth Material] (https://www.tutorialspoint.com/graph_theory/index.htm)

### Data Structures
When solving any programming problem, one of the first things that must be determined is how data will be stored.
This section contains links to information about common graph data structures.

[Adjacency Lists and Matrices] (http://www.geeksforgeeks.org/graph-and-its-representations/)

### Algorithms
Once a dataset has been recognized as a graph, it is possible to use graph algorithms to solve problems that relate to that dataset.
This section contains links to information about common graph algorithms.

[Dijkstra's Algorithm] (http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/) -
Dijkstra's algorithm is used to find the shortest path between two vertices in a graph.
Given a graph with airports as vertices and flights as edges (where edge length is flight price), it would be possible to find the cheapest way to get from one airport to another.

[Kruskal's Algorithm] (http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/) -
Kruskal's algorithm is used to find the [minimum spanning tree] (http://algs4.cs.princeton.edu/43mst/) of a given graph.
