# Greedy Algorithms continued

## Horn Formulas

- Assume a set of boolean values
- Do logic with them
- These can be implications (A => B) or pure negative clauses (!B) [this second has to be ors between booleans]
- <b>Modus Ponens</b>: p => q, works if TT or FT or FF but not TF

- Algorithm:
    - Input is a horn formula (the set of booleans)
    - Output is a satisfying assignment if there is one

    ```
    set all variables to false
    
    while there is an implication that is not satisfied, set the right hand variable of the implication to true

    if all pure negative clauses are satisfied return the assignment
    else return "formula is not satisfiable"
    ```

    - Example:
        - Formulas are: 
            - (w and y and z) => x
            - (x and z) => w
            - x => y
            - => x
            - (x and y) => w
            - (!w or !x or !y)
            - !z
        - Steps:
            - Change x to true with 4
            - Change y to true with 3
            - Change w to true with 5
            - Rule 2 is good because the left side is false
            - Rule 1 is good because the left side is false
            - Pure negative 1 (6) is not good 
            - Pure negative 2 (7) is good
        - Since pure negative 1 is not good, we return not satisfiable


## Set Cover

- Assume a universe of <i>U</i> elements
- Assume a set <i>S</i> of subsets of the universe
- We want to find the minimum number of subsets that can be unioned to cover the universe of elements
- Greedy?
    - Grab the subset that covers the max amount of remaining elements that are not covered
- There is no polynomial solution to get an optimal solution
    - Our greedy algorithm can give us anything <i>k</i> (the optimal solution) to <i>kln(n)</i> (with the ln(n) correction factor)


## Machine Learning

- We want to take data sets with examples of classifications and learn so that we can generalize good answers when we later receive new unforeseen data
- This includes things like medical diagnosis, stock market prediction, speech recognition, self driving cars, etc.
- Decision trees are learned using greedy divide and conquer algorithms that leads to very good results

- Example: Pizza Classifications
    - Assume <i>A<sub>1</sub></i> is a binary feature (Veggie, Meaty)
    - Assume <i>A<sub>2</sub></i> is a 3 value feature (Thin/Stuffed/Thick crust)
    - To get a node, find the feature that, when splitting along that node, gives you the most pure node (has the most unified set of data points)
        - Keep that node and split down the other branch on the other attribute
        - Keep doing that until you get all pure (ish) nodes
    - Now when you get a new data point, follow its characteristics down the tree to the outcome


## Conclusion

- They can get optimal solutions for some things, but not others
- They are good for finding solutions for things that would otherwise take exponential time
- They are usually simple algorithms and efficient



# Test Review


