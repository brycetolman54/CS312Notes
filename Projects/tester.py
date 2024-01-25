import sys
import fermat

if __name__ == '__main__':

    if(len(sys.argv) != 3):
        print("Usage: python fermat.py <N> <k>")
        sys.exit(1)

    N = int(sys.argv[1])
    k = int(sys.argv[2])

    result = fermat.miller_rabin(N,k)
    print(f"The result is that {N} is {result}")
