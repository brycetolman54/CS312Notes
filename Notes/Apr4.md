# Genetic Algorithms

- In some search spaces, we want to search more broadly instead of focusing on a solution based on an initial state
- The process:
    - Grab a couple of initial states across the whole search space
    - Let them interact to create a new solution
    - We can do local mutation around those solution areas now
- Example: we want to do knapsack with repetition
    - A solution is any list of positive integers (the number of that item we have in the sack)
    - Each solution has a fitness associated with it, in this case it would just be whatever the sum of the values are (unless it exceeds the weight requirement, in which case it is 0)
    - So, we populate our space with initial random solutions and then we can change them
        - We can do a local search with mutation to change one of the integers to a differnt integer (a small mutation, not large)
        - We can do a more exploratory search with crossover (recombination) where we take two parent solutions (generally with higher fitness, but not the highest) and do a single crossover of the ranges somewhere in the middle of the list of integers
    - When we have created children, we have to drop as many solutions as children we created
        - We want to choose to drop the solutions at random, but making the higher fitness solutions more likely to stay and the lower fitness solutions more likely to be dropped

- Procedure Evolutionary Algorithm:

```
t = 0;
Initialize Population P(t);
Evaluate P(t);
Until Done {Sufficient iterations passed with no improvement (BSSF), or sufficiently "good" individuals discovered, etc.}
    t = t + 1
    Parent_Selection P(t);
    Crossover P(t);
    Mutate P(t);
    Evaluate P(t); // Evaluate new and adjusted genomes
    Survive P(t);
}
```

- Again, we want the most fit solutions to be the ones we carry on, but we don't want to get rid of the least fit still
- We use the <i>Fitness Proportionate Selection</i> model to make the most fit more likely to survive
    - $`Pr(h_i)=\frac{Fitness(h_i)}{\sum_{j=1}^{|population|}Fitness(h_j)}`$

## Fitness Function Evaluation

- Each solution needs to have a fitness based on the fitness function, which depends on the application
- Sometimes it's easy (knapsack value, length of path in TSP, accuracy of learning model with a set of weights)
- Stopping criteria: usually just looking at when the best candidates stop improving
    - Keep a BSSF and stop if after <i>m</i> generations, if the BSSF doesn't change, stop
