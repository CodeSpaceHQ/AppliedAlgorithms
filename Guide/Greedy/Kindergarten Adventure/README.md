# Kindergarten Adventure
[https://www.hackerrank.com/challenges/kindergarten-adventures](https://www.hackerrank.com/challenges/kindergarten-adventures)

Category: Greedy

Difficulty: Medium


## Problem

### Overview
####Given:
* A set of student IDs {1, 2, ..., n}.
* The number of time each student, i, needs to finish the project, t<sub>i</sub>.

####Goal:
* Pick a student ID that the teacher can start with that:
    * will allow the most students to finish their project.
    * that has the lowest ID number. 

## Algorithm
### Overview
<p>
Without much thought, it is fairly easy to come up with the brute force way to solve this problem. 
If you started at each child you could count the number of children done and pick the starting child that allowed the most children to finish. 
However, this algorithm will have an O(n<sup>2</sup>) time complexity and is too slow. 
However, we can convert it into Algorithmic Crush, a problem we efficiently solved in another section.
</p>

#### Important things to note:
* Each child, i, has enough time to finish if the teacher starts in the range [ (i + 1) % n, ((i + 1) + (n - t<sub>i</sub>)) % n).
    * if (i + 1) % n == ((i + 1) + (n - t<sub>i</sub>)) % n then there is nothing in the range.
* The algorithm used to solve Algorithmic Crush will not work if there are ranges that loop back to zero.
    * The ranges could be [ i + 1, (i + 1) + (n - t<sub>i</sub>) ) as long as the array you use to store the values is 2n + 1 in size.
        * For this the number of children that will be done when you start at child i, after preforming the Algorithmic Crush algorithms, is the number of children that finish if position i is the start plus the number that finish if position i + n is the start.

### Pseudo Code
1. Read in the number of children into n.
2. Make an array called times of size n.
3. Read in the additional time each child, i, needs into times[i].
4. Make an array called ranges of size 2n + 1.
5. For i = 0 to n:
    1. ranges[i + 1] = ranges[i + 1] + 1
    2. ranges[(i + 1) + (n - times[i])] = ranges[(i + 1) + (n - times[i])] - 1
6. For i = 1 to 2n + 1:
    1. ranges[i] = ranges[i] + ranges[i - 1]
7. Make an array called numComplete of size n.
8. For i = 0 to n:
    1. numComplete[i] = ranges[i] + ranges[i + n]
9. Find the biggest number in numComplete and print its index plus one. 

### Analysis
<p>
The biggest loop in this algorithm goes from 1 to 2n + 1. Becasue time complexity drops constants, 
the time complexity is O(n), even though the full formula is n + 2n + n + n => 5n. While this is O(n), there is a more efficient O(n) solution. 
It follows this same basic algorithm, but it gets rid of most of the loops. Its full formula is 2n. It is also included in the solution file.  
</p>

## Conclusion
<p>
Many computer science problems can be reduced to other problems that have already been solved
or that are simpler. This problem is an example of reducing a problem to another problem
that has already been solved. Becasue this problem was reducable, it ran faster and most of the
algorithm to solve it was already thought up. This saved time when writing the code.
</p>