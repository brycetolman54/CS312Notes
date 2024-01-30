# Complexity
- It's called asymptotic complexity because it's the complexity as you go to infinity

## Big Theta
- Big Theta is a special set called an 'equivalence class'
- The definition takes care of the small n where algorithms aren't necessarily more efficient, it looks at the limit
- To prove that a function is part of a Big Theta:
    - Show that: `0 <= c_1g(n) <= f(n) <= c_2g(n) FOR ALL n >= n_0`
    - You plug in the functions and choose an n_0
    - The n_0 is the value after which that things is true (think linear vs parabola, linear starts out higher)
- When you pass n_0, all functions in Big Theta's set fall between the one function multiplied by c_1 and c_2
- This is the = (but the function scan differ by a constant factor)

## Big O
- When you pass an n_0, all functions fall below the function multiplied by a constant (c)
- This includes everything in the Big Theta of that function and anything of a lower order
- This is the <=
- We usually say Big O when we could use Big Theta or Big Omega to be more precise, but that is usually okay

## Big Omega
- When you pass an n_0, all functions fall above the function multiplied by a constant (c)
- This includes everything in the Big Theta of that function and anything of a higher order
- This is the >=

## Simpler Way to Calculate Complexity
- __Max Rule__: O(w(n) + z(n)) = O(max(w(n), z(n))) (drop any terms that are lower than the max order)    [DO THIS FIRST!]
- __The Limit Rule__: `lim(n->oo) f(n)/g(n)`
    - If that is:
        - A Real number, it is ___Big Theta___ (f = Theta(g))     (that real number is the constant by which they differ)
        - 0, it is ___Big O___ (f = O(g))
        - +oo, it is ___Big Omega___ (f = Omega(g))

## Analysis
- There is best, worst and average case
- We usually just care about the worst case

- When looking at and comparing algorithms, in the asymptote, we only care about the Big Theta
- However, when we are at small n, the constant factor matters and we have to take it into account

## Arithmetic Examples of Complexity

### Addition
- Addition of two numbers of length n
- To add two numbers, you need to add three digits in each step (the carry over, the digit of one, the digit of the other)
- With numbers of length n, your algorithm time is 3n (3 digits to add for each digit the numbers have), so n
- Space complexity is 2n, so also n
- Computers have addition of O(1), becuase we have a fixed size. So, complexity is based on the number of data items, not their length



