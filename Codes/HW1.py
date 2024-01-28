
# get the imports
import sys
import time

# define the function for exponential
def fab(n):
    if n ==0 or n == 1 or n == 2:
        return 1
    else:
        return fab(n - 1) + fab(n - 2) * fab(n - 3)
     
# define the function for linear
def fabb(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        n1 = 1
        n2 = 1
        n3 = 1
        n4 = 0
    for i in range (n - 2):
        n4 = n1 + n2 * n3
        n1 = n2
        n2 = n3
        n3 = n4
    return n4

     
if __name__ == "__main__":
    # make sure we have enough arguments
    if len(sys.argv) != 2:
        print("Usage: python HW1.py <n>")
        sys.exit(1)

    # if all is good, extract the n
    n = int(sys.argv[1])

    # get the number and report it
    start = time.time()
    result = fab(n)
    end = time.time()
    print(f"The number for position {n} is: {result} [exponential]")
    print(f"Time taken: {end - start}")

    print()
    
    start = time.time()
    result2 = fabb(n)
    end = time.time()
    print(f"The number for position {n} is: {result} [linear]")
    print(f"Time taken: {end - start}")
