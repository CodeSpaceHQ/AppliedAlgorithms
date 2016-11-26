# New Year Chaos




## Problem
This problem comes from [HackerRank](https://www.hackerrank.com/challenges/new-year-chaos).  
Category: Constructive Algorithm  
Difficulty: Medium

### Overview
Here is a breakdown of what the problem is really asking.

1. Suppose there is an ordered list of N elements numbered 1 to N.
- An element can swap with the element before it at most 2 twos.
- We are given a list of numbers where each number marks the original position of an element.
- From this list we are to determine whether or not it was possible to get to this state given (1) & (2)
- If it was not possible, output “Too chaotic”, else output the minimum number of swaps it would take to get from (1) to the given list at (3).

## Algorithm
### Overview
The only data structure used in this solution is an array for storing the list.  
For this algorithm, we can assume that the list is possible as we are checking for that while taking in the input.  
If we iterate through the list backwards, swapping elements as we go we will be able to make two assumptions that are needed to solve the problem.  
For element with value _x_ at position _i_ , _1 <= i <=N_:

Assumption 1: Since we are swapping and therefore sorting as we iterate, we can assume that for any element at the current position, all elements with positions greater than the current position are where they are supposed to be and have values greater than the value of element at the current position.

Assumption 2: From the breakdown, we know that _x_ has a lower bound of i+1 and from the previous assumption we know that x has a greater bound of _i_ inclusively. Therefore, if _i_ does not equal _x_, then either _i-1_ or _i-2_ equals _x_

If (while using these assumptions, iterating through the list backwards and swapping elements as we go) we increment a counter by 1 every time _x_ is at _i-1_ and by 2 every time _x_ is at _i-2_, the counter will equal the minimum number of swaps needed by the end of the iteration.

### Pseudo Code
1. Read in values into a list _line_.
- For each value _x = line[i]_ check to see if _x > i+2_. If so, return "Too chaotic" else continue
- Initialize a counter to 0.

We only care about 3 people & 3 positions at a time.  
Suppose it starts as follows:  
Person A at position X  
Person B at position Y  
Person C at position Z  

Then the line looks like this:  
Person : C B A  
Position : Z Y X  

We want the person at position X to be the greatest value. We can assume that anybody behind (to the right) of position X is already where they are supposed to be. AKA every person after position X has a value greater than every person at and before position X.

#### Person A:
First check to see if A is where they should be, if not, we need to find out if A swapped once or twice.    
A is not supposed to be here, since we know they aren’t behind position n, he must have been bribed!  
The question is, who bribed him? B or C? Regardless, we need to increment counter and find out the value of person B.  

If person A isn’t where he is supposed to be, then no matter whether he was bribed by B or C, A needs to be in the middle.  
Now where C & B need to be changes depending on whether it was C or B that did the bribing

#### Person B:
Now we know person A isn’t right spot, we need to see if person B is in the right spot.  
If we stop here, our line will look like this: CAB  
If person B was also not supposed to be here, C must have bribed two people!  
We have already incremented count once, now just increment once more to reflect that it was 2 bribes, not 1.  
Since we know CBA and CAB were not correct, the correct ordering of these three people to make it so the person at position X has the greatest value MUST BE BAC.  
Increment counter;

If person B was the one who bribed person A, all we need to do is finish the swap. (Remember: We already set _line[n - 1] = x_)

Finally, the counter now holds the correct output value.




### Analysis
Within in the source code are two for loops (Ignoring the one for test cases).  
Both of these for loops are linear with size _N_. Therefore the Big-O for this algorithm is _O(N)_.  
Upon submitting this, the solution passes all of HackerRank’s test cases, gaining a score of 40.0.   
The longest test case was Test Case #6 with a runtime of 0.16s.


## Conclusion
Overall this is a good problem to see as there are actually quite a few ways to solve this problem. Several of my fellow students also tried this problem and their best results had a complexity of _n*lg(n)_. This results from the back that they didn’t consider looping backwards through the list.  
So with that my takeaway is this;  
Before committing to a solution imagine your data in a different way.  
What changes when you sort the data first? In ascending or descending?  
What if the data was shuffled?  
Or, like in this case, what if you simply just went through the data backwards?  
