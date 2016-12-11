# Contacts
This problem comes from [HackerRank](https://www.hackerrank.com/challenges/contacts) and is under the Data Structures Domain.

##### Tags

[Trie](https://en.wikipedia.org/wiki/Trie) / [Hash Table](https://en.wikipedia.org/wiki/Hash_table) / [Class](https://en.wikipedia.org/wiki/Class_(computer_programming))

## Problem
### Statement

We're going to make our own Contacts application! The application must perform two types of operations:

1. add name, where _name_  is a string denoting a contact name. This must store  as a new contact in the application.
2. find partial, where _partial_ is a string denoting a partial name to search the application for. It must count the number of contacts starting with  and print the count on a new line.

Given _n_ sequential **_add_** and **_find_** operations, perform each operation in order.

**Input Format**

The first line contains a single integer, _n_, denoting the number of operations to perform. 
Each line _i_ of the _n_ subsequent lines contains an operation in one of the two forms defined above.

Constraints
* 1 <= n <= 10^5
* 1 <= | _name_ | <= 21
* 1 <= | _partial_ | <= 21


It is guaranteed that  and  contain lowercase English letters only.
The input doesn't have any duplicate  for the  operation.
Output Format

#### Output Format

For each _find partial_ operation, print the number of contact names starting with _partial_  on a new line.

#### Sample Input
4</br>
add hack</br>
add hackerrank</br>
find hac</br>
fink hak</br>

#### Sample Output
2</br>
0</br>

#### Explanation

We perform the following sequence of operations:

1. Add a contact named _hack_.
2. Add a contact named _hackerrank_.
3. Find and print the number of contact names beginning with _hac_. There are currently two contact names in the application and both of them start with _hac_, so we print 2 on a new line.
4. Find and print the number of contact names beginning with _hak_. There are two contact names in the application but neither of them start with _hak_, so we print 0 on a new line

### Overview

This is a two step problem.

1. Setting up the Trie data structure.
2. Finding the number of sub strings.

A Trie can be implemented in more than one way. I chose to create my own Trie class that contained a HashMap that mapped
characters to other objects of type Trie.  I also had an integer value in my class so I could keep track of the the times that i had
seen that substring when doing the add.

## Algorithm

### Overview

#### Part 1

Part one of this problem lies in the creation of the data structure that will be used to store the input strings and subsequent sub-strings.
This data structure is called a Trie (from re-_trie_-val) and can be thought of as a tree of characters, Like the following:

&nbsp;&nbsp;&nbsp;&nbsp; a</br>
&nbsp;&nbsp;&nbsp;&nbsp; / \\</br>
&nbsp;&nbsp;r&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t</br>
&nbsp;/</br>
t</br>

This is a trie that contains two words (art and at), as you can see it is space efficient because if they both contain the same substring (a in this case)
space is not being wasted.  This is the data structure we are trying to create, but at each node (or letter in this case) we would like to store an integer
value of how many times we have seen this character in the past, thus our Class will need two variable. One being the HashMap that will store the Characters, and the Tries that they link to, and an integer value that will store the number of times that we have seen the substring.

The next step is to add the functionality that is described in the problem. Specifically the add and find functions.  The meat of this problem is in the add function.  In our main function we must create an initial Trie object.  The add function should take in a string and add this specific string to the Trie. in order to do this we need to separate the string out into its characters, and map each character to a trie containing the next character.  The trick to get the efficience in the find functions is to keep track of the number of times we are adding each character at each specific location.  Using the example from above when we add the a from art, we also need to increment counter associated with at this location. Next we must use the Trie associated with a, and add the r from art, and again increment the counter, and so forth until the whole string is added.  Once we have added "art" next we want to add "at".  Since we already have a in the first hash map, we dont need to add a new Trie at this location, all we need to do is
increment the counter, then go to the Trie associated with a already.  Next we just need to add the 't' to the new HashMap, and increment the counter and we are done.

The next step is to create the find functionality. Since we have gone through the trouble of keeping track of all of the times we saw a specific character at a specific level, the find
functionality is very easy to implement.  At this point all we need to do is search through the trie one character at a time until we hit the end, or a character in the substring is not contained
in the trie.  At that point we return the integer value denoting the number of times we've seen the substring, or 0 if it is not in the trie.

#### Part 2

Once the class Trie class is created with all the necessary functionality, part 2 of this is super easy.  All you have to do is read in the strings to add to the trie, and add them.  Once you have inserted all the strings, all you need to do is search through the trie for the sub-strings and return the integer value that is associated with the last character from the substring, if it exists in the trie.


### Pseudo Code

1. Create Trie Class
  * HashMap that maps characters to Trie Class.
  * Integer value to keep track of times character has been seen.
2. Add proper functionality to Trie class. 
  * Create Add function.
  * Create Find function.
3. Add all strings to trie.
4. Search through trie on find instruction and return the integer value associated with the last character.

### Analysis
Adding the Strings to The trie class should take N time where N is the length of the String that you're attempting to add to the trie.
Similarly the find function will take M time where M is the length of the substring. So adding is O(N) and looking for substrings is O(M)
Therefor, the time complexity of this will be O(N).

### Conclusion
A Trie is a very useful data structure to learn. You can clearly see the advantages of the space efficiency of this data structure.  A real world example of where this data structure is used is in predictive text on your phones.  For other uses feel free to browse the wikipedia page linked above.
