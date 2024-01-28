import sys
import random
import time

# the function to split up the array
def ms(nums): 
    
    # get the length for further use
    length = len(nums)

    # see if we need to be done
    if length == 1:
        return nums

    # recursively call to break up the array
    return merge(ms(nums[:(length // 2)]), ms(nums[(length // 2):]))



# the function to merge subarrays
def merge(nums1, nums2):

    # get the lengths
    length1 = len(nums1)
    length2 = len(nums2)

    # see if either is empty
    if length1 == 0:
        return nums2
    elif length2 == 0:
        return nums1

    # return the appropriate one now
    if nums1[0] <= nums2[0]:
        return nums1[:1] + merge(nums1[1:], nums2)
    else:
        return nums2[:1] + merge(nums1, nums2[1:])
    

# the function to actually run the program
if __name__ == "__main__":
    
    # make sure we have enough arguments
    if len(sys.argv) < 2:
        print("\u001b[38;5;160m\tUsage: python MergeSort.py <numbers> \n\t  or \n       \tpython MergeSort.py r<number>\u001b[38;5;15m")
        sys.exit(1)

    # if we want a random array
    elif len(sys.argv) == 2:

        # get the argument
        arg = sys.argv[1]
        length = len(arg)

        if (arg[0] == 'r' and length != 1):
            
            # start array
            nums = []

            # fill array
            for i in range(1, int(arg[1:]) + 1):
                nums.append(random.randrange(100))

        else:
            print("\u001b[38;5;160m\tError: you have to provide a number of random elements for the list\u001b[38;5;15m")
            sys.exit(1)

    # if we give a list
    else:   
        nums = sys.argv[1:]

    # get the result and print it
    start = time.time()
    result = ms(nums)
    end = time.time()
    print(f"\u001b[38;5;46m\tThe resulting sorted array is: {result}\n\tThis was obtained in {end - start} seconds\u001b[38;5;160m")
