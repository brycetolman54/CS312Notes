# Greedy Algorithms

## More on Prims

- We start with all nodes out
- Start adding the shortest distance node into the set
- Each time you add a new node to the set, you have to update paths into the set to be the shortest
- Set the prev pointer as well when you update the edges in
- The minimal spanning tree is not necessarily getting the shortest path to each node, it is getting the minimal amount of cost for the edges in the graph
- Complexity? (we are using a priority queue, a heap, to do this)
    - <i>V</i> to set up the nodes
    - <i>VlogV</i> to make the queue
    - <i>VlogV</i> to get the smallest 
    - <i>ElogV</i> to look at the edges and update them in the tree
    - Total: O([E+V]logV)

- Choosing between Kruskal's and Prim's?
    - They're the same for a sparsse graph
    - The array implementation is better when the graph is dense


## Huffman Encoding
- Example: mp3 compression
- How to do it?
    - Digitize the analog by choosing little sections and doing a sort of rectangular bit with height as the middle of the rectangle area (like a coarse integral)
    - Put those numebrs into a quantized library (define what values you can have, how many bits each value can be)
    - We can choose some bits to be represented with fewer bits (those that occur more often) and some with longer bits (those that happen less often)
        - This allows us to be more efficient and take less space
        - But this doesn't work because we don't know when the bits start and when they end, we can't separate them
    - So, we use <b>Huffman Encoding</b>

- <i>Prefix-Free Property</i>: No code word can be the prefix of another
    - This can fix the problem with variable bit size
- We build a binary tree where kids are <b>0</b> or <b>1</b>
    - The frequent kids have to come higher in the tree
    - The leaves are the codewords
    - The path to the codewords is their bit representation
    - How do we find the optimal tree?
        - There is an exponential amount of options
        - We can get the cost of the tree by this: `cost(Tree) = sum<sub>i=1</sub>f<sub>i</sub>*depth_of_f`

- Algorithm!!
    - Repeat until all codewords are used
    - Pull the two codewords with the smallest frequency
    - Make them children of a new node with a frequncy of <i>f<sub>a</sub> + f<sub>b</sub></i>
    - Insert that new node into the list of codewords
    - The tree will have exactly <i>2n-1</i> node, <i>n</i> leaves, and <i>n-1</i> internal nodes
        - We will use a priority queue to do this
    - We can get the tree cost by summing the frequency of every node (internal and leaf) in the tree as we go
    - Complexity:
        - We have to do n inserts, so <i>nlogn</i>
        - We have to do n delete min, so <i>nlogn</i>
        - Time Total: O(nlogn)
        - We have to store all leaves (n) and all internal nodes (n - 1)
        - Space Total: O(n)

# Traveling Salesman Problem

- You can't get an optimal solution for many cities
- You have <i>n!</i> possible paths
- You can use a greedy algorithm though to get an approximate solution in n<sup>2</sup> time
- 

