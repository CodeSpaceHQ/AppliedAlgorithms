# Stable Marriage
https://en.wikipedia.org/wiki/Stable_marriage_problem

Category: Greedy

## Problem
Given _n_ men and _n_ women, where each person has ranked all members of the opposite sex in order of preference, marry the men and the women together such that there are no two people of opposite sex who would both rather have ach other than their current partners. When there are no such pairs of people, the set of marriages is deemed stable.


### Overview
_From Wikipedia:_
>Stable marriage problem (also stable matching problem or SMP)
> is the problem of finding a stable matching between two
> equally sized sets of elements given an ordering of
> preferences for each element. A matching is a mapping from
> the elements of one set to the elements of the other set. A > matching is not stable if:

>   a. There is an element A of the first matched set which prefers
> some given element B of the second matched set over the
> element to which A is already matched, and
>   b. B also prefers A over the element to which B is already
> matched.

i.e. a _matching_ is stable when there is no match **(A,B) and (C,D)**  where **A** prefers **D** and **D** prefers **A** or any other combination where both **A** and **B** would be individually better off than they are with the element they are currently matched with.

### Applications
* Assigning users to servers in a large distributed internet service
* Assigning graduating medical students to their first hospital appointments
* Preferences problems



## Algorithm
### Overview
We will use the Gale-Shapely algorithm, discovered in 1962 by David Gale and Lloyd Shapely. This algorithm proves that for any equal number of men and women it is always possible to solve the stable marriage problem.  

We will use sets of men _m_ and women _w_, and find a one-to-one correspondence between them using the preferences of each man in _m_ and woman in _w_ such that each pairing is considered _stable_.

Each element of each set will have a list of preferences mapping to each element of the other set, i.e. male M<sub>1</sub> in set _m_ will have a list [W<sub>1</sub>, W<sub>5</sub>m...W<sub>N</sub>] of preferred women in _w_ in decreasing order, as well as a state (single, engaged):

| m  | Status | Preferences  |  
|----|--------|--------------|
| m<sub>1</sub> | Single | [w<sub>1</sub>, w<sub>2</sub>,w<sub>3</sub>,w<sub>4</sub>] |
| m<sub>2</sub> | Single | [w<sub>2</sub>, w<sub>1</sub>,w<sub>3</sub>,w<sub>4</sub>] |
| m<sub>3</sub> | Single | [w<sub>3</sub>, w<sub>1</sub>,w<sub>4</sub>,w<sub>2</sub>] |
| m<sub>4</sub> | Single | [w<sub>4</sub>, w<sub>3</sub>,w<sub>2</sub>,w<sub>1</sub>] | 


### Pseudo Code
[The algorithm]
### Analysis
[Analyze the algorithm, here's where things such as complexity can be discussed]

## Conclusion
[Any final thoughts here, maybe discuss other ways to solve the problem that would be equally efficient]
