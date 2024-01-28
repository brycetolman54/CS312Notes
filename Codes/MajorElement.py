import sys
import random


def LinearMaj(nums):

    # get the length of nums
    length = len(nums)
    
    # see if there is only one left
    if length == 1:
        return nums[0]
    elif length == 0:
        return []

    # go thorugh and make pairs
    new_nums = []
    for i in range(0, length // 2):
        if nums[2 * i] == nums[2 * i + 1]:
            new_nums.append(nums[2 * i])

    # if we have an odd number of elements
#    if length % 2 != 0:
#        print(f"inside, {nums[length - 1]}")
#        new_nums.append(nums[length - 1])
#        print(f"{new_nums}")

    # go again
    return LinearMaj(new_nums)



# the function to actually run the program
if __name__ == "__main__":
    
    # make sure we have enough arguments
    if len(sys.argv) < 2:
        print("\u001b[38;5;160m\tUsage: python MajorElement.py <numbers>\u001b[38;5;15m")
        sys.exit(1)
    # if we give a list
    else:   
        nums = sys.argv[1:]

    # get the result and print it
    result = LinearMaj(nums)
    if len(result) == 0:
        print("\u001b[38;5;46m\tThere is no majority element\u001b[38;5;15m")
    else:
        print(f"\u001b[38;5;46m\tThe majority element of this array is {result}\u001b[38;5;15m")
