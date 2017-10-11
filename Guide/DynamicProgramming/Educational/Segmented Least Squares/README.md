# Shortest Path Tree in a Graph

This problem is introduced in [Dr. Gelfond Applied Algorithms](http://redwood.cs.ttu.edu/~mgelfond/FALL-2012/slides.pdf) and is further discussed by [Princeton](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/06DynamicProgrammingI.pdf) as well as other universities.

Category: Dynamic Programming

Difficulty: Hard

## Problem

To understand the problem of _Segmented least squares_ we must first understand the problem of _Least Squares_.

#### Least Squares

Given _n_ points in the plane: _(x<sub>1</sub>, y<sub>1</sub>),  (x<sub>2</sub>, y<sub>2</sub>),..., (x<sub>n</sub>, y<sub>n</sub>)_.
Find *a line* _y = ax + b_ that minimizes the sum of the squared error given by the equation:

![Sum of squared errors formula](./assets/sse.png)

The SSE formula is minimized when the slope _a_ of the line and the y-intercept _b_ are found using:

![slope and intercept formulas for minimizing sum of the squared errors](./assets/a_and_b.png)

A Least Squares solution would look like this (from Princeton University lecture slides):

![Least squares solution example](./assets/least_squares/sol.png)

The red line from the point to the solution line is the error value for that point. The solution line minimizes the sum of all
of the error values for each point.


#### Segmented Least Squares

### Overview

### Input Format

1. A list of points in _S_ where each point is in the format `[x, y]`. An example input would look like:

```Python
    [[10, 9], [3, 4], [5, 6]]
```
2. A constant _C_ which is the cost of adding a new segment.

### Output Format

## Algorithm
### Overview

### Pseudo Code



## Analysis


## Example

## Conclusion


