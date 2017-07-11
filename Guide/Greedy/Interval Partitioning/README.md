# Interval Partitioning

This problem is introduced in [Dr. Gelfond Applied Algorithms](http://redwood.cs.ttu.edu/~mgelfond/FALL-2012/slides.pdf).

Category: Greedy

Difficulty: N/A


## Problem

Given a set _J = {i<sub>1</sub> . . . , i<sub>n</sub>}_ of jobs where each request _i_ is
associated with an interval _[s(i), f(i)_] and each request requires one
of many available resources in _R_, schedule all jobs using as few resources as possible.

### Overview

Examples of this problem would be: scheduling classes using as few classrooms as possible (here, classrooms are the resources), or
allocating printing jobs using as few printers as possible (the printers are the resources), etc.

So we have a set of resources and a set of jobs that have a start time _s(i)_ and a finish time _f(i)_, and we need to complete all of
these jobs while using as few resources as possible. If I have a request that starts at 12:00PM and finishes at 2:00PM, and another that
starts at 3:00PM and finishes at 4:00PM, I will only have to use one resource because the two jobs do not overlap. However, if the second request were
to start at 1:30PM, I would then need to use two resources because the two jobs overlap.

Likewise, if we have a set of jobs:

    J = [ (12PM, 3PM), (2PM, 5PM), (4PM, 6PM) ],

we would then need to use at least 3 resources because all three jobs overlap.
From this can draw the conclusion that the amount of resources we need will be equal to the amount of jobs in _J_ that overlap.

## Algorithm
### Overview

Since each request will have a definitive start time and finish time, it makes sense that we schedule the jobs that start the earliest
first. As we move from request to request in increasing order of start time, we can use resources that are free but that have already been used by
previous jobs, and if none are available we will have to use another available resource from _R_. This will split our resources up into three categories:
ones that are in use (occupied), ones that have been used but are now free (released), and ones that have not been used and are free (R). If possible
we would like to select our resource from released.

### Pseudo Code

```Python

    def interval_partitioning(set J: jobs, set R: resources):
        released = 0
        occupied = 0
        m = resource
        1. Sort J by starting time
        2. For every j in J:
            a. move all resources in occupied that finished before the start of j into released
            b. if released is not empty:
                i. m = get resource from released
            c. else
                i. m = next resource in R
            d. move m into occupied
            e. put j into m????



```



### Analysis
[Analyze the algorithm, here's where things such as complexity can be discussed]

## Conclusion
[Any final thoughts here, maybe discuss other ways to solve the problem that would be equally efficient]
