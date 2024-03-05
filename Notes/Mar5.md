# Dynamic Programming Continued

- We don't always have the nice setup like we see in edit distance, what else can we do?
- What if I have  sequence of numers and want to find the longest increasing subsequence therein?
    - Example:
        - 5 2 8 6 3 6 9 7
        - Answer: 2 3 6 7
        - Other answer: 2 3 6 9
    - But how do we do that?
- Make a table that has the longest path for each number of nodes up to <i>n</i>
    - This is after representing the sequence as nodes in a DAG
    - To get the length for each node, we have to look at all previous iterations to see which has the largest length and corresponds to a node lower in value than you
    - You have to keep a prev to the place in the table that you are following
    - Time Complexity:
        - You have to look at each node to see what its length is
        - You have to look at all <i>n</i> nodes before hand
        - So we get O(n</sup>2<sup>)
    - Space Complexity:
        - We are only using a 1D table of size <i>n</i>, so we get O(n)
    - We can get multiple correct answers, any <b>legal</b> linearization works

|  Nodes | Length | Values |
| :----: | :----: | :----: |
|    0   |  0 (-) |    -   |
|    1   |  1 (0) |    5   |
|    2   |  1 (0) |    2   |
|    3   |  2 (1) |    8   |
|    4   |  2 (2) |    6   |
|    5   |  2 (2) |    3   |
|    6   |  3 (5) |    6   |
|    7   |  4 (6) |    9   |
|    8   |  4 (6) |    7   |


- The <b>Optimality Property</b> tells us that an optimal solution to a problem is built from optimal solutions to its sub-problems
- We also use the <b>Markovian Assumption</b> that we don't care about the <i>history</i> of the cell we are using, just the <i>current state</i>


## Knapsack problem

- DP is the best way to solve this problem (pretty much)
- You are given <i>n</i> items with a <i>weight</i> and a <i>value</i>
- You want to get the max <i>value</i> under a constraint of total <i>weight</i>
- There are two types of this, with repetition and without repetition

### With Repetition

- We need to know how to break it into sub-problems
- We could consider knapsacks with less capacity
- We could also consider subsets of the items
- Let's do it this way:
    - Define K(w) = max value with knapsack of capacity w
    - Start with w = 0 and fill in K(w) until we get to K(W)
    - Similar to earlier, we have a table and bags that we add the max value item that can fit into the sack given the space we have
    - We look at weights of each item, look at the bag that we would need to add to (if we are at w=9 and we have an item of w=3 we have to add to the w-6 bag)
    - We choose the item/bag that will give us the max value

- Table of items:

|  Item | Weight | Value |
| :---: | :----: | :---: |
|   A   |    2   |  $ 9  |
|   B   |    3   |  $14  |
|   C   |    4   |  $16  |
|   D   |    6   |  $30  |

- Algorithm Table

|   w   |   K(w)  |
| :---: | :-----: |
|   0   |   0 (-) |
|   1   |   0 (-) |
|   2   |   9 (0) |
|   3   |  16 (0) |
|   4   |  18 (2) |
|   :   |    :    |
|   :   |    :    |

- Complexity:
    - Time: this will be O(nW)
    - Problem is that we can get a huge W
    - n is usually log<sub>b</sub>(W)
    - So we really get O(nb<sup>n</sup>)
    - It is an NP complete problem

- How do we do it then?
    - We can do a sort of recursion (not straight recursion because that would be exponential)
    - This is called memoization:
        - We solve for a value K(w) and put it in a hashtable
        - If we need a K(w), we can check the hash table and see if we have it
        - This super helps in our time and makes the recursion doable
        - This gives the same time complexity as DP, but we can get some better constant factors than DP

### Without Repetition

- A little bit harder, because we have to keep track of the items in the sack
- We now have K(w,j) where <i>w</i> is still the weight and <i>j</i> is a number meaning the number of items that we can use (1 means we can only use item 1)
- We have to keep a table of w by j
- At each row and column, we can either add the item for that row to a an earlier bag of smaller w from the row above, or we can not include the item
