# Convex Hull

- Basic Algorithm
    - Take each pair of points (n<sup>2</sup>)
    - See if all points are on one side (n)
    - Total is n<sup>3</sup>

- New Algorithm
    - Sort all points by x values (nlogn)
    - Divide and conquer
        - Find the convex hull of the left side
        - Find the convex hull of the right side
        - Recursive call down to one point each (or four, that works too)
        - Merge the hulls (this is the part to be smart about)
    - How to be smart?
        - We can drop points not in the hull
            - This will increase the speed, but only by constant time
        - Merging two hulls
            - We don't have to test all the edges, we can test just the edges in the two hulls (this gets us n instead of n<sup>2</sup>)
            - We then have to add two new edges (this is order 1, you have a fixed set of potential edges to test)
            - This gives us a runtime of n<sup>2</sup> instead of n<sup>3</sup>
        - Better merge (this is what you will do)
            - If we keep the hulls ordered, the merge will be faster (think mergesort)
            - The way that we will order the hull
                - Keep the leftmost point
                - Put the rest in by decreasing slope from the left point
                - To actually merge, you have to get the upper and lower tangent
                    - Look at the rightmost point on the left hull and the leftmost point on the right hull
                    - Pivot the left hull point until slope stops going down
                    - Change then to pivot the right hull point until the slope stops going up
                    - Change back to the left hull and repeat to the right hull until you don't change anymore in both of them
                    - This takes n time
                    - To do the lower tangent, work the other way (the slopes still need to change the same directions)
            - Merging is now n, no longer n<sup>2</sup>
    - Total complexity?
        - n for merging
        - logn for sorting the list and the hulls
        - So, nlogn!!
    - Space complexity?
        - We go down each branch before another (so we only ever have one branch on the stack)
        - We have n on top, n/2 next, n/4 next, ...
        - Total is about 2n
        - So, order n!!

## Project Description

- Look at the Project Page


# Divide and Conquer

- Mergesort is good, but it is rough because the best case, worst case, and average are the same
    - You also need extra memory for the merging
- Quicksort is better, it works in place
    - Algorithm
        - Choose a pivot
        - Swap the first element from the left that is > <i>pivot</i> with the first element on the right that is <= <i>pivot</i>
        - Continue that until we get to the middle of the list
        - Once in the middle, swap the 3 with the last swap made
        - Now do quicksort on either side of that 3
        - We get a complexity of n<sup>2</sup> for the worst case (n at each level, could be n levels)
    - Pros/cons?
        - We need a pivot that is roughly in the middle to get a good sort
        - The best case, if we pick a good pivot, is nlogn
        - That is the average too

## Median

- We want to find the median to get a good pivot
- Easy way?
    - Sort it. then get the middle number... that's nlogn
- Let's do a more general algorithm: Selection(S, k)
    - Finds the k<sup>th</sup> smallest item on the list of size n
    - Median: Selection(S, floor(S/n))
    - How to do it?
        - Pick a random <i>pivot</i> from the list
        - Split the list into three:
            - those greater than the <i>pivot</i>
            - those less than the <i>pivot</i>
            - those equal to the <i>pivot</i>
            - That is O(n)
        - Knowing k, you can choose which list the value must be in and only look at that one
            - You choose a new k since you know (from the lengths of the other lists) what element in that list it must be
            - Call selection on that list

    - Example:
        - S = {2, 36, 5, 21, 8, 13, 15, 11, 20, 5, 4, 1}
        - We want the median, so k = 6
        - Choose 13 as the pivot
            - S<sub>L</sub> = {2, 5, 8, 11, 5, 4, 1}
            - S<sub>E</sub> = {13}
            - S<sub>R</sub> = {36, 21, 15, 20}
            - We have to go in the first list
                - k is now 3
                - Choose 8 as the pivot
                    - S<sub>L</sub> = {2, 5, 5, 4, 1}
                    - S<sub>E</sub> = {8}
                    - S<sub>R</sub> = {11}
                    - We go to the S<sub>E</sub> list since the S<sub>L</sub> list has 5
                    - We get that 8 is the median!!
        - What is the trick?
                - We get rid of a lot of the list everytime (roughly 1/3)
            - What is the complexity?
                - a = 1
                - b = 3
                - d = 1
                - ratio = 1/3 < 1
                - So, O(n<sup>1</sup>)
