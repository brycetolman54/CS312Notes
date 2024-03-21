# More Intelligent Search

## Partial Path State Space

- This is what we will use in our project
- We will arbitrarily make the first state represent city 1
    - The root node is city 1
    - Each of the children are the other n - 1 nodes
    - We will end up with (n - 1)! leaves that represent the solutions
- We need to look at the state of each node (that is the reduced cost matrix at each node)
- The root node, city 1, has the initial reduced cost matrix
- When we choose a node to go to (say we go from (city 1 to city 2), we can update the matrix from the city 1 node by updating the column corresponding to the city we go to and the row corresponding to the city we are coming from (you can only enter and exit a city once) to infinity
- Then we have to reduce the matrix again and add that to the cost of the last matrix (that of city 1) along with the value of the edge we took to get from city 1 to city 2
- If there is no edge from city 1 to another city (their index is infinity), you just prune it
- Remember, when we travel to the next city, we have to add the node to the queue if it has a lower bound less than the BSSF, that is a priority queue, so go for the lowest lowerbound always
- Rows are where you are leaving from, columns are where you are going to
- If we update the matrix with infinities and find a row or column that doesn't have a 0, we prune the branch
- For reduction after traveling to a new city, you don't look at reducing the columns or that you have infinitized
- For your project, make a class to hold a state that tells you which columns and rows you don't need to look at anymore and can also hold the path that you have so far and also the lower bound of the state, that's a good idea
- You could also make it so that you only make a matrix that is the size that you need at each state and a vector or something that lets you know what the cities of the different columns and matrices are
- Once you get to the leaf, you have to make sure you can make it back to 1, or else it isn't a valid solution

- Work:

State 13 (going to city 3 from 4)
|       |   1   |   2   |   3   |   4   |   5   |
| :---: | :---: | :---: | :---: | :---: | :---: |
|   1   |  inf  |  inf  |  inf  |  inf  |  inf  |
|   2   |  inf  |  inf  |  inf  |  inf  |   0   |
|   3   |  inf  |   0   |  inf  |  inf  |  inf  |
|   4   |  inf  |  inf  |  inf  |  inf  |  inf  |
|   5   |   0   |  inf  |  inf  |  inf  |  inf  |

- Lower bound is just 21, since we add 0 for reducing the matrix

State 14 (going to city 5 from 4)
|       |   1   |   2   |   3   |   4   |   5   |
| :---: | :---: | :---: | :---: | :---: | :---: |
|   1   |  inf  |  inf  |  inf  |  inf  |  inf  |
|   2   |  inf  |  inf  |   0   |  inf  |  inf  |
|   3   |  inf  |   0   |  inf  |  inf  |  inf  |
|   4   |  inf  |  inf  |  inf  |  inf  |  inf  |
|   5   |   0   |  inf  |  inf  |  inf  |  inf  |

- Lower bound is 28, we add 1 from reducing the matrix at 2,3 and 6 from the path from 4 to 5

- We would put both on the queue
- we would go to 13 next
- Complexity?
    - n<sup>3</sup> because we have n children states and n<sup>2</sup> tables at each state that has a 
    - Space is the same
- In order to avoid a ton of shallow digging while you keep your OG BSSF, you can do some "deeper digging" to allow you to find a BSSF earlier
- For the project, you have to adjust the prioirty queue to prioritize something like deepness as well as lower bound to get a BSSF earlier, you have to come up with this for your project  and be creative (but not too intense)

- Complexity of Branch and Bound:   
    - Kind of n<sup>2</sup> times the number of things on your queue, so it's not really definite


## Include/Exclude State Space Search

- Does a little bit better than partial path at TSP because it digs a bit deeper
- We don't choose a city to start at
- We have a binary tree, one edge is the include side and the other is the exclude side
- The edges we choose for exclude and include are the ones with the biggest disparity (max the difference between b(exclude) and b(include))
- We still have to do the reduced cost matrix
- We can choose the 0 value in the row or column for the shortest edges
- We can choose the 
