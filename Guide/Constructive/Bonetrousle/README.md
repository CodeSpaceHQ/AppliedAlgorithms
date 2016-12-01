# Bonetrousle
[https://www.hackerrank.com/challenges/bonetrousle](https://www.hackerrank.com/challenges/bonetrousle)

Nothing

Medium


## Problem
### Statement
Once upon a time, Papyrus the skeleton went to buy some pasta from the store. The store's inventory is bare-bones and they only sell one thing — boxes of uncooked spaghetti! The store always stocks exactly k boxes of pasta, and each box is numbered sequentially from 1 to k. This box number also corresponds to the number of sticks of spaghetti in the box, meaning the first box contains 1 stick, the second box contains 2 sticks, the third box contains 3 sticks, …, and the k<sup>th</sup> box contains k sticks. Because they only stock one box of each kind, the store has a tendon-cy to sell out of spaghetti.

During each trip to the store, Papyrus likes to buy exactly n sticks of spaghetti by purchasing exactly b boxes (no more, no less). Not sure which boxes to purchase, Papyrus calls Sherlock Bones for help but he's also stumped! Do you have the guts to solve this puzzle?

Given the values of n, k, and b for t trips to the store, determine which boxes Papyrus must purchase during each trip. For each trip, print a single line of b distinct space-separated integers denoting the box number for each box of spaghetti Papyrus purchases (recall that the store only has one box of each kind). If it's not possible to buy n sticks of spaghetti by purchasing  boxes, print -1 instead.

###Input Format

The first line contains a single integer, t, denoting the number of trips to the store.
Each of the t subsequent lines describes a trip to the store in the form of three space-separated integers describing the respective values of n (the number of sticks to buy), k (the number of boxes the store has for sale), and b (the number of boxes to buy) for that trip to the store.

###Constraints

* 1 <= t <= 20

* 1 <= b <= 10<sup>5</sup>

* 1 <= n <= 10<sup>18</sup>

* 1 <= k <= 10<sup>18</sup>

* b <= k

###Output Format

For each trip to the store:

* If there is no solution, print -1 on a new line.

* Otherwise, print a single line of  distinct space-separated integers where each integer denotes the box number (i.e., the number of spaghetti sticks in the box) that Papyrus must purchase.

If there are multiple possible solutions, you can print any one of them. Do not print any leading or trailing spaces.

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
It is important to keep in mind that for this problem some variable values could exceed
the value of an int in Java. Also, System.out.println(), may be too slow for big inputs.
Instead, use OutputStream.
</p>