
# get the imports
import sys

# define the function
def modexp(x, y, N):
    # simple case
    if y == 0:
        return 1
    # get the 
    z = modexp(x, y // 2, N)        # n or n^2 (the division is just a shift)
    # check the y
    if y % 2 == 0:
        return (z ** 2) % N         # n^2 
    else:
        return (x * z ** 2) % N     # n^2
     

    # The whole thing is going to be n^3 because we have to do it n times
        # it is a recursive tree that is depth of n


if __name__ == "__main__":
    # make sure we have enough arguments
    if len(sys.argv) != 4:
        print("Usage: python Jan16.py <x> <y> <N>")
        sys.exit(1)

    # if all is good, extract the arguments
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    N = int(sys.argv[3])

    # get the result and print it
    result = modexp(x,y,N)
    print(f"The result of {x}^{y} mod {N} is: {result}")
