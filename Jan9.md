# Introduction

- We are going to be talking about algorithms
    - Analysis from both practical and theoretical points of view
    - Efficiency of Algorithm (time and space)
    - Fundamental paradigms
        - Divide and conquer, graph, greedy, dynamic, linear, intelligent search, local search, probabilistic

- __Always remember the Bigger Picture__: Become a better person
- Computation is as easy as: `take an input, do stuff, give an output` 
    - The computation is the stuff you do in the middle, mapping input to output
    - The goal of computer science is to do the mapping efficiently
- What is an algorithm?
    - A finite sequence of well-defined steps for solving a problem

- There are three questions to always ask when proposing an algorithm for a particular task:
    - Is the algorithm correct?
    - How long does it take as a function of n (the size of the data), the problem size?
        - Also how much space (memory) does it take?
    - __Can we do__ ___better___?
     
- Example: Is a person's name in a list of size n?
    - Run through list one by one to see if it is in there 
    - Time complexity: 
        - Worst: n
        - Best: 1
        - Average: n/2 
        - Precise: p(in)*n/2 + (1-p(in))*n
    - Space complexity: n
     
# Complexity
- There are different complexities (n^2, n, nlogn)
- We have asymptotic complexity as well
    - Big O
    - Big theta (includes all Big 0 that are of the same complexity class)
        - Big theta(n) has O(n) and O(n+2) and O(10n + 1000) and ...
    - We want to focus on paradgims that drop us from one class to another, not just drop us lower in one class
