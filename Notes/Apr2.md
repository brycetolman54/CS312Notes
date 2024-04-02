# Machine Learning

- Example of 3 input perceptron with a bias neuron


| Pattern | Target(t) | Weight Vector (wi) |  Net  | Output(z) |       dW    |
| :-----: | :-------: | :----------------: | :---: | :-------: | :---------: |
|  0011   |    0      |    0000            |   0   |     0     |     0000    |
|  1111   |    1      |    0000            |   0   |     0     |     1111    |
|  1011   |    1      |    1111            |   3   |     1     |     0000    |
|  0111   |    0      |    1111            |   3   |     1     |  0-1-1-1-1  |

## Linear Separability

- This refers to the fact that the data that a perceptron can interpret is able to be separated by a line
- The bias value allows us to change the y intercept so it doesn't have to go through the origin
- Data that is not linearly separable is not possible to do with one layer of nodes

## Multiplayer Perceptron (MLP)

- We can use multiple layers of nodes (this allows interactions between the input nodes instead of each just being affected by their weights)
- To get error and update the weights, we have to do <b>back propagation</b>, which gets the error at the output nodes and moves back to the previous nodes
    - $`\Delta W_ij = C \delta_j Z_i`$
- We don't have to worry about this in practice because there are <b>SO</b> many weights that are being adjusted that not all of them "can" have a local minimum at the same point in your nD surface
- 
