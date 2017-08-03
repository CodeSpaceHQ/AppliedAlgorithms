# Minimize Maximum Lateness Scheduling

This problem is discussed in [Dr. Gelfond Applied Algorithms](http://redwood.cs.ttu.edu/~mgelfond/FALL-2012/slides.pdf)


Category: Greedy

Difficulty: N/A

## Problem
### Overview
Given a set _R_ of requests where each request _i_ has a duration _t<sub>i</sub>_ and a deadline
_d<sub>i</sub>_, and a single unlimited resource, schedule each request _i_ into an interval with
a start time _s(i)_ and a finish time _f(i)_ i.e. _[s(i), f(i))_ with length _t<sub>i</sub>_ such
that each interval is disjoint.

A request _i_ is late if _f(i) > d<sub>i</sub>_. A requests lateness _L<sub>i</sub>_ is calculated by
_f(i) - d<sub>i</sub>_ if _i_ is late and 0 otherwise.

Find a schedule of all requests which:
- Starts at a given point _s_ and,
- Minimizes maximum lateness, L = max<sub>i</sub>(L<sub>i</sub>)


### Input Format
- The set R of requests, each having a duration and a deadline in the form of _(t<sub>i</sub>, d<sub>i</sub>)_.
### Constraints


### Output Format
- A list of the requests with their start time and finish time in the form _(s<sub>i</sub>, f<sub>i</sub>)_

## Algorithm
### Overview
To minimize the lateness that the jobs run, it makes sense to schedule the ones with the earliest deadlines first.

### Pseudo Code

```Python
    def min_max_lateness(R: set of requests):
        1. Sort request by their deadline (earliest first)
        2. f = 0 # initialize 'Finish' to 0
        3. For every request i in R:
            a. start of i = f
            b. finish of i = start of i + time i requires to finish
            c. f = f + time i requires to finish
        4. Return [s(i), f(i)] for every i
```

### Analysis
This algorithm is much like interval scheduling and interval partitioning. The time complexity is largely influenced by that of the
sorting algorithm used. In this case we will use quick sort, which has an average time complexity of O(nlogn), and a worst case of O(n<sup>2</sup>).
This will give our scheduling an average time complexity of O(nlogn).


### Example


## Conclusion

