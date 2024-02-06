# More Breadth First Search (BFS)

- Visit each node, keeping track of the distance of each node
- Keep the nodes in a queue and take them off the fron of the queue each time you need a new one
- When you visit a node, update its distance and then put its children on the queue
- The distance is set to infinity at first, but then when you change it you update it to be the distance of youself plus one
- This is to find the distance from one node to each other
- Complexity?
    - We have to do <i>V</i> injects and ejects into the queue and <i>V</i> nodes to look at
    - We have to look at the total number of edges once or twice each, so we get <i>E</i>
    - Inject and eject are constant time, so we end up with O(V+E)
- Space?
    - This gets as wide as the tree, which is a problem at large <i>n</i>

- We will talk later about "Best" first search (combo of both that allows us to choose the optimal one)


# Graph Paths

- We can have lengths on edges instead of them all being equal length
- We can't use BFS to get the shortest path, we get to use <b>Dijkstra's Algorithm</b>
    - This uses a priority queue, which isn't simple FIFO, we order the queue as we desire
    - We will get to visited nodes, but that can lead us to a shorter path, so we don't dismiss visited nodes

## Priority Queues

- Holds a set of elements with an ordering key
- Operations:
    - Insert (add a new element)
    - Decrease-Key (decrease the key of one value, we want this specifically for shortest path, but it could be a different operation based on what our queue is for)
    - Delete-min (return the element with the smallest key, like eject or dequeue)
    - Make-queue (build a queue with the key values)


## Dijkstra's Algorithm

```
procedure djikstra (G, l, s)
Input: Graph G = (V,E), directed or not
       positive edge lengths; vertex s that is in V
OUtput: For all vertices u reachable from s, dist(u) is set to the distance from s to u (or infinity if not reachable)

for all u in V:
    # sets the distance 
    dist(u) = infinity
    # pointer to the last point to keep track of the path
    prev(u) = nil
# set the distance to the start node
dist(s) = 0

H = makequeue(V) # using the dist values as keys for ordering (the dist values you assigned just earlier)
while H is not empty:
    # pull the node off the queue
    u = deletemin(H)
    # check the edges
    for all edges (u,v) in E
        # if the path to the children is less than their min already, update it
        if dist(v) > dist(u) + l(u,v)
            dist(v) = dist(u) + l(u,v)
            # set the prev for the path
            prev(v) = u
            # updates the key value in the queue
            decreaseky(H,v)

```

- You know you have a shortest path once you pop a point off the queue
    - This is because you are always taking the shortest path one from the front of the queue
- Complexity?
    - We have to do <i>V</i> deletemin, one makequeue of <i>V</i> inserts, a total of <i>E</i> for the edges we visit which includes the decreasekey for each one
    - This gives us O(V\*deletemin + V\*insert + E\*decreasekey)
    - I missed the <i>V</i> from initializing
- Space?
    - I think that it would be O(V+E), since we are storing the number of nodes and the number of edges
    - It seems like we are updating things dynamically though, maybe... ?
    - The overall size really depends on the size of the graph we have (V<sup>2</sup> or V + E)



### Priority Queue Implementations

- Array 
    - Size <i>V</i>
    - Indexed by node number
    - Key is kept there too
    - Insert complexity
        - O(1) because you are just setting an element
    - Decrease-key complexity
        - O(1) because you are just setting an element 
    - Delete-min complexity
        - O(v) because you have to search the whole array to get the smallest
    - So Dijkstra's would be O(V<sup>2</sup>), darn, but this is good for a dense graph where <i>E</i> ~= <i>V<sup>2</sup></i>

- D-ary heap (like binary)
    - Complete binary tree
    - This is what we have to implement
    - <b>Special Constraint</b>: the key value of any node has to be less than or equal to that of its children
    - The minimum node is always at the top of the tree then
    - Insert complexity
        - We never leave a gap
        - We have to put the new node at the next open space until we fill in the level (keep a heap counter to know where to go)
        - Bubble it up until we are greater than our parent
        - Max number of swaps is log<sub>2</sub>V and each is O(1)
        - So, O(logV)
    - Decrease-key complexity
        - Have to find it
            - Keep a separate array that keeps track of where in the heap the node is
            - Look that up in constant time
            - Point to the nodes
            - You have to update that array with every action now, but that is constant time
        - Bubble up in logV time
    - Delete-min complexity
        - Delete the top one (that is O(1))
        - Get rid of bottom rightmost one
        - Sift down (choose the smallest child)
        - That is O(logV)
    - We implement this with an array, but it is <b>not</b> an array implementation
        - To find the parent, you just have to divide by 2 and floor
        - To find the child, you mutliply by 2 and add 0 (left child) or 1 (right child)
