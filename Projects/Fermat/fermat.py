import random

# This is main function that is connected to the Test button. You don't need to touch it.
def prime_test(N, k):
	return fermat(N,k), miller_rabin(N,k)

# You will need to implement this function and change the return value.
def mod_exp(x, y, N): 
    if y == 0:
        return 1
    z = mod_exp(x, y // 2, N)
    if y % 2 == 0:
        return (z ** 2) % N
    else:
        return (x * (z ** 2)) % N
	
# You will need to implement this function and change the return value.   
def fprobability(k):
    return 1 - (1 / (2 ** k))

# You will need to implement this function and change the return value.   
def mprobability(k):
    return 1 - (1 / (4 ** k))

# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likley want to use
# random.randint(low,hi) which gives a random integer between low and
# hi, inclusive.
def fermat(N,k):

    # initialize the values holder
    k_values = []

    # get the values between 2 and N - 1
    for i in range(k):
        k_values.append(random.randint(2, N - 1))

    # go through each and return composite if mod_exp is not 1
    for k_value in k_values:
        if(mod_exp(k_value, N - 1, N) != 1):
            return 'composite'

    # if none show composite, return prime
    return 'prime'

# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likley want to use
# random.randint(low,hi) which gives a random integer between low and
#  hi, inclusive.
def miller_rabin(N,k):

    # initialize the values holder
    k_values = []

    # get the values between 2 and N - 1
    for i in range(k):
        k_values.append(random.randint(2, N - 1))

    # check each k and return appropriately
    for k_value in k_values:

        # set the y value
        y = N - 1

        # we need to go until y is 0
        while(y >= 1):

            # get the value
            check_value = mod_exp(k_value, y, N)

            # check it
            if check_value == 1:
                if (y / 2) // 1 == y: # make sure the resulting y will be a whole number
                    y = y / 2
                else:
                    break
            elif (check_value == N - 1):
                break
            else:
                return 'composite'

    # if none show composite, return prime
    return 'prime'
