
def max_num(num1, num2, num3):
    # checks if num1 is the biggest
    if num1 >= num2 and num1 >= num3:
        return num1
    # checks if num2 is the biggest
    elif num2 >= num1 and num2 >= num3:
        return num2
    # if num1 and num2 is not the biggest, return num3
    else:
        return num3

print(max_num(300, 40, 5))