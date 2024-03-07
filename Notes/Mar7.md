# Dynamic Programming

## Knapsack without repetition

- Example of Knapsack without repetition


|  Item | Weight | Value |
| :---: | :----: | :---: |
|   1   |    6   |  $30  |
|   2   |    3   |  $14  |
|   3   |    4   |  $16  |
|   4   |    2   |  $ 9  |


|  j/w  |   0   |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |   10  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|   0   |   0   |   0   |   0   |   0   |   0   |   0   |   0   |   0   |   0   |   0   |   0   |
|   1   |   0   |   0   |   0   |   0   |   0   |   0   |  30   |  30   |  30   |  30   |  30   |
|   2   |   0   |   0   |   0   |  14   |  14   |  14   |  30   |  30   |  30   |  44   |  44   |
|   3   |   0   |   0   |   0   |  14   |  16   |  16   |  30   |  30   |  30   |  44   |  46   |
|   4   |   0   |   0   |   9   |  14   |  16   |  23   |  30   |  30   |  39   |  44   |  46   |

- To get the list of items that you added to your sack:
    - Go back through the back pointers
    - Check the value of the box that you are in and that of the one you point to
    - If the value has changed, you add the item that corresponds to the row you are in
    - Go to the previous box
- Complexity:
    - Time: 
        - We have a w\*n size table
        - Each cell is constant time
        - So O(wn)
    - Space:
        - The table is O(wn)


## Matrix Multiply

- If matrices are <i>m</i>x<i>n</i> and <i>n</i>x<i>p</i>, we have a time of O(mnp)
- Matrices are not commutative, but are associative (we have to do them in an order, but we can do multiple in any groups that we want to)
    - We can do A x B x C x D as (A x B) x (C x D) or A x (B x C) x D
- The cost to do  different groups is way important because they can have varying costs
- We can represent the parentheses as a binary tree (the leafs sharing the same parent node are multiplied, we go bottom to top)
- If we want to multiply A<sub>1</sub> x A<sub>2</sub> x A<sub>3</sub> x A<sub>4</sub>:
    - These have dimensions of m<sub>0</sub> x m<sub>1</sub>, m<sub>1</sub> x m<sub>2</sub>, ...
    - The cost of the subtree is the cost of its two children subtrees and their cost of combination
        - C(i,j) = min<sub>i<=k<j</sub>[C(i,k) + C(k+1, j) + m<sub>i-1</sub> x m<sub>k</sub> x m<sub>j</sub>]
        - For this problem, we have A (50 x 20), B (20 x 1), C (1 x 10), D (10 x 100)
        - So, for k=1 we get C(1,1) + C(2,4) + 50 x 20 x 100
        - For k=2 we get C(1,2) + C(3,4) + 50 x 1 x 100
        - For k=3 we get C(1,3) + C(4,4) + 50 x 10 x 100
    - Let's show it as a table (columns are j, rows are i), the goal box is the top right [1,4]
        - For the box [1,2], we get 0 + 0 + 50 x 20 x 1 (for their costs and the dimensions)
 
|  i/j  |   1   |    2    |    3    |    4    |
| :---: | :---: | :-----: | :-----: | :-----: |
|   1   |   0   |  1000   |  1500   |         |
|   2   |   -   |    0    |   200   |         |
|   3   |   -   |    -    |    0    |  1000   |
|   4   |   -   |    -    |    -    |    0    |

- Total time is n<sup>3</sup>
    - The table is n<sup>2</sup> size
    - Filling in once cell, you have to split the children along each of the possible values, which is size n
    - The time then is O(n<sup>3</sup>)


## Shortest Paths and DP

- We want to get the shortest path between all nodes and every other node
- That would be O(V<sup>2</sup>E) with Djikstra's (but E is larger than V)
- Floyd's algorithm gets it in O(V<sup>3</sup>)

### Floyd-Warshal algorithm

- Define dist(i,j,k) as the shortest path between i and j that can go through nodes {1,2,...k}
- This is really to see if adding node k to the path will improve things
- You can set this up as a 3D table of size n x n
    - Or as a set of n x n tables for each k value (but there are n k values)
- The whole table for k = 0 is the base case, just the list of edges in our graph
- The diagonal is always 0
- The column and row for the k we are on will always be the same as the previous table (k is the node, like node 1 or 2, not just the number of extra nodes we can go through)


## Traveling Salesman Problem

- 

