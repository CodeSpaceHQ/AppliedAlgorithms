# Nikita And The Game
This problem comes from [HackerRank](https://www.hackerrank.com/challenges/array-splitting)  
Category: Dynamic Programming  
Difficulty: Medium  

## Problem


### Overview
This was problem of medium difficulty. There are multiple ways to solve this problem and on top of that there are a couple tricks one can implemented that, in certain scenarios, the solution can be determined early on, allowing for a quick end to the program.

After reading the problem statement including input, output and examples, these are my initial impressions:
- It's important to note that the array can only be partitioned. As opposed to reordered. That actually simplifies things greatly.
- How should we handle an array consisting of all zeros?

## Algorithm
### Overview
If we have to partition an array into sub arrays with equal size then we can deduce this formula:
- Let the sum of the values of the sub arrays equal x. Then the sum of values of the full array must equal 2x.
- From this we can see that the sum of values of an array must even if we are to partition it evenly.
- While the sum of the values of an array must be even, the size of the array does not need to be.
- Is there more than 1 way an array can be partitioned into two sub arrays of equal sum values? (The answer is no, and that’s good to know. This means that once we find a way to partition an array correctly, we don't have to keep checking that array.)

### Terminology
**Main Array**: An array from which two sub-arrays are partitioned from  
**SumVal**: The sum of the values of an array  
**Goal**: The value we want to reach with our sub array
### Pseudo Code
For each test case:  

#### Stage 1
1. Read in size of array (Keep track of **SumVal** of initial array)
- If **SumVal** equals 0 then the solution is the size of the array minus 1  
- If **SumVal** is an odd number then the solution is 0  
- Else let **Main Array** equal the initial array and **Goal** equal the **SumVal** of the initial array divided by 2  

#### Stage 2
With **Main Array** and **Goal**  
1. If **Main Array**'s size is less than 1 or **Goal** equals 0 then return 0  
- Iterate through **Main Array**  from left to right adding the values at that point to **SumVal** and each time check:  
  1. If **SumVal** > **Goal** we cannot split **Main Array**, return 0  
  - If **SumVal** == **Goal** we can split **Main Array**  
    1. Call this stage again  with **Main Array** = the sub part of the **Main Array** already iterated through and **Goal** = **Goal**/2 and return 1 + result  
    - Call this stage again with **Main Array** = the sub part of the **Main Array** not yet iterated through and **Goal** = **Goal**/2 and return 1 + result  
    - If **SumVal** < **Goal** continue  

### Analysis
By looking at the source code, we can see the only looping that happens per test case is:
```CPP
  for (int seq_index = 0; seq_index < seq_size; seq_index++) {
    //... The bulk of the code here
  }
```
from this we can conclude that the complexity of this algorithm is _O(N)_
## Conclusion
This solution passes the problem tests with the worst being Test Case 10 at 0.00s time.
