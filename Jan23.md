# Divide and Conquer

- Split up the task into subtasks
- Recursively solve the subtasks
- Combine the results appropriately

- For example:
    - We have a tree
    - The depth is logn

- It is not always useful to do divide and conquer, you have to do so intelligently
    - think about grading tests (splitting it up for one person doesn't matter)
    - think about sorting lists (spitting is better) => this will give us O(nlogn) from the logn depth and n for each level
        

# Multiplication by divide and conquer

-  split x and y into halves
    - x * y = 2<sup>n</sup>x<sub>L</sub>y<sub>L</sub> + 2<sup>n/2</sup>(x<sub>L</sub>y<sub>R</sub> + x<sub>R</sub>y<sub>L</sub>) + x<sub>R</sub>y<sub>R</sub>

```
5218 * 4376 =
(5200 + 18) * (4300 + 76) = 
(52 * 10<sup>2</sup> + 18) * (43 * 10<sup>2</sup> + 76)

Tree:
                                5218      *     4376
            /                   /                 \           \
         52 * 43             52 * 76             18 * 43     18 * 76
    /   /       \       \
5 * 4   5 * 3   2 * 4   2 * 3
(100)    (10)    (10)     (1)
```

- a<sup>log<sub>b</sub>n</sup> = n<sup>log<sub>b</sub>a</sup>
- The number of leaf nodes is n<sup>2</sup> where n is the bits of the number
- This leaves us with order n at the top (just adds and shifts) and n<sup>2</sup> at the bottom (for the multiplies)
- This leaves us with O(n<sup>2</sup>) complexity, not great

## A Key Takeaway

- Assume complexity at level `k` is *C(k)*
    - If this decreases as we go down, the total complexity is that of the root
    - If this increases as we go down, the toal complexity is that of the leaves


# A better divide and conquer for multiplication

- Product of 2 complex numbers
    - (a+bi)(c+di) = ac - bd + (bc + ad)i
    - Gauss noticed that: bc + ad = (a+b)(c+d) - ac - bd
    - Plug that in for above and you only have to do three multiplications instead of 4
    - That's one less node at each level
    - This gives n<sup>1.59</sup> leaves at the bottom

# Master Theorem

- Quick way to get the complexity of a divide and conquer algorithm
- Cast the problem as a recurrence relation
- Given: `t(n) = at(roof(n/b)) + O(n<sup>d</sup>)`
    - We need to know a, b, and d (all greater than 0)
        - n = task size
        - a = number of subtasks for each node
        - n/b = size of sub-instances
        - d = polynomial order of work at each node
    ```
             /  O(n<sup>d</sup>)    if a/b<sup>d</sup> < 1 (d > log<sub>b</sub>a)
            |
    t(n) = <    O(n<sup>d</sup>logn)    if a/b<sup>d</sup> = 1 (d = log<sub>b</sub>a)
            |
             \  O(n<sup>log<sub>b</sub>a</sup>)    if a/b<sup>d</sup> > 1 (d < log<sub>b</sub>a)

    ```

- a/b<sup>d</sup> is the increase in geometric complexity as we go down
- n<sup>log<sub>b</sub>a</sup> is the number of leaf nodes

- Examples:
    - T(n) = 5T(n/3) + O(n<sup>3</sup>)
        - a = 5, b = 3, d = 3
        - a/b<sup>d</sup> = 5/27 < 1
        - So, O(n<sup>3</sup>)
    - T(n) = 4T(n/2) + O(n<sup>2</sup>)
        - a = 4, b = 2, d = 2
        - a/b<sup>d</sup> = 4/4 = 1
        - So, O(n<sup>2</sup>logn)
    - Binary Tree
        - a = 1 (split into two but only look at one branch), b = 2 (split into two each time), d = 0 (comparison is O(1) time)
        - a/b<sup>d</sup> = 1/2<sup>0</sup> = 1
        - So, O(n<sup>0</sup>logn) = O(logn)


# Convex Hull Project

- Find the convex hull of a set of Q points that is the smallest polygon possible that includes all points in the set inside or on the border
