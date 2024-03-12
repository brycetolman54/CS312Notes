# Linear Programming

- This is the other sledgehammer of algortihms that can be used when more specialized methods fail
- The hard part of dynamic programming is finding the subproblems and how to relate those to the main problem, this is all about the solution
- Linear programming is focused on the problems of a specific format. The hard part is to see if our problem fits in the bucket of problems we have
- Here's the idea:
    - We are doing optimization problems
    - We want to find the maximum of something (a sum of items with their respective coefficients)
        - This is the <b>objective function</b>
        - The coefficients are inherent to the problem (like the value of an item in the knapsack problem)
        - The x<sub>i</sub> is the thing that we can change in order to solve the problem, we call these the <b>decision variables</b>
    - We have a list of <b>constraints</b> that we have to solve the problem with
        - This is a list of inequalities that we have to meet, we can't just choose the <b>decision variables</b>
        - We can have as many <b>constraints</b> as we want to have
        - We assume that all <b>decision variables</b> are greater than 0 (for this class)
    - We solve the problem by finding a value for all of the <b>decision variables</b>
- The reason that we call this linear programming is because the <b>objective function</b> and <b>constraints</b> is a linear combination of things

## Examples

- First Example:
    - We have a chocolate shop that makes two chocolates
        - <i>Pyramide</i> gives $1 profit
        - <i>Pyramide Nuit</i> gives $6 profit
    - Constraints:
        - Max demand is 200 per day for <i>Pyramide</i>
        - Max demand is 300 per day for <i>Pyramide Nuit</i>
        - We can only make 400 chocolates per day
    - Setting up the problem
        - x<sub>1</sub> is <i>Pyramide</i>
        - x<sub>2</sub> is <i>Pyramide Nuit</i>
    - We can set these up on a plot with the axes being the <b>decision variables</b> and then find the <i>feasible region</i>, the area of the curve in which we can satisfy all of the constraints
    - Then we can look in that area to find the point that satisfies the <b>objective function</b>
        - This will only ever be one of the vertices of the polygon

- Code:
```
Simplex(P)      // This is the simple version of simplex
    v = 0       // start at the origin and itx vertex
    while v has a neighbor u such that obj(u) > obj(v) do       // move along the vertices to a neighbor that has a better value of the objective function
        v = u       // set that vertex to be the new one
    return v        // once there are not other neighbors with better values for the objective function, return that one
```
    - In its worst case, this is exponential, but in practice it doesn't really get there (about n<sup>2</sup> to n<sup>3</sup>)


- New Example: the divisible (we don't need integer <b>objective variables</b>) knapsack with constraints

| Item  | Weight | Value |
| :---: | :----: | :---: |
|   x1  |   6    |  $10  |
|   x2  |   2    |  $ 4  |

- Objective Function:
    - max of 10x<sub>1</sub> + 4x<sub>2</sub>
- Constraints:
    - x<sub>1</sub>, x<sub>2</sub> >= 0 (nonnegative)
    - x<sub>1</sub> + x<sub>2</sub> <= 3 (max items)
    - 6x<sub>1</sub> + 2x<sub>2</sub> <= 9 (max weight)

## Problems that we may encounter

- <i>Infeasbility</i> means that there are no values of our <b>decision variables</b> that satisfy the <b>constraints</b>
- <i>Unboundedness</i> means that there is no limit to our feasible region, we have no polygon
