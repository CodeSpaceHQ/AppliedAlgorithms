# Abbreviation

## Problem
This problem comes from [HackerRank](https://www.hackerrank.com/contests/world-codesprint-6/challenges/abbr).
Category: Dynamic Programming
Difficulty: Medium

### Overview
Read the link instructions,
they are helpful when solving
greater than eye deep

Edge cases and complexities are covered below. Please read the problem first.

## Algorithm
### Overview
This problem is complex because of the edge cases that exist. Some
solutions don't need to worry about them, however when trying to maximize
efficiency it becomes a problem. When I approached the problem I tried to
use a double pointer method, iterating through both strings at the same time.

The following example will show why this problem is tough to get right
the first time, or second.

It looks like this (credit to Orion for the edge case),
- A = abcBBcA and B = ABBCA
  - p1 (pointer one) = a | p2 (pointer two) = A
    - a can be turned into A, so B is possible so far.
  - p1 = b | p2 = B
    - Another match
  - p1 = c | p2 = B
    - Move p1 forward (since c can be ignored and deleted).
  - p1 = B | p2 = B
    - Both are uppercase and they match, so move both pointers forward.
  - p1 = B | p2 = C
    - Oops! This situation causes a return of "NO", even though it should
    print "YES". The problem is that the lowercase 'b' "uses" a slot that
    should be used by the uppercase 'B'. Because lowercase characters can
    be deleted but uppercase cannot, **every uppercase character must be
    used by the algorithm.**

So what's the solution? Well, either you can backtrack whenever you reach
an uppercase character that could have been used up by a lowercase
character previously. Or, you can create a kind of "memory" for the
algorithm. A memory would need the following,
- A unique ID for combinations of lowercase characters.
- A way for uppercase characters to check if they could replace those
lowercase characters that had been previously used.

It should be possible to create a nearly unique ID for any combination of
lowercase characters. By having a counter that increases as new
characters are added to memory, and multiplying the numeric value
of new characters by it as part of the hash, it will help guarantee a
nearly unique ID for each sequence. Like the following example,
- abc compared to bca where counter starts at one.
  - a*counter + b*(counter+1) + c*(counter+2) = 1*1 + 2*2 + 3*3 = 14
  - b*counter + c*(counter+1) + a*(counter+2) = 2*1 + 3*2 + 1*3 = 11

This memory will be stored in an array, like a hash map. By adding
in a modulus operator and by using a prime number for the
modulus, we help guarantee that few IDs will conflict. The prime
number will also match the size of the array used to store the
memory.

In using this memory we make it possible to get an O(M + N)
time complexity for this problem, since there is no need
to backtrack.

Assumption: Although lowercase letters may be turned uppercase,
every lowercase character remaining must be deleted. This is not
explicitly stated in the problem, but it is an assumption I am
using.

### Pseudo Code
1. Read in the number of string pairs or "queries" as they are called.
2. Read in the next pair of strings. Create index pointers and set to 0.
3. If the char at p1 can match the char p2,
  - If the char at p1 is lowercase, add it to memory.
  - Else, if it can be replaced by a char in memory, do so,
  otherwise clear the memory.
  - If the char at the first pointer was lowercase or memory was cleared,
  advance both p1 and p2.
4. Else if both characters are uppercase and don't match, check if
the memory has a char that took the place of the char at p1.
  - Continue until the char at p1 is no longer uppercase or
  it has reached the end of the string. Advance p1 after each iteration.
5. If both p1 and p2 are less than the length of their respective strings,
continue at step 3.
6. If p2 does not equal the length of the final string, print "NO".
7. If the p1 does not equal the length of the original string,
  - Scan through the rest of the original string and check if any
  remaining uppercase chars need to (and can be) replaced by
  memory. If any cannot be replaced, then print "NO".
8. If the algorithm has not printed "NO" for the query, print "YES".
9. Start at step 2 if queries remain. Otherwise finish.

### Analysis
For each query the loop iterates a maximum number of O(M + N) times
where M is the length of the original string and N is the length of the
final string. The hash set has O(1) access, insert, and retrieval and
it does not change in size.

This algorithm wil run in O(M + N) time. The max runtime was .22s for
Test Case #10.

## Conclusion
This is a good problem to practice dynamic programming on. Although my
solution wasn't exactly dynamic programming, it's possible to create a
recursive solution and make it faster by using memoization. Other
things to consider are,
- It would be interesting to see how different solutions match up as the
test cases get much larger in size. My solution is slower than DP solutions
at test case sizes of the ones we used.
- Is there a neat way to distribute this problem across many machines
in chunks of the string?
