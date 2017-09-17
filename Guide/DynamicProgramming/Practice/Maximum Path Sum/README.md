# Maximum Path Sum
 This problem comes from [HackerRank](https://www.hackerrank.com/contests/projecteuler/challenges/euler018) and is categorized as a Dynamic Programming Problem

##### Tags
[Dynaimc Programming](https://en.wikipedia.org/wiki/Dynamic_programming) / [Array Construction](https://en.wikipedia.org/wiki/Array_data_structure)

## Problem
### Statement

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is: <br /> 
<br />
The path is denoted by numbers in bold. 
<br /><br />
&nbsp;&nbsp;&nbsp; **3** <br />
&nbsp;&nbsp;  **7** 4 <br/>
&nbsp; 2 **4** 6 <br/>
 8 5 **9** 3
 
That is, 3 + 7 + 4 + 9 = 23
Find the maximum total from top to bottom of the triangle given in input.

#### Input Format

The first line contains _**T**_, the number of testcases, For each testcase:
The first line contains _**N**_, the number of rows in the triangle.
For the next _**N**_ lines, the _**i**_'th line contains _**i**_ numbers.

### Overview
This problem is relatively straightforward. Starting from the top (or bottom), find the maximum path to the opposite side.

1. Store the values in a 2d array
2. Loop through the 2d array again, calculating the sums at each level
3. Scan the bottom level and print the maximum value

## Algorithm

### Overview

The Algorithm for this problem is quite nice.  All that is necessary is a 2d array.
I initally set the size to the maximum possible size the problem describes.

I then loop through the 2d Array storing the values, using variables j and k where
_0 <= j < n_  (where n is the number of rows in the triangle) and
_0 <= k <= j_

using the example from above this will appear like this:

3 <br />
7 4 <br />
2 4 6 <br />
8 5 9 3 <br />

Once the original triangle from the problem is constructed, We must loop through again and find the sums at each
level. In order to do this we use the same looping format as shown above. At each level we'll want to change the current value
to the maximum of the current value plus the value above it to the left, or the value above it to the right.  We repeat this
for every row, building the sums at each level as we go down.  In this portion you must be wary of the edge cases.
(when k = 0 or k = j).  In this circumstance you must set the left or right side to 0 in order to avoid an array out of
bounds error.

Again using the example, the folloing will be the result of compiling the sums.

3 <br />
10 7 <br />
12 14 13 <br />
20 19 23 16 <br />

Lastly, all that is needed is to look through the bottom row and find the maximum value. Which in this case is 23.

### Pseudo Code
1. Create 2d Array of size max size
2. Read in and fill array with the triangle given in the problem
3. Rescan through triangle computing the sum of the current value based on whats is above it to the left and right.
4. Scan through the bottom row to find the maximum value (this step can be cut out by keeping track during the additions)

### Analysis

Within the code the bottlenecks only show up when running through the 2d Array.  But as you can see, the way the 2d array
is set up, each item in the array is only being looked at once.  So each scan through the 2d array is of length N.  Since we 
do this scan twice (once to read in the values, another to calculate the sums), the Big-O notation is O(2N) -> O(N).

## Conclusion

If you're just beginning to learn dynamic programming problems, this is a great place to start.  The solution to this problem
is easy to visualize, and you can see how building upon sub-problems leads to a reletively elegant solution to a somewhat challenging problem.

