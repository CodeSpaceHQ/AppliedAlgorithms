# Journey to the Moon
This problem comes from [HackerRank](https://www.hackerrank.com/challenges/journey-to-the-moon)

Category: Graph Theory

Difficulty: Medium

## Problem

### Overview
Given 'N' objects numbered from 0 to 'N' - 1 and 'I' pairs taken from those 'N' objects.
- Determine which of the objects are grouped together.
    - A grouping is formed through pairs.
    - For example, if 1, 2, and 3 are objects and there are two pairs (1,2) and (2,3), then all three objects are in the same group even though 1 and 3 aren't directly connected.
- Compute the number of ways that a pair of objects from different groups can be picked.

### Input Format
- The first line contains two integers 'N' and 'I' separated by a space.
- The next 'I' lines contain two integers 'A' and 'B' (in this order) each separated by a space.
    - 'A' and 'B' are both objects that are paired.

### Constraints
- 1 <= N <= 10^5
- 1 <= I <= 10^4

### Output Format
- A single line with the computed value.

## Algorithm

### Overview
The core of this solution is the adjacency list that holds pair data.
Given this input:

5 2

0 2

1 2

The adjacency list should look like this:

|  0  |  1  |  2  |  3  |  4  |
| --- | --- | --- | --- | --- |
|  2  |  2  |  0  |  _  |  _  |
|  _  |  _  |  1  |  _  |  _  |

In order to solve this problem, one must first figure out which objects are in a group together and how large the groups are.
The size of the groups is vital, because this problem ultimately boils down to combinations, which can be determined through the multiplication of different group sizes.
For instance, in the above example there are three groups with sizes 3, 1, and 1 respectively.
Order doesn’t matter, so the method for determining the number of ways there are to pick pairs is as follows:

3 * (1 + 1) + 1 * (1) = 7

Or more generally:

Group 1 * (Group 2 + Group 3) + Group 2 * (Group 1)

There are three requirements for determining the size of a given group.
- A counter to store the size.
- A hash map to keep track of which objects have already been accounted for.
- A stack to keep track of which object entries in the adjacency list still need to be visited.

In order to prevent an infinite loop, values must be removed from the adjacency list after they are operated on.
But this creates an issue in that groups with only a single object in them appear to be empty according to the adjacency list.
So before doing operations on the adjacency list, one must first iterate through it and create a new group of size one for every empty entry.

### Pseudo Code
Given an adjacency list 'pairs' implemented using a 2D vector, a vector 'countries' that will contain object group sizes, a variable 'numAsts' that contains the number of objects, and a variable 'result' that stores the number of ways a pair can be chosen.
- The first dimension of 'pairs' contains an entry corresponding to each of the N objects.
- The second dimension of 'pairs' contains all objects that the given object is paired with.
- For each entry in 'pairs' that is empty, push a value of 1 to 'countries.'
- For each entry in 'pairs.'
    - If the entry is not empty.
        - Set the counter 'countryAsts' to 0.
        - Create a hashMap 'tempMap.'
        - Create a vector 'targetAsts.'
        - Add the current entry to 'targetAsts.'
        - Add the current entry to 'tempMap.'
        - Add 1 to 'countryAsts.'
        - While 'targetAsts' isn't empty.
            - Pop the last element of 'targetAsts' into 'current.'
            - While the entry corresponding to 'current' isn't empty.
                - Pop the last element of the entry corresponding to 'current' into 'tempAst.'
                - If 'tempAst' isn't in 'tempMap.'
                    - Add 'tempAst' to 'targetAsts.'
                    - Add 'tempAsp' to 'tempMap.'
                    - Increment 'countryAsts' by 1.
        - Add 'countryAsts' to 'countries.'
- For each element in 'countries.'
    - Subtract the current element from 'numAsts.'
    - Add the product of 'numAsts' and the current element.

### Analysis
This algorithm runs in linear time.
There are two simple loops that contain only constant time operations, the loop that searches for single object groups and the loop that calculates 'result.'
While the portion of the algorithm that calculates group sizes does feature a loop containing nested loops, it visits each value in 'pairs' a constant number of times.
Given that 'pairs' contains 'I' * 2 values, it can be considered a linear time operation.

## Conclusion
This problem is particularly good at highlighting the importance of not focusing on the most obvious parts of a solution.
For instance, the last step is calculating the number of possible unique pairs, an operation that can be accomplished with four lines of code.
Because of its simplicity, it is easy to code the last step without thinking about the correct method to use.
Given a list of group sizes, the naive method involves adding the product of a given element and all other elements until the end of the list, for each element in the list.
This results in an O(G^2) operation, where G is the number of groups.
This is far inferior to the method shown in this solution, which is an O(G) operation.
