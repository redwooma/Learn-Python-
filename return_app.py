#  when calling a function, it does it's tasks.
#  may want to get information back from the function.

def cube(num):
    return num * num * num
    # specify any value we want this function to give us.
    # can not type code after the return statement
    # return keyword breaks us out of the function
    # can return any data type we want

result = cube(4)
print(result)