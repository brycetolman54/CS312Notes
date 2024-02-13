# More on Graphs

- How do we get a shortest path with DAGs?
    - Linearize G (this eliminates the need for a priority queue)
        - Makes it so we go on a path we have to go on
    - For all edges from the nodes in linearized order, update them
    - Update the edge if the new edge would be shorter
    - What would be the complexity?
        - Time: We do each node once and each edge once, so <i>V + E</i> (also the linearization by DFS is <i>V + E</i>)



# Greedy Algorithms

- The idea is to make the choice based on immediate rewards without looking ahead to see the omptimum choice
- More effective that looking ahead because looking ahead would be exponential
- We could do an <i>N</i>-order greedy algorithm in which we look <i>N</i> moves ahead, but that is exponential
- This can lead us to have solutions that don't work or that aren't the <b>most</b>optimal

## Minimum Spanning Tree

- Given a connected and undirected graph, find the "cheapest" connected version of that graph (a tree)
- We need to have <b>exactly</b> <i>V - 1</i> edges
- How could we do that with a greedy algorithm?
    - We could take off the biggest edge each time until we have <i>V - 1</i> edges that connect the graph
    - We would sort the <i>E</i> in <i>ElogE</i> time
    - We would remove the biggest one, then check if we have all the nodes by DFS (Which is <i>E * (E + V)</i>)

### Kruskal's Algorithm

- Start with an empty graph
    - Make each node its own set
- Sort the edges by their weight
- Add the next smallest edge that doesn't make a cycle
    - How to check if we have a cycle?
    - Make sets of nodes that are connected
    - If two nodes are in the same set, don't add that edge

#### Directed Tree Representation

- You have to store the nodes in an array
- Each node has a pointer to its parent and a rank (how far do you have to go to get to a leaf)
- To unionize two sets, you see which has a root node with a greater rank and point the lower ranked root node to the higher ranked root node
    - If they are equal, you promote one of them and connect the other to it
- What is the complexity?
    - Making all the nodes into their own sets is <i>V</i> times of constant time, so O(V)
    - Sorting the edges is ElogE or ElogV (because E = V<sup>2</sup> worst case and ElogV<sup>2</sup> = 2ElogV = ElogV)
    - To go through the edges and choose the right ones, we have to do it <i>E</i> times and each time we do two finds (to make sure we aren't the same set) which are logV (because that is the depth of each tree)
        - The gives a total of ElogV
    - That leaves us with ElogV total
    - The space complexity is V, because we have to store all the nodes in their set
        - The graph is larger than our dat structure still, so it's whatever


### Prim's Algorithm

- Have one strongly connected component
- Arbitrarily add one node into S
- Add one node at a time
- Whenever a new node joins S, update the shortest edge for the nodes not in S that are connected to that added edge
- Add the node that has the shortest path into S (this needs a priority queue)
