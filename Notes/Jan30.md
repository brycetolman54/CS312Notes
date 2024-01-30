# Finish Divide and Conquer

- What is the complexity of the selection algorithm?
    - Well, if we can split the list in half every time:
        - t(n) = 1 x t(n/2) + O(n)
        - So a = 1, b = 2, d = 1, ratio = 1/2
        - So, O(n)
    - Well, that's the best case. What's the worst? What if we choose the smallest value every time?
        - t(n) = 1 x t(n - 1) + O(n)
        - That's not divide and conquer. We have n levels and n time for each so O(n<sup>2</sup>)
    - The average is around O(n). But how do we find the average?

## Average Case Complexity

- For this selection algorithm:
    - Assume a good pivot is between the 25<sup>th</sup> and 75<sup>th</sup> percentile, so we get a good pivot half the time
    - That means we get a good pivot within two choices, so on average we divide the list by 3/4 and not 1/2
        - t(n) = 1 x t(3n/4) + O(n)
        - So, a = 1, b = 4/3, d = 1, ratio = 3/4
        - And O(n) is the average case (since the work is dominated by the root node, you are decreasing work as you go down)



# Chapter 3: Graphs

- Lots of things are graphs :)
    - Think the internet, maps, etc.
- This chapter is focused on looking at connectivity, the next is about algorithms for finding the shortest paths in a graph
- There are directed and undirected graphs
- We can represent the graphs with adjaceny matrices or adjacency lists
- We think about complexity in terms of <i>V</i> (the number of nodes) and <i>E</i> (the number of edges) instead of n
- For matrices:
    - Space is V<sup>2</sup>
    - Lookup is constant time
- For lists:
    - Space is V + E
    - Lookup is (worst time) E
- Which do we use? Depends on what we want
    - Sparse is better with lists
    - Dense is better with matrices


## Depth-First Search (DFS) of Graphs

- You go far down first, then back up
- You have to make sure not to go back to a path you have gone
- You make a tree of all the places you can go from a certain node
- You can't always get to all nodes from one node, so you have to search and make multiple trees (this is called a forest)
- Complexity of explore?
    - Roughly V (from visitng all nodes, though there can be unconnected graphs) + E (you visit each edge twice at least in an undirected graph becuase you have to see if you have seen a node before)
    - For a directed graph, you only see each E once
    - In reality, it is more like E, because the V is really equal to E since the things are connected and V <= E at most (this is for one tree, not the whole graph)
    - That is for a sparse graph though. It is closer to V<sup>2</sup> for a dense graph since E is about that
- DFS goes to all nodes so you see all the disconnected components of the graph
    - What is this complexity?
        - O(V + E)
        - You have to see all nodes
        - You will only look at each edge once or twice (undirected v directed)


## Visiting the whole graph and doing previsit and postvisit

- You can start on any node you want and go in any order (going from component to component)
- See some code about this: [DFS Code](../Codes/Jan30/py)
