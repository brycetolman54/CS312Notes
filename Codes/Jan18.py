
# get the imports
import sys

# define the extended euclid
def ExtendedEuclid(a, b):
    if b == 0:
        return [1, 0, a]
    else:
        [x_p, y_p, d] = ExtendedEuclid(b, a % b)
        return [y_p, x_p - (a // b) * y_p, d]

# run the program
if __name__ == '__main__':
    # make sure we have enough arguments
    if (len(sys.argv) != 3):
        print("Usage: python Jan18.md <a> <b> for a mod b")
        sys.exit(1)

    # get the args
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    # get the results and print them
    result = ExtendedEuclid(b,a)
    if result[2] == 1:
        print(f"The inverse of {a} mod {b} is: {result[1]}")
    else: 
        print(f"There is no inverse of {a} mod {b}")
