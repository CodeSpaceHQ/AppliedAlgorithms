# Shortest Path Tree in a Graph

This problem is introduced in [Dr. Gelfond Applied Algorithms](http://redwood.cs.ttu.edu/~mgelfond/FALL-2012/slides.pdf) and is further discussed by [Princeton](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/06DynamicProgrammingI.pdf) as well as other universities.

Category: Dynamic Programming

Difficulty: Hard

## Problem

Given _n_ points in the plane: _(x<sub>1</sub>, y<sub>1</sub>),  (x<sub>2</sub>, y<sub>2</sub>),..., (x<sub>n</sub>, y<sub>n</sub>)_.
Find *a sequence of lines* that minimizes _f(x) = E + cL_ where:
- _E_ is the sum of the sum of squared errors for each segment
- _L_ is the number of segments in the solution
- _c_ > 0 is a given constant


### Overview

To understand the problem of _Segmented least squares_ we must first understand the problem of _Least Squares_.
The notes over these two problems are taken from Princeton's lecture slides on them found above.

#### Least Squares

Given _n_ points in the plane: _(x<sub>1</sub>, y<sub>1</sub>),  (x<sub>2</sub>, y<sub>2</sub>),..., (x<sub>n</sub>, y<sub>n</sub>)_.
Find *a line* _y = ax + b_ that minimizes the sum of the squared error given by the equation:

![Sum of squared errors formula](./assets/sse.png)

The SSE formula is minimized when the slope _a_ of the line and the y-intercept _b_ are found using:

![slope and intercept formulas for minimizing sum of the squared errors](./assets/a_and_b.png)

A Least Squares solution would look like this:

![Least squares solution example](./assets/least_squares/sol.png)

The red line from the point to the solution line is the error value for that point. The solution line minimizes the sum of all
of the error values for each point.

#### Segmented Least Squares

Given _n_ points in the plane: _(x<sub>1</sub>, y<sub>1</sub>),  (x<sub>2</sub>, y<sub>2</sub>),..., (x<sub>n</sub>, y<sub>n</sub>)_.
Find *a sequence of lines* that minimizes _f(x) = E + cL_ where:
- _E_ is the sum of the sum of squared errors for each segment
- _L_ is the number of segments in the solution
- _c_ > 0 is a given constant

The difference is is that here we are trying to find multiple "lines" or "segments" that
will minimize the sum of squared errors while also trying to balance how many segments we have (using the given _c_).

A Segmented least squares solution could look like this:

![Segmented least squares solution 1](./assets/seg_least_squares_sol1.png)

Another solution if the given _c_ value was really low could be:

![Segmented least squares solution 2](./assets/seg_least_squares_sol2.png)

As you can see, _c_ will control how many lines v.s. how accurate the fit is.

### Input Format

1. A list of points in _S_ where each point is in the format `[x, y]`. An example input would look like:

```Python
    [[10, 9], [3, 4], [5, 6]]
```
2. A constant _c_ which is the cost of adding a new segment to the optimal solution.

### Output Format

- the total "cost" of the optimal solution (i.e. the sum of the costs of the segments), and
- a visual graph depicting the points in _S_ and the segments in the optimal solution.


## Algorithm
### Overview

### Pseudo Code



## Analysis


## Example

## Conclusion


