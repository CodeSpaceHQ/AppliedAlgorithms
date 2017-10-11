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

- _OPT(j)_ will denote the minimum cost for points _p<sub>1</sub>,p<sub>2</sub>,...,p<sub>j</sub>.
- _e(i,j)_ will denote the minimum sum of squared errors for points _p<sub>i</sub>,p<sub>i+1</sub>,...,p<sub>j</sub>_

To compute _OPT(j)_ we will use the formula:

![OPT(j)](./assets/opt_j.png)

Where _OPT(i-1)_ is the cost of the previous minimum costing segment for some points, _c_ is the cost of adding a new segment,
and _e(i,j)_ is the sum of squared errors for a segment running though points  _p<sub>i</sub>,...,p<sub>j</sub>_

1. Sort _S_ by x coordinates.
2. Compute _e(i,j)_ for every possible segment in _S_.
3. Go through each segment and find _OPT(j)_, storing the value in an array _m_ at index _j_
4. Since _m_ keeps track of the accumulating costs of the minimum costing segments included in the optimal solution, the cost of the optimal solution will be in the last element of _m_.


### Pseudo Code

This pseudo code follows the above algorithm and returns the cost of the optimal solution. It should be noted that in the
actual implementation there are a few more simple parts required so that the optimal solution can be graphed as well.

````Python

    def segmented_least_squares(points, c):

        points = sort_points(points)  # sort by x values
        n = len(points)

        for j = 1 to n:  # for each point
            for i = 1 to j:   # for each point up to j
                compute the least squares error e(i,j) for the segment pi, pi+1,...,pj

        m[0] = 0  # initialize array with 0 cost
        for j = 1 to n:
            for i = 1 to j:
                m[j] = min(e(i,j) + c + m[i-1])  # m[j] is the minimum costing segment for the points pi to pj

        return m[n]
````

## Analysis

The segmented least squares algorithm has a time complexity of O(n<sup>3</sup>):
- O(n<sup>3</sup>) for finding all _e(i,j)_ values + O(n<sup>2</sup>) for finding all _OPT(j)_ values.
and a space complexity of O(n<sup>2</sup>).

This time complexity can be improved to O(n<sup>2</sup>) time and O(n) space by pre-computing
various statistics.

## Example

For our example we will be using a series of 9 points given in input format:

`[[3, 3], [2, 2], [1, 1], [4, 3], [5, 3], [6, 3], [9, 6], [7, 4], [8, 5]]`

Which plotted on a graph looks like:

![Input Plotted](./assets/initial_plot.png)

As you can imagine, the desired number of segments _L_ would be 3, provided the given input _c_ allowed for that.

*Step 1: sort the input*

Using quick sort, our resulting points look like:

`[[1, 1], [2, 2], [3, 3], [4, 3], [5, 3], [6, 3], [7, 4], [8, 5], [9, 6]]`

*Step 2: computing _e(i,j)_*

We can now go through each possible segment and compute _e(i,j)_ -- the sum of least squared error.
This computation is rather lengthy so it will not be traced over here. The implementation of this computation can be found in
the solution file under the function `compute_err`.

To compute all _e(i,j)_ values, we have a pointer _j_ pointing to the end of a segment, and a pointer _i_ pointing to the beginning of a segment.
_j_ is moved back every time _i_ reaches it, causing a loop through of all possible segments in _S_.

The resulting dictionary holding all _e(i,j)_ values looks like this:
```
{(1, 2): 0.0, (5, 6): 0.0, (1, 3): 0.16666666666666669, (4, 8): 0.4000000000000007, (4, 5): 0.0, (2, 8): 1.8571428571428572, (1, 7): 1.107142857142857, (2, 7): 1.0857142857142859, (1, 4): 0.3000000000000001, (6, 7): 0.0, (2, 6): 0.3999999999999998, (1, 6): 0.5714285714285712, (0, 7): 1.4047619047619049, (6, 8): 0.0,
(3, 7): 0.7000000000000001, (2, 5): 0.0, (0, 8): 1.9833333333333336, (0, 3): 0.30000000000000016, (5, 8): 0.0, (3, 5): 0.0, (0, 1): 0.0, (0, 5): 1.0857142857142859, (4, 6): 0.16666666666666669, (4, 7): 0.29999999999999954, (1, 5): 0.4, (7, 8): 0.0, (5, 7): 0.0, (0, 2): 0.0,
(3, 8): 1.0857142857142863, (0, 6): 1.1071428571428572, (1, 8): 1.869047619047619, (3, 6): 0.2999999999999998, (0, 4): 0.7000000000000001, (2, 3): 0.0, (3, 4): 0.0, (2, 4): 0.0}`
```

*Step 3: compute _OPT(j)_*


## Conclusion


