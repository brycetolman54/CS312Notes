# Modular Arithmetic

- In mod, two numbers that give the same answer are equivalent (8 mod 3 is the same as 11 mod 3)
- These numbers that are the same belong to equivalence classes (there are three equivalence classes for mod 3: 0, 1, 2)
- For modular addition, we take `n` for addition and `n` for the subtraction to get it back into the mod so it's n<sup>2</sup>

## Modular Exponentiation

- Doing x<sup>y</sup> would be a lot to do, and very slow
- How can we do that efficiently?
- What if:
    - We just multiply x by itself y times
        - That gives us an 2<sup>n</sup>
    - We do modular:
        - x<sup>21</sup> = x<sup>20</sup> + x<sup>1</sup>
        - x<sup>10101</sup> = x<sup>10000</sup> + x<sup>0000</sup> + x<sup>100</sup> + x<sup>00</sup> + x<sup>1</sup>
         

|   x   |   y   | y<sub>bin</sup> |   power of x   |   z   | return value |
| :---: | :---: | :-------------: | :------------: | :---: | :----------: |
|   2   |   25  |        1        | x<sup>1</sup>  |   16  |      12      |
|   2   |   12  |        1        | x<sup>2</sup>  |   4   |      16      |
|   2   |   6   |        1        | x<sup>4</sup>  |   8   |       4      |
|   2   |   3   |        1        | x<sup>8</sup>  |   2   |       8      |
|   2   |   1   |        1        | x<sup>16</sup> |   1   |       2      |
|   2   |   0   |        1        |      ----      |   NA  |       1      |
 
- What's the complexity?
    - see the code here: [ModExp Code](../Codes/Jan16.py)


# Fermat's Theorem

- This states: \"If __p__ is prime, then a<sup>p-1</sup> = 1 mod p for any __a__ such that 1 <= a < p\"
    - If any of the __a__ values return something that is not 1, then __p__ is not prime
    - There are some numbers that come back as prime that actually aren't
        - These are Carmichael numbers
        - The probability of this is less than 0.5
        - So we can do the algorithm many times (k times with different values of a) and return a result of prime or not with a probability of 1 - 0.5<sup>k</sup>
        
