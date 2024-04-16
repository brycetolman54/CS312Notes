# Exam Review

## Dynamic Programming

- This is the idea that we want to avoid recalculating things, so we keep a memory of what we have calculated and look to that when we need it
- Review Floyd's algorithm
- Memoization is the idea that we "remember" things

## Linear Programming

- You have a set of constraints that are linear and an objective function that is linear
- To solve it, you draw out the constraints and find the plausible region
- You are guaranteed that the solution is one of the vertices
- You use the objective function to check each vertex
    - You look at all neighbors and jump to the first one that gives a better answer than what you have
- Primal and dual: each problem has its dual, the opposite whose solution is the same as the one we care about but it is focused on finding the minimum objective function

## Intelligent Search

- Review backtracking
- We need some heuristic, some feeling about how good the solution is
    - With beam branch and bound, we have a constant size memory, and we lop off the lowest ones when we exceed that size

## Complexity

- P is polynomial, we can find the solution in polynomial time
- NP is nondeterministic polynomial, we can't find the solution in polynomial time, but we can confirm that a solution is a solution in polynomial time
- NP-complete means a problem (1) has to be NP and (2) all other NP problems reduce to it in polynomial time
    - NP complete because all NP problems can reduce to it, it is representative of the <b>complete</b> set of NP problems

## Bounded Approximation Algorithms

- You don't know the optimal, but you know what factor you are within to the optimal solution

## Local Search

- Choose some solutions
- Check the neighborhood around that solution
- Continue until you don't find a better solution all around you (you go to the first one that gives you a better solution)
- You will find the local optima, which isn't necessarily the global optimum
- Perceptron algorithm: review this
- Genetic algorithm:
    - We start with a population of solutions
    - We get the fitness for each solution (we need a function for that)
    - We can do mutations, or crossovers
    - We eliminate some solutions (this is random, but more probable to drop lower fitness individuals)
    - We stop after a certain number of generations, or when we haven't had a better solution in some time

## Analysis

- Empirical:
    - We use a represetnative data set for what we will be using the algorithms for
    - We run the algorithms on all of those data sets and get our average
    - Take the best one of the two
- Average: we can figure out mathematically our complexity with probabilities and distributions of our function

## Random Algorithms

- Las Vegas: guarantees right answer, but we have no idea of the time it will take
    - Think quicksort, you have to choose a random pivot, but we get the answer for sure (after some unknown time)
    - Think selection, we choose a random pivot, but we get the answer for sure
- Monte Carlo: we can set how long it takes, but it is not guaranteed to get a correct solution (the longer you run, the more likely to get a good solution)
    - Think Fermat, we choose random integers for the Fermat test, we aren't sure in the end that the number is prime, but we can get better probability of it the more we run it
    - Think genetic algorithms, you choose random solutions and get better solutions the longer you run it

## When to use different paradigms

- You choose!
