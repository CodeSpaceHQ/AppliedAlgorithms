# Shortest Path Tree in a Graph

This problem is introduced in [Dr. Gelfond Applied Algorithms](http://redwood.cs.ttu.edu/~mgelfond/FALL-2012/slides.pdf) and is further discussed by [Washington University](https://courses.cs.washington.edu/courses/cse521/13wi/slides/06dp-sched.pdf)

This problem is a vriation of the simpler [Interval Scheduling](../../Greedy/Educational/Interval Scheduling) problem that can be solved using a greedy algorithm.

Category: Dynamic Programming

Difficulty: Hard

## Problem
Given _n_ requests where each request _i_ has an associated interval _[s<sub>i</sub>, f<sub>i</sub>)_ and has a weight/value
_v<sub>i</sub>_, and one server, select a subset of mutually compatible requests with maximum weight/value.

### Overview
Ordering intervals by the earliest finishing time like we did in the [Interval Scheduling](../../Greedy/Educational/Interval Scheduling) solution does not work.
Later intervals may not be compatible with the current one and may have much higher weights.

First we must solve a simpler problem - finding the maximum sum of weights. To do this we will use a helper function `opt()` that will return
an array containing the max value for a schedule containing j and not containing j for each request j.

### Input Format

A list of requests R such that each request _i_ has a start time _s<sub>i</sub>_, a finish time _f<sub>i</sub>_ a value or weight _v<sub>i</sub>_ and an index
of the first previous request compatible with _i_.

### Constraints
The input list of requests must be sorted by finish time before the main part of our algorithm.

### Output Format
The output will be a list of indices of the requests in the optimal schedule. If the sorted list of request is [A, C, B, E, D, G, F] and the optimal
schedule is [C, D, F], our algorithm will return [1, 4, 6].

## Algorithm
### Overview
Finding an optimal schedule of weighted intervals has a few steps:
1. Sort the requests by finish time
2. Find p(j) for each request (p(j) is the largest index of the previous request compatible with j)
3. Find the value of optimal solutions to the problem consisting of job requests 1, 2, ..., j if j were included in the schedule or not included.
4. Using the list from step #3, find the schedule with the max sum of request values.

So the trickiest part here is step #3. Basically to accomplish this we loop through each request _r_ in the set of requests _R_ and see if _r_ plus its previous
compatible request values is bigger than the request before it plus its previous compatible request values. The easiest way at this point to understand this is just by seeing
its implementation and pseudo code.



### Pseudo Code

```Python

   def opt(requests: set of requests scheduled by finish time):
        m = []
        m[0] = 0  # the first request has no previous requests.. so its opt is 0
        for i from 1...len(requests):
            # m[i] is the max between this request and its previous compatible
            # requests, and the previous set of compatible requests.
            m[i] = max(value of i + m[p(i)], m[i-1])
        return m

   def find_solution(m, i):
        # i is the last index in the array of requests
        if i == 0:
            return [i]
        if value of request at index i + m[p(i)] > m[i-1]:
            return find_solution(m, p(i)) + [i]
        return find_solution(m, i-1)

```

## Analysis

## Example


### Directed Graph

## Conclusion
