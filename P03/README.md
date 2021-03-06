Practicum 3
===========

Learning objective:

  - Implementing a decision tree classifier (i.e., Assignment 1)
  

## The basics

  - Section 4.3.2 of the book introduces Hunt's algorithm for growing a decision tree in a recursive fashion.
  - Section 4.3.5 of the book presents an algorithm for decision tree induction.
  - When implementing this general algorithm, you will need to make a number of design decisions:
    * Determine how to split the records
    * Determine when to stop splitting
  - You can look at two specific decision tree algorithms, ID3 and C4.5, to get some ideas on how to address these issues.

## ID3

The basic ideas behind ID3:

  - Each node corresponds to a non-categorical attribute and each outgoing edge to a possible value of that attribute.
  - Each node should be associated with the non-categorical attribute which is most informative among the attributes not yet considered in the path from the root. (This establishes what a "good" decision tree is.)
  - The informativeness of the node is measured using Entropy.


## C4.5

C4.5 is an extension of ID3 that accounts for missing values, continuous attribute values, pruning of decision trees, etc.


## References

  - [ID3 in Wikipedia](https://en.wikipedia.org/wiki/ID3_algorithm)
  - [C4.5 in Wikipedia](https://en.wikipedia.org/wiki/C4.5_algorithm)
  - [Tutorial on ID3 and C4.5](http://cis-linux1.temple.edu/~giorgio/cis587/readings/id3-c45.html)
  - [Building decision trees in Python](http://www.onlamp.com/pub/a/python/2006/02/09/ai_decision_trees.html)
    