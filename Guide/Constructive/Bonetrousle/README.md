# Bonetrousle
[https://www.hackerrank.com/challenges/bonetrousle](https://www.hackerrank.com/challenges/bonetrousle)

Category: Constructive

Difficulty: Medium


## Problem

### Overview

####Given:
* The number of boxes to buy, b.
* The number of noodles to buy, n.
* The set of boxes available to buy {1, 2, ..., k}

####Goal:
* Pick a subset, S, of the boxes available to buy which:
    * has a size equal to b.
    * the values of the boxes in S equals n.

## Algorithm

### Overview
<p>
For this problem you may have come up with a formula similar to e + (e + 1) + ... + (e + t - 1) = n.
Where e is the number of noodles in the first box picked. However this equation by itself will not work.
For example if you had the boxes 1, 2, 3, and 4 and you needed 6 noodles, no two consecutive boxes
will give you six, but if you pick boxes 2 and 4 you will get 6 noodles. This algorithm modifies the
formula above so that it does work. Note that the problem says that any combination of boxes that produces
the needed number of noodles is a valid solution.
</p>

<p>
It is important to keep in mind that for this problem some variable values could exceed
the value of an int in Java. Also, System.out.println(), may be too slow for big inputs.
Instead, use OutputStream.
</p>

### Pseudo Code
1. Read in n, k, and b.
2. Make a variable called numConstants, a variable called amountShort, and a variable called e.
3. numConstants = (b/2) * (b-1)
4. amountShort = (n - numConstants) % b
5. e = (n - numConstants) / b
6. if e < 1 or (amountShort == 0 and e+b-1 > k) or (amountShort != 0 and e+b > k):
    1. print("-1")
7. else:
    1. Make a variable called boxToSkip and a variable called lastNumPrinted.
    2. boxToSkip = b - amountShort
    3. lastNumPrinted = e
    4. for i = 1 to b:
        1. if i == boxToSkip:
            1. lastNumPrinted = lastNumPrinted + 2
        2. else:
            1. lastNumPrinted = lastNumPrinted + 1
        3. print(" " + lastNumPrinted)

Note that the actual problem asks you to do this algorithm for t test cases.

### Analysis
<p>
Since this algorithm uses mainly math, the largest part of the code is the loop that prints
the list of boxes out. This loop goes b times and thusly the algorithm's time complexity is O(b).
</p>

## Conclusion
<p>
As computer science is closely related to math, some problems can be easily solved 
using math to create a formula. This problem is a great example of this. Without the formula stated
above, this problem would have been much more difficult. When starting to solve a programming
problem, it is always best to see if there is a formula that can be derived quickly 
that will accurately produce a solution. 
</p>