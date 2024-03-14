# Duality

- Every linear programming problem has a dual problem
- So, if you can solve the sister (dual) problem, you can get insight into the original (primal) problem
- Example: Chocolae Shop Redux problem
    - Objective function:
        - max $`x_1 + 6x_2 + 13x_3`$
    - Constraints: $`x_1 \leq 200  x_2 \leq 300 \newline x_1 + x_2 + x_3 \leq 400 \newline x_2 + 3x_3 \leq 600 \newline x_1, x_2, x_3 \geq 0`$
    - Let's say that we take the third constraint and multiply by 13 to make it similar to the objective function
    - This will let us put a max constraint on the problem  because 13 times the third constraint gives us something for sure greater than or equal to the objective function (because all variables in that constraint are now greater than or equal to the ones in the objective function)
    - We can come up with multiple ways to do this same thing with combinations of the constraints
    - Let's make an algorithm of it
        - Let's say we can multiply any of the constraints by a constant, y<sub>n</sub>, where n is the constraint that the y is multiplied by
        - Then we can sum all of those new constraints together (we don't do the multiplication by the greater than 0 bounds though)
        - This gives us new equations where we want to minimize the right side (the values) by changing the y<sub>n</sub> values
        - In doing this, we need to make sure the coefficients in front of each decision variable in the summed equation is greater than or equal to the coefficient of the decision variable it accounts for
        - The summed equation is now the objective function and the constraints (apart from the nonnegative) are the sums of y<sub>n</sub> values for each coefficient of the previous decision variables
    - Hope that makes sense
    - Some cool things:
        - The coefficients in the objective function of the primal problem are the right hand side of the inequalities for the dual problem and vice versa
        - Also, the values of the coefficients in the constraints of the primal problem are the transpose of those in the dual problem
        - If the dual problem has an optimal solution, then so does the primal problem, and those values are the same


# Zero-sum Games

- There is a decision matrix
- There is a row player and a column player
- Each chooses their respective row or column
- The index at the intersect of those two choices is the outcome
- One player is the maximizer, when they "win", there is a positive outcome in the matrix
- The other is the minimizer, when they "win", there is a negative outcome in the matrix
- Called zero-sum because you have to get something from the other player, there is no outside <i>utility unit</i>
- Outcomes:
    - What happens when one person always chooses the same thing?
        - The other can strategize and get the outcome they want every time
    - What if we randomize strategy?
        - Then neither of the players know what is going to happen, you can't strategize against that
    - What if we choose actions with a probability?
        - With equal columns and rows (a symmetric matrix like in rock paper scissors), each option is just as likely
        - What if that is not so simple?
- What if we have a matrix like this:
```math
\begin{bmatrix} 0 & 1 & -2 \\
-3 & 0 & 4 \\
5 & -6 & 0
\end{bmatrix}
```
- If the column player knows x (the probability distribution that the row player is going to do)
- The column player needs to find the best way to hurt the row player
- Knowing this, the row player's strategy is to change the probability distribution in order to get the best loss (the greatest value of the lowest values of loss)
- The objective function for the column player would be $`min(0x_1 - 3x_2 + 5x_3, 1x_1 + 0x_2 - 6x_3, -2x_1 + 4x_2 + 0x_3)`$
- The objectinve function for hte column player would, knowing this, be $`max(min(0x_1 - 3x_2 + 5x_3, 1x_1 + 0x_2 - 6x_3, -2x_1 + 4x_2 + 0x_3))`$
    - With constraints $`x_1 + x_2 + x_3 = 1`$ and $`x_1, x_2, x_3 \geq 0`$
- We can rewrite this last to be: $`max \quad z \newline subject \quad to \newlinex_1 + x_2 + x_3 = 1 \newline0x_1 - 3x_2 + 5x_3 \geq z \newline1x_1 + 0x_2 -6x_3 \geq z \newline-2x_1 + 4x_2 + 0x_3 \geq z \newlinex_1, x_2, x_3 \geq 0 \\`$

- Now you can manipulate z until it hits the first of those constraints (that is the minimum)
- You can do the same thing with the column player now
    - That will end up giving us the dual of the row player's primal!!
- This means that there is some solution to both!
    - We call this solution the value of the game (the actual value, not the values of the decision variables)
    - So, if you deviate from that optimal solution, that only benefits other player
    - This is called <b>Nash Equilibrium</b>
