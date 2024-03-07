#number = int(input("Enter a number: "))
#print(number)

# outputs an error if the input is a string not an integer

# try and except block : allows our program to try out a piece of code and if everything goes will, then we're great.

# can accept specific errors
# value = 10/0

# can create two different except box to catch two different errors.

try:
    answer = 10/0 # returns invalid but we did not input anything invalid.
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: # prefers for catching specific errors
    # if the user inputs something wrong, it will catch it
    print(err)
except ValueError:
    print("Invalid input.")

# can store error as a variable.