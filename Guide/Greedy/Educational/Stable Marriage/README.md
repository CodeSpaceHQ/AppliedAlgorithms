# Stable Marriage

This problem is introduced in [Dr. Gelfond Applied Algorithms](http://redwood.cs.ttu.edu/~mgelfond/FALL-2012/slides.pdf) and is further discussed in [Stable Marriage Problem Wikipedia](https://en.wikipedia.org/wiki/Stable_marriage_problem)

Category: Greedy

Difficulty: N/A

## Problem

### Overview

Given _n_ men and _n_ women, where each person has ranked all members of the opposite sex in order of preference, marry the men and the women together such that there are no two people of opposite sex who would both rather have each other than their current partners. When there are no such pairs of people, the set of marriages is deemed stable.

From Wikipedia:
>Stable marriage problem (also stable matching problem or SMP) is the problem of finding a stable matching between two equally sized sets of elements given an ordering of preferences for each element. A matching is a mapping from the elements of one set to the elements of the other set. A matching is not stable if:

>- There is an element A of the first matched set which prefers some given element B of the second matched set over the element to which A is already matched, and

>- B also prefers A over the element to which B is already matched.

i.e. a _matching_ is stable when there is no match _(A,B)_ and _(C,D)_  where _A_ prefers _D_ and _D_ prefers _A_ or any other combination where both _A_ and _B_ would be individually better off than they are with the element they are currently matched with.

### Input Format
- The first line is a set of key-value pairs of n men _(k, v)_ where _k_ is an integer greater than zero and _v_ is a list of integers greater than zero of size n.
- The second line is a set of key-value pairs of n women _(k, v)_ where _k_ is an integer greater than zero and _v_ is a list of integers greater than zero of size n.

### Constraints
- Set of men and set of women must be equal in size.
- Each match must be stable.
- Each man must be engaged to a single woman and each woman to a single man.

### Output Format
- n rows of the form _(M, W)_ where _M_ is a male in input 1 who is engaged to woman _W_ in input 2.

## Algorithm
### Overview
We will use the Gale-Shapely algorithm, discovered in 1962 by David Gale and Lloyd Shapely. This algorithm proves that for any equal number of men and women it is always possible to solve the stable marriage problem.  

Find a one-to-one correspondance between the set of men _m_ and women _w_ using the preferences of each man in _m_ and woman in _w_ such that each pairing is considered _stable_.

Each element in each set will have a list of preferences mapping to each element in the other set, i.e. male M<sub>1</sub> in set _m_ will have a list [W<sub>1</sub>, W<sub>5</sub>m...W<sub>N</sub>] of preferred women in _w_ in decreasing order, as well as a status (single, engaged). The initial sets would look something like:

<table>
<tr><th> Set of Men </th><th> Set of Women </th></tr>
<tr><td>

| m  | Preferences  |  
|----|--------------|
| m<sub>1</sub> | [w<sub>2</sub>, w<sub>3</sub>,w<sub>4</sub>,w<sub>1</sub>] |
| m<sub>2</sub> | [w<sub>2</sub>, w<sub>1</sub>,w<sub>3</sub>,w<sub>4</sub>] |
| m<sub>3</sub> | [w<sub>1</sub>, w<sub>3</sub>,w<sub>4</sub>,w<sub>2</sub>] |
| m<sub>4</sub> | [w<sub>1</sub>, w<sub>2</sub>,w<sub>3</sub>,w<sub>4</sub>] | 

</td><td>

| w  | Preferences  |  
|----|--------------|
| w<sub>1</sub> | [m<sub>2</sub>, m<sub>4</sub>,m<sub>1</sub>,m<sub>3</sub>] |
| w<sub>2</sub> | [m<sub>3</sub>, m<sub>1</sub>,m<sub>2</sub>,m<sub>4</sub>] |
| w<sub>3</sub> | [m<sub>1</sub>, m<sub>2</sub>,m<sub>4</sub>,m<sub>3</sub>] |
| w<sub>4</sub> | [m<sub>1</sub>, m<sub>2</sub>,m<sub>4</sub>,m<sub>3</sub>] |

</td></tr>
</table>

Where m<sub>2</sub> prefers w<sub>2</sub> first, w<sub>1</sub> second, and so on. This is the same for the womens set _w_, where  w<sub>3</sub> prefers m<sub>3</sub> first, m<sub>2</sub> second, and so on.

**To solve the stable marriage problem**, we will iterate through the set of males while there exists a free male _m_ who has not yet "proposed" to every woman in set _w_. This _m_ will then propose to his highest ranked woman _w_ who he has not yet proposed to. If _w_ is single, she will accept and the two will become "engaged", otherwise _w_ is already engaged to _m<sub>x</sub>_ and she will only leave her current engagement if she prefers _m_ over _m<sub>x</sub>_.

### Pseudo Code
``` Python
def match(set M: men, set W: women):

    while there exists a single man (m) in M who has not yet proposed to every woman in W:
    
        1. let m propose to highest-ranked woman (w) he has not yet proposed to
        2. if w is free let her accept (m,w) become "engaged"
        3. if w prefers m to her current m1, let her break the engagment
           with m1 and accept m's proposal.
        
    return the set of all engaged pairs
```

## Analysis
The while loop in the stable marriage algorithm goes through each individual male in the set of males at least one time, and at most n times. This leaves the time complexity to be O(n<sup>2</sup>) for the worst case and O(n) for the best case in finding a stable matching of n males and females.

**1<sup>st</sup> iteration**
1. Man = m<sub>1</sub>
2. m<sub>1</sub> proposes to w (w<sub>2</sub>) and she is single, so she accepts

<table>
<td>

| Engagements (M, W) |
|:------------------:|
|(m<sub>1</sub>, w<sub>2</sub>)|

</td>
<td>

![Step 1](assets/step1.PNG "Man 1 proposes to woman 2")

</td>
</table>

----
**2<sup>nd</sup> iteration**
1. Man = m<sub>2</sub>
2. m<sub>2</sub> proposes to w (w<sub>2</sub>) and she is taken...
3. w<sub>2</sub> ranks m<sub>1</sub> higher than m<sub>2</sub>, so m<sub>2</sub> stays single

<table>
<td>

| Engagements (M, W) |
|:------------------:|
|(m<sub>1</sub>, w<sub>2</sub>)|

</td>
<td>

![Step 2](assets/step2.PNG "Man 2 proposes to woman 2")

</td>
</table>

**Note**: We could either move on to m<sub>3</sub>, or we could try m<sub>2</sub> again with his next preffered woman, here we will
do the latter.

----       
**3<sup>rd</sup> iteration**
1. Man = m<sub>2</sub> (again)
2. m<sub>2</sub> proposes to w (w<sub>1</sub>) and she is single, so she accepts

<table>
<td>

| Engagements (M, W) |
|:------------------:|
|(m<sub>1</sub>, w<sub>2</sub>)|
|(m<sub>2</sub>, w<sub>1</sub>)|

</td>
<td>

![Step 3](assets/step3.PNG "Man 2 proposes to woman 1")

</td>
</table>

----
**4<sup>th</sup> iteration**
1. Man = m<sub>3</sub> 
2. m<sub>3</sub> proposes to w (w<sub>1</sub>) and she is taken...
3. w<sub>1</sub> ranks m<sub>2</sub> higher than m<sub>3</sub>, so m<sub>3</sub> stays single

<table>
<td>

| Engagements (M, W) |
|:------------------:|
|(m<sub>1</sub>, w<sub>2</sub>)|
|(m<sub>2</sub>, w<sub>1</sub>)|

</td>
<td>

![Step 4](assets/step4.PNG "Man 3 proposes to woman 1")

</td>
</table>

----
**5<sup>th</sup> iteration**
1. Man = m<sub>3</sub> (again)
2. m<sub>3</sub> proposes to w (w<sub>3</sub>) and she is single, so she accepts

<table>
<td>

| Engagements (M, W) |
|:------------------:|
|(m<sub>1</sub>, w<sub>2</sub>)|
|(m<sub>2</sub>, w<sub>1</sub>)|
|(m<sub>3</sub>, w<sub>3</sub>)|

</td>
<td>

![Step 5](assets/step5.PNG "Man 3 proposes to woman 3")

</td>
</table>

----
**6<sup>th</sup> iteration**
1. Man = m<sub>4</sub>
2. m<sub>4</sub> proposes to w (w<sub>1</sub>) and she is taken...
3. w<sub>1</sub> ranks m<sub>2</sub> higher than m<sub>4</sub>, so m<sub>4</sub> stays single

<table>
<td>

| Engagements (M, W) |
|:------------------:|
|(m<sub>1</sub>, w<sub>2</sub>)|
|(m<sub>2</sub>, w<sub>1</sub>)|
|(m<sub>3</sub>, w<sub>3</sub>)|

</td>
<td>

![Step 6](assets/step6.PNG "Man 4 proposes to woman 1")

</td>
</table>

----
**7<sup>th</sup> iteration**
1. Man = m<sub>4</sub> (again)
2. m<sub>4</sub> proposes to w (w<sub>2</sub>) and she is taken...
3. w<sub>2</sub> ranks m<sub>1</sub> higher than m<sub>4</sub>, so m<sub>4</sub> stays single

<table>
<td>

| Engagements (M, W) |
|:------------------:|
|(m<sub>1</sub>, w<sub>2</sub>)|
|(m<sub>2</sub>, w<sub>1</sub>)|
|(m<sub>3</sub>, w<sub>3</sub>)|

</td>
<td>

![Step 7](assets/step7.PNG "Man 4 proposes to woman 2")

</td>
</table>

----
**8<sup>th</sup> iteration**
1. Man = m<sub>4</sub> (again)
2. m<sub>4</sub> proposes to w (w<sub>3</sub>) and she is taken...
3. w<sub>3</sub> ranks m<sub>4</sub> higher than m<sub>3</sub>, so m<sub>3</sub> is now single and m<sub>4</sub> becomes engaged

<table>
<td>

| Engagements (M, W) |
|:------------------:|
|(m<sub>1</sub>, w<sub>2</sub>)|
|(m<sub>2</sub>, w<sub>1</sub>)|
|(m<sub>4</sub>, w<sub>3</sub>)|

</td>
<td>

![Step 8](assets/step8.PNG "Man 4 proposes to woman 3")

</td>
</table>

----
**9<sup>th</sup> iteration**
1. Man = m<sub>3</sub> (again)
2. m<sub>3</sub> proposes to w (w<sub>4</sub>) and she is single, so she accepts

<table>
<td>

| Engagements (M, W) |
|:------------------:|
|(m<sub>1</sub>, w<sub>2</sub>)|
|(m<sub>2</sub>, w<sub>1</sub>)|
|(m<sub>4</sub>, w<sub>3</sub>)|
|(m<sub>3</sub>, w<sub>4</sub>)|

</td>
<td>

![Step 9](assets/step9.PNG "Man 3 proposes to woman 4")

</td>
</table>


No more single men, done.

## Conclusion
For each woman, we can create **inverse** of preference list of men. This would mean that n would end up proposing to n women (where n is the size of the set of men and women). The best case would be if each man only had to propose once, or n times, and the worst case would be if each man had to propose n times, or n<sup>2</sup>.

Upon termination - due to the fact that a single man proposes to a woman he has not yet proposed to - every man is engaged. This is due to the fact that once a woman is engaged, she remains engaged, and only switches engagements to men she prefers more. Thus at the end every woman is engaged to some man.
