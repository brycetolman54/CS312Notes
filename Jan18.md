# More on Primes

- Carmichael  numbers are composites that pass Fermat's test for all a<sub>i</sub> that are relatively prime to the number
    - Relatively prime means that the greatest common denominator (gcd) of the two is 1
- Miller-Rabin said that the probability of a number giving a false positive is 0.25 (that is how to do the probability of MR for Projett 1)


# Euclid's Algorithm

- How do we find the gcd of x and y?
    - gcd(x,y) = gcd(x mod y,y)
    - Here's a function
        - Function euclid(a,b)
            Input: two integers a and b with a >= b >= 0
            Output: gcd(a,b)

            if b = 0 return a
            else return Euclid(b, a mod b)

        - Example:
            a   b
           --- ---
            15  12
            12  3
            3   0
        - Other Example:
            a   b
           --- ---
            15  11
            11  4
            4   3
            3   1
            1   0
    - What's the complexity? (for recursion, ask these questions)
        - How much does the algorithm cost to do once? (n<sup>2</sup> because we have to do division each time with mod and that is n<sup>2</sup>)
        - How many times do we do it? (we cut it in half each time, we drop a bit each time, so we have to do it n times since we have n bits)

# Modular Division

- We have to multiply by the inverse in mod division
    - z/a is computed as z * 1/a
- For modular arithmetic we say that __x__ is the multiplicative inverse of __a mod N__ if ___ax = 1 (mod N)___
    - Example:
        - Inverse of 3 mod 5? Would be 2 (2\*3 = 6 mod 5 = 1)
- We have to know if there exists a multiplicative inverse
    - There always is if a and N are relatively prime (a mod N)


# Extended Euclid

- This will tell us if two things are relatively prime and will tell us the multiplicative inverse of the __a__
    - Fucntion ExtendedEuclid(a, b)
        Input: a and b such that a >= b >= 0
        Output: gcd (d) and x and y

        if b = 0: return (1,0,a)
        (x',y',d) = ExtendedEuclid(b, a mod b)
        return (y',x' - floor(a/b)y',d)

- Example:
    - 9 mod 11 divided by 3 mod 11
    - Inverse of 3 mod 11 is 4
    - 9 mod 11 \* 4
    - 36 mod 11
    - 3
- ___REMEMBER___ that we need the largest number first, so we usually have to switch a and b (becuase a mod b, b is larger), and then switch x and y at the end
- Walk through:

|   a   |   b   |   x'  |   y'  |   d   |  ret1  |  ret2  |  ret3  |
| :---: | :---: | :---: | :---: | :---: | :----: | :----: | :----: |
|  79   |  20   |   1   |  -1   |   1   |   -1   |    4   |    1   |
|  20   |  19   |   0   |   1   |   1   |    1   |   -1   |    1   |
|  19   |   1   |   1   |   0   |   1   |    0   |    1   |    1   |
|   1   |   0   | ----- | ----- | ----- |    1   |    0   |    1   |
 
- What is the complexity?
    - For one run time? (we have n<sup>2</sup> becuase of the mod and the floor and the multiply)
    - How many times? (n because we are dropping by half every time [we are shifting])
    - Overall? (n<sup>3</sup> then)


# RSA Cryptography

- You have a message x, you use `e(.)` to encrypt [to give message y] and `d(.)` to decrypt [to get message x back]
- 
