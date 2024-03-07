# exponent function is basically going to allow us to take a certain number and raise it to a specific power

print(2**3) # 2^3

# create an exponent function using for loops
# input takes 2 numbers
def exponent(base_num, power_num):
    # result is where we store the result of the math
    result = 1
    # power_num raises 0 to the power number of times.
    for index in range(power_num):
        # we multiple the base number by the range of the power number.
        # exponent(2, 3)
        # range is 0 to 3
        # 2 * 2 * 2 = 8
        result = result * base_num

    return result

print(exponent(2, 3))