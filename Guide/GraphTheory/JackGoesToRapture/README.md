# Jack goes to Rapture

## Problem
This problem comes from [HackerRank](https://www.hackerrank.com/challenges/jack-goes-to-rapture).
Category: Graph Theory
Difficulty: Medium

### Overview
Essentially the problem is giving the following challenge,

1. Assume you are given a list of edges for vertices from 1...n.
2. Find the weight of the path starting at 1 and ending at n such that the
cost of going from 1 to n is minimized. If no such path exists print "NO
PATH EXISTS".
3. The cost of a path is the maximum weight (cost) of any edge in that path.
4. No two edges have the same cost and no cost is negative.

## Algorithm
### Overview
The data structure best suited to this problem is Union-Find (UF). UF is
a data structure that efficiently merges groupings of objects together
and checks to see if two objects share the same group. In this case each
integer represents a vertex. It has the following operations,
- find(int i): returns the ID of the group that 'i' is in.
- count(): returns the number of groupings
- connected(int a, int b): returns true if 'a' and 'b' are in the same group.
- union(int a, int b): merges the groups of 'a' and 'b'.

NOTE: I used the implementation of UF from a [Princeton course](http://algs4.cs.princeton.edu/15uf/UF.java.html).

Using UF we can union the edges with the smallest weight until we get a
path from 1 to n. By using UF in this way, we minimize the cost of getting
from 1 to n.

Assumption: We don't care if we get extra edges in our set of minimal cost
edges because fair cost is the max edge cost among all edges. By going from
smallest cost to largest, if we reach the destination we can assume that
all previously used edges have a lower cost.

### Pseudo Code
1. Read in values 3 at a time, creating edges and adding them to a list.
2. Sort all edges in ascending order by weight (cost).
3. Iterate through the list of edges, calling union on each pair of vertices
until vertices 1 and n are connected, or until reaching the end of the list.
4. If there is a path from 1 to n, print the max edge value from that
path. Else, print "NO PATH EXISTS".

### Analysis
The best sorting algorithms under average conditions achieve a time
complexity of _O(m*log(m))_. Where m is the number of edges.
Union-Find has a time complexity of _O(log(m))_.
We apply Union-Find a maximum of m times during our loop through the list
of edges.
So the resulting time complexity of this solution is _O(m*log(m))_.

The longest running test case was #15 at 2.3s. This solution gets a full
score of 80 on HackerRank.

## Conclusion
This is a fun problem because it both tests your knowledge of graph theory
and your knowledge of different data structures. Although it can be fun to
try, as far as we know there is no _O(m)_ or _O(log(m))_ solution to this
problem. Other interesting challenges to consider are as follows.
- Does the solution change if edges can have the same weight? If so, how?
- How would you solve this problem if there were so many edges that you
could not fit them all on the same machine?
