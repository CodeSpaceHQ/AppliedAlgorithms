# Counting Inversions

This problem is discussed in [Dr. Gelfond Applied Algorithms](http://redwood.cs.ttu.edu/~mgelfond/FALL-2012/slides.pdf) and in [Geeks for Geeks](http://www.geeksforgeeks.org/counting-inversions/)


Category:

Difficulty to Understand:

## Problem
Given a person’s preferences (for books, movies, etc.)
match them with preferences of other people on the Web with
similar interests to provide a suggestion.

Preferences are often defined by rankings, labeling the objects
from 1 to n. So the problem is to define the distance between
two people's rankings. Calculate the number of inversions between each person's
rankings to represent the distance between them.

### Overview
Finding "similarity" or "distance" between two rankings. Given a sequence of n numbers 1..n (assume all numbers are distinct). Define a measure that tells us how far this list is from being in ascending order.
The value should be 0 if a_1 < a_2 < ... < a_n and should be higher as the list is more "out of order".

*Inversion*: _i_, _j_ form an inversion if a<sub>i</sub> > a<sub>j</sub>, i.e. if the two elements a<sub>i</sub> and a<sub>j</sub> are out of order.

We simply need to sort the list of preferences in ascending order and count the number of swaps we have to do.

### Input Format
A list of rankings [0, 1, 2, 3, 4, ...n]

### Constraints
Every number in the input list must be unique, a person can not give two items equal rankings.

### Output Format
The original set
The resulting count of inversions
The newly sorted set

## Algorithm
### Overview
We will use a [Divide and Conquer](https://en.wikipedia.org/wiki/Divide_and_conquer_algorithm) algorithm. This type of algorithm is used in popular sorting algorithms like  quicksort and merge sort, as well as various other algorithms.



### Pseudo Code


### Analysis

## Example

----

## Conclusion
