# Dynamic Programming

- These can be used in broader sets of applications than greedy or divide and conquer programming
- We don't need to resolve the problem over and over again, we can store the info as we find it and then access it later
- Think of Fibbonaci as an example:
    - Each time we solve a fib number, we can put it in a table and use those values in the table iteratively to find the next
- The hardest part of dynamic programming is finding the recurrence relation that lets us find the new number from what we have

- Let's think about how to do the <b>Choose</b> operator:
- We want to do C(5,3) which means 5 choose 3

- The base cases:

|  n, k |   0   |   1   |   2   |   3   |
| :---: | :---: | :---: | :---: | :---: |
|   0   |   1   |   0   |   0   |   0   |
|   1   |   1   |   1   |   0   |   0   |
|   2   |   1   |       |   1   |   0   |
|   3   |   1   |       |       |   1   |
|   4   |   1   |       |       |       |
|   5   |   1   |       |       |       |

- The rest: you have to have a full cell above you and to the left of you

|  n, k |   0   |   1   |   2   |   3   |
| :---: | :---: | :---: | :---: | :---: |
|   0   |   1   |   0   |   0   |   0   |
|   1   |   1   |   1   |   0   |   0   |
|   2   |   1   |   2   |   1   |   0   |
|   3   |   1   |   3   |   3   |   1   |
|   4   |   1   |   4   |   6   |   4   |
|   5   |   1   |   5   |  10   |  10   |

- Complexity? 
    - You have <i>n*k</i> cells (pretty much n<sup>2</sup> because k can only be up to n really)
    - You have to do constant time at each cell, so total is O(n\*k)
    - Space would be <i>n</i> because you only have to keep the row above you which is size n

- <b>General Approach to DP</b>
    - Create a recurrence relation
    - Create a d-dimensional table
    - Set the base cases
    - Fill in the tabe following DAG dependencies until you get your answer


## Edit Distance

- This is our project! 
- The edit distance is the minimum number of edits to convert one string to another
- The only edits we can do are <i>substitute</i>, <i>insert</i>, or <i>delete</i>
- For example:
    - The edit distance between THARS and OTHER is 3 (<b>-</b>TH<b>A</b>R<b>S</b> and OTHER<b>-</b>)
- We need a recurrence relation that can take a long word and split it into subwords that we can solve, that's where the creativity comes in;2
    - Let's say that f(n) = f(i) + f(j) (split the word into smaller words)
    - We need to build a table of size m\*n (the size of the words)
    - The most optimal edit distance is shown along the diagonal

- Base Case:

|       |       |   O   |   T   |   H   |   E   |   R   |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|       |   0   |   1   |   2   |   3   |   4   |   5   |
|   T   |   1   |       |       |       |       |       |
|   H   |   2   |       |       |       |       |       |
|   A   |   3   |       |       |       |       |       |
|   R   |   4   |       |       |       |       |       |
|   S   |   5   |       |       |       |       |       |

- The rest:
    - We find the optimal choice out of insertion, deletion, and substitution and add that to a cell next to us
    - For match, we don't add anything, we have a cost of 0
    - For substitution, we add a cost of 1 to the cell up and to the left of the one we are in
    - For insert, we add a cost of 1 to the cell that is to our left
    - For delete, we add a cost of 1 to the cell that is above us
    - Choose the one that gives the lowest value for the current cell
    - If there is a tie, choose one randomly
    - We can get the cost by looking at the value of the goal cell, but we also have to keep a <i>prev</i> pointer to keep track of the edits we need

|       |       |   O   |   T   |   H   |   E   |   R   |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|       |   0   |   1i  |   2i  |   3i  |   4i  |   5i  |
|   T   |   1i  |   1s  |   1m  |   2i  |   3i  |   4i  |
|   H   |   2i  |   2s  |   2s  |   1m  |   2i  |   3i  |
|   A   |   3i  |   3s  |   3s  |   2d  |   2s  |   3s  |
|   R   |   4i  |   4s  |   4s  |   3d  |   3s  |   2m  |
|   S   |   5i  |   5s  |   5s  |   4d  |   4s  |   3d  |

- Path: (0,1) [1i], (1,2) [1m], (2,3) [1m], (3,4) [2s], (4,5) [2m], (5,5) [1i]
- Complexity: 
    - Space: Let's say m\*n, since we want to keep the whole table and thus keep our path, so we get O(m\*n)
    - Time: We are doing m\*n cells and constant time in each cell, so we get O(m\*n)

