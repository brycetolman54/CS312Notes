# Intelligent Search

- DFS and BFS search the whole tree
- We want something faster
- We can prune branches in the tree that won't lead to something good (hopefully)
- We need some "intelligence" in order to do so

- Go and learn about backtracking later


## Branch and Bound

- Keep track of the <b>BSSF</b>, the <b>Best Solution so Far</b>
- Look at the lowerbound for different branches in the tree and prune them if they are worse than the <b>BSSF</b>
- The <i>bound</i> is how we look at the lower bound
- The <i>branch</i> is how we cut off that branch

- Example:
    - The branches in this tree are the lengths of curvy roads
    - The table shows the straight line distance from each city to E

```mermaid
graph TD;
    A-- 10 --B;
    A-- 8 --C;
    A-- 12 --D;
    B-- 8 --E;
    B-- 15 --F;
    C-- 7 --D;
    D-- 9 --E;
    E-- 9 --G;
    F-- 6 --G;
```


|  City | Distance to E |
| :---: | :-----------: |
|   A   |       14      |
|   B   |        6      |
|   C   |        7      |
|   D   |        5      |
|   E   |        0      |
|   F   |        4      |
|   G   |        7      |

    - We want to find the straightest (Shortest distance) from <i>A</i> to <i>E</i>
    - The <b>BSSF</b> starts out as &`\inf`$
    - Make subproblems and expand it into the smaller problems
    - Start with A:

```mermaid
graph TD;
    A--B["10+6=16"]
    A--C["8+7=15"]
    A--D["12+5=17"]
```

    - If one of those nodes is the complete solution (<i>E</i> in this case), update the <b>BSSF</b>
    - If not and the lowerbound of that branch (the straight line distance plus the curvy road distance from A), add the Node to the queue (which we are calling S)
    - We are calling S a priority queue, so take the lowest node from S to look at it and explore its children
    - We choose C

```mermaid
graph TD;
    A--B[16]
    A--C[15]
    A--D[17]
    C--D'["8+7+5=20"]
```

    - Now let's pop off B
        - We don't need to do lower bound for all from B because we have a complete solution with B
        - We update <b>BSSF</b> and don't add F to S


```mermaid
graph TD;
    A--B[16]
    A--C[15]
    A--D[17]
    C--D'["8+7+5=20"]
    B--F
    B--E["10+8=18"]
```

    - Now we get to D
        - It's lower bound is less than the <b>BSSF</b> so we have to check it
    - Then we get to D' and drop it because it has a worse lower bound
    - Then we are done!

- This <b>DOES</b> give an optimal solution
- It is exponential, but it is pretty quick still


## Beam Search

- You only keep some of the solutions to subproblems
- Set a beam width and when you get more subproblems than that, drop the wrost ones
- It is possible that you drop the optimal solution, but that is the risk you are willing to take
- This gives you a lot more control over specifcally space complexity, but also time (since you force yourself to prune off options)
- This is something you sort of add on to the branch and bound algorithm


- For the branc and bound method, you have to have a bounding function that defines how you want to move and what you prioritize in the solution
- You need this bound to be really close to the optimal solution, without getting too tight
- Make sure you don't overestimate the needed steps for a state or else you m ay end up throwing out optimal solutions
- If the function gets too tight, then you spend all your time trying to get the lower bound (that's the actual solution you are aiming for)
- If the function gets too loose, you have to do an exhaustive search, which takes all your time
- You need to find some good "search space" in which to look for the solution


## Traveling Salesperson (TSP) Lower Bound Function

- What will our bounding function be?
    - We can take the current partial distance plust the MST of the remaining nodes
    - We can take the current partial distance and the sum of the shortest edges leaving remaining nodes (nodes that you haven't visited yet, just the shortest edge out of the city)
- So what will we actually use?
    - Every tour has to leave every city and it has to arrive at every city
    - We will look at the edges leaving every city and the ones going into every city
    - We don't just want to sum them, that is not good, we will do something else
    - What we do is look at the edges going out of the cities and sum them up, then find the lowest edge and subtract that from the other paths going out of that city
    - Once we do that, we look at the edges going into the cities, we add that distance to our lowerbound and subtract it from all edges going into that city
    - You do this in an array
        - Find the min value of the row (that shows the edges out of the city) and subtract it from the row
        - Do that for all rows (but if there is a 0, don't waste your time subtracting)
        - Then do that for each column
        - Make sure you add that value to the bound for each row and column

- Example Problem:


|       |    A   |   B   |   C   |   D   |
| :---: |  :---: | :---: | :---: | :---: |
|   A   |   inf  |   8   |   12  |   4   |
|   B   |    3   |  inf  |   7   |   1   |
|   C   |    2   |   6   |  inf  |   4   |
|   D   |   inf  |   3   |   5   |  inf  |
LB = 2 + 3 + 5 + 1

|       |    A   |   B   |   C   |   D   |
| :---: |  :---: | :---: | :---: | :---: |
|   A   |   inf  |   5   |   7   |   3   |
|   B   |    1   |  inf  |   2   |   0   |
|   C   |    0   |   3   |  inf  |   3   |
|   D   |   inf  |   0   |   0   |  inf  |
LB = 11 + 3

|       |    A   |   B   |   C   |   D   |
| :---: |  :---: | :---: | :---: | :---: |
|   A   |   inf  |   2   |   4   |   0   |
|   B   |    1   |  inf  |   2   |   0   |
|   C   |    0   |   3   |  inf  |   3   |
|   D   |   inf  |   0   |   0   |  inf  |
LB = 14

- Complexity?
    - Time would be O(n<sup>2</sup>), you have to go through the 2D table twice
- You can do it rows then columns or columns and then rows
    - This will maybe give you different answers, but both will be lower bounds
- Do rows then columns for the homework
- We don't want to have an initial value for BSSF of infinity, because we can't prune until we have a BSSF, so how do we get one?
    - We could do a greedy thing
    - We do want a BSSF as high as possible and lower bounds as low as possible


## State Space Search

- One example of this is the branch and bound, but that is only one thing that we can do this for
- 
