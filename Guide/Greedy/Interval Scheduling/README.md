# Interval Scheduling

This problem is discussed in [Dr. Gelfond Applied Algorithms](http://redwood.cs.ttu.edu/~mgelfond/FALL-2012/slides.pdf) and in [Wikipedia](https://en.wikipedia.org/wiki/Interval_scheduling)
 

Category: Greedy

Difficulty: N/A

## Problem
### Overview
There is one resource which can be used by at most one person at a time. Multiple people request the use of this resource with a start time _s_ and a finish time _f_. Maximize the number of accepted requests so that no request (s, f) overlap, and the set of accepted requests are optimal, i.e. there is no other compatible set of requests with more requests.

_From Wikipedia:_
> Interval schedluing is a class of problems in computer science, particularly in the area of algorithm design. THe problems consider a set of tasks. Each task is represented by an _interval_ describing the time in which it needs to be executed. For instance, task A might run from 2:00 to 5:00, task B might run from 4:00 to 10:00, and task C might run from 9:00 to 11:00. A subset of intervals is _compatible_ if no two intervals overlap. For example, the subset {A, C} is compatible, as is the subset {B}; but neither {A, B} or {B, C} are compatible subsets, because the intervals within each subset overlap.

### Input Format
- A set S containing n rquests in the form of (s, f) where s is the start time and f is the finish time of a request.

### Constraints
- No two intervals (s, f) may overlap within a solution, and the solution must be the most optimal soltuion of S, i.e. maximum number of requests in the solution.

### Output Format
- a list of the intervals existing in the optimal solution.

## Algorithm
### Overview
For our interval scheduling algorithm we will re-state the problem in a more precise way:

> Given a set *R* = {i<sub>1</sub>...,i<sub>n</sub>} of requests where each request _i_ is associated witha n interval [s(i), f(i)), find a best schedule, i.e. a subset *A* of requests from *R* such that: 

> 1. *A* is _compatible_, i.e. *A* contains no overlapping requests and 

> 2. *A* is _optimal_, i.e. there is no compativle subset of *R* which has more requests than *A*.


### Pseudo Code

The first version of the pseudo code assumes that the set of intervals is already sorted by earliest finish time first.
This version also has to loop over the entire set of intervals and remove the incompatible intervals each time.

```python

    def interval_scheduling(set_of_intervals):
      1. While set_of_intervals is not empty
        a. select a request _i_ from set_of_intervals with earliest finish time
        b. add _i_ it to the solution set
        c. remove all all sets incompatible with _i_ from set_of_intervals including _i_
      2. return the solution set
```

The second version has to sort the set of intervals before the solution set is built up. This version also loops over the entire
set of intervals only once, and instead of removing incompatible intervals it finds more compatible ones as it traverses.

```python

    1. Sort set_of_intervals in order of finishing time.
    2. i = 0, n = len(set_of_intervals)
    3. f := − 1
    4. while i <= n:
        a. if set_of_intervals[i]'s finish time is greater than or equal to f:
            1. append the interval to the solution set
            2. f = the intervals finish time
        b. i = i + 1
    5. return the solution set

```

### Analysis
[Analyze the algorithm, here's where things such as complexity can be discussed]

## Conclusion
[Any final thoughts here, maybe discuss other ways to solve the problem that would be equally efficient]
