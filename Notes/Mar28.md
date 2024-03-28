# Approximation and Local Search

## Clusters

- Say you have data points that are in random clusters
- We want to find the diameter that is smallest that includes all points
- We can do this in exponential time or we can do an approximation
- The approximation algorithm:
    - Choose a total of k points to be representative of clusters
    - Choose the first arbitrarily
    - Choose the next to be furthest from that one
    - Choose the next to be the furthest from both of those
    - Continue until you get k points
    - Then assign each point to the cluster that is the closest to each k point
    - Complexity?
        - O(kn) because we are looking at all n for every k point
    - We know that our solution with this is within a factor of 2 to the optimal, but we can't know the optimal
    - 


## Local search

- Start with some intial solution
- Move from that to a slightly different solution that at least improves the overall objective function
- Local because you are just looking close to the solution instead of searching the whole solution space
- You look around the neighborhood, but this will look different for each problem
    - You can't make it to small, because then you go so slow
    - You can't make it so large, because you may skip over good solutions
    - We want small jumps, but not too small 
- Example: Travelling Salesperson
    - You choose a random cycle
    - You take two points and switch the cities that they point to
    - If that is better, you change to that
    - If not, you don't
- What are the perks?
    - It can be simple and is widely applicable
    - The downside is that we don't know how long it will take
    - It finds local optima instead of the absolute optimum (it could get the optimal, but we don't know)
- How to deal with local optima?
    - The amount of this has to do with the problem
    - We can just start at a different point and see what that gets us
    - You could add randomness and let it go to a place occasionaly that gets worse, in the hopes it moves you to a better place eventually
- Gradient descent
    - Find the gradient at your point
    - See which direction you will most decrease your objective function the most
    - You take the partial derivative of the objective function with respect to the parameters you can change and go the steepest way (faster than looking all around you)


# Inductive Learning

- Gather a set of data and divide it into a <i>training set</i> and a <i>test set</i>
- Train some learning model on the <i>training set</i> until it can predict correctly the answers you want
- You ultimately want to train the model to be accurate on novel data, like the <i>test set</i> that you have from before

## Neural Networks

- 
