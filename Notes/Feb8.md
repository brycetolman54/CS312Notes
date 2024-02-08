# Graphs

- We just need to know the number of nodes and then we can declare an array that has the appropriate amount of spaces for each node, it never gets bigger
- We have another array that just tells which place each node is located in our tree array


- What if we have negative edges?

# Dealing with Negative Edges

- We can't use a priority queue any longer, since we have negative edges we can get smaller paths
- The <b>max</b> number of <i>E</i> for a shortest path has to be <i>V</i> - 1 or else we would have to have a cyclic graph
- We have to go from the <b>source</b> node to the <b>target</b> node through all possible paths

## Shortest path algorithm

- Initialize all nodes with <b>dist</b> of infinity and <b>prev</b> or nil
- Do the following <i>V</i> - 1 times
    - Update each edge 
        - If the distance to a node gets better by using that edge, update the node's distance


|  Node |   0   |   1   |   2   |   3   |   4   |   5   |   6   |   7   |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|   S   |   0   |   0   |   0   |   0   |   0   |   0   |   0   |   0   |
|   A   |  inf  |  10   |  10   |   5   |   5   |   5   |   5   |   5   |
|   B   |  inf  |  inf  |  inf  |  10   |   6   |   5   |   5   |   5   |
|   C   |  inf  |  inf  |  inf  |  inf  |  11   |   7   |   6   |   6   |
|   D   |  inf  |  inf  |  inf  |  inf  |  inf  |  14   |  10   |   9   |
|   E   |  inf  |  inf  |  12   |   8   |   7   |   7   |   7   |   7   |
|   F   |  inf  |  inf  |   9   |   9   |   9   |   9   |   9   |   9   |
|   G   |  inf  |   8   |   8   |   8   |   8   |   8   |   8   |   8   |

- Trick?
    - Only look at the edges belonging to a node that was updated last time
- Complexity?
    - You do the look over <i>V</i> - 1 times (O(V))
    - You do <i>E</i> edges every time
    - So you get O(E\*V) for time
    - You have a table of <i>V<sup>2</sup></i>
        - You don't have to keep the whole table to get the cost of the shortest path, but you do if you want to know the path
- Does this improve the time?
    - Not really. It is only a constant factor increase, not a Big-O improvement
- How to tell if it is a negative cycle?
    - Run the algorithm loop one more time (<i>V</i> times and not <i>V</i> - 1) and if things change, you have a negative cycle
