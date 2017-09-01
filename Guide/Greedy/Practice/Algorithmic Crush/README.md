# Algorithmic Crush
This problem comes from [HackerRank](https://www.hackerrank.com/challenges/crush)

Category: Greedy Algorithms

Difficulty: Hard

## Problem

### Overview
- Given a list of size N with elements initialized to zero
- Perform M operations with parameters a (start), b (end), and k (value)
    - Each operation adds the value of k to each element from position a (index a-1) to position b inclusively
- Return the value of the element in the list with the greatest final value

### Input Format
- The first line contains two integers N and M separated by a space
- The list will be of size N
- The next M lines contain three integers a, b, and k (in this order) each separated by a space

### Constraints
- 3 <= N <= 10^7
- 1 <= M <= 2 * 10^5
- 1 <= a <= b <= N
- 0 <= k <= 10^9

### Output Format
- A single line with the returned value

## Algorithm

### Overview
The main realization that helps reduce the complexity of the problem is that one doesn’t need to worry about when a specific operation begins or ends.

For example, one could have this input:

5 2

1 3 100

3 5 100

This would result in this final list:

100 100 200 100 100

However, this could also be achieved with the input:

5 2

1 5 100

3 3 100

In this case, the only facts one needs to take into account are as follows:
- An operation starts adding 100 at element 1
- An operation starts adding 100 at element 3
- An operation stops adding 100 after element 3
- An operation stops adding 100 after element 5

### Pseudo Code
Given an array of size 'N' + 1 and two integers 'current' and 'max' initialized to 0
- For each of the elements in the array
    - Set the value of the element to 0
- For each of the 'M' operations
    - Add the value of 'k' to the element in the (a - 1)th index
    - Subtract the value of 'k' from the element in the (b)th index
- For each of the elements in the array
    - Add the value of the element to 'current'
    - If the value of 'current' is greater than 'max'
        - Set 'max' to the value of 'current'

### Analysis
All of the loops in the algorithm iterate either over the 'N' + 1 elements in the array or the 'M' operations provided by input.
None of the inner loops contain operations with complexity greater than constant time.
As a result, the algorithm can be classified as O(N).

## Conclusion
This problem is particularly good at highlighting the usefulness of eliminating repeated operations.
Without optimization the solution can be costly.
For instance, the naive method to solve this problem involves adding the value of ‘k’ to each element in the list from ‘a’ to ‘b’ inclusively for each of the ‘M’ operations.
The worst case would be if ‘a’ is 1 and ‘b’ is ‘N’ for each of the ‘M’ operations, making this algorithm an O(N*M) operation.
However, there are fairly obvious places where optimization can happen, as shown in this solution.

Additionally, the solution is quite simple, so one doesn't get sidetracked with the minutiae of implementation.
