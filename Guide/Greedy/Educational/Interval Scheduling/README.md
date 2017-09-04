# Interval Scheduling

This problem is discussed in [Dr. Gelfond Applied Algorithms](http://redwood.cs.ttu.edu/~mgelfond/FALL-2012/slides.pdf) and in [Wikipedia](https://en.wikipedia.org/wiki/Interval_scheduling)
 

Category: Greedy

Difficulty: Medium

## Problem
### Overview
There is one resource which can be used by at most one person at a time. Multiple people request the use of this resource with a start time _s_ and a finish time _f_. Maximize the number of accepted requests so that no request (s, f) overlap, and the set of accepted requests are optimal, i.e. there is no other compatible set of requests with more requests.

_From Wikipedia:_
> Interval schedluing is a class of problems in computer science, particularly in the area of algorithm design. The problems consider a set of tasks. Each task is represented by an _interval_ describing the time in which it needs to be executed. For instance, task A might run from 2:00 to 5:00, task B might run from 4:00 to 10:00, and task C might run from 9:00 to 11:00. A subset of intervals is _compatible_ if no two intervals overlap. For example, the subset {A, C} is compatible, as is the subset {B}; but neither {A, B} or {B, C} are compatible subsets, because the intervals within each subset overlap.

### Input Format
- A set _S_ containing n rquests in the form of _(s, f)_ where _s_ is the start time and _f_ is the finish time of a request.

### Constraints
- No two intervals _(s, f)_ may overlap within a solution, and the solution must be the most optimal soltuion of _S_, i.e. maximum number of requests in the solution.

### Output Format
- a list of the intervals existing in the optimal solution.

## Algorithm
### Overview
For our interval scheduling algorithm we will re-state the problem in a more precise way:

> Given a set _R_ = {i<sub>1</sub>...,i<sub>n</sub>} of requests where each request _i_ is associated with an interval [s(i), f(i)), find a best schedule, i.e. a subset _A_ of requests from _R_ such that:

> 1. _A_ is _compatible_, i.e. _A_ contains no overlapping requests and 

> 2. _A_ is _optimal_, i.e. there is no compatible subset of _R_ which has more requests than _A_.


### Pseudo Code

## Version 1

```python

    def interval_scheduling(set_of_requests):
      1. While set_of_requests is not empty
        a. select a request x from set_of_requests with earliest finish time
        b. add x to the solution set
        c. remove all sets incompatible with x from set_of_requests including x
      2. return the solution set
```

## Version 2

```python
    def interval_scheduling(set_of_requests):
        1. Sort set_of_requests in order of finishing time.
        2. i = 0, n = len(set_of_requests)
        3. f := − 1
        4. while i <= n:
            a. if set_of_requests[i]'s finish time is greater than or equal to f:
                1. append the request to the solution set
                2. f = the requests finish time
            b. i = i + 1
        5. return the solution set

```

### Analysis

## Version 1

Version 1 of the solution has a worst case time complexity of O(n<sup>2</sup>) and a best case of O(n). Since the list of requests is not sorted
the algorithm must loop over the list of requests n times for the outer while loop, and n more times for finding the minimal finish time.

## Example

Requests = [(6, 9), (2, 3), (1, 4), (1, 3), (4, 5)]

Solution = []

Step 1:

    a. first request with minimum finish time is (2, 3)
    
    b. Solution = [(2, 3)]
    
    c. Requests = [(6, 9), (4, 5)]

Step 2:

    a. request with minimum finish time is (4, 5)
    
    b. Solution = [(2, 3), (4, 5)]
    
    c. Requests = [(6, 9)]

Step 3:

    a. request with minimum finsih time is (6, 9)
    
    b. Solution = [(2, 3), (4, 5), (6, 9)]
    
    c. Request = []

Solution set = [(2, 3), (4, 5), (6, 9)]

## Version 2

Version 2 of the solution has a worst case time complexity of O(n<sup>2</sup>) and an average time complexity of O(n log n) from quick sorting the set of requests before finding the optimal solution.
The time complexity of the algorithm when the entire set of requests is sorted by finish time is simply n, and the time complexity of sorting
the un-sorted set of requests is O(n log n), which means T(n) = O(n log n) + O(n) wherein the extra addition of n can be dropped.
A faster sorting algorithm such as Radix sort which has a time complexity of O(kn) where k is the number of requests to be sorted, or
counting sort which is O(N + k) where k is the range of the requests to be sorted, would both cause Version 2 to have a time complexity of O(n).

To be precise, radix sort is O(kN), where k is the number of digits in the values to be sorted.
 Counting sort is O(N + k), where k is the range of the numbers to be sorted.

## Example

Requests = [(6, 9), (2, 3), (1, 4), (1, 3), (4, 5)]
Solution = []

1. Sort requests by finish time. Requests = [(1, 3), (2, 3), (1, 4), (4, 5), (6, 9)]

First Iteration:

    request = (1, 3)
    
    Since the previous finish time (-1) is greater than this requests start time (1), 
    the request is added to the solution set and the new finsh time is 3.
    
    solution set = [(1, 3)]

Second Iteration:

    request = (2, 3)
    
    Since the previous finsh time (3) is greater than this requests start time (2),
    the request is not added to the solution set and the finish time is still 3.
    
    solution set = [(1, 3)]
    
Third Iteration:

     request = (1, 4)
     
     Since the previous request finish time (3) is greater than this requests start time (1),
     the request is not added to the solution set and the finish time is still 3.
     
     soltion set = [(1, 3)]
     
Fourth Iteration:

     request = (4, 5)
     
     Since the previous request finish time (3) is less than this requests start time (4),
     the request is added to the solution set and the finish time is now 5.
     
     solution set = [(1, 3), (4, 5)]
     
Fifth Iteration:

     request = (6, 9)
     
     Since the previous request finish time (5) is less than this requests start time (6),
     the request is added to the solution set and the finish time is now 9.

     solution set = [(1, 3), (4, 5), (6, 9)]
     
 We have completed looping over the entire sorted set of requests and placed compatible ones in the solution set.
 Final Solution Set = [(1, 3), (4, 5), (6, 9)]


## Conclusion

For the conclusion we will view a short piece from the Wiki (modified slightly) on Interval Scheduling (discussing version 1 of the algorithm):

> Whenever we select an interval at step a, we may have to remove many intervals in step c.
> However, all these intervals necessarily cross the finishing time of x, and thus they all cross each other.
> Hence, at most 1 of these intervals can be in the optimal solution.
> Hence, for every interval in the optimal solution, there is an interval in the greedy solution.
> This proves that the greedy algorithm indeed finds an optimal solution.
