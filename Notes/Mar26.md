# Finishing up Branch and Bound

- More on include/exclude
- We don't want premature cycles
- We only want cycles of size n, the one that is our solution
- You cannot get premature cycles in the State Space Search with partial path because you blank out every row and column of the nodes that you are going to and coming from and you just keep going down the tree
- For the include/exclude, we have to choose the edges that gives the biggest difference between the bounds (you choose a 0 edge for your smallest and the max edge for your largest, the 0 edge that gives us the biggest difference)
- Complexity?
    - It is still n</sup>3<sup> for expansion, because you have to check n edges at each node (there are n columns and rows and you have a 0 in each column/row to check)
    - Each check is n</sup>2<sup> because of the matrix
- This can sometimes be more effective than partial path, but it doesn't super matter 


# Complexity

- P (polynomial), NP (nondeterministic polynomial), NP-Complete
- If we can test a polynomial subset of the potentially exponential solutions and get an optimal and real solution, we are in the <i>P</i> class
- If we may have to test an exponential amount of cases, but we can verify the solution in polynomial time, we are in the <i>NP</i> class (of which P is a subset)
- All of the <i>NP-Complete</i> are similar in what makes them difficult. If we could find a solution to one, we could pretty much find a solution to all
- P: solved in polynomial time on a deterministic Turing machine
- NP: solved in polynomial time on a non-deterministic Turing machine (letting us see all possibilities)
- <b><i>A PROBLEM IS NP COMPLETE IF ALL OTHER PROBLEMS IN NP COMPLETE REDUCE TO IT</b></i>
- An algorithm can be said to reduce to another if you can make A into B by a polynomial time function, solve B, and then use another polynomial time function on that solution to get the solution to A


# Empirical and Average Case Analysis

- We want to know the empirical and average case complexity, not just asymptotic analysis
- Empirical is to do a lot of tests and find the average
    - You have to test with data that is similar to what it will be run on in the future
- Average is to find the probabilities of being one case or another and doing a sort of weighted average
    - We have to find representative data again
